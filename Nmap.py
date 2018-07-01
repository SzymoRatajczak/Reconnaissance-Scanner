import os


def Nmap(kind_of_scanning,ip_address):
    command='Nmap'+kind_of_scanning+' ' + ip_address
    process=os.popen(command)
    result=str(process.read())
    return result