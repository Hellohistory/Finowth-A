import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockIndexDaily(BaseModel):
    symbol: str = Field(..., title="带市场标识的股票指数代码",
                        description="例：sz399552")


# 指数数据-新浪财经-历史行情数据
@router.post("/stock_zh_index_daily",
             operation_id="post_stock_zh_index_daily")
def post_stock_zh_index_daily(request: StockIndexDaily):
    """
    指数数据-新浪财经-历史行情数据

    接口: stock_zh_index_daily

    目标地址: https://finance.sina.com.cn/realstock/company/sz399552/nc.shtml(示例)

    描述: 股票指数的历史数据按日频率更新

    限量: 单次返回指定带市场标识的股票指数代码的所有历史行情数据
    """
    try:
        stock_zh_index_daily = ak.stock_zh_index_daily(
            symbol=request.symbol
        )
        stock_zh_index_daily_df = sanitize_data_pandas(stock_zh_index_daily)

        return stock_zh_index_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-腾讯-历史行情数据
@router.post("/stock_zh_index_daily_tx",
             operation_id="post_stock_zh_index_daily_tx")
def post_stock_zh_index_daily_tx(request: StockIndexDaily):
    """
    指数数据-腾讯-历史行情数据

    接口: stock_zh_index_daily_tx

    目标地址: https://gu.qq.com/sh000919/zs

    描述: 股票指数(或者股票)历史行情数据

    限量: 单次返回具体某个股票指数(或者股票)的所有历史行情数据
    """
    try:
        stock_zh_index_daily_tx = ak.stock_zh_index_daily_tx(
            symbol=request.symbol
        )
        stock_zh_index_daily_tx_df = sanitize_data_pandas(stock_zh_index_daily_tx)

        return stock_zh_index_daily_tx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockIndexDailyEM(BaseModel):
    symbol: str = Field(..., title="带市场标识的股票指数代码",
                        description="例：sz399552,支持 sz: 深交所, sh: 上交所, csi: 中信指数 + id(000905)")
    start_date: str = Field(..., title="开始查询时间",
                            description="例：19900101")
    end_date: str = Field(..., title="结束查询时间",
                          description="例：20500101")


# 指数数据-东方财富-历史行情数据
@router.post("/stock_zh_index_daily_em",
             operation_id="post_stock_zh_index_daily_em")
def post_stock_zh_index_daily_em(request: StockIndexDailyEM):
    """
    指数数据-东方财富-历史行情数据

    接口: stock_zh_index_daily_em

    目标地址: http://quote.eastmoney.com/center/hszs.html

    描述: 东方财富股票指数数据, 历史数据按日频率更新

    限量: 单次返回具体指数的所有历史行情数据
    """
    try:
        stock_zh_index_daily_em = ak.stock_zh_index_daily_em(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )
        stock_zh_index_daily_em_df = sanitize_data_pandas(stock_zh_index_daily_em)

        return stock_zh_index_daily_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexZHAHist(BaseModel):
    symbol: str = Field(..., title="带市场标识的股票指数代码",
                        description="例：sz399552,支持 sz: 深交所, sh: 上交所, csi: 中信指数 + id(000905)")
    period: str = Field(..., title="时间周期",
                        description="可选择：天：daily, 周：weekly, 月：monthly")
    start_date: str = Field(..., title="开始查询时间",
                            description="例：19900101")
    end_date: str = Field(..., title="结束查询时间",
                          description="例：20500101")


# 指数数据-东方财富-历史行情数据-通用
@router.post("/index_zh_a_hist",
             operation_id="post_index_zh_a_hist")
def post_index_zh_a_hist(request: IndexZHAHist):
    """
    指数数据-东方财富-历史行情数据-通用

    接口: index_zh_a_hist

    目标地址: http://quote.eastmoney.com/center/hszs.html

    描述: 东方财富网-中国股票指数-行情数据

    限量: 单次返回具体指数指定 period 从 start_date 到 end_date 的之间的近期数据
    """
    try:
        index_zh_a_hist = ak.index_zh_a_hist(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date
        )
        index_zh_a_hist_df = sanitize_data_pandas(index_zh_a_hist)

        return index_zh_a_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexZHAHistMinEM(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：399006")
    period: str = Field(..., title="时间周期",
                        description="可选择：一分钟：1, 五分钟：5, 十五分钟：15, 三十分钟：30, 六十分钟：60")
    start_date: str = Field(..., title="开始查询时间",
                            description="例：19900101")
    end_date: str = Field(..., title="结束查询时间",
                          description="例：20500101")


# 指数数据-东方财富-历史行情数据-通用
@router.post("/index_zh_a_hist_min_em",
             operation_id="post_index_zh_a_hist_min_em")
def post_index_zh_a_hist_min_em(request: IndexZHAHistMinEM):
    """
    指数数据-东方财富-历史行情数据-通用

    接口: index_zh_a_hist_min_em

    目标地址: https://quote.eastmoney.com/center/hszs.html

    描述: 东方财富网-指数数据-分时行情

    限量: 单次返回具体指数指定时间周期从指定开始时间到指定结束时间的之间的近期数据，该接口不能返回所有历史数据
    """
    try:
        index_zh_a_hist_min_em = ak.index_zh_a_hist_min_em(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date
        )
        index_zh_a_hist_min_em_df = sanitize_data_pandas(index_zh_a_hist_min_em)

        return index_zh_a_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
