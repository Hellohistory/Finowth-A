from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field
import Finowth

router = APIRouter()


class NewsRequest(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240725，数据开始于20070101")


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
        # 调用抓取函数获取新闻数据
        news_data = Finowth.finowth_data.news.news_xinwenlianbo_text(request.date)
        return {"date": request.date, "data": news_data}

    except HTTPException as e:
        # 返回HTTP异常
        raise e
    except Exception as e:
        # 其他异常处理
        raise HTTPException(status_code=500, detail=f"未知错误: {e}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
