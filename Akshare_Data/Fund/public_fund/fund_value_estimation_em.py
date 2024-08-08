import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FundValuEstimationEM(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="可选择：全部, 股票型, 混合型, 债券型, 指数型, "
                                    "QDII, ETF联接, LOF, 场内交易基金")


# 公募基金数据-基金排行-东方财富-净值估算
@router.post("/fund_value_estimation_em",
             operation_id="post_fund_value_estimation_em")
def post_fund_value_estimation_em(request: FundValuEstimationEM):
    """
    公募基金数据-基金排行-东方财富-净值估算

    接口: fund_value_estimation_em

    目标地址: http://fund.eastmoney.com/fundguzhi.html

    描述: 东方财富网-数据中心-净值估算

    限量: 单次返回当前交易日指定类型的所有数据
    """
    try:
        fund_value_estimation_em = ak.fund_value_estimation_em(symbol=request.symbol)
        fund_value_estimation_em_df = sanitize_data_pandas(fund_value_estimation_em)

        return fund_value_estimation_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
