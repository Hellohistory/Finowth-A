import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FundETFSpotTHS(BaseModel):
    symbol: str = Field(..., title="指定类型",
                      description="可选择：全部, 股票型, 混合型, 债券型, 指数型, QDII, FOF")


# 公募基金数据-基金排行-东方财富-开放式基金排行
@router.post("/fund_open_fund_rank_em",
             operation_id="fund_open_fund_rank_em")
def fund_open_fund_rank_em(request: FundETFSpotTHS):
    """
    公募基金数据-基金排行-东方财富-开放式基金排行

    接口: fund_open_fund_rank_em

    目标地址: https://fund.eastmoney.com/data/fundranking.html

    描述: 东方财富网-数据中心-开放式基金排行

    限量: 单次返回当前时刻所有数据
    """
    try:
        fund_open_fund_rank_em = ak.fund_open_fund_rank_em(symbol=request.symbol)
        fund_open_fund_rank_em_df = sanitize_data_pandas(fund_open_fund_rank_em)

        return fund_open_fund_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-基金排行-东方财富-场内交易基金排行榜
@router.get("/fund_exchange_rank_em", operation_id="fund_exchange_rank_em")
async def fund_exchange_rank_em():
    """
    公募基金数据-基金排行-东方财富-场内交易基金排行榜

    接口: fund_exchange_rank_em

    目标地址: https://fund.eastmoney.com/data/fbsfundranking.html

    描述: 东方财富网-数据中心-场内交易基金排行榜

    限量: 单次返回当前时刻所有数据, 每个交易日 17 点后更新
    """
    try:
        fund_exchange_rank_em = ak.fund_exchange_rank_em()
        fund_exchange_rank_em_df = sanitize_data_pandas(fund_exchange_rank_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_exchange_rank_em_df.to_dict(orient="records")


# 公募基金数据-基金排行-东方财富-货币型基金排行
@router.get("/fund_money_rank_em", operation_id="fund_money_rank_em")
async def fund_money_rank_em():
    """
    公募基金数据-基金排行-东方财富-货币型基金排行

    接口: fund_money_rank_em

    目标地址: https://fund.eastmoney.com/data/hbxfundranking.html

    描述: 东方财富网-数据中心-货币型基金排行

    限量: 单次返回当前时刻所有数据, 每个交易日 17 点后更新, 货币基金的单位净值均为 1.0000 元，最新一年期定存利率: 1.50%
    """
    try:
        fund_money_rank_em = ak.fund_money_rank_em()
        fund_money_rank_em_df = sanitize_data_pandas(fund_money_rank_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_money_rank_em_df.to_dict(orient="records")


# 公募基金数据-基金排行-东方财富-香港基金排行
@router.get("/fund_hk_rank_em", operation_id="fund_hk_rank_em")
async def fund_hk_rank_em():
    """
    公募基金数据-基金排行-东方财富-香港基金排行

    接口: fund_hk_rank_em

    目标地址: https://overseas.1234567.com.cn/FundList

    描述: 东方财富网-数据中心-基金排行-香港基金排行

    限量: 单次返回当前时刻所有数据
    """
    try:
        fund_hk_rank_em = ak.fund_hk_rank_em()
        fund_hk_rank_em_df = sanitize_data_pandas(fund_hk_rank_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_hk_rank_em_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
