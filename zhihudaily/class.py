import urllib.request as http
import json
import re #正则表达式

class APIMgr:
    def __init__(self):
        self.apiLatest='http://news-at.zhihu.com/api/3/news/latest'
        self.apiBefore='http://news.at.zhihu.com/api/3/news/before/'
        self.apiID='http://news-at.zhihu.com/api/3/news/'
    def access(self,url):
        return http.urlopen(url).decode('gb2312')
    def getLatestNews(self):
        return self.access(self.apiLatest)
    def getBeoreNews(self,date):
        return self.access(self.apiBefore+date)
    def getAssignedNews(self,id_):
        return self.access(self.apiID+id_)

class NewsMgr:
    def __init__(self,newsData):
        self.data=newsData
    def parse(slef):
        return json.load(self.data)
    def getType(self):
        return self.data['type']
    def getID(self):
        return self.data['id']
    def getCSS(self):
        return self.data['css'][0]
    def getBody(self):
        return self.data['body']
    def getImageSource(self):
        return self.data['date']
    def getTitle(self):
        return self.data['stories']
    def getShareUrl(self):
        return self.data['share_url']
    def getGaOrefix(self):
        return self.data['ga_prefix']
    def __repr__(self):
        return self.parse()
    
class SingleNews(NewsMgr):
    def  __init__(self,apimgr,id_):
        NewsMgr.__init__(self,apimgr.getAssignedNews(id_))
    def getImages(self):return self.data['image']
    def __len__(self):
        return len(self.getBody())
        
class AllDateNews(NewsMgr):
    def __init__(self,apimgr,date=''):
        if len(date)==0:
            NewsMgr.__init__(self,apimgr.getLatestNews())
        elif self.dateIsLegal(date):
            NewsMgr.__init__(self,apimgr.getBeoreNews(date))
        else:
            raise 'DateError:date is not legal' 
    def getImages(self):return self.data['images'][0]
    def getNewsNum(self):
        return len(self.data['stories'])
    def getDate(self):
        return self.data['date']
    def getStories(self):
        return self.data['stories']
    def __len__(self):
        return self.getNewsNum()
    def dateIsLegal(self,date):
        return re.match(r'(?!0000)[0-9]{4}[0-9]{4}',date)

if __name__=='__main__':
    apimgr=APIMgr()
    single=SingleNews(apimgr,'20')
    allnews=AllDateNews(apimgr)
    print(single)
    print(allnews)
