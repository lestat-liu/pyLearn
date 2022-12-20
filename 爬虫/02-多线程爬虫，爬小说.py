import requests
from lxml import etree
import re
import pymysql
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def get_conn():
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           db="novels",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def get_xpath_resp(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)  # 用etree解析html
    return tree, resp


def get_chapters(url):
    tree, _ = get_xpath_resp(url)
    # 获取小说名字
    novel_name = tree.xpath('//*[@id="info"]/h1/text()')[0]
    # 获取小说数据节点
    dds = tree.xpath('/html/body/div[4]/dl/dd')
    title_list = []
    link_list = []
    for d in dds[:15]:
        title = d.xpath('./a/text()')[0]  # 章节标题
        title_list.append(title)
        link = d.xpath('./a/@href')[0]  # 章节链接
        chapter_url = url + link  # 构造完整链接
        link_list.append(chapter_url)
    return title_list, link_list, novel_name


def get_content(novel_name, title, url):
    try:
        cursor = None
        conn = None
        conn, cursor = get_conn()
        # 插入数据的sql
        sql = 'INSERT INTO novel(novel_name,chapter_name,content) VALUES(%s,%s,%s)'
        tree, resp = get_xpath_resp(url)
        # 获取内容
        content = re.findall('<div id="content">(.*?)</div>', resp.text)[0]
        # 对内容进行清洗
        content = content.replace('<br />', '\n').replace('&nbsp;', ' ').replace(
            '全本小说网 www.qb5.tw，最快更新<a href="https://www.qb5.tw/book_116659/">宇宙职业选手</a>最新章节！<br><br>', '')
        print(title, content)
        cursor.execute(sql, [novel_name, title, content])  # 插入数据
        conn.commit()  # 提交事务保存数据
    except:
        pass
    finally:
        sleep(2)
        close_conn(conn, cursor)  # 关闭数据库


if __name__ == '__main__':
    # 获取小说名字，标题链接，章节名称
    title_list, link_list, novel_name = get_chapters('https://www.qb5.tw/book_116659/')
    with ThreadPoolExecutor(5) as t:  # 创建5个线程
        for title, link in zip(title_list, link_list):
            t.submit(get_content, novel_name, title, link)  # 启动线程
