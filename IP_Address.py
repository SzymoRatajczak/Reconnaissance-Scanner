import os

def get_ipAddress(domain_name):
    command='host'+domain_name
    process=os.popen(command)
    result=str(process.read())
    marker=result.find('has address')+12
    return  result[marker:].splitlines()[0]

 