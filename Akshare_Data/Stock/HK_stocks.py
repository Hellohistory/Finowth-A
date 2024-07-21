import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import StockHistoryRequest, StockDailyRequest, StockMinuteRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-港股-实时行情
@router.get("/stock_hk_spot_em", operation_id="get_stock_hk_spot_em")
def get_stock_hk_spot_em():
    """
    接口: stock_hk_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#hk_stocks

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
@router.get("/stock_hk_main_board_spot_em", operation_id="get_stock_hk_main_board_spot_em")
def get_stock_hk_main_board_spot_em():
    """
    接口: stock_hk_main_board_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_mainboard

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
@router.get("/stock_hk_spot", operation_id="get_stock_hk_spot")
def get_stock_hk_spot():
    """
    港股-实时行情数据是从新浪财经获取的数据, 更新频率为实时, 由于新浪服务器因素行情延时 15 分钟

    接口: stock_hk_spot

    目标地址: http://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk

    描述: 获取所有港股的实时行情数据 15 分钟延时

    限量: 单次返回当前时间戳的所有港股的数据
    """
    try:
        stock_hk_spot_df = ak.stock_hk_spot()
        return stock_hk_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-港股-每日分时行情
@router.post("/stock_hk_hist_min_em", operation_id="post_stock_zh_ah_spot")
async def post_stock_hk_hist_min_em(request: StockMinuteRequest):
    """
    接口: stock_hk_hist_min_em

    目标地址: http://quote.eastmoney.com/hk/00948.html

    描述: 东方财富网-行情首页-港股-每日分时行情

    限量: 单次返回指定上市公司最近 5 个交易日分钟数据, 注意港股有延时
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
@router.post("/stock_hk_hist", operation_id="post_stock_hk_hist")
async def post_stock_hk_hist(request: StockHistoryRequest):
    """
    接口: stock_hk_hist

    目标地址: https://quote.eastmoney.com/hk/08367.html

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
@router.post("/stock_hk_daily", operation_id="post_stock_hk_daily")
async def post_stock_hk_daily(request: StockDailyRequest):
    """
    接口: stock_hk_daily

    目标地址: http://stock.finance.sina.com.cn/hkstock/quotes/01336.html(个例)

    描述:港股-历史行情数据, 可以选择返回复权后数据,更新频率为日频

    限量: 单次返回指定上市公司的历史行情数据(包括前后复权因子), 提供新浪财经拥有的该股票的所有数据(
    并不等于该股票从上市至今的数据)
    """
    try:
        stock_hk_daily_df = ak.stock_hk_daily(symbol=request.symbol, adjust=request.adjust)
        return stock_hk_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
