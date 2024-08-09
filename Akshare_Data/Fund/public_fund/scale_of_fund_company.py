import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-东方财富-基金公司规模-基金规模详情
@router.get("/fund_aum_em", operation_id="fund_aum_em")
async def fund_aum_em():
    """
    公募基金数据-东方财富-基金公司规模-基金规模详情

    接口: fund_aum_em

    目标地址: https://fund.eastmoney.com/Company/lsgm.html

    描述: 天天基金网-基金数据-基金规模

    限量: 单次返回所有基金规模数据
    """
    try:
        fund_aum_em = ak.fund_aum_em()
        fund_aum_em_df = sanitize_data_pandas(fund_aum_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_aum_em_df.to_dict(orient="records")


# 公募基金数据-东方财富-基金公司规模-基金规模走势
@router.get("/fund_aum_trend_em", operation_id="fund_aum_trend_em")
async def fund_aum_trend_em():
    """
    公募基金数据-东方财富-基金公司规模-基金规模走势

    接口: fund_aum_trend_em

    目标地址: http://fund.eastmoney.com/Company/default.html

    描述: 天天基金网-基金数据-市场全部基金规模走势

    限量: 单次返回所有市场全部基金规模走势数据
    """
    try:
        fund_aum_trend_em = ak.fund_aum_trend_em()
        fund_aum_trend_em_df = sanitize_data_pandas(fund_aum_trend_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_aum_trend_em_df.to_dict(orient="records")


class FundValuEstimationEM(BaseModel):
    year: str = Field(..., title="指定年份",
                      description="例：2023，数据从 2001 年开始")


# 公募基金数据-基金排行-东方财富-净值估算
@router.post("/fund_aum_hist_em",
             operation_id="fund_aum_hist_em")
def fund_aum_hist_em(request: FundValuEstimationEM):
    """
    公募基金数据-基金排行-东方财富-净值估算

    接口: fund_aum_hist_em

    目标地址: http://fund.eastmoney.com/Company/lsgm.html

    描述: 天天基金网-基金数据-基金公司历年管理规模排行列表

    限量: 单次返回所有基金公司历年管理规模排行列表数据
    """
    try:
        fund_aum_hist_em = ak.fund_aum_hist_em(
            year=request.year
        )
        fund_aum_hist_em_df = sanitize_data_pandas(fund_aum_hist_em)

        return fund_aum_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
