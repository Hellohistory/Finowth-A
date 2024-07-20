import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas, sanitize_data

router = APIRouter()


class StockHistoryRequest(BaseModel):
    symbol: str
    period: str = "daily"
    start_date: str
    end_date: str
    adjust: str = ""


# 东方财富-沪深京 A 股日频率数据
@router.post("/stock_zh_a_hist", operation_id="post_stock_zh_a_hist")
def get_stock_zh_a_hist(request: StockHistoryRequest):
    """
    描述: 东方财富-沪深京 A 股日频率数据
    限量: 单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据
    """
    try:
        stock_zh_a_hist_df = ak.stock_zh_a_hist(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_zh_a_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-沪深京 A 股的数据
@router.post("/stock_zh_a_daily", operation_id="post_stock_zh_a_daily")
def get_stock_zh_a_daily(request: StockHistoryRequest):
    """
    接口: stock_zh_a_daily
    P.S. 建议切换为 stock_zh_a_hist 接口使用(该接口数据质量高, 访问无限制)
    描述: 新浪财经-沪深京 A 股的数据, 历史数据按日频率更新
    限量: 单次返回指定沪深京 A 股上市公司指定日期间的历史行情日频率数据
    """
    try:
        stock_zh_a_daily_df = ak.stock_zh_a_daily(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        stock_zh_a_daily_df.rename(columns={
            "symbol": "日期",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "close": "收盘价",
            "volume": "成交量",
            "amount": "成交金额",
            "outstanding_share": "流通股本",
            "turnover": "换手率"
        }, inplace=True)
        return stock_zh_a_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockAdjustFactorRequest(BaseModel):
    symbol: str
    adjust: str


# 前复权因子
@router.post("/stock_qfq_factor", operation_id="post_stock_qfq_factor")
def get_stock_qfq_factor(request: StockAdjustFactorRequest):
    """
    前复权因子
    """
    try:
        qfq_factor_df = ak.stock_zh_a_daily(symbol=request.symbol, adjust=request.adjust)
        return qfq_factor_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 后复权因子
@router.post("/stock_hfq_factor", operation_id="post_stock_hfq_factor")
def get_stock_hfq_factor(request: StockAdjustFactorRequest):
    """
    后复权因子
    """
    try:
        hfq_factor_df = ak.stock_zh_a_daily(symbol=request.symbol, adjust=request.adjust)
        return hfq_factor_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 腾讯证券-日频-股票历史数据
@router.post("/stock_zh_a_hist_tx", operation_id="post_stock_zh_a_hist_tx")
def get_stock_zh_a_hist_tx(request: StockHistoryRequest):
    """
    描述: 腾讯证券-日频-股票历史数据
    限量: 单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据
    """
    try:
        stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_zh_a_hist_tx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockTickRequest(BaseModel):
    symbol: str


# 历史分笔数据
@router.post("/stock_zh_a_tick_tx_js", operation_id="post_stock_zh_a_tick_tx_js")
def get_stock_zh_a_tick_tx_js(request: StockTickRequest):
    """
    描述: 每个交易日 16:00 提供当日数据; 如遇到数据缺失, 请使用 ak.stock_zh_a_tick_163() 接口(注意数据会有一定差异)
    限量: 单次返回最近交易日的历史分笔行情数据
    """
    try:
        stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol=request.symbol)
        return stock_zh_a_tick_tx_js_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockCDRDailyRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class StockDailyRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    adjust: str


class StockMinuteRequest(BaseModel):
    symbol: str
    period: str
    adjust: str


# B 股行情数据-上海证券交易所-科创板-CDR
@router.post("/stock_zh_a_cdr_daily", operation_id="post_stock_zh_a_cdr_daily")
def get_stock_zh_a_cdr_daily(request: StockCDRDailyRequest):
    """
    描述: 上海证券交易所-科创板-CDR
    限量: 单次返回指定 CDR 的日频率数据
    """
    try:
        stock_zh_a_cdr_daily_df = ak.stock_zh_a_cdr_daily(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )
        stock_zh_a_cdr_daily_df = sanitize_data_pandas(stock_zh_a_cdr_daily_df)

        return stock_zh_a_cdr_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# B 股行情数据-东方财富网-实时行情数据
@router.get("/stock_zh_b_spot_em", operation_id="get_stock_zh_b_spot_em")
def get_stock_zh_b_spot_em():
    """
    描述: 东方财富网-实时行情数据
    限量: 单次返回所有 B 股上市公司的实时行情数据
    """
    try:
        stock_zh_b_spot_em_df = ak.stock_zh_b_spot_em()
        data = stock_zh_b_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# B 股行情数据-新浪财经-实时行情数据
@router.get("/stock_zh_b_spot", operation_id="get_stock_zh_b_spot")
def get_stock_zh_b_spot():
    """
    描述: B 股数据是从新浪财经获取的数据, 重复运行本函数会被新浪暂时封 IP
    限量: 单次返回所有 B 股上市公司的实时行情数据
    """
    try:
        stock_zh_b_spot_df = ak.stock_zh_b_spot()
        return stock_zh_b_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# B 股历史行情数据
@router.post("/stock_zh_b_daily", operation_id="post_stock_zh_b_daily")
def get_stock_zh_b_daily(request: StockDailyRequest):
    """
    描述: B 股数据是从新浪财经获取的数据, 历史数据按日频率更新
    限量: 单次返回指定 B 股上市公司指定日期间的历史行情日频率数据
    """
    try:
        stock_zh_b_daily_df = ak.stock_zh_b_daily(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_zh_b_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# B 股历史行情数据-前复权因子
@router.post("/stock_qfq_factor_b", operation_id="post_stock_qfq_factor_b")
def get_stock_qfq_factor_b(request: StockMinuteRequest):
    """
    前复权因子
    """
    try:
        qfq_factor_df = ak.stock_zh_b_daily(
            symbol=request.symbol, adjust="qfq-factor"
        )
        return qfq_factor_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# B 股历史行情数据-后复权因子
@router.post("/stock_hfq_factor_b", operation_id="post_stock_hfq_factor_b")
def get_stock_hfq_factor_b(request: StockMinuteRequest):
    """
    后复权因子
    """
    try:
        hfq_factor_df = ak.stock_zh_b_daily(
            symbol=request.symbol, adjust="hfq-factor"
        )
        return hfq_factor_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经 B 股股票或者指数的分时数据
@router.post("/stock_zh_b_minute", operation_id="post_stock_zh_b_minute")
def get_stock_zh_b_minute(request: StockMinuteRequest):
    """
    描述: 新浪财经 B 股股票或者指数的分时数据
    限量: 单次返回指定股票或指数的指定频率的最近交易日的历史分时行情数据
    """
    try:
        stock_zh_b_minute_df = ak.stock_zh_b_minute(
            symbol=request.symbol, period=request.period, adjust=request.adjust
        )
        return stock_zh_b_minute_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 字段名称映射
field_mapping = {
    "symbol": "新浪代码",
    "code": "股票代码",
    "name": "股票简称",
    "open": "开盘价",
    "high": "最高价",
    "low": "最低价",
    "volume": "成交量",
    "amount": "成交额",
    "mktcap": "市值",
    "turnoverratio": "换手率"
}


@router.get("/stock_zh_a_new", operation_id="get_stock_zh_a_new")
def get_stock_zh_a_new():
    """
    描述: 新浪财经-行情中心-沪深股市-次新股
    限量: 单次返回所有次新股行情数据, 由于次新股名单随着交易日变化而变化，只能获取最近交易日的数据
    """
    try:
        stock_zh_a_new_df = ak.stock_zh_a_new()

        # 重命名字段为中文名称
        stock_zh_a_new_df.rename(columns=field_mapping, inplace=True)

        return stock_zh_a_new_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
