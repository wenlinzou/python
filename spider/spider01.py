import re
import urllib.request
import urllib
 
from collections import deque
 #用到的数据结构简介以及爬虫Ver1.0 alpha
#  在爬虫程序中, 为了不重复爬那些已经爬过的网站, 我们需要把爬过的页面的url放进集合中, 在每一次要爬某一个url之前, 先看看集合里面是否已经存在. 如果已经存在, 我们就跳过这个url; 如果不存在, 我们先把url放入集合中, 然后再去爬这个页面.
# Python提供了set这种数据结构. set是一种无序的, 不包含重复元素的结构. 一般用来测试是否已经包含了某元素, 或者用来对众多元素们去重. 与数学中的集合论同样, 他支持的运算有交, 并, 差, 对称差.
# 创建一个set可以用 set() 函数或者花括号 {} . 但是创建一个空集是不能使用一个花括号的, 只能用 set() 函数. 因为一个空的花括号创建的是一个字典数据结构. 以下同样是Python官网提供的示例.

queue = deque()
visited = set()
 
url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
 
queue.append(url)
cnt = 0
 
while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问
 
  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1
  urlop = urllib.request.urlopen(url)
  if 'html' not in urlop.getheader('Content-Type'):
    continue
 
  # 避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read().decode('utf-8')
  except:
    continue
 
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile('href=\"(.+?)\"')
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)
      print('加入队列 --->  ' + x)
#爬虫是可以工作了, 但是在碰到连不上的链接的时候,
#它并不会超时跳过. 而且爬到的内容并没有进行处理, 没有获取对我们有价值的信息,
#也没有保存到本地. 下次我们可以完善这个alpha版本.
