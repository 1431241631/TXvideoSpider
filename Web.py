# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 14:46
# @Author  : #
# @File    : Web.py
# @Software: PyCharm
# web服务

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from Spider import Spider

app = FastAPI()
# 配置跨域访问
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 实例化爬虫
Spider = Spider()


# 搜索接口
@app.get("/api/search")
async def search(data: str):
    ret = await Spider.search_tx(data)
    return ret


# 获取视频
@app.get("/api/getvideo")
async def getvideo(url: str):
    ret = await Spider.transform("https://v.qq.com" + url)
    return ret


# 获取视频列表
@app.post("/api/videolist")
async def get_video_list(url: str = Form(None)):
    ret = await Spider.play_html(url)
    return ret


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
