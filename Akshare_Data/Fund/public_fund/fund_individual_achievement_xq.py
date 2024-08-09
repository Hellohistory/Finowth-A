import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FundIndividualAchievementXQ(BaseModel):
    symbol: str = Field(..., title="基金代码", description="例：000001")


# 公募基金数据-基金排行-雪球-基金业绩
@router.post("/fund_individual_achievement_xq",
             operation_id="fund_individual_achievement_xq")
def fund_individual_achievement_xq(request: FundIndividualAchievementXQ):
    """
    公募基金数据-基金排行-雪球-基金业绩

    接口: fund_individual_achievement_xq

    目标地址: https://danjuanfunds.com/rn/funding/:code/RankInfo?symbol=000001&fd_type=2&btn_pos=1

    描述: 雪球基金-基金详情-基金业绩-详情

    限量: 单次返回单只基金业绩详情
    """
    try:
        fund_individual_achievement_xq = ak.fund_individual_achievement_xq(symbol=request.symbol)
        fund_individual_achievement_xq_df = sanitize_data_pandas(fund_individual_achievement_xq)

        return fund_individual_achievement_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金排行-雪球-基金数据分析
@router.post("/fund_individual_analysis_xq",
             operation_id="fund_individual_analysis_xq")
def fund_individual_analysis_xq(request: FundIndividualAchievementXQ):
    """
    公募基金数据-基金排行-雪球-基金数据分析

    接口: fund_individual_analysis_xq

    目标地址: https://danjuanfunds.com/funding/000001

    描述: 雪球基金-基金详情-数据分析

    限量: 返回单只基金历史表现分析数据
    """
    try:
        fund_individual_analysis_xq = ak.fund_individual_analysis_xq(symbol=request.symbol)
        fund_individual_analysis_xq_df = sanitize_data_pandas(fund_individual_analysis_xq)

        return fund_individual_analysis_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金排行-雪球-基金盈利概率
@router.post("/fund_individual_profit_probability_xq",
             operation_id="fund_individual_profit_probability_xq")
def fund_individual_profit_probability_xq(request: FundIndividualAchievementXQ):
    """
    公募基金数据-基金排行-雪球-基金盈利概率

    接口: fund_individual_profit_probability_xq

    目标地址: https://danjuanfunds.com/funding/000001

    描述: 雪球基金-基金详情-盈利概率；历史任意时点买入，持有满X时间，盈利概率，以及平均收益

    限量: 单次返回单只基金历史任意时点买入，持有满 X 时间，盈利概率，以及平均收益
    """
    try:
        fund_individual_profit_probability_xq = ak.fund_individual_profit_probability_xq(symbol=request.symbol)
        fund_individual_profit_probability_xq_df = sanitize_data_pandas(fund_individual_profit_probability_xq)

        return fund_individual_profit_probability_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundIndividualDetailHoldXQ(BaseModel):
    symbol: str = Field(..., title="基金代码", description="例：000001")
    date: str = Field(..., title="日期", description="例：20231231")


# 公募基金数据-基金排行-雪球-基金持仓资产比例
@router.post("/fund_individual_detail_hold_xq",
             operation_id="fund_individual_detail_hold_xq")
def fund_individual_detail_hold_xq(request: FundIndividualDetailHoldXQ):
    """
    公募基金数据-基金排行-雪球-基金持仓资产比例

    接口: fund_individual_detail_hold_xq

    目标地址: https://danjuanfunds.com/rn/fund-detail/archive?id=103&code=000001

    描述: 雪球基金-基金详情-基金持仓-详情

    限量: 单次返回单只基金指定日期的持仓大类资产比例
    """
    try:
        fund_individual_detail_hold_xq = ak.fund_individual_detail_hold_xq(
            symbol=request.symbol,
            date=request.date
        )
        fund_individual_detail_hold_xq_df = sanitize_data_pandas(fund_individual_detail_hold_xq)

        return fund_individual_detail_hold_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金排行-雪球-基金交易规则
@router.post("/fund_individual_detail_info_xq",
             operation_id="fund_individual_detail_info_xq")
