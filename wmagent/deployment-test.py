#!/usr/bin/env python
# encoding: utf-8
"""
deployinator.py

Created by Dave Evans on 2011-04-19.
Copyright (c) 2011 Fermilab. All rights reserved.
"""

import sys
import getopt
import os
import subprocess
import logging
import glob
import re
import select



help_message = '''
Script to run and test a deployment for WMAgent
Arguments:

'''


logger = logging.getLogger("deployment")
logger.setLevel(level=logging.DEBUG)
loggerStream = logging.StreamHandler()
loggerStream.setLevel(level = logging.DEBUG)
logger.addHandler(loggerStream)
logger.debug("initialised...")


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

class DeploymentTest:
    """
    _DeploymentTest_

    Configurable object for running the deployment and management tests
    """
    def __init__(self, **args):
        self.workingDir = args.get("directory", os.getcwd() )
        self.agentTag   = args.get("agent", None)
        self.thisDir = os.path.dirname(os.path.abspath(__file__))
        self.installDir = os.path.join(self.workingDir, "install")
        if not os.path.exists(self.installDir):
            os.makedirs(self.installDir)
        self.nocleanup = args.get("nocleanup", False)
        self.startedManage = False
        verbose = args.get("verbose", False)
        if not verbose:
            print "not verbose"
            loggerStream.setLevel(logging.INFO)
        #loggerFile = logging.FileHandler("%s/log" % self.deployDir, 'w', )
        #loggerFile.setLevel(logging.DEBUG)
        #logger.addHandler(loggerFile)

        logger.info("Deployment Test Starting:")
        logger.info("  Install    in: %s" % self.installDir)
        logger.info("  WMAgent Tag: (None=default from deploy)  %s" % self.agentTag)


    def __call__(self):
        """
        Invoke the deployment process
        """
        self.machineTest()
        self.runDeploy("prep")
        self.checkPrep()
        self.runDeploy("sw")
        self.checkSw()
        self.runDeploy("post")
        self.manageTests()
        self.cleanup()


    def machineTest(self):
        """
        _machineTest_

        Run a few test commands to check the machine environment
        """
        # rpm db needs to be readable
        checkProcess = subprocess.Popen(
                    ["/bin/bash"], shell = True, cwd = os.getcwd(), env = os.environ,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    )
        comm = "rpm -qa"
        logger.info("Running rpm -qa")
        checkProcess.stdin.write(comm)
        stdout, stderr = checkProcess.communicate()
        logger.debug(stdout)
        logger.debug(stderr)
        retCode = checkProcess.returncode
        if retCode != 0:
            msg = "Unable to read rpmdb, rpm -qa failed with exit code: %s" % retCode
            logger.error(msg)
            self.bailout()

        check2 = subprocess.Popen(
            ["/bin/bash"], shell = True, cwd = os.getcwd(), env = os.environ,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            )
        comm = "rpm -qa | grep HEP_OSlibs"
        logger.info("Running rpm -qa | grep HEP_OSlibs")
        check2.stdin.write(comm)
        stdout, stderr = check2.communicate()
        logger.debug(stdout)
        logger.debug(stderr)
        retCode = check2.returncode
        if retCode != 0:
            msg = "Unable to check for HEP_OSlibs,  rpm -qa failed with exit code: %s" % retCode
            logger.error(msg)
            self.bailout()
        if "HEP_OSlibs" not in stdout:
            msg = "HEP_OSlibs check failed, seems to not be installed"
            logger.error(msg)
            self.bailout()



    def runDeploy(self, step, version = "v01"):
        """
        _runDeployCommand_

        Run the Deploy script for the step & version provided

        """
        logger.info("Running Deploy %s " % step)
        deploymentPkg = os.path.dirname(self.thisDir)
        scriptProcess = subprocess.Popen(
                ["/bin/bash"], shell = True, cwd = deploymentPkg, env = os.environ,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                )

        deployCommand = "./Deploy -s %s" % step
        deployCommand += " -t %s " % version
        deployCommand += " %s " % self.installDir
        deployCommand += " wmagent\n"
        logging.debug("Executing Command: %s " % deployCommand)

        scriptProcess.stdin.write(deployCommand)
        stdout, stderr = scriptProcess.communicate()
        logger.debug(stderr)
        logger.info(stdout)
        retCode = scriptProcess.returncode
        if retCode != 0:
            logging.error("Failed to run Deploy Command for step %s" % step)
            self.bailout()
        return

    def checkPrep(self):
        """
        _checkPrep_

        Check Prep stage worked
        """
        checkPaths = [
            os.path.join(self.installDir, "current"),
            os.path.join(self.installDir, "current", "apps"),
            os.path.join(self.installDir, "current", "config"),
        ]
        missingPath = False
        for p in checkPaths:
            logger.debug("Checking %s exists after prep" % p )
            if not os.path.exists(p):
                logging.error("Missing Dir After Prep Phase")
            else:
                logger.debug("%s exists" % p)

        if missingPath:
            self.bailout()


    def checkSw(self):
        """
        _checkSw_

        Check SW step worked
        """
        checkPaths = [
            os.path.join(self.installDir, "current", "apps", "wmcore"),
            os.path.join(self.installDir, "current", "apps", "couchdb"),
            os.path.join(self.installDir, "current", "apps", "mysql"),
            os.path.join(self.installDir, "current", "apps", "wmagent"),
            os.path.join(self.installDir, "current", "apps", "pystack"),
            os.path.join(self.installDir, "current", "config", "wmagent"),
            os.path.join(self.installDir, "current", "config", "reqmgr"),
            os.path.join(self.installDir, "current", "config", "workqueue"),
            os.path.join(self.installDir, "current", "config", "mysql"),
            os.path.join(self.installDir, "current", "config", "couchdb"),
            os.path.join(self.installDir, "current", "install", "wmagent"),
            os.path.join(self.installDir, "current", "install", "reqmgr"),
            os.path.join(self.installDir, "current", "install", "workqueue"),
            os.path.join(self.installDir, "current", "install", "mysql"),
            os.path.join(self.installDir, "current", "install", "couchdb"),

        ]

        swDir = os.path.join(self.installDir, "current", "sw")
        bootstrapLog = glob.glob("%s/bootstrap*.log" % swDir)[0]
        scramVersion = os.path.basename(bootstrapLog)
        scramVersion = scramVersion.replace("bootstrap-", "")
        scramVersion = scramVersion.replace(".log", "")
        extPath = os.path.join(swDir, scramVersion, "external")



        externals = ["py2-cheetah",
            "cherrypy",
            "py2-cjson",
            "couchapp",
            "py2-httplib2",
            "py2-sqlalchemy",
            "couchdb",
            "mysql",
            "py2-mysqldb"
            ]
        for external in externals:
            checkPaths.append(os.path.join(extPath, external))


        missingPath = False
        for p in checkPaths:
            logger.debug("Checking %s exists after sw" % p )
            if not os.path.exists(p):
                logger.error("Missing Dir After sw Phase")
            else:
                logger.debug("%s exists" % p)

        if missingPath:
            self.bailout()

        readBootstrap = subprocess.Popen(
                    ["/bin/bash"], shell = True, cwd = swDir, env = os.environ,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    )
        readBootstrap.stdin.write("tail -5 %s\n" % bootstrapLog)
        stdout, stderr = readBootstrap.communicate()
        nonZeroExit = re.compile("exit[\W]+[1-9]+")
        logger.debug("Checking Bootstrap Log: %s" % bootstrapLog)
        for line in stdout.split("\n"):
            logger.debug(" ==> Bootstrap Log: %s" % line)
            if nonZeroExit.search(line) != None:
                msg = "Non Zero exit in bootstrap file:\n %s\n%s" % (bootstrapLog, line)
                logger.error(msg)
                self.bailout()





    def manageTests(self):
        """
        _manageTests_

        Run series of manage test commands
        """

        self.manageActivate()
        self.startedManage = True
        try:
            logger.info('Starting Services...')
            stdout, stderr = self.runManageCommand('start-services')
            logger.info("\n%s\n" % stdout)
        except Exception, ex:
            logger.error("Error starting services")
            self.bailout()
        #ToDo: Test services are running

        try:
            logger.info("Initialising Agent...")
            stdout, stderr = self.runManageCommand('init-agent')
            logger.info("\n%s\n" % stdout)
        except Exception, ex:
            logger.error("Error starting services")
            self.bailout()
        cfgPath  = os.path.join(self.installDir, "current", "config")
        if not os.path.exists(os.path.join(cfgPath, "wmagent", "config.py")):
            logger.error("init-agent did not produce a wmagent/config.py")
            self.bailout()
        if not os.path.exists(os.path.join(cfgPath, "reqmgr", "config.py")):
            logger.error("init-agent did not produce a reqmgr/config.py")
            self.bailout()
        if not os.path.exists(os.path.join(cfgPath, "workqueue", "config.py")):
            logger.error("init-agent did not produce a workqueue/config.py")
            self.bailout()
        try:
            logger.info("Starting Agent...")
            stdout, stderr = self.runManageCommand('start-agent')
            logger.info(stdout)
        except Exception, ex:
            logger.error("Error starting services")
            self.bailout()
        #Todo: Check agent is running/heartbeats etc
        try:
            self.runManageCommand('stop-agent')
        except Exception, ex:
            logger.error("Error starting services")
            self.bailout()

        try:
            self.runManageCommand('stop-services')
        except Exception, ex:
            logger.error("Error stopping services")
            self.bailout()






    def runManageCommand(self, command):
        """
        _runManageCommand_

        Run the manage script to execute the command provided, return stdout, stderr
        Raise error of non-zero

        """
        executeFrom = os.path.join(self.installDir, "current")
        logger.info("Running manage %s" % command)

        stdoutHandle = open(os.path.join(self.installDir, "current", "install.out"), 'w')
        stderrHandle = open(os.path.join(self.installDir, "current", "install.err"), 'w')


        manageCommand = ["/bin/bash", "./config/wmagent/manage", command ]
        logger.debug("Executing %s" % manageCommand)
        runmanage = subprocess.Popen(
                        manageCommand, cwd = executeFrom, env = os.environ,
                        stdout=stdoutHandle,
                        stderr=stderrHandle,
                        )

        while True:
            (rdready, wrready, errready) = select.select(
                [stdoutHandle.fileno(),
                 stderrHandle.fileno()],[],[])
            # see if the process is still running
            runmanage.poll()
            if (runmanage.returncode != None):
                break
            # give the process some time to fill a buffer
            select.select([], [], [], .1)

        retCode = runmanage.wait()
        stdoutHandle.close()
        stderrHandle.close()

        stdout = open(os.path.join(self.installDir, "current", "install.out"), 'r').read()
        stderr = open(os.path.join(self.installDir, "current", "install.err"), 'r').read()

        logger.debug("manage %s exited with %s" %(command, retCode))
        if retCode != 0:
            logger.error("Failed to run manage %s, exited %s " % (command, retCode) )
            logger.error(stdout)
            logger.error(stderr)
            raise RuntimeError("Manage Command %s Failed" % command)
        return stdout, stderr


    def manageActivate(self):
        """
        _manageActivate_

        Test the activate manage commands
        """
        instPath = os.path.join(self.installDir, "current", "install")
        cfgPath  = os.path.join(self.installDir, "current", "config")
        try:
            self.runManageCommand("activate-agent")
        except Exception, ex:
            print ex
            self.bailout()
        if not os.path.exists(os.path.join(instPath, "wmagent", ".using")):
            logger.error("Activation file %s/wmagent/.using missing after activate-agent" % instPath)
            self.bailout()
        if not os.path.exists(os.path.join(cfgPath, "wmagent", "config-template.py")):
            logger.error("Config Template file %s/wmagent/config-template.py missing after activate-agent" % cfgPath)
            self.bailout()
        try:
            self.runManageCommand("activate-workqueue")
        except:
            self.bailout()
        if not os.path.exists(os.path.join(instPath, "workqueue", ".using")):
            logger.error("Activation file %s/wmagent/.using missing after activate-workqueue" % instPath)
            self.bailout()
        if not os.path.exists(os.path.join(cfgPath, "workqueue", "config-template.py")):
            logger.error("Config Template file %s/workqueue/config-template.py missing after activate-workqueue" % cfgPath)
            self.bailout()
        try:
            self.runManageCommand("activate-reqmgr")
        except:
            self.bailout()
        if not os.path.exists(os.path.join(instPath, "reqmgr", ".using")):
            logger.error("Activation file %s/reqmgr/.using missing after activate-reqmgr" % instPath)
            self.bailout()
        if not os.path.exists(os.path.join(cfgPath, "reqmgr", "config-template.py")):
            logger.error("Config Template file %s/reqmgr/config-template.py missing after activate-reqmgr" % cfgPath)
            self.bailout()



    def cleanup(self):
        if self.nocleanup:
            return
        os.system("rm -rf %s" %self.installDir)
        return

    def bailout(self):
        """test failed, bailout and cleanup"""
        print "Bailing Out..."

        if self.startedManage:
            try:
                self.runManageCommand('stop-agent')
            except Exception, ex:
                pass
            try:
                self.runManageCommand('stop-services')
            except Exception, ex:
                pass
        self.cleanup()
        sys.exit(1)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    config = {}
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ht:v", ["help", "dir=", "tag=", "verbose", "nocleanup"])
        except getopt.error, msg:
            raise Usage(msg)

        # option processing
        for option, value in opts:
            if option == "--verbose":
                config['verbose'] = True
            if option == "--nocleanup":
                config['nocleanup'] = True

            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("--dir"):
                config['directory'] = value
            if option in ("-t", "--tag"):
                config['tag'] = value

    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2
    deployTest = DeploymentTest(**config)
    deployTest()


if __name__ == "__main__":
    sys.exit(main())
