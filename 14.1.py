import urllib.request

req = urllib.request.Request("http://focus.tianya.cn")
res = urllib.request.urlopen(req)
html = res.read(320)
print(html.decode("utf-8"))
res.close()

'''
import requests
def getHTMLText(url):
    r=requests.get(url,timeout=15)
    r.raise_for_status()
    r.encoding='utf-8' # utf-8
    return r.text[:320]


url = "http://focus.tianya.cn"
text=getHTMLText(url)
print(text)
'''
