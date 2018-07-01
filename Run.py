from Domain_Name import *
from IP_Address import *
from Nmap import *
from Robots import *
from WebScanner import *
from WhoIs import *


ROOT_DIR='companies/'
Directory(ROOT_DIR)


def gather_info(name,url):
    domain_name=Get_Domain(url)
    ip_addres=get_ipAddress(domain_name)
    nmap=Nmap('-F',ip_addres)
    robot=get_robots(url)
    who=WhoIs(url)
    create_report(name,url,domain_name,nmap,robot,who)


def create_report(name,url,domain_name,namp,robot,who):
    project_dir=ROOT_DIR+'/'+name
    Directory(project_dir)
    File(project_dir,url)
    File(project_dir, domain_name)
    File(project_dir, namp)
    File(project_dir, robot)
    File(project_dir, who)
