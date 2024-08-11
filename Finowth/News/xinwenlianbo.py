import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class NewsRequest(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240725，数据开始于20070101")


async def fetch_news(date: str):
    url = f"https://cn.govopendata.com/xinwenlianbo/{date}/"
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.select('div.heti h2.h4')
    if not news_items:
        raise HTTPException(status_code=404, detail="未找到相关的新闻数据")

    news_data = []
    for item in news_items:
        title = item.text.strip()
        content = item.find_next_sibling('p').text.strip() if item.find_next_sibling('p') else "内容缺失"
        news_data.append({'title': title, 'content': content})

    return news_data


@router.post("/news_xinwenlianbo_text", operation_id="news_xinwenlianbo_text")
async def news_xinwenlianbo_text(request: NewsRequest):
    """
    新闻_新闻联播文字稿

    接口: news_xinwenlianbo_text

    目标地址: https://cn.govopendata.com/xinwenlianbo

    描述: 新闻联播文字稿

    限量: 单次返回指定时间的新闻联播文字稿，数据开始于20070101
    """
    try:
        news_data = await fetch_news(request.date)
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"请求新闻数据时发生错误: {str(e)}")

    return news_data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
