# 本项目致力于使用fastapi封装开源金融数据库，以下是目前支持的开源库

- [Akshare](https://github.com/akfamily/akshare/tree/main)

本项目支持所有数据的缓存工作，缓存方式为如下方案：
1. 请求缓存：每一次有用户请求某接口数据以后，都会缓存到本地，下次请求时直接从本地读取数据，减少请求数据的访问次数，提高效率。
2. 时间缓存：支持用户自定义时间，默认为1天，超过时间后，会重新请求数据，并更新缓存。
3. 不进行缓存：当用户设置不需要缓存时，会直接请求数据，不进行缓存。