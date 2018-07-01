import os
from urllib.parse import urlparse

def Directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def File(file,data):
    f=open(file,'w')
    f.write(data)
    f.close()


def Domain(url):
    re=urlparse(url)
    return  re

