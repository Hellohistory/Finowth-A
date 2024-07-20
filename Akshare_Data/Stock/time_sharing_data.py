import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, SymbolDateRequest, RestrictedReleaseSummaryRequest, \
    SymbolPeriodAdjust, StockMinuteRequest

router = APIRouter()


# 新浪财经-沪深京 A 股股票或者指数的分时数据
@router.post("/stock_zh_a_minute", operation_id="post_stock_zh_a_minute")
async def post_stock_zh_a_minute(request: SymbolPeriodAdjust):
    """
    接口: stock_zh_a_minute

    目标地址: http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml

    描述: 新浪财经-沪深京 A 股股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率, 可以指定是否复权

    限量: 单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据; 注意调用频率

    请求类型: `POST`
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
async def post_stock_zh_a_hist_min_em(request: StockMinuteRequest):
    """
    接口: stock_zh_a_hist_min_em

    目标地址: https://quote.eastmoney.com/concept/sh603777.html

    描述: 东方财富网-行情首页-沪深京 A 股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置

    限量: 单次返回指定股票、频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 5 个交易日数据且不复权

    请求类型: `POST`
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
async def post_stock_intraday_em(request: SymbolDateRequest):
    """
    接口: stock_intraday_em

    目标地址: https://quote.eastmoney.com/f1.html?newcode=0.000001

    描述: 东财财富-分时数据

    限量: 单次返回指定股票最近一个交易日的分时数据, 包含盘前数据

    请求类型: `POST`
    """
    try:
        stock_intraday_em_df = ak.stock_intraday_em(symbol=request.symbol)
        return stock_intraday_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-日内分时数据
@router.post("/stock_intraday_sina", operation_id="post_stock_intraday_sina")
async def post_stock_intraday_sina(request: SymbolDateRequest):
    """
    接口: stock_intraday_sina

    目标地址: https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000001

    描述: 新浪财经-日内分时数据

    限量: 单次返回指定交易日的分时数据；只能获取近期的数据

    请求类型: `POST`
    """
    try:
        stock_intraday_sina_df = ak.stock_intraday_sina(symbol=request.symbol, date=request.date)
        return stock_intraday_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票行情-盘前数据
@router.post("/stock_zh_a_hist_pre_min_em", operation_id="post_stock_zh_a_hist_pre_min_em")
async def post_stock_zh_a_hist_pre_min_em(request: RestrictedReleaseSummaryRequest):
    """
    接口: stock_zh_a_hist_pre_min_em

    目标地址: https://quote.eastmoney.com/concept/sh603777.html

    描述: 东方财富-股票行情-盘前数据

    限量: 单次返回指定个股的最近一个交易日的股票分钟数据, 包含盘前分钟数据

    请求类型: `POST`
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
async def post_stock_zh_a_tick_tx(request: SymbolRequest):
    """
    接口: stock_zh_a_tick_tx

    目标地址: http://gu.qq.com/sz300494/gp/detail(示例)

    描述: 每个交易日 16:00 提供当日数据; 如遇到数据缺失, 请使用 **stock_zh_a_tick_163** 接口(注意数据会有一定差异)

    限量: 单次返回最近交易日的历史分笔行情数据

    请求类型: `POST`
    """
    try:
        # 使用akshare获取分笔行情数据
        stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol=request.symbol)
        # 将DataFrame转换为字典格式
        data = stock_zh_a_tick_tx_js_df.to_dict(orient="records")
        return {"symbol": request.symbol, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取分笔行情数据失败: {str(e)}")
