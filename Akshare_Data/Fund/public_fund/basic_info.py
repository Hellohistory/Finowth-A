import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-东方财富-基金基本信息
@router.get("/fund_name_em", operation_id="get_fund_name_em")
async def get_fund_name_em():
    """
    公募基金数据-东方财富-基金基本信息

    接口: fund_name_em

    目标地址: http://fund.eastmoney.com/fund.html

    描述: 东方财富网-天天基金网-基金数据-所有基金的基本信息数据

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_name_em = ak.fund_name_em()
        fund_name_em_df = sanitize_data_pandas(fund_name_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_name_em_df.to_dict(orient="records")


class FundIndividualBasicInfo(BaseModel):
    symbol: str = Field(..., title="基金代码", description="例：000001")


# 公募基金数据-雪球-基金基本信息
@router.post("/fund_individual_basic_info_xq", operation_id="post_fund_individual_basic_info_xq")
def post_fund_individual_basic_info_xq(request: FundIndividualBasicInfo):
    """
    公募基金数据-雪球-基金基本信息

    接口: fund_individual_basic_info_xq

    目标地址: https://danjuanfunds.com/funding/000001

    描述: 雪球基金-基金详情

    限量: 单次返回单只基金基本信息
    """
    try:
        fund_individual_basic_info_xq = ak.fund_individual_basic_info_xq(symbol=request.symbol)
        fund_individual_basic_info_xq_df = sanitize_data_pandas(fund_individual_basic_info_xq)

        return fund_individual_basic_info_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FundInfoIndexEM(BaseModel):
    symbol: str = Field(..., title="基金类型",
                        description="可选择：全部, 沪深指数, 行业主题, 大盘指数, 中盘指数, 小盘指数, 股票指数, 债券指数")
    indicator: str = Field(..., title="指数类型", description="可选择：全部, 被动指数型, 增强指数型")


# 公募基金数据-东方财富-基金基本信息-指数型
@router.post("/fund_info_index_em", operation_id="post_fund_info_index_em")
def post_fund_info_index_em(request: FundInfoIndexEM):
    """
    公募基金数据-东方财富-基金基本信息-指数型

    接口: fund_info_index_em

    目标地址: http://fund.eastmoney.com/trade/zs.html

    描述: 东方财富网-天天基金网-基金数据-基金基本信息-指数型

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_info_index_em = ak.fund_info_index_em(
            symbol=request.symbol,
            indicator=request.indicator
        )
        fund_info_index_em_df = sanitize_data_pandas(fund_info_index_em)

        return fund_info_index_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-东方财富-基金申购状态
@router.get("/fund_purchase_em", operation_id="get_fund_purchase_em")
async def get_fund_purchase_em():
    """
    公募基金数据-东方财富-基金申购状态

    接口: fund_purchase_em

    目标地址: http://fund.eastmoney.com/Fund_sgzt_bzdm.html#fcode,asc_1

    描述: 东方财富网站-天天基金网-基金数据-基金申购状态

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_purchase_em = ak.fund_purchase_em()
        fund_purchase_em_df = sanitize_data_pandas(fund_purchase_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_purchase_em_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
