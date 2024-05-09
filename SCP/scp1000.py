'scp'
from selenium import webdriver
from selenium.webdriver.common.by import By
import easygui
from bs4 import BeautifulSoup
from tqdm import tk
from selenium.webdriver.edge.options import Options
tmp = {}
options = Options()
def a(b):
    B = str(b)  # 将B转换为字符串以便进行长度检查和填充

    if len(B) == 1:  # 如果B是一位数
        B = '00' + B  # 在前面添加两个零
    elif len(B) == 2:  # 如果B是两位数
        B = '0' + B  # 在前面添加一个零
        
    return B
# 设置窗口不显示
options.add_argument("--headless")

driver=webdriver.Edge(options=options)
def scp(scp):
    driver.get(f'view-source:https://scp-wiki.wikidot.com/scp-{scp}')
    content = driver.find_element(By.XPATH, "/html/body/table/tbody").text
    content =  BeautifulSoup(content, 'lxml')
    content = content.find(id='main-content')
    return content.text
b = 1930
while b != 2000:
    tmp['scp'] =  b
    tmp['content'] = str(scp(a(b)))
    print(tmp)
    with open('scp.txt', 'a', encoding='utf-8') as f:
        f.write(str(tmp))
        f.write('\n')
    b += 1