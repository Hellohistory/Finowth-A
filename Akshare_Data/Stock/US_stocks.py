import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, StockHistoryRequest, StockDailyRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-美股-实时行情
@router.get("/stock_us_spot_em", operation_id="get_stock_us_spot_em")
def get_stock_us_spot_em():
    """
    描述: 东方财富网-美股-实时行情
    限量: 单次返回美股所有上市公司的实时行情数据
    """
    try:
        stock_us_spot_em_df = ak.stock_us_spot_em()
        data = stock_us_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-美股-实时行情
@router.get("/stock_us_spot", operation_id="get_stock_us_spot")
def get_stock_us_spot():
    """
    描述: 新浪财经-美股; 获取的数据有 15 分钟延迟
    限量: 单次返回美股所有上市公司的实时行情数据
    """
    try:
        us_stock_current_df = ak.stock_us_spot()
        return us_stock_current_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-美股-每日行情
@router.post("/stock_us_hist", operation_id="post_stock_us_hist")
async def post_stock_us_hist(request: StockHistoryRequest):
    """
    描述: 东方财富网-行情-美股-每日行情
    限量: 单次返回指定上市公司的指定 adjust 后的所有历史行情数据
    """
    try:
        stock_us_hist_df = ak.stock_us_hist(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_us_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-美股-每日分时行情
@router.post("/stock_us_hist_min_em", operation_id="post_stock_us_hist_min_em")
async def post_stock_us_hist_min_em(request: SymbolRequest):
    """
    描述: 东方财富网-行情首页-美股-每日分时行情
    限量: 单次返回指定上市公司最近 5 个交易日分钟数据
    """
    try:
        stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol=request.symbol)
        return stock_us_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-美股-历史行情数据
@router.post("/stock_us_daily", operation_id="post_stock_us_daily")
async def post_stock_us_daily(request: StockDailyRequest):
    """
    描述: 美股历史行情数据
    限量: 单次返回指定上市公司的指定 adjust 后的所有历史行情数据
    """
    try:
        stock_us_daily_df = ak.stock_us_daily(symbol=request.symbol, adjust=request.adjust)
        return stock_us_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美股粉单市场的实时行情数据
@router.get("/stock_us_pink_spot_em", operation_id="get_stock_us_pink_spot_em")
def get_stock_us_pink_spot_em():
    """
    描述: 美股粉单市场的实时行情数据
    限量: 单次返回所有粉单市场的行情数据
    """
    try:
        stock_us_pink_spot_em_df = ak.stock_us_pink_spot_em()
        data = stock_us_pink_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美股-知名美股的实时行情数据
@router.post("/stock_us_famous_spot_em", operation_id="post_stock_us_famous_spot_em")
async def post_stock_us_famous_spot_em(request: SymbolRequest):
    """
    描述: 美股-知名美股的实时行情数据
    限量: 单次返回指定 symbol 的行情数据
    """
    try:
        stock_us_famous_spot_em_df = ak.stock_us_famous_spot_em(symbol=request.symbol)

        stock_us_famous_spot_em_df = sanitize_data(stock_us_famous_spot_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
