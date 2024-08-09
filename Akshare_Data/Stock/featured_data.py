import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class TFDateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20230808")


# 东方财富-数据中心-特色数据-停复牌信息
@router.post("/stock_tfp_em", operation_id="stock_tfp_em")
async def stock_tfp_em(request: TFDateRequest):
    """
    东方财富-特色数据-停复牌信息

    接口: stock_tfp_em

    目标地址: https://data.eastmoney.com/tfpxx/

    描述: 东方财富-数据中心-特色数据-停复牌信息

    限量: 单次获取指定时间的停复牌数据, 具体更新逻辑跟目标网页统一
    """
    try:
        stock_tfp_em = ak.stock_tfp_em(date=request.date)
        stock_tfp_em_df = sanitize_data_pandas(stock_tfp_em)
        return stock_tfp_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 百度股市通-交易提醒-停复牌
@router.post("/news_trade_notify_suspend_baidu", operation_id="news_trade_notify_suspend_baidu")
async def news_trade_notify_suspend_baidu(request: TFDateRequest):
    """
    百度股市通-交易提醒-停复牌

    接口: news_trade_notify_suspend_baidu

    目标地址: https://gushitong.baidu.com/calendar

    描述: 百度股市通-交易提醒-停复牌

    限量: 单次获取指定时间的停复牌数据, 提供港股的停复牌数据
    """
    try:
        news_trade_notify_suspend_baidu = ak.news_trade_notify_suspend_baidu(date=request.date)
        news_trade_notify_suspend_baidu_df = sanitize_data_pandas(news_trade_notify_suspend_baidu)
        return news_trade_notify_suspend_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 百度股市通-交易提醒-分红派息
@router.post("/news_trade_notify_dividend_baidu", operation_id="news_trade_notify_dividend_baidu")
async def news_trade_notify_dividend_baidu(request: TFDateRequest):
    """
    百度股市通-交易提醒-分红派息

    接口: news_trade_notify_dividend_baidu

    目标地址: https://gushitong.baidu.com/calendar

    描述: 百度股市通-交易提醒-分红派息

    限量: 单次获取指定时间的分红派息数据, 提供港股的分红派息数据
    """
    try:
        news_trade_notify_dividend_baidu_ = ak.news_trade_notify_dividend_baidu(date=request.date)
        news_trade_notify_dividend_baidu_df = sanitize_data_pandas(news_trade_notify_dividend_baidu_)
        return news_trade_notify_dividend_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
