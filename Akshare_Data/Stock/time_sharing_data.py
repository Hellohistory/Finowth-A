import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

router = APIRouter()


class StockMinuteRequest(BaseModel):
    symbol: str
    period: str
    adjust: str = ""


class StockRequest(BaseModel):
    symbol: str


class StockHistMinRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    period: str
    adjust: str = ""


class StockIntradayRequest(BaseModel):
    symbol: str
    date: str


class StockPreMinRequest(BaseModel):
    symbol: str
    start_time: str
    end_time: str


# 新浪财经-沪深京 A 股股票或者指数的分时数据
@router.post("/stock_zh_a_minute", operation_id="post_stock_zh_a_minute")
async def post_stock_zh_a_minute(request: StockMinuteRequest):
    """
    描述: 新浪财经-沪深京 A 股股票或者指数的分时数据
    限量: 单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据; 注意调用频率
    """
    try:
        # 获取分时数据
        stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol=request.symbol, period=request.period, adjust=request.adjust)

        # 返回数据的JSON格式
        return stock_zh_a_minute_df.to_dict(orient="records")
    except Exception as e:
        # 提供更详细的错误信息给用户
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")


# 东方财富网-沪深京 A 股-每日分时行情
@router.post("/stock_zh_a_hist_min_em", operation_id="post_stock_zh_a_hist_min_em")
async def post_stock_zh_a_hist_min_em(request: StockHistMinRequest):
    """
    描述: 东方财富网-行情首页-沪深京 A 股-每日分时行情
    限量: 单次返回指定股票、频率、复权调整和时间区间的分时数据
    """
    try:
        stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            period=request.period,
            adjust=request.adjust
        )
        return stock_zh_a_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东财财富-分时数据
@router.post("/stock_intraday_em", operation_id="post_stock_intraday_em")
async def post_stock_intraday_em(request: StockIntradayRequest):
    """
    描述: 东财财富-分时数据
    限量: 单次返回指定股票最近一个交易日的分时数据, 包含盘前数据
    """
    try:
        stock_intraday_em_df = ak.stock_intraday_em(symbol=request.symbol)
        return stock_intraday_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-日内分时数据
@router.post("/stock_intraday_sina", operation_id="post_stock_intraday_sina")
async def post_stock_intraday_sina(request: StockIntradayRequest):
    """
    描述: 新浪财经-日内分时数据
    限量: 单次返回指定交易日的分时数据；只能获取近期的数据
    """
    try:
        stock_intraday_sina_df = ak.stock_intraday_sina(symbol=request.symbol, date=request.date)
        return stock_intraday_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票行情-盘前数据
@router.post("/stock_zh_a_hist_pre_min_em", operation_id="post_stock_zh_a_hist_pre_min_em")
async def post_stock_zh_a_hist_pre_min_em(request: StockPreMinRequest):
    """
    描述: 东方财富-股票行情-盘前数据
    限量: 单次返回指定 symbol 的最近一个交易日的股票分钟数据, 包含盘前分钟数据
    """
    try:
        stock_zh_a_hist_pre_min_em_df = ak.stock_zh_a_hist_pre_min_em(
            symbol=request.symbol,
            start_time=request.start_time,
            end_time=request.end_time
        )
        return stock_zh_a_hist_pre_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_zh_a_tick_tx", operation_id="post_stock_zh_a_tick_tx")
async def post_stock_zh_a_tick_tx(request: StockRequest):
    """
    获取A股分笔行情数据
    :param request: 包含股票代码的请求体
    :return: 分笔行情数据的JSON格式
    """
    try:
        # 使用akshare获取分笔行情数据
        stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol=request.symbol)
        # 将DataFrame转换为字典格式
        data = stock_zh_a_tick_tx_js_df.to_dict(orient="records")
        return {"symbol": request.symbol, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取分笔行情数据失败: {str(e)}")
