import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas, sanitize_data

router = APIRouter()


class StockHistoryRequest(BaseModel):
    symbol: str = Field(..., title="指定个股", description="例：000001")
    period: str = Field(..., title="时间周期",
                        description="例：daily; 所有可选参数为：daily(日), weekly(周), monthly(月)")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据")


# 东方财富-沪深京 A 股日频率数据
@router.post("/stock_zh_a_hist", operation_id="post_stock_zh_a_hist")
async def post_stock_zh_a_hist(request: StockHistoryRequest):
    """
    东方财富-沪深京 A 股日频率数据

    接口: stock_zh_a_hist

    目标地址: https://quote.eastmoney.com/concept/sh603777.html?from=classic(示例)

    描述: 东方财富-沪深京 A 股日频率数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取

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


class XinLangStockHistoryRequest(BaseModel):
    symbol: str = Field(..., title="指定个股(需携带市场标识)", description="例：sh600000")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; "
                                    "qfq: 返回前复权后的数据; "
                                    "hfq: 返回后复权后的数据; "
                                    "hfq-factor: 返回后复权因子; "
                                    "qfq-factor: 返回前复权因子")


# 新浪财经-沪深京 A 股的数据
@router.post("/stock_zh_a_daily", operation_id="post_stock_zh_a_daily")
async def post_stock_zh_a_daily(request: XinLangStockHistoryRequest):
    """
    新浪财经-沪深京 A 股日频率数据

    接口: stock_zh_a_daily

    P.S. 建议切换为 stock_zh_a_hist 接口使用(该接口数据质量高, 访问无限制)

    目标地址: https://finance.sina.com.cn/realstock/company/sh600006/nc.shtml (示例)

    描述: 新浪财经-沪深京 A 股的数据, 历史数据按日频率更新; 注意其中的 **sh689009** 为 CDR, 请 通过 **ak.stock_zh_a_cdr_daily** 接口获取

    限量: 单次返回指定沪深京 A 股上市公司指定日期间的历史行情日频率数据, 多次获取容易封禁 IP
    """
    try:
        stock_zh_a_daily_df = ak.stock_zh_a_daily(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        stock_zh_a_daily_df.rename(columns={
            "date": "交易日",
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


class TXStockHistoryRequest(BaseModel):
    symbol: str = Field(..., title="指定个股(需携带市场标识)", description="例：sz000001")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; "
                                    "qfq: 返回前复权后的数据; "
                                    "hfq: 返回后复权后的数据")


@router.post("/stock_zh_a_hist_tx", operation_id="post_stock_zh_a_hist_tx")
async def post_stock_zh_a_hist_tx(request: TXStockHistoryRequest):
    """
    腾讯证券-日频-股票历史数据

    接口: stock_zh_a_hist_tx

    目标地址: https://gu.qq.com/sh000919/zs

    描述: 腾讯证券-日频-股票历史数据; 历史数据按日频率更新, 当日收盘价请在收盘后获取

    限量: 单次返回指定沪深京 A 股上市公司、指定周期和指定日期间的历史行情日频率数据
    """
    try:
        stock_zh_a_hist_tx_df = ak.stock_zh_a_hist_tx(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )

        # 重命名列名称
        stock_zh_a_hist_tx_df.rename(columns={
            'date': '交易日',
            'open': '开盘价',
            'close': '收盘价',
            'high': '最高价',
            'low': '最低价',
            'amount': '交易量'
        }, inplace=True)

        return stock_zh_a_hist_tx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class KCBCDRDayRequest(BaseModel):
    symbol: str = Field(..., title="指定个股(需携带市场标识)", description="例：sh689009")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# A 股行情数据-上海证券交易所-科创板-CDR
@router.post("/stock_zh_a_cdr_daily", operation_id="post_stock_zh_a_cdr_daily")
async def post_stock_zh_a_cdr_daily(request: KCBCDRDayRequest):
    """
    上海证券交易所-科创板-CDR

    接口: stock_zh_a_cdr_daily

    目标地址: https://finance.sina.com.cn/realstock/company/sh689009/nc.shtml

    描述: 上海证券交易所-科创板-CDR

    限量: 单次返回指定 CDR 的日频率数据, 分钟历史行情数据可以通过 stock_zh_a_minute 获取
    """
    try:
        stock_zh_a_cdr_daily_df = ak.stock_zh_a_cdr_daily(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )

        stock_zh_a_cdr_daily_df.rename(columns={
            "date": "日期",
            "prevclose": "前收盘价",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "close": "收盘价",
            "volume": "成交量",
            "amount": "成交金额",
            "postVol": "盘后成交量",
            "postAmt": "盘后成交金额"
        }, inplace=True)

        stock_zh_a_cdr_daily_df = sanitize_data_pandas(stock_zh_a_cdr_daily_df)

        return stock_zh_a_cdr_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# B 股行情数据-东方财富-实时行情数据
@router.get("/stock_zh_b_spot_em", operation_id="get_stock_zh_b_spot_em")
def get_stock_zh_b_spot_em():
    """
    东方财富-实时行情数据

    接口: stock_zh_b_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#hs_b_board

    描述: 东方财富-实时行情数据

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
    新浪财经-B 股行情数据

    接口: stock_zh_b_spot

    目标地址: http://vip.stock.finance.sina.com.cn/mkt/#hs_b

    描述: B 股数据是从新浪财经获取的数据, 重复运行本接口会被新浪暂时封 IP, 建议增加时间间隔

    限量: 单次返回所有 B 股上市公司的实时行情数据
    """
    try:
        stock_zh_b_spot_df = ak.stock_zh_b_spot()
        return stock_zh_b_spot_df.to_dict(orient="records")
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
    新浪财经-沪深股市-次新股

    接口: stock_zh_a_new

    目标地址: http://vip.stock.finance.sina.com.cn/mkt/#new_stock

    描述: 新浪财经-行情中心-沪深股市-次新股

    限量: 单次返回所有次新股行情数据, 由于次新股名单随着交易日变化而变化，只能获取最近交易日的数据
    """
    try:
        stock_zh_a_new_df = ak.stock_zh_a_new()

        stock_zh_a_new_df.rename(columns=field_mapping, inplace=True)

        return stock_zh_a_new_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
