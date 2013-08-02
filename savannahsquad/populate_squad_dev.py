#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-
## CMS Web login needs XHTMLFormParser to work.

## make a new DefaultFactory
from mechanize import XHTMLCompatibleFormParser
from mechanize._html import DefaultFactory,FormsFactory
from mechanize import Browser,LinkNotFoundError
from unicodedata import normalize
import sys,optparse,re,logging
import ConfigParser
from pprint import pprint
from SiteDB import getCMSNamesToAdmin
from SiteDB import getSiteDBSiteNames

# added in 2011-02-11
config = ConfigParser.SafeConfigParser()
config.read('config.ini')

######################################################################
#for some logging...
logger = logging.getLogger('populate_squad')
hdlr = logging.FileHandler('./populate_squad.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
#######################################################################
LINK_SECTION='SAVANNAH_URLS'
login_page=config.get(LINK_SECTION,'LOGIN_PAGE')
squads_page=config.get(LINK_SECTION, 'SQUADS_PAGE')
members_list=config.get(LINK_SECTION, 'MEMBERS_LIST')
directory=config.get(LINK_SECTION, 'DIRECTORY')
add_to_group_page=config.get(LINK_SECTION, 'ADD_TO_GROUP_PAGE')
create_ticket=config.get(LINK_SECTION, 'CREATE_TICKET')
create_site=config.get(LINK_SECTION, 'CREATE_SITE')
check_open_ticket=config.get(LINK_SECTION, 'CHECK_OPEN_TICKET')
cmscompinfrasup_link=config.get(LINK_SECTION, 'CMSCOMPINFRASUP_LINK')

# create and initialize the robot engine
# 2011-02-01
def init():
    new_form_fac=FormsFactory(form_parser_class=XHTMLCompatibleFormParser)
    new_def_fac=DefaultFactory()
    new_def_fac._forms_factory=new_form_fac
    br=Browser(factory=new_def_fac)

    #br.set_handle_referer(True)
    br.set_handle_refresh(True)
    #br.set_handle_equiv(True)

    ## HTTP Error 403: request disallowed by robots.txt
    br.set_handle_robots(False)
    br.open(login_page)

    ## 'Search' form is form 0
    ## login form is form 1
    br.select_form(nr=1)
    #br.form.set_all_readonly(False)
    #reading from my_secret.txt
    f = open('my_secret.txt', 'r')
    passwd=f.readline()
    f.close()
    br['form_loginname']='sitedbrobot'
    br['form_pw']=passwd.replace('\n','')
    br.submit()
    return br

def rb_open_ticket(br,ticket_title,cms_name,code_new_members,x,new_member_dict_inv,add_cmscompinfrasup ,mismatch_emails,contact_emails):
    y=x
    new_and_added=''
    mismatch=''
    compinfrasup=''
    for key in new_member_dict_inv.keys():
        new_and_added+='   * '+new_member_dict_inv[key]+'\n'
    if(len(mismatch_emails) !=0):
        for r in mismatch_emails:
            mismatch+='   * '+r[0]+'  ('+r[1]+')\n'
    for s in add_cmscompinfrasup:
        compinfrasup+='   * '+new_member_dict_inv[s]+'\n'
    br.open(check_open_ticket)
    text_body="""Dear Site admin,

In order to improve the CMS Facilities Operations trouble shooting procedure, we are currently creating Savannah squads for
each CMS site and assign the appropriate people to each site according to the information in SiteDB.

As a result of this procedure, we have identified the following people from your Site in SiteDB which we propose to add to your
site squad:
%s
The following people would be added, but they are not yet  Savannah members (just ignore if empty):
%s
You will need to request to add some members on  cmscompinfrasup group as well (just ignore if empty):
%s
%s
Just to make sure that we are adding the right people to your squad, please, also verify and notify in this ticket if the following person is not currently in your site (just ignore if empty):
%s
If you agree, could you please contact the concerned people and ask them to register in https://savannah.cern.ch/ if not yet done and/or remove any people of the first list from SiteDB if obsolete

*Important* : once done, could we please ask you to close the present ticket. Also, don't change the "Status": the robot will do it after you close this ticket.

Many Thanks,
Jadir Silva
CMS Facilities Operations
"""%(new_and_added,y,y,compinfrasup,mismatch)
    try:
        br.select_form(nr=0)
        br["words"]=cms_name
        br["type_of_search"]=['support']
        br.submit()
        br.follow_link(text_regex=ticket_title, nr=0)
        extract_date=br.response().read()
        search_date='20[0-9]{2}-[0-9]{2}-[0-3][0-9] [0-2][0-9]:[0-5][0-9]'
        p = re.compile(search_date,re.IGNORECASE)
        date_list=p.findall(extract_date)
        last_ticket=date_list[0]
        from datetime import datetime
        last=datetime.strptime(last_ticket, "%Y-%m-%d %H:%M")
        now=datetime.now()
        difference=now-last
        number_days=difference.days
        br.select_form(nr=1)
        control1 = br.form.find_control("status_id", type="select")
        control3=br.form.find_control("resolution_id", type="select")
        ##The ticket is closed ('3')...
        if (control1.value[0]=='1'):
            print('ticket still opened')
        else:
            print('ticket was closed')
        print('Ticket sent  %s days ago' %(number_days))
#If the ticket is closed (control1='3')....
        if(control1.value[0]=='3'):
            #...and the status is'None"(100) we can proceed...
            if (control3.value[0]=='100'):
                br.back()
            #The previous ticket was closed, the number of days is >=3 since it was send and the status (control3=1) is done. This is another request. I should create a new ticket and exit
            if((number_days>0)&(control3.value[0]=='1')):
                br.open(create_ticket)
                squad_name=cms_name.replace('_','').lower()
                if (squad_name=='t1defzk'):
                    squad_name='t1_de_fzk'
                if (squad_name=='t2brsprace'):
                    squad_name=='t2_br_sprace'
                html_page= br.response().read()
                find_regex='<option value=\"[0-9]{1,}\">%s' %(cms_name)
                q = re.compile(find_regex)
                temp_site_number=q.findall(html_page)
                if (len(temp_site_number)==0):
                    site_number='100'
                else:
                    site_number=temp_site_number[0].split('"')[1]
                find_regex='<option value=\"[0-9]{1,}\">cmscompinfrasup-%s</option>'%(squad_name)
                p = re.compile(find_regex)
                temp_squad_number=p.findall(html_page)
                try:
                    squad_number=temp_squad_number[0].split('"')[1]
                except IndexError:
                    if(len(code_new_members)!=0):
                        squad_number=code_new_members[0]
                    else:
                        # assign to jmsilva(me)
                        squad_number='7381'
                br.select_form(nr=1)
                br['assigned_to']=[squad_number]
                br['privacy']=['1']
                br['custom_sb1']=[site_number]
                br['severity']=['5']
                br['category_id']=['123']
                br['summary']=ticket_title
                br['details']= text_body
                br['add_cc']=contact_emails
                #br.submit()
                print text_body
                print('ticket sent to create squad for %s' %(cms_name))
                return sys.exit()
        #but, if the ticket still opened ('1'), or another option on "status" menu was done... I will abort
        else:
            return sys.exit()
    except LinkNotFoundError:
        br.open(create_ticket)
        squad_name=cms_name.replace('_','').lower()
        if (squad_name=='t1defzk'):
            squad_name='t1_de_fzk'
        if (squad_name=='t2brsprace'):
            squad_name=='t2_br_sprace'
        html_page= br.response().read()
        find_regex='<option value=\"[0-9]{1,}\">%s' %(cms_name)
        q = re.compile(find_regex)
        temp_site_number=q.findall(html_page)
        if (len(temp_site_number)==0):
            site_number='100'
        else:
            site_number=temp_site_number[0].split('"')[1]
        find_regex='<option value=\"[0-9]{1,}\">cmscompinfrasup-%s</option>'%(squad_name)
        p = re.compile(find_regex)
        temp_squad_number=p.findall(html_page)
        try:
            squad_number=temp_squad_number[0].split('"')[1]
        except IndexError:
            if(len(code_new_members)!=0):
                squad_number=code_new_members[-1]
            else:
                # assign to jmsilva(me)   
                squad_number='7381'
        br.select_form(nr=1)
        br['assigned_to']=[squad_number]
        br['privacy']=['1']
        br['custom_sb1']=[site_number]
        br['severity']=['5']
        br['category_id']=['123']
        br['summary']=ticket_title
        br['details']= text_body
        br['add_cc']=contact_emails
        #br.submit()
        print text_body
        print('ticket sent to user/squad  number  %s' %(squad_number))
        return sys.exit()

################################################################################
def rb_add_to_group(br,new_member_dict_inv,add_to_cmscompinfrasup):
    br.open(add_to_group_page)
    br.select_form(nr=3)
    br['words']=new_member_dict_inv[add_to_cmscompinfrasup]
    br.submit()
    br.select_form(nr=4)
    br['user_id[]']=[add_to_cmscompinfrasup]
    #br.submit()
################################################################################
def rb_members_not_in_group(br,cms_name,code_new_members):
    # find for people that not joined to cmscompinfrasup
    # group

    # points mechanize browser to 
    # https://savannah.cern.ch/project/admin/useradmin.php?group=cmscompinfrasup
    br.open(add_to_group_page)
    br.select_form(nr=2)
    br.form.set_all_readonly(False)
    ## We have to add to cmscompinfrasup group, if aren't
    control2 = br.form.find_control("user_id[]", type="select")
    # cmscompinfrasup members
    possibleChoises = [x.name for x in control2.items]
    notAtGroup = set(code_new_members).difference(possibleChoises)
    notAtGroup = list(notAtGroup)

    print "People out of cmscompinfrasup group(Harvesting #1): %s"%notAtGroup

    ##Administrators aren't showed in the list. After last filter, lets check it
    add_to_cmscompinfrasup = []
    for guy in notAtGroup:
      br.select_form(nr=0)
      br["words"]= "#%s"%guy
      br["type_of_search"]=['people']
      br.submit()
      try:
        br.find_link(url_regex='/projects/cmscompinfrasup/', nr=0)
      except LinkNotFoundError:
        add_to_cmscompinfrasup.append(guy)
      except Exception,e:
        print "Erro: %s"%e

    br.back()
    print "People out of cmscompinfrasup group(Harvesting #2): %s"%add_to_cmscompinfrasup
    return add_to_cmscompinfrasup
#####################################################################
def rb_createsavannahsquad(br,cms_name):
    br.open(squads_page)
    savannah=cms_name.replace('_', '').lower()
#These two squad have different names. If you try to create with the  usual name an error will appear
    if (savannah=='t2brsprace'):
        savannah='t2_br_sprace'

    if len(savannah)>16:
       savannah=savannah[0:15]
    print "creating %s squad(%s)..."%(savannah,cms_name)
    #find the last "Rank" to be displayed
    br.select_form(nr=1)
    br.form.set_all_readonly(False)
    br['form_loginname']=savannah
    br['form_realname']=cms_name
    br.submit()
#####################################################################
def rb_verify(br,cms_name, code_new_members):

    ###First see if the site exists
    br.open(create_site)
    try:
        br.follow_link(text_regex=cms_name, nr=0)
        br.back()
    except:
        print('Site %s was not there. Ticket \"status\" not changed to done' %(cms_name))
        return -1
    ###Second if the squad was really created
    br.open(squads_page)
    try:
        br.follow_link(text_regex=cms_name, nr=0)
    except LinkNotFoundError:
        print('Squad for %s not found. Ticket \"status not\" changed to done' %(cms_name))
        return 1
    ###Third with all the guys that we suppose to add was really there
    if(len(code_new_members)==0):
        pass
    else:
        br.open(squads_page)
        br.follow_link(text_regex=cms_name, nr=0)
        br.select_form(nr=2)
        control = br.form.find_control("user_id[]", type="select")
        in_savannah=[]
        for item in control.items:
            in_savannah.append(item.name)
        for i in code_new_members:
            if(i in in_savannah):
                pass
            else:
                print "Error:one person not added to the squad at least. Ticket \"status\" not changed to done"
                return 2
    return 0
#############################################################################
def rb_compare_email(br,x):
    br.open(login_page)
    br.select_form(nr=0)
    br["words"]= x
    br["type_of_search"]=['people']
    br.submit()
    savannah_email=br.find_link(text_regex=".*@.*\..*", nr=0)
    #imagine that in the previous page has a (I hope only one) ticket with " Problems @CERN"...
    if (savannah_email.url.replace('/sendmessage.php?touser=', '').count('support')>=1):
        test2=br.find_link(text_regex=".*@.*\..*", nr=1)
    br.back()
    return savannah_email.text
##################################################################
def rb_remove_accents(txt):
    return normalize('NFKD', txt.decode('utf-8')).encode('ASCII','ignore')

##########################################################################

def main():
    parser = optparse.OptionParser()
    parser.add_option('--cmsname', '-n', default="1")
    parser.add_option('--delete', '-d',default=0)
    parser.add_option('--add', '-a',default=0)
    parser.add_option('--onlyifempty','-i',default="0")
    options, arguments = parser.parse_args()
    if(len(sys.argv)>=2):
        cms_name=options.cmsname
    else:
        sys.exit("None option passed. Aborting.")
######################How to check members? Get the list from siteDB

    # load blacklist
    try:
      fp = open('blacklist.ini','r')
      blacklist = eval(fp.read())
      fp.close()
    except Exception,e:
      print('Error loading blacklist configuration... Aborting.')
      exit(0)

    # load exception list
    try:
      fp = open('exceptions.ini', 'r')
      exception_dict=eval(fp.read())
      fp.close()
    except Exception,e:
      print('Error loading exceptionlist configuration... Aborting.')
      exit(0)


    # now initialize the robot
    br=init()


    print('Trying to create a squad for %s' %(cms_name))
    allSites = getSiteDBSiteNames()
    siteAlias= [x[0] for x in allSites if x[1] == cms_name]  
    list_sitedb = getCMSNamesToAdmin(siteAlias[0])
    list_sitedb=[(x[0],x[1].split()[-1],x[2]) for x in list_sitedb]

    if (len(list_sitedb)==0):
        print('Site %s not found at SiteDB database or without contacts'%(cms_name))
        sys.exit()


    # remove from list_sitedb everybody blacklisted
    try:
      site_blacklist=blacklist[cms_name]
      temp_list=[]
      for member in list_sitedb:
        aMember=" ".join(member[:-1])
        if aMember not in site_blacklist:
          temp_list.append(member)
      list_sitedb=temp_list
    except KeyError:
      print('Site %s has no blacklist'%cms_name)
    except Exception,e:
        print(e)
        exit(2)
  
    #print(list_sitedb)

    ################How to extract the members list?
    br.open(members_list)
    new_member_dict={}
    questionable_members=[]
    code_new_members=[]
    exist_savannah=[]
    to_remove_savannah=[]
    non_savannah_list=[]
    non_savannah_members=''
    contact_emails=''
    l=0
    for l in  range(len(list_sitedb)):
        member_name=" ".join(list_sitedb[l][:-1]).strip()

        print 'finding for member "%s"'%member_name
        if(member_name in exception_dict):
            member_name=exception_dict[member_name]

        if(member_name.replace(' ', '') in blacklist):
            pass
        else:
            try:
                # I will use the default "Search" interface. It is more powerfull than a regexp search in members page
                br.select_form(nr=0)
                #br["words"]=list_sitedb[l][-2]
                br["words"]=member_name
                br["type_of_search"]=['people']
                br.submit()
                research_page=br.response().read()
                try:
                    #test2=br.find_link(text_regex=".*@.*\..*", nr=0)
                    test2=br.find_link(url_regex=re.compile(".*sendmessage\.php.*"), nr=0)
                except LinkNotFoundError:
                    br.select_form(nr=0)
                    br["words"]=list_sitedb[l][-2]
                    br["type_of_search"]=['people']
                    br.submit()
                    research_page=rb_remove_accents(br.response().read())
                    search_name='<a href=\"/users/[a-zA-Z0-9.+-_]{1,}\">[a-zA-Z0-9.+-_]{1,}</a><td>%s</td>'%(member_name)
                    #This case the person has two or more accounts. I have to find one
                    p = re.compile(search_name,re.IGNORECASE)
                    temp_result_research=p.findall(research_page)
                    if (len(temp_result_research)==0):
                        br.back()
                        br.select_form(nr=0)
                        br["words"]=member_name
                        br["type_of_search"]=['people']
                        br.submit()
                        research_page=rb_remove_accents(br.response().read())
                        p = re.compile(search_name,re.IGNORECASE)
                        temp_result_research=p.findall(research_page)
                    if (len(temp_result_research)!=0):
                        for ix1 in  temp_result_research:
                            result_research=ix1.split('"')[1]
                            result_research=result_research.split('"')[0]
                            br.open('https://savannah.cern.ch'+result_research)
                            temp_test2=br.find_link(text_regex=".*@.*\..*", nr=0)
                            #imagine that in the previous page has a (I hope only one) ticket with " Problems @CERN"...
                            if (temp_test2.url.replace('/sendmessage.php?touser=', '').count('support')>=1):
                                temp_test2=br.find_link(text_regex=".*@.*\..*", nr=1)
                            savannah_username= temp_test2.base_url.replace('https://savannah.cern.ch/users/', '')
                            if (temp_test2.text.lower()==list_sitedb[l][-1].lower()):
                                questionable_members.append([member_name,savannah_username])
                            #       test2=temp_test2
                            test2=temp_test2
                    else:
                        test2=br.find_link(text_regex=".*@.*\..*", nr=0)
                        br.back()
                #imagine that in the previous page has a (I hope only one) ticket with " Problems @CERN"...
                if (test2.url.replace('/sendmessage.php?touser=', '').count('support')>=1):
                    test2=test2.url.replace('/sendmessage.php?touser=', '')
                test3=test2.url.replace('/sendmessage.php?touser=', '')
                code_new_members.append(test3)
                new_member_dict[test3]=member_name
                contact_emails=contact_emails+list_sitedb[l][-1]+','
                br.back()
            except:
                #this list contains guys that dont have savannah account
                non_savannah_list.append(member_name)
                non_savannah_members+= '  * %s %s \n' %(member_name,list_sitedb[l][-1])
    l+1
    br.open(squads_page)
    to_remove_savannah=[]
    try:
        br.follow_link(text_regex=cms_name, nr=0)
        #this is the delete form. There is registered all guys already on savannah there!
        br.select_form(nr=2)
        control = br.form.find_control("user_id[]", type="select")
        for item in control.items:
            exist_savannah.append(item.name)
        #why a try here? Some users are in Savannah and not in SiteDB...
            try:
                del new_member_dict[item.name]
            except KeyError:
                to_remove_savannah.append(item.name)
        item.selected = False
        code_new_members=new_member_dict.keys()
    except LinkNotFoundError:
        print('There is not a squad. I will create after ticket be closed')
#now lets remove guys that need to be added in cmscompinfrasup
    add_cmscompinfrasup=rb_members_not_in_group(br,cms_name,code_new_members)
    r=0
    old_member_dict_inv=new_member_dict.copy()
    for r in range(len(add_cmscompinfrasup)):
        code_new_members.remove(add_cmscompinfrasup[r])
    r=r+1
##########Preparing the ticket############
    ticket_title='Savannah squad account for %s' %(cms_name)
#None all guys with Savannah account was added or nor the guys that don't have
    if ((len(new_member_dict)!=0)|(len(non_savannah_list)!=0)):
        rb_open_ticket(br,ticket_title,cms_name,code_new_members,non_savannah_members,new_member_dict,add_cmscompinfrasup,questionable_members,contact_emails)
    else:
        print('Site %s is updated' %(cms_name))
###########################################
#if, after you checked the siteDB, look at savannah and checked that the ticket was closed, but not all savannah accounts was created...
    if(len(non_savannah_members)!=0):
        print('this site did not contact non savannah members to create an account, with codes: %s. I will abort' %(non_savannah_members))
        sys.exit()
#check, also, if after the ticket was closed, if the site has all members added in cmscompinfrasup group
    if(len(add_cmscompinfrasup)!=0):
        print('this site did not include all members in cmscompinfrasup, with codes: %s. I will abort'%(add_cmscompinfrasup))
        sys.exit()
####################################################################
#all steps done, you can now:
    br.open(squads_page)
#1)create the squad, if it is not here
    try:
        br.follow_link(text_regex=cms_name, nr=0)
    except LinkNotFoundError:
        print "rb_createsavannahsquad(cms_name)"
        print cms_name
#2)Remove guys that aren't in siteDB but were in Savannah
    print "People that will be removed from Savannah:"
    print to_remove_savannah
    if((len(to_remove_savannah)!=0)&(options.delete=="1") ):
        br.select_form(nr=2)
        br.form.set_all_readonly(False)
        br["user_id[]"]= to_remove_savannah
    #   br.submit()
#2)add people to a squad:
    for l3 in code_new_members:
        print 'adding user with code %s to the squad'%(l3)
    br.open(squads_page)
    br.follow_link(text_regex=cms_name, nr=0)
    br.select_form(nr=3)
    br.form.set_all_readonly(False)
    br["user_id[]"]= code_new_members
    if(options.add=="1"):
        if(len(code_new_members)!=0):
            print "user added"
############################################################################
##Verify if the job was done.
#what happens if all the guys aren't in cmscompinfrasup group?
    if(len(code_new_members)==0):
        pass
    else:
        if(rb_verify(br,cms_name, code_new_members)==0):
        ##Now, you have to update de last ticket:
            br.open(check_open_ticket)
            ticket_title='Savannah squad account for %s' %(cms_name)
            br.select_form(nr=0)
            br["words"]=cms_name
            br["type_of_search"]=['support']
            br.submit()
            br.follow_link(text_regex=ticket_title, nr=0)
            br.select_form(nr=1)
            br['resolution_id']=['1']
            br.submit()
            print('Ticket status changed to done')
        else:
            print('Some error occurred. Ticket status not changed')
    return

if __name__ == '__main__':
    main()
