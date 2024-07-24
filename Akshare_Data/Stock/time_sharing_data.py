import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import Field, BaseModel

router = APIRouter()


class XinLangMinuteStock(BaseModel):
    symbol: str = Field(..., title="个股代码(需带有市场标识)", description="例：sh600900")
    period: str = Field(..., title="时间频率", description="可选值: 1, 5, 15, 30, 60")
    adjust: str = Field(..., title="复权形式", description="默认为空: 返回不复权的数据; "
                                                           "qfq: 返回前复权后的数据; "
                                                           "hfq: 返回后复权后的数据;")


# 新浪财经-沪深京 A 股股票/指数-分时数据
@router.post("/stock_zh_a_minute", operation_id="post_stock_zh_a_minute")
async def post_stock_zh_a_minute(request: XinLangMinuteStock):
    """
    新浪财经-沪深京 A 股股票/指数-分时数据

    接口: stock_zh_a_minute

    目标地址: http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml

    描述: 新浪财经-沪深京 A 股股票或者指数的分时数据，目前可以获取 1, 5, 15, 30, 60 分钟的数据频率, 可以指定是否复权

    限量: 单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据; 注意调用频率
    """
    try:
        stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol=request.symbol, period=request.period, adjust=request.adjust)
        stock_zh_a_minute_df.rename(columns={
            "day": "日期",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "close": "收盘价",
            "volume": "成交量"
        }, inplace=True)
        return stock_zh_a_minute_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")


class DongCaiMinuteRequest(BaseModel):
    symbol: str = Field(..., title="个股代码", description="例：000001")
    start_date: str = Field(..., title="开始日期(需精确到分钟)", description="例：2024-07-22 09:30:00")
    end_date: str = Field(..., title="结束日期(需精确到分钟)", description="例：2024-07-22 15:00:00")
    period: str = Field(..., title="时间周期", description="可选值: 1, 5, 15, 30, 60，"
                                                           "其中 1 分钟数据返回近 5 个交易日数据且不复权")
    adjust: str = Field(..., title="复权形式", description="默认为空: 返回不复权的数据; "
                                                           "qfq: 返回前复权后的数据; "
                                                           "hfq: 返回后复权后的数据;其中 1 分钟数据返回近 5 个交易日数据且不复权")


# 东方财富-沪深京 A 股-每日分时行情
@router.post("/stock_zh_a_hist_min_em", operation_id="post_stock_zh_a_hist_min_em")
async def post_stock_zh_a_hist_min_em(request: DongCaiMinuteRequest):
    """
    东方财富-沪深京 A 股-每日分时行情

    接口: stock_zh_a_hist_min_em

    目标地址: https://quote.eastmoney.com/concept/sh603777.html

    描述: 东方财富-行情首页-沪深京 A 股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置

    限量: 单次返回指定股票、频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 5 个交易日数据且不复权
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


class DongCaiDayMinute(BaseModel):
    symbol: str = Field(..., title="个股代码", description="例：000001")


# 日内分时数据-东财
@router.post("/stock_intraday_em", operation_id="post_stock_intraday_em")
async def post_stock_intraday_em(request: DongCaiDayMinute):
    """
    东财财富-日内分时数据

    接口: stock_intraday_em

    目标地址: https://quote.eastmoney.com/f1.html?newcode=0.000001

    描述: 东财财富-日内分时数据

    限量: 单次返回指定股票最近一个交易日的分时数据, 包含盘前数据
    """
    try:
        stock_intraday_em_df = ak.stock_intraday_em(symbol=request.symbol)
        return stock_intraday_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangDayMinute(BaseModel):
    symbol: str = Field(..., title="个股代码(需带有市场标识)", description="例：sh600900")
    date: str = Field(..., title="指定交易日", description="例：20230701，只能获取近期的数据")


# 新浪财经-日内分时数据
@router.post("/stock_intraday_sina", operation_id="post_stock_intraday_sina")
async def post_stock_intraday_sina(request: XinLangDayMinute):
    """
    新浪财经-日内分时数据

    接口损坏，暂无法使用

    接口: stock_intraday_sina

    目标地址: https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000001

    描述: 新浪财经-日内分时数据

    限量: 单次返回指定交易日的分时数据；只能获取近期的数据
    """
    try:
        stock_intraday_sina_df = ak.stock_intraday_sina(symbol=request.symbol, date=request.date)
        return stock_intraday_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiPanQianRequest(BaseModel):
    symbol: str = Field(..., title="个股代码", description="例：600900")
    start_time: str = Field(..., title="开始时间", description="例：09:30,默认返回所有数据")
    end_time: str = Field(..., title="结束时间", description="例：09:35,默认返回所有数据")


# 东方财富-股票行情-盘前数据
@router.post("/stock_zh_a_hist_pre_min_em", operation_id="post_stock_zh_a_hist_pre_min_em")
async def post_stock_zh_a_hist_pre_min_em(request: DongCaiPanQianRequest):
    """
    东方财富-股票行情-盘前数据

    接口: stock_zh_a_hist_pre_min_em

    目标地址: https://quote.eastmoney.com/concept/sh603777.html

    描述: 东方财富-股票行情-盘前数据

    限量: 单次返回指定个股的最近一个交易日的股票分钟数据, 包含盘前分钟数据
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


class TXTickHistoryRequest(BaseModel):
    symbol: str = Field(..., title="个股代码(需带有市场标识)", description="例：sz300494")


# 腾讯-分笔数据
@router.post("/stock_zh_a_tick_tx", operation_id="post_stock_zh_a_tick_tx")
async def post_stock_zh_a_tick_tx(request: TXTickHistoryRequest):
    """
    腾讯-分笔数据

    接口: stock_zh_a_tick_tx

    目标地址: http://gu.qq.com/sz300494/gp/detail(示例)

    描述: 每个交易日 16:00 提供当日数据; 如遇到数据缺失, 请使用stock_zh_a_tick_163接口(注意数据会有一定差异)

    限量: 单次返回最近交易日的历史分笔行情数据
    """
    try:
        stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol=request.symbol)
        data = stock_zh_a_tick_tx_js_df.to_dict(orient="records")
        return {"symbol": request.symbol, "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取分笔行情数据失败: {str(e)}")
