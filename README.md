# PTT 熱門新聞文字雲生成器

這是一個用於從 PTT 熱門新聞版面爬取前十篇新聞的推文內容，並生成文字雲的 Python 程式碼。此程式碼使用了 BeautifulSoup 來解析 HTML，利用 jieba 進行中文分詞，並使用 WordCloud 和 matplotlib 生成文字雲圖像。

## 功能

- 爬取 PTT 熱門新聞版面中的前十篇熱門新聞文章的推文內容。
- 對爬取的推文內容進行分詞處理，提取關鍵詞。
- 基於關鍵詞生成文字雲，並將其顯示出來。

## 安裝

在使用此程式碼之前，請確保你已安裝以下 Python 套件。你可以使用以下命令來安裝這些套件：

```bash
pip install requests beautifulsoup4 jieba wordcloud matplotlib
==============================================================
## 使用說明
1、下載或克隆此專案

你可以使用以下命令來克隆此專案到本地：
git clone https://github.com/你的用戶名/ptt-news-wordcloud.git
cd ptt-news-wordcloud

2、準備中文字典檔案

下載 dict.txt.big 字典檔案，並將其放置在專案目錄下。

3、確保系統中有合適的字體文件

程式碼默認使用 C:\\Windows\\Fonts\\msyh.ttc 作為字體檔案。如果你在使用其他操作系統，請將 font_path 變數中的路徑更改為你的系統字體檔案路徑，或者將字體檔案放到 C:\\Windows\\Fonts\\ 目錄中。

4、運行程式

在專案目錄下運行以下命令：
python webcloud.py

程式碼將自動爬取前十篇熱門新聞的推文內容，並生成一張文字雲圖像。
