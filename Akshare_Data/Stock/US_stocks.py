import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, StockHistoryRequest, StockDailyRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-美股-实时行情
@router.get("/stock_us_spot_em", operation_id="get_stock_us_spot_em")
def get_stock_us_spot_em():
    """
    接口: stock_us_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#us_stocks

    描述: 东方财富网-美股-实时行情

    限量: 单次返回美股所有上市公司的实时行情数据

    请求类型: `GET`
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
    接口: stock_us_spot

    目标地址: https://finance.sina.com.cn/stock/usstock/sector.shtml

    描述: 新浪财经-美股; 获取的数据有 15 分钟延迟; 建议使用 stock_us_spot_em 端口来获取数据

    限量: 单次返回美股所有上市公司的实时行情数据，需要注意该端口数据量较大，获取时间较长，需要耐心等待

    请求类型: `GET`
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
    接口: stock_us_hist

    目标地址: https://quote.eastmoney.com/us/ENTX.html#fullScreenChart

    描述: 东方财富网-行情-美股-每日行情

    限量: 单次返回指定上市公司的指定 adjust 后的所有历史行情数据

    请求类型: `POST`
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
    接口: stock_us_hist_min_em

    目标地址: https://quote.eastmoney.com/us/ATER.html

    描述: 东方财富网-行情首页-美股-每日分时行情

    限量: 单次返回指定上市公司最近 5 个交易日分钟数据, 注意美股数据更新有延时

    请求类型: `POST`
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
    接口: stock_us_daily

    目标地址: http://finance.sina.com.cn/stock/usstock/sector.shtml

    描述: 美股历史行情数据，设定 adjust="qfq" 则返回前复权后的数据，默认 adjust="", 则返回未复权的数据，历史数据按日频率更新

    限量: 单次返回指定上市公司的指定复权类型后的所有历史行情数据

    请求类型: `POST`
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
    接口: stock_us_pink_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#us_pinksheet

    描述: 美股粉单市场的实时行情数据

    限量: 单次返回指定所有粉单市场的行情数据

    请求类型: `GET`
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
    接口: stock_us_famous_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#us_wellknown

    描述: 美股-知名美股的实时行情数据

    限量: 单次返回指定个股的行情数据

    请求类型: `POST`
    """
    try:
        stock_us_famous_spot_em_df = ak.stock_us_famous_spot_em(symbol=request.symbol)

        stock_us_famous_spot_em_df = sanitize_data(stock_us_famous_spot_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
