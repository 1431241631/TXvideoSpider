# TXvideoSpider
爬取免费视频解析接口解析TX视频
# 演示地址
[演示地址](http://39.107.226.153/)
# 项目思路
百度有很多免费的视频解析接口，可以解析很多网站的VIP视频，但是他们的网站都是提交源播放网址再进行解析。  
于是就有了直接爬取对应网站的搜索功能和视频解析接口对接起来  
搜索关键字即可解析视频
# 项目概述
项目分为爬虫和Web后台  
全异步架构  
爬虫使用aiohttp库进行异步请求  
Web使用fastapi做后台
# 项目结构
## Spider.py
爬虫  
用来爬取解析接口和视频网站的搜索接口  
## Web.py
后台  
用来提供api给前台访问
# 效果展示
本项目并未提供前台  
因为我前台太水就不扔出来了  
随便写了个效果  
![首页](https://minami373-1251572732.cos.ap-beijing.myqcloud.com/1.jpg)  
![搜索](https://minami373-1251572732.cos.ap-beijing.myqcloud.com/2.jpg)
![播放](https://minami373-1251572732.cos.ap-beijing.myqcloud.com/3.jpg)

# 个人博客
[浇花的个人主页](http://baoyue.vip)
