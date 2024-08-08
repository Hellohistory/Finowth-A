import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-基金行情-东方财富-基金净值-开放式基金-实时数据
@router.get("/fund_open_fund_daily_em", operation_id="get_fund_open_fund_daily_em")
async def get_fund_open_fund_daily_em():
    """
    公募基金数据-基金行情-东方财富-基金净值-开放式基金-实时数据

    接口: fund_open_fund_daily_em

    目标地址: http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1

    描述: 东方财富网-天天基金网-基金数据, 此接口在每个交易日 16:00-23:00 更新当日的最新开放式基金净值数据

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_open_fund_daily_em = ak.fund_open_fund_daily_em()
        fund_open_fund_daily_em_df = sanitize_data_pandas(fund_open_fund_daily_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_open_fund_daily_em_df.to_dict(orient="records")


class FundETFSpotTHS(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="例：710001，可通过请求 fund_open_fund_daily_em 获取")
    indicator: str = Field(..., title="单位值", description="请求 fund_open_fund_info_em 获取")
    period: str = Field(..., title="时间周期",
                        description="可选择：1月, 3月, 6月, 1年, 3年, 5年, 今年来, 成立，"
                                    "需注意该参数只对 累计收益率走势 有效")


# 公募基金数据-基金行情-东方财富-开放式基金-历史数据
@router.post("/fund_open_fund_info_em", operation_id="post_fund_open_fund_info_em")
def post_fund_open_fund_info_em(request: FundETFSpotTHS):
    """
    公募基金数据-基金行情-东方财富-开放式基金-历史数据

    接口: fund_open_fund_info_em

    目标地址: http://fund.eastmoney.com/pingzhongdata/710001.js

    描述: 东方财富网-天天基金网-基金数据-具体基金信息

    限量: 单次返回当前时刻所有历史数据, 在查询基金数据的时候注意基金前后端问题
    """
    try:
        fund_open_fund_info_em = ak.fund_open_fund_info_em(
            symbol=request.symbol,
            indicator=request.indicator,
            period=request.period,
        )
        fund_open_fund_info_em_df = sanitize_data_pandas(fund_open_fund_info_em)

        return fund_open_fund_info_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金行情-东方财富-货币型基金-实时数据
@router.get("/fund_money_fund_daily_em", operation_id="get_fund_money_fund_daily_em")
async def get_fund_money_fund_daily_em():
    """
    公募基金数据-基金行情-东方财富-货币型基金-实时数据

    接口: fund_money_fund_daily_em

    目标地址: http://fund.eastmoney.com/HBJJ_pjsyl.html

    描述: 东方财富网-天天基金网-基金数据-货币型基金收益, 此接口数据每个交易日 16:00～23:00

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_money_fund_daily_em = ak.fund_money_fund_daily_em()
        fund_money_fund_daily_em_df = sanitize_data_pandas(fund_money_fund_daily_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_money_fund_daily_em_df.to_dict(orient="records")


class FundMoneyFundDailyEM(BaseModel):
    fund: str = Field(..., title="基金代码",
                      description="例：000009，可通过请求 fund_money_fund_daily_em 获取")


# 公募基金数据-基金行情-东方财富-货币型基金-历史数据
@router.post("/fund_money_fund_info_em", operation_id="post_fund_money_fund_info_em")
def post_fund_money_fund_info_em(request: FundMoneyFundDailyEM):
    """
    公募基金数据-基金行情-东方财富-货币型基金-历史数据

    接口: fund_money_fund_info_em

    目标地址: http://fundf10.eastmoney.com/jjjz_004186.html

    描述: 东方财富网-天天基金网-基金数据-货币型基金-历史净值

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_money_fund_info_em = ak.fund_money_fund_info_em(
            fund=request.fund
        )
        fund_money_fund_info_em_df = sanitize_data_pandas(fund_money_fund_info_em)

        return fund_money_fund_info_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundMoneyFundInfoEM(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="例：000134，可通过请求 fund_financial_fund_daily_em 获取")


# 公募基金数据-基金行情-东方财富-货币型基金-历史数据
@router.post("/fund_financial_fund_info_em", operation_id="post_fund_financial_fund_info_em")
def post_fund_financial_fund_info_em(request: FundMoneyFundInfoEM):
    """
    公募基金数据-基金行情-东方财富-货币型基金-历史数据

    接口: fund_financial_fund_info_em

    目标地址: http://fundf10.eastmoney.com/jjjz_000791.html

    描述: 东方财富网站-天天基金网-基金数据-理财型基金收益-历史净值明细

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_financial_fund_info_em = ak.fund_financial_fund_info_em(
            symbol=request.symbol
        )
        fund_financial_fund_info_em_df = sanitize_data_pandas(fund_financial_fund_info_em)

        return fund_financial_fund_info_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金行情-东方财富-分级基金-实时数据
@router.get("/fund_graded_fund_daily_em", operation_id="get_fund_graded_fund_daily_em")
async def get_fund_graded_fund_daily_em():
    """
    公募基金数据-基金行情-东方财富-分级基金-实时数据

    接口: fund_graded_fund_daily_em

    目标地址: http://fund.eastmoney.com/fjjj.html#1_1__0__zdf,desc_1

    描述: 东方财富网-天天基金网-基金数据-分级基金-实时数据, 此接口数据每个交易日 16:00～23:00

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_graded_fund_daily_em = ak.fund_graded_fund_daily_em()
        fund_graded_fund_daily_em_df = sanitize_data_pandas(fund_graded_fund_daily_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_graded_fund_daily_em_df.to_dict(orient="records")


class FundGradedFundDailyEM(BaseModel):
    fund: str = Field(..., title="基金代码",
                      description="例：000009，可通过请求 fund_money_fund_daily_em 获取")


# 公募基金数据-基金行情-东方财富-货币型基金-历史数据
@router.post("/fund_graded_fund_info_em", operation_id="post_fund_graded_fund_info_em")
def post_fund_graded_fund_info_em(request: FundGradedFundDailyEM):
    """
    公募基金数据-基金行情-东方财富-分级基金-历史数据

    接口: fund_graded_fund_info_em

    目标地址: http://fundf10.eastmoney.com/jjjz_004186.html

    描述: 东方财富网站-天天基金网-基金数据-分级基金-历史数据

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_graded_fund_info_em = ak.fund_graded_fund_info_em(
            fund=request.fund
        )
        fund_graded_fund_info_em_df = sanitize_data_pandas(fund_graded_fund_info_em)

        return fund_graded_fund_info_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金行情-东方财富-分级基金-实时数据
@router.get("/fund_etf_fund_daily_em", operation_id="get_fund_etf_fund_daily_em")
async def get_fund_etf_fund_daily_em():
    """
    公募基金数据-基金行情-东方财富-分级基金-实时数据

    接口: fund_etf_fund_daily_em

    目标地址: http://fund.eastmoney.com/cnjy_dwjz.html

    描述: 东方财富网站-天天基金网-基金数据-场内交易基金-实时数据, 此接口数据每个交易日 16:00～23:00

    限量: 单次返回当前时刻所有数据
    """
    try:
        fund_etf_fund_daily_em = ak.fund_etf_fund_daily_em()
        fund_etf_fund_daily_em_df = sanitize_data_pandas(fund_etf_fund_daily_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_etf_fund_daily_em_df.to_dict(orient="records")


class FundETFFundInfoEM(BaseModel):
    fund: str = Field(..., title="基金代码",
                      description="例：000009，可通过请求 fund_money_fund_daily_em 获取")
    start_date: str = Field(..., title="开始日期", description="例：20000101")
    end_date: str = Field(..., title="结束日期", description="例：20500101")


# 公募基金数据-基金行情-东方财富-场内交易基金-历史数据
@router.post("/fund_etf_fund_info_em", operation_id="post_fund_etf_fund_info_em")
def post_fund_etf_fund_info_em(request: FundETFFundInfoEM):
    """
    公募基金数据-基金行情-东方财富-场内交易基金-历史数据

    接口: fund_etf_fund_info_em

    目标地址: http://fundf10.eastmoney.com/jjjz_004186.html

    描述: 东方财富网站-天天基金网-基金数据-场内交易基金-历史净值数据

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_etf_fund_info_em = ak.fund_etf_fund_info_em(
            fund=request.fund,
            start_date=request.start_date,
            end_date=request.end_date
        )
        fund_etf_fund_info_em_df = sanitize_data_pandas(fund_etf_fund_info_em)

        return fund_etf_fund_info_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundETFFundInfoEM(BaseModel):
    code: str = Field(..., title="基金代码",
                      description="例：1002200683，可通过请求 fund_em_hk_rank 获取")
    symbol: str = Field(..., title="指定类型", description="可选择：历史净值明细, 分红送配详情")


# 公募基金数据-基金行情-东方财富-香港基金-历史数据
@router.post("/fund_hk_fund_hist_em", operation_id="post_fund_hk_fund_hist_em")
def post_fund_hk_fund_hist_em(request: FundETFFundInfoEM):
    """
    公募基金数据-基金行情-东方财富-香港基金-历史数据

    接口: fund_hk_fund_hist_em

    目标地址: http://overseas.1234567.com.cn/f10/FundJz/968092#FHPS

    描述: 东方财富网站-天天基金网-基金数据-香港基金-历史净值明细

    限量: 单次返回指定基金代码和指定类型所有历史数据
    """
    try:
        fund_hk_fund_hist_em = ak.fund_hk_fund_hist_em(
            code=request.code,
            symbol=request.symbol
        )
        fund_hk_fund_hist_em_df = sanitize_data_pandas(fund_hk_fund_hist_em)

        return fund_hk_fund_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
