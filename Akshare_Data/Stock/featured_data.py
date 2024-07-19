import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DateRequest(BaseModel):
    date: str


# 东方财富网-数据中心-特色数据-停复牌信息
@router.post("/stock_tfp_em")
def get_stock_tfp_em(request: DateRequest):
    """
    描述: 东方财富网-数据中心-特色数据-停复牌信息
    限量: 单次获取指定 symbol 的停复牌数据
    """
    try:
        stock_tfp_em_df = ak.stock_tfp_em(date=request.date)
        return stock_tfp_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 百度股市通-交易提醒-停复牌
@router.post("/news_trade_notify_suspend_baidu")
def get_news_trade_notify_suspend_baidu(request: DateRequest):
    """
    描述: 百度股市通-交易提醒-停复牌
    限量: 单次获取指定 symbol 的停复牌数据, 提供港股的停复牌数据
    """
    try:
        news_trade_notify_suspend_baidu_df = ak.news_trade_notify_suspend_baidu(date=request.date)
        return news_trade_notify_suspend_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 百度股市通-交易提醒-分红派息
@router.post("/news_trade_notify_dividend_baidu")
def get_news_trade_notify_dividend_baidu(request: DateRequest):
    """
    描述: 百度股市通-交易提醒-分红派息
    限量: 单次获取指定 symbol 的分红派息数据, 提供港股的分红派息数据
    """
    try:
        news_trade_notify_dividend_baidu_df = ak.news_trade_notify_dividend_baidu(date=request.date)
        # 清洗数据
        sanitized_df = sanitize_data_pandas(news_trade_notify_dividend_baidu_df)

        return sanitized_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
