import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class MacroInfoWS(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240514")


# 全球宏观-宏观日历
@router.post("/macro_info_ws", operation_id="post_macro_info_ws")
async def post_macro_info_ws(request: MacroInfoWS):
    """
    全球宏观-宏观日历

    接口: macro_info_ws

    目标地址: https://wallstreetcn.com/calendar

    描述: 华尔街见闻-日历-宏观

    限量: 单次返回指定时间的数据
    """
    try:
        macro_info_ws = ak.macro_info_ws(date=request.date)
        macro_info_ws_df = sanitize_data_pandas(macro_info_ws)

        return macro_info_ws_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 全球宏观-全球宏观事件
@router.post("/news_economic_baidu", operation_id="post_news_economic_baidu")
async def post_news_economic_baidu(request: MacroInfoWS):
    """
    全球宏观-宏观日历

    接口: news_economic_baidu

    目标地址: https://gushitong.baidu.com/calendar

    描述: 全球宏观指标重大事件

    限量: 单次返回指定时间的数据
    """
    try:
        news_economic_baidu = ak.news_economic_baidu(date=request.date)
        news_economic_baidu_df = sanitize_data_pandas(news_economic_baidu)

        return news_economic_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
