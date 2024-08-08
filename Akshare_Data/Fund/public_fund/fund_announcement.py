import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FundReportStockCninfo(BaseModel):
    symbol: str = Field(..., title="基金代码",
                        description="调用 fund_name_em 获取")


# 公募基金数据-东方财富-基金公告-人事公告
@router.post("/fund_announcement_personnel_em",
             operation_id="post_fund_announcement_personnel_em")
def post_fund_announcement_personnel_em(request: FundReportStockCninfo):
    """
    公募基金数据-东方财富-基金公告-人事公告

    接口: fund_announcement_personnel_em

    目标地址: http://fundf10.eastmoney.com/jjgg_000001_4.html

    描述: 东方财富网站-天天基金网-基金档案-基金公告-人事调整

    限量: 返回所有历史数据
    """
    try:
        fund_announcement_personnel_em = ak.fund_announcement_personnel_em(
            symbol=request.symbol
        )
        fund_announcement_personnel_em_df = sanitize_data_pandas(fund_announcement_personnel_em)

        return fund_announcement_personnel_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
