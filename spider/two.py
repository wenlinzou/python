#代码实现(二): 用Python简单处理URL
import urllib
import urllib.request
 #如果要抓取百度上面搜索关键词为Jecvay Notes的网页, 则代码如下
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
#data=data.decode('UTF-8')
print(data)