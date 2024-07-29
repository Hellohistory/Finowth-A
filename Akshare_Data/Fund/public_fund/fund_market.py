import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-基金行情-东方财富-ETF基金实时行情
@router.get("/fund_etf_spot_em", operation_id="get_fund_etf_spot_em")
async def get_fund_etf_spot_em():
    """
    公募基金数据-基金行情-东方财富-ETF基金实时行情

    接口: fund_etf_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#fund_etf

    描述: 东方财富-ETF 实时行情

    限量: 单次返回所有数据
    """
    try:
        fund_etf_spot_em = ak.fund_etf_spot_em()
        fund_etf_spot_em_df = sanitize_data_pandas(fund_etf_spot_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_etf_spot_em_df.to_dict(orient="records")


class FundETFSpotTHS(BaseModel):
    date: str = Field(..., title="指定日期", description="例：20240620，为空则返回最新数据")


# 公募基金数据-基金行情-同花顺-ETF基金实时行情
@router.post("/fund_etf_spot_ths", operation_id="post_fund_etf_spot_ths")
def post_fund_etf_spot_ths(request: FundETFSpotTHS):
    """
    公募基金数据-基金行情-同花顺-ETF基金实时行情

    接口: fund_etf_spot_ths

    目标地址: https://fund.10jqka.com.cn/datacenter/jz/kfs/etf/

    描述: 同花顺理财-基金数据-每日净值-ETF-实时行情

    限量: 单次返回指定 date 的所有数据
    """
    try:
        fund_etf_spot_ths = ak.fund_etf_spot_ths(date=request.date)
        fund_etf_spot_ths_df = sanitize_data_pandas(fund_etf_spot_ths)

        return fund_etf_spot_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金行情-东方财富-LOF基金实时行情
@router.get("/fund_lof_spot_em", operation_id="get_fund_lof_spot_em")
async def get_fund_lof_spot_em():
    """
    公募基金数据-基金行情-东方财富-LOF基金实时行情

    接口: fund_lof_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#fund_lof

    描述: 东方财富-LOF 实时行情

    限量: 单次返回所有数据
    """
    try:
        fund_lof_spot_em = ak.fund_lof_spot_em()
        fund_lof_spot_em_df = sanitize_data_pandas(fund_lof_spot_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_lof_spot_em_df.to_dict(orient="records")


class FundETFSpotSina(BaseModel):
    symbol: str = Field(..., title="指定基金类型",
                        description="可选择 封闭式基金, ETF基金, LOF基金")


# 公募基金数据-基金行情-新浪财经-基金实时行情
@router.post("/fund_etf_category_sina", operation_id="post_fund_etf_category_sina")
def post_fund_etf_category_sina(request: FundETFSpotSina):
    """
    公募基金数据-基金行情-新浪财经-基金实时行情

    接口: fund_etf_category_sina

    目标地址: http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf

    描述: 新浪财经-基金列表及行情数据

    限量: 单次返回指定类型基金的所有数据
    """
    try:
        fund_etf_category_sina = ak.fund_etf_category_sina(symbol=request.symbol)
        fund_etf_category_sina_df = sanitize_data_pandas(fund_etf_category_sina)

        return fund_etf_category_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundETFSpotSina(BaseModel):
    symbol: str = Field(..., title="ETF代码",
                        description="可通过fund_etf_spot_em获取")
    start_date: str = Field(..., title="开始时间",
                            description="例：1979-09-01 09:32:00")
    end_date: str = Field(..., title="结束时间",
                          description="例：2222-01-01 09:32:00")
    period: str = Field(..., title="时间周期",
                        description="可选择一分钟：1, 五分钟：5, 十五分钟：15, 三十分:30, 六十分钟：60")
    adjust: str = Field(..., title="复权类型",
                        description="为空不复权, 'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权")


# 公募基金数据-基金行情-东方财富-ETF基金分时行情
@router.post("/fund_etf_hist_min_em", operation_id="post_fund_etf_hist_min_em")
def post_fund_etf_hist_min_em(request: FundETFSpotSina):
    """
    公募基金数据-基金行情-新浪财经-基金实时行情

    接口: fund_etf_hist_min_em

    目标地址: https://quote.eastmoney.com/sz159707.html

    描述: 东方财富-ETF 分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置

    限量: 单次返回指定 ETF、频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 5 个交易日数据且不复权
    """
    try:
        fund_etf_hist_min_em = ak.fund_etf_hist_min_em(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            period=request.period,
            adjust=request.adjust,
        )
        fund_etf_hist_min_em_df = sanitize_data_pandas(fund_etf_hist_min_em)

        return fund_etf_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundLOFHistEM(BaseModel):
    symbol: str = Field(..., title="LOF代码",
                        description="可通过 fund_lof_spot_em 获取")
    start_date: str = Field(..., title="开始时间",
                            description="例：1979-09-01 09:32:00")
    end_date: str = Field(..., title="结束时间",
                          description="例：2222-01-01 09:32:00")
    period: str = Field(..., title="时间周期",
                        description="可选择日：daily', 周：weekly, 月：monthly")
    adjust: str = Field(..., title="复权类型",
                        description="为空不复权, 'qfq': 前复权, 'hfq': 后复权")


# 公募基金数据-基金行情-东方财富-LOF基金历史行情
@router.post("/fund_lof_hist_em", operation_id="post_fund_lof_hist_em")
def post_fund_lof_hist_em(request: FundLOFHistEM):
    """
    公募基金数据-基金行情-新浪财经-LOF基金历史行情

    接口: fund_lof_hist_em

    目标地址: https://quote.eastmoney.com/sz166009.html

    描述: 东方财富-LOF 行情; 历史数据按日频率更新, 当日收盘价请在收盘后获取

    限量: 单次返回指定 LOF、指定周期和指定日期间的历史行情日频率数据
    """
    try:
        fund_lof_hist_em = ak.fund_lof_hist_em(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            period=request.period,
            adjust=request.adjust,
        )
        fund_lof_hist_em_df = sanitize_data_pandas(fund_lof_hist_em)

        return fund_lof_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundETFHistSina(BaseModel):
    symbol: str = Field(..., title="ETF代码",
                        description="可通过 fund_etf_category_sina 获取")


# 公募基金数据-基金行情-新浪财经-基金历史行情
@router.post("/fund_etf_hist_sina", operation_id="post_fund_etf_hist_sina")
def post_fund_etf_hist_sina(request: FundETFHistSina):
    """
    公募基金数据-基金行情-新浪财经-基金历史行情

    接口: fund_etf_hist_sina

    目标地址: http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf

    描述: 新浪财经-基金行情的日频率行情数据

    限量: 单次返回指定基金的所有数据
    """
    try:
        fund_etf_hist_sina = ak.fund_etf_hist_sina(symbol=request.symbol)
        fund_etf_hist_sina_df = sanitize_data_pandas(fund_etf_hist_sina)

        return fund_etf_hist_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
