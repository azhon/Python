from urllib import request
from bs4 import BeautifulSoup as bs


# 文章对象
class jjArticle(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def to_string(self):
        return "文章标题：" + self.title + "\n" + "文章链接：" + self.url


# 首页地址
jjUrl = "https://juejin.im/welcome/android"
# 详情地址
jjDetails = "https://juejin.im"

user_agent = "User-Agent"
user_agent_value = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"

resp = request.Request(jjUrl)
# 模拟浏览器
resp.add_header(user_agent, user_agent_value)
resp = request.urlopen(resp)
# 网页返回的数据
htmlCode = resp.read().decode("utf-8")
# print(htmlCode)
# 格式化html
soup = bs(htmlCode, "html.parser")
# 输出格式化好的html内容
# print(soup.prettify())

# 分析html得 获取a标签内class属性为title的元素 即为文章的标题
articleList = soup.find_all("a", {"class", "title"})
# 获取到的所有文章标题
allArticle = []
for article in articleList:
    url = article.get("href")
    # 创建一个保存文章的对象
    article = jjArticle(article.string, jjDetails + url)
    allArticle.append(article)

for article in allArticle:
    print(article.to_string(), "\n")
