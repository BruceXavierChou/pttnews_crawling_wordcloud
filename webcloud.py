from bs4 import BeautifulSoup
import requests
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba.analyse as analyse
import os
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 設定重試策略
retry_strategy = Retry(
    total=3,  # 重試總次數
    backoff_factor=1,  # 等待時間間隔的倍數
    status_forcelist=[429, 500, 502, 503, 504],  # 需要重試的狀態碼
    allowed_methods=["HEAD", "GET", "OPTIONS"]  # 新版用法
)

# 添加重試適配器到請求會話
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

# 挂上 headers 模擬使用者讀取網頁的行為
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

# 目標網站
url = 'https://www.pttweb.cc/hot/news/today'
# 發出 GET 請求
resp = http.get(url, headers=headers)
# 網頁編碼
resp.encoding = 'utf-8'
# 透過 BeautifulSoup 進行網頁解析
soup = BeautifulSoup(resp.text, 'html.parser')
# 找出所有 div 區塊中帶有目標 class 名的元素
divs = soup.find_all('div', 'e7-right-top-container e7-no-outline-all-descendants')
# 新增一個 list 存取爬下來的內容
articles = []
# 網頁根目錄
root = 'https://www.ptt.cc'
for div in divs:
    link = div.find('a')['href']
    title = div.find('span', 'e7-show-if-device-is-not-xs').text
    articles.append({
        'title': title.replace('\u3000', ' '),
        'link': root + link + '.html'
    })

# 爬取每篇文章的內容
for article in articles:
    res = http.get(article['link'], headers={'cookie': 'over18=1;'})
    time.sleep(random.uniform(1, 3))  # 隨機延遲1到3秒
    if res.status_code == 404:
        articles.remove(article)
        continue
    else:
        soup = BeautifulSoup(res.text, 'lxml')
        main = soup.find('div', id='main-content')
        if main is None:
            print(f"Warning: 'main-content' not found in {article['link']}")
            continue
        main_tag = main.find_all('div', class_='push')
        # 新增一個位置存取文章的推文內容
        comment = []

        for i in main_tag:
            # 如果沒有推文就跳過
            if not i.find('span', 'push-tag'):
                continue
            # 把: 標點符號替換掉
            push_content = i.find('span', 'push-content').text.replace(': ', "")
            # 推文內容存入
            comment.append(push_content)
        article['content'] = comment

# 確認字典文件路徑
dict_path = os.path.join(os.path.dirname(__file__), 'dict.txt.big')
if not os.path.exists(dict_path):
    raise FileNotFoundError(f"{dict_path} 文件不存在，請確認路徑是否正確。")

# 設定 jieba 字典
jieba.set_dictionary(dict_path)

# 合併前十篇熱門新聞的內容
all_content = []
for article in articles[:10]:
    if 'content' not in article:
        print(f"Skipping article due to no content: {article['title']}")
        continue
    all_content.extend(article['content'])

# 將所有內容合併成一個字串
content_text = " ".join(all_content)

# 提取關鍵詞及其權重
tfidf_fre = jieba.analyse.extract_tags(content_text, topK=100, withWeight=True, allowPOS=())
# 將分析完的詞頻輸出成字典
count_dic = {word: weight for word, weight in tfidf_fre}

# 確認字體文件路徑
font_path = 'C:\\Windows\\Fonts\\msyh.ttc'
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found at {font_path}, please check the path.")

# 生成文字雲
myWordCloud = WordCloud(
    width=1200,  # 圖的寬度
    height=600,  # 圖的長度
    background_color="black",  # 背景顏色 默認是白色
    colormap="Dark2",
    font_path=font_path  # 使用系統字體路徑
).fit_words(count_dic)

# 用 plt 顯示文字雲
plt.figure(figsize=(8, 6), dpi=100)
plt.imshow(myWordCloud)
plt.axis("off")
plt.show()

