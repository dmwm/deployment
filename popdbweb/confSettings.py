import ConfigParser
import logging
import os
#from django.conf import settings
from Apps.popCommon.PopularityException import PopularityConfigException


logger = logging.getLogger(__name__)

class confSettings:

    def __init__(self):
        configfilenames = ['conf.ini','conf_secret.ini']
        #self.popularity_base = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../.."))
        #self.popularity_base = "@POPDBWEB_ROOT@/"
        self.popularity_base = ["@CONFIG@", "@AUTH@"]
        try:
            self.configfilepath = [self.dirwalk(self.popularity_base[index], configfilename).next()+'/'+configfilename for index,configfilename in enumerate(configfilenames)]
            logger.info("popularity_base: %s" % self.popularity_base)
        except Exception, err:
            raise PopularityConfigException("configfile not found")
        try:
            self.parser = ConfigParser.SafeConfigParser()
            self.parser.optionxform = str
            found = self.parser.read(self.configfilepath)
            logger.info("config found: %s" % found)
        except ConfigParser.ParsingError, err:
            raise PopularityConfigException("exception while reading config file - %s" % err.message)
            #raise err
            #logger.error("CONFIG FILE NOT FOUND")            

    def getSetting(self, section, property):
        if self.parser.has_section(section):
            if self.parser.has_option(section, property): 
                return self.parser.get(section, property)
            else: 
                raise PopularityConfigException("option %s not found" % property)
                #raise Exception("config file error: option %s not found" % property)
                #logger.error("config file error: option %s not found" % property) 
        else: 
            raise PopularityConfigException("section %s not found" % section)
            #raise Exception("config file error: section %s not found" % section)
            #logger.error("config file error: section %s not found" % section)

    def getConfigSectionMap(self,section):
        confdict = {}
        for option in self.parser.options(section):
            confdict[option] = self.getSetting(section,option)
        return confdict

    def getNestedConfigSectionMap(self,section):
        confdict = {}
        for option in self.parser.options(section):
            confdict[option] = self.getConfigSectionMap(self.getSetting(section,option))
            logger.info("setting for section %s is %s" % (section,confdict))
        return confdict

    def dirwalk(self, relativedir, filename):
        """
        Walk a directory tree and look-up for __init__.py files.
        If found yield those dirs. Code based on
        http://code.activestate.com/recipes/105873-walk-a-directory-tree-using-a-generator/
        """
        idir = relativedir
        for fname in os.listdir(idir):
            fullpath = os.path.join(idir, fname)
            if  os.path.isdir(fullpath) and not os.path.islink(fullpath):
                for subdir in self.dirwalk(fullpath, filename):  # recurse into subdir
                    yield subdir
            else:
                initdir, initfile = os.path.split(fullpath)
                if  initfile == filename:
                    yield initdir
