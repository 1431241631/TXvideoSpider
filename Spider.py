import aiohttp
import asyncio
import base64
import time
import json
from bs4 import BeautifulSoup
import urllib.parse


async def http_get(url):
    """
    异步get请求
    :param url:
    :return:
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            ret = await res.text()
            return ret


async def http_post(url, data):
    """
    异步post请求
    :param data: 请求参数
    :param url: 请求地址
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        , "Content-Type": "application/x-www-form-urlencoded"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=data) as res:
            ret = await res.text()
            return json.loads(ret)


def str2base64(_str: str):
    return base64.b64encode(_str.encode('utf-8')).decode('utf-8')


class Spider:
    def __init__(self):
        self.__base_url = 'http://5.nmgbq.com/jx.php'
        self.__api_url = 'http://5.nmgbq.com/2/api.php'

    async def transform(self, url: str):
        """
        把原视频链接进行解析获取免费播放的视频
        :param url:
        :return:
        """
        referer = str2base64(self.__base_url + "?url=" + url)
        other = str2base64(url)
        ref = 0
        __time = int(time.time() * 1000)
        data = {"url": url, "referer": referer, "other": other, "ref": ref, "time": __time}
        ret = await http_post(self.__api_url, data)
        return ret

    async def search_tx(self, data: str):
        """
        爬取TX的搜索接口
        :rtype: object
        """
        data = urllib.parse.quote(data, encoding="utf-8")
        url = f'https://v.qq.com/x/search/?q={data}&stag=101&smartbox_ab='
        html = await http_get(url)
        soup = BeautifulSoup(html, 'html.parser')
        search_list = soup.select("div[r-notemplate='true'][data-index]")
        video_list = []
        for item in search_list:
            img = item.select("img[class='figure_pic']")[0]['src']
            a_el = item.select("div._infos a[_stat='video:poster_tle']")[0]
            name = a_el.find("em").get_text()
            play_url = a_el['href']
            video = {"img": img, "name": name, "play_url": play_url}
            video_list.append(video)
        return video_list

    async def play_html(self, url):
        """
        获取视频播放页面的每一集的视频链接
        :param url:
        :return:
        """
        html = await http_get(url)
        soup = BeautifulSoup(html, 'html.parser')
        search_list = soup.select("div.mod_episode a")
        video_list = []
        for item in search_list:
            href = item['href']
            episode = item.get_text().strip()
            video_list.append({"href": href, "episode": episode})
        return video_list


