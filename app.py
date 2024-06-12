import requests
from bs4 import BeautifulSoup

def fetch_visible_text(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    
    # 检查请求是否成功
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
    
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 提取所有可见的文本
    # 这里假设网页的主要内容在<div>标签中
    main_content = soup.find('div', {'id': 'content'})
    
    if main_content:
        # 获取文本并打印
        visible_text = main_content.get_text(separator='\n', strip=True)
        print(visible_text.replace("九九藏书","").replace("99lib•net","").replace("九*九*藏*书*网","").replace("ｈｔtp://wｗｗ•９９ｌｉb.neｔ","").replace("；sophia",""))
    else:
        print("Could not find the main content on the page.")

# 示例使用
url = 'https://www.99csw.com/book/9772/350183.htm'
fetch_visible_text(url)
