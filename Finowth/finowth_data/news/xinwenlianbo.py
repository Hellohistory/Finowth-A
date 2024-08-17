#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/8/16
Desc: 新闻联播文字稿抓取
https://cn.govopendata.com/xinwenlianbo
"""

import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException


def news_xinwenlianbo_text(date: str):
    url = f"https://cn.govopendata.com/xinwenlianbo/{date}/"

    try:
        # 请求数据
        response = requests.get(url)
        response.encoding = 'utf-8'
        response.raise_for_status()
    except requests.RequestException as e:
        # 请求失败时抛出异常
        raise HTTPException(status_code=500, detail=f"请求失败: {e}")

    try:
        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.select('div.heti h2.h4')

        if not news_items:
            # 如果没有找到新闻数据，抛出404异常
            raise HTTPException(status_code=404, detail="未找到相关的新闻数据")

        # 提取新闻标题和内容
        news_data = []
        for item in news_items:
            title = item.text.strip()
            next_paragraph = item.find_next_sibling('p')
            content = next_paragraph.text.strip() if next_paragraph else "内容缺失"
            news_data.append({'title': title, 'content': content})

        return news_data

    except Exception as e:
        # 处理解析过程中可能出现的异常
        raise HTTPException(status_code=500, detail=f"数据解析失败: {e}")


if __name__ == "__main__":
    news_xinwenlianbo_text = news_xinwenlianbo_text(date="20240816")
    print(news_xinwenlianbo_text)
