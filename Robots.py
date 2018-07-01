from urllib import request
import io


def get_robots(url):
    if url.endswith('/'):
        path=url
    else:
        path=url+'/'

    req= request.urlopen( path+'robot.txt',data=None)
    data=io.TextIOWrapper(req,encoding='utf-8')
    return  data.read()
