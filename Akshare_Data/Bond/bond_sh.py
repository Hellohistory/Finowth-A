import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class BondDateRequest(BaseModel):
    date: str = Field(..., title="需查询的日期", description="例：20200111")


# 债券-上交所债券-债券现券市场概览
@router.post("/bond_cash_summary_sse", operation_id="post_bond_cash_summary_sse")
def post_bond_cash_summary_sse(request: BondDateRequest):
    """
    债券-上交所债券-债券现券市场概览

    接口: bond_cash_summary_sse

    目标地址: https://bond.sse.com.cn/data/statistics/overview/bondow/

    描述: 上登债券信息网-市场数据-市场统计-市场概览-债券现券市场概览

    限量: 单次返回指定交易日的债券现券市场概览数据
    """
    try:
        bond_cash_summary_sse = ak.bond_cash_summary_sse(date=request.date)
        bond_cash_summary_sse_df = sanitize_data_pandas(bond_cash_summary_sse)

        return bond_cash_summary_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-上交所债券-债券成交概览
@router.post("/bond_deal_summary_sse", operation_id="post_bond_deal_summary_sse")
def post_bond_deal_summary_sse(request: BondDateRequest):
    """
    债券-上交所债券-债券成交概览

    接口: bond_deal_summary_sse

    目标地址: http://bond.sse.com.cn/data/statistics/overview/turnover/

    描述: 上登债券信息网-市场数据-市场统计-市场概览-债券成交概览

    限量: 单次返回指定交易日的债券成交概览数据
    """
    try:
        bond_deal_summary_sse = ak.bond_deal_summary_sse(date=request.date)
        bond_deal_summary_sse_df = sanitize_data_pandas(bond_deal_summary_sse)

        return bond_deal_summary_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
