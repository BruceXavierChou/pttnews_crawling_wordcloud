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

