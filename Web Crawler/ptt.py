import urllib.request as req
def getData(url):

    #建立一個 Request物件,附加 Request Headers 的資訊
    request = req.Request(url, headers = {
        'cookie':'over18=1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    #解析原始碼,取得每篇文章的標題
    import bs4

    data = bs4.BeautifulSoup(data, "html.parser") #讓 BeautifulSoup 協助我們解析 HTML 格式文件
    titles = data.find_all('div', class_ = 'title') # 尋找所有 class = 'title' 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤(沒有被刪除), 印出來
            print(title.a.string)  # 取得標題
            print('https://www.ptt.cc' + title.a.get('href'))  # 取得連結

    # 抓取上一頁的連結
    nextLink = data.find('a',string = '‹ 上頁') #找到內文是 < 上頁的 a 標籤
    return nextLink['href']
    
pageurl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
count=0
while count<3:
    pageurl = 'https://www.ptt.cc'+ getData(pageurl)
    count+=1
