import requests
import os

def download_pdf(url, filename):
    # 发送HTTP GET请求
    response = requests.get(url)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 获取当前目录
        current_directory = os.getcwd()
        # 构建文件路径
        file_path = os.path.join(current_directory, filename)
        
        # 将内容写入文件
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"PDF文件已成功下载并保存为: {file_path}")
    else:
        print(f"下载失败，HTTP状态码: {response.status_code}")

# 使用函数下载PDF
url = "https://static.cninfo.com.cn/finalpage/2024-06-06/1220273635.PDF"
filename = "1220323723.PDF"
download_pdf(url, filename)
