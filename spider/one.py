
#encoding:UTF-8
#V代码实现(一): 用Python抓取指定页面
import urllib.request
 
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
print(data)