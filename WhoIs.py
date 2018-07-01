import os


def WhoIs(domain_name):
    command='WhoIs'+ domain_name
    result=os.popen(command)
    data=str(result.read())
    return  data