import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


class StockHistoryRequest(BaseModel):
    symbol: str
    period: str
    start_date: str
    end_date: str
    adjust: str = ""


class StockMinuteRequest(BaseModel):
    symbol: str
    period: str
    adjust: str
    start_date: str
    end_date: str


class StockDailyRequest(BaseModel):
    symbol: str
    adjust: str = ""


# 东方财富网-港股-实时行情
@router.get("/stock_hk_spot_em")
def get_stock_hk_spot_em():
    """
    描述: 所有港股的实时行情数据; 该数据有 15 分钟延时
    限量: 单次返回最近交易日的所有港股的数据
    """
    try:
        stock_hk_spot_em_df = ak.stock_hk_spot_em()
        sanitized_data = stock_hk_spot_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 港股主板实时行情数据-东财
@router.get("/stock_hk_main_board_spot_em")
def get_stock_hk_main_board_spot_em():
    """
    描述: 港股主板的实时行情数据; 该数据有 15 分钟延时
    限量: 单次返回港股主板的数据
    """
    try:
        stock_hk_main_board_spot_em_df = ak.stock_hk_main_board_spot_em()
        sanitized_data = stock_hk_main_board_spot_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-港股-实时行情
@router.get("/stock_hk_spot")
def get_stock_hk_spot():
    """
    描述: 获取所有港股的实时行情数据 15 分钟延时
    限量: 单次返回当前时间戳的所有港股的数据
    """
    try:
        stock_hk_spot_df = ak.stock_hk_spot()
        return stock_hk_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-港股-每日分时行情
@router.post("/stock_hk_hist_min_em")
def get_stock_hk_hist_min_em(request: StockMinuteRequest):
    """
    描述: 东方财富网-行情首页-港股-每日分时行情
    限量: 单次返回指定上市公司最近 5 个交易日分钟数据
    """
    try:
        stock_hk_hist_min_em_df = ak.stock_hk_hist_min_em(
            symbol=request.symbol,
            period=request.period,
            adjust=request.adjust,
            start_date=request.start_date,
            end_date=request.end_date
        )
        return stock_hk_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-港股-历史行情数据
@router.post("/stock_hk_hist")
def get_stock_hk_hist(request: StockHistoryRequest):
    """
    描述: 港股-历史行情数据, 可以选择返回复权后数据, 更新频率为日频
    限量: 单次返回指定上市公司的历史行情数据
    """
    try:
        stock_hk_hist_df = ak.stock_hk_hist(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_hk_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-港股-历史行情数据
@router.post("/stock_hk_daily")
def get_stock_hk_daily(request: StockDailyRequest):
    """
    描述: 港股-历史行情数据, 可以选择返回复权后数据, 更新频率为日频
    限量: 单次返回指定上市公司的历史行情数据
    """
    try:
        stock_hk_daily_df = ak.stock_hk_daily(symbol=request.symbol, adjust=request.adjust)
        return stock_hk_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