def fund_individual_detail_info_xq(request: FundIndividualAchievementXQ):
    """
    公募基金数据-基金排行-雪球-基金交易规则

    接口: fund_individual_detail_info_xq

    目标地址: https://danjuanfunds.com/djapi/fund/detail/675091

    描述: 雪球基金-基金详情-基金交易规则

    限量: 单次返回单只基金基金交易规则
    """
    try:
        fund_individual_detail_info_xq = ak.fund_individual_detail_info_xq(symbol=request.symbol)
        fund_individual_detail_info_xq_df = sanitize_data_pandas(fund_individual_detail_info_xq)

        return fund_individual_detail_info_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundPortfolioHoldEM(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="例：000001，可通过 fund_name_em 获取")


# 公募基金数据-基金排行-东方财富-基金持仓
@router.post("/fund_portfolio_hold_em",
             operation_id="fund_portfolio_hold_em")
def fund_portfolio_hold_em(request: FundPortfolioHoldEM):
    """
    公募基金数据-基金排行-东方财富-基金持仓

    接口: fund_portfolio_hold_em

    目标地址: https://fundf10.eastmoney.com/ccmx_000001.html

    描述: 天天基金网-基金档案-投资组合-基金持仓

    限量: 单次返回指定 symbol 和 date 的所有持仓数据
    """
    try:
        fund_portfolio_hold_em = ak.fund_portfolio_hold_em(symbol=request.symbol)
        fund_portfolio_hold_em_df = sanitize_data_pandas(fund_portfolio_hold_em)

        return fund_portfolio_hold_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundPortfolioBondHoldEM(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="例：000001，可通过 fund_name_em 获取")
    date: str = Field(..., title="指定年份", description="例：2023")


# 公募基金数据-基金排行-东方财富-债券持仓
@router.post("/fund_portfolio_bond_hold_em",
             operation_id="fund_portfolio_bond_hold_em")
def fund_portfolio_bond_hold_em(request: FundPortfolioBondHoldEM):
    """
    公募基金数据-基金排行-东方财富-债券持仓

    接口: fund_portfolio_bond_hold_em

    目标地址: https://fundf10.eastmoney.com/ccmx_000001.html

        描述: 天天基金网-基金档案-投资组合-债券持仓

    限量: 单次返回指定指定基金和指定时间的所有持仓数据
    """
    try:
        fund_portfolio_bond_hold_em = ak.fund_portfolio_bond_hold_em(
            symbol=request.symbol,
            date=request.date
        )
        fund_portfolio_bond_hold_em_df = sanitize_data_pandas(fund_portfolio_bond_hold_em)

        return fund_portfolio_bond_hold_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金排行-东方财富-行业配置
@router.post("/fund_portfolio_industry_allocation_em",
             operation_id="fund_portfolio_industry_allocation_em")
def fund_portfolio_industry_allocation_em(request: FundPortfolioHoldEM):
    """
    公募基金数据-基金排行-东方财富-行业配置

    接口: fund_portfolio_industry_allocation_em

    目标地址: https://fundf10.eastmoney.com/hytz_000001.html

    描述: 天天基金网-基金档案-投资组合-行业配置

    限量: 单次返回指定基金和指定年份的所有持仓数据
    """
    try:
        fund_portfolio_industry_allocation_em = ak.fund_portfolio_industry_allocation_em(
            symbol=request.symbol,
            date=request.date
        )
        fund_portfolio_industry_allocation_em_df = sanitize_data_pandas(fund_portfolio_industry_allocation_em)

        return fund_portfolio_industry_allocation_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundPortfolioHoldEM(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="例：000001，可通过 fund_name_em 获取")
    indicator: str = Field(..., title="类型",
                           description="可选择 累计买入 或 累计卖出")
    date: str = Field(..., title="指定年份", description="例：2023")


# 公募基金数据-基金档案-东方财富-重大变动
@router.post("/fund_portfolio_change_em",
             operation_id="fund_portfolio_change_em")
def fund_portfolio_change_em(request: FundPortfolioHoldEM):
    """
    公募基金数据-基金档案-东方财富-债券持仓

    接口: fund_portfolio_change_em

    目标地址: https://fundf10.eastmoney.com/ccbd_000001.html

    描述: 天天基金网-基金档案-投资组合-重大变动

    限量: 单次返回指定 symbol、indicator 和 date 的所有重大变动数据
    """
    try:
        fund_portfolio_change_em = ak.fund_portfolio_change_em(
            symbol=request.symbol,
            indicator=request.indicator,
            date=request.date
        )
        fund_portfolio_change_em_df = sanitize_data_pandas(fund_portfolio_change_em)

        return fund_portfolio_change_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
