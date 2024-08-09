import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class NewCompositeIndexCbond(BaseModel):
    indicator: str = Field(..., title="查询类型",
                           description="可选择 全价, 净价, 财富, 平均市值法久期, 平均现金流法久期, 平均市值法凸性, "
                                       "平均现金流法凸性, 平均现金流法到期收益率, 平均市值法到期收益率, "
                                       "平均基点价值, 平均待偿期, 平均派息率, 指数上日总市值, 财富指数涨跌幅, "
                                       "全价指数涨跌幅, 净价指数涨跌幅, 现券结算量")
    period: str = Field(..., title="时间周期",
                        description="可选择总值, 1年以下, 1-3年, 3-5年, 5-7年, 7-10年, 10年以上, 0-3个月, "
                                    "3-6个月, 6-9个月, 9-12个月, 0-6个月, 6-12个月")


# 债券-中债指数-总指数-综合类指数-新综合指数
@router.post("/bond_new_composite_index_cbond",
             operation_id="bond_new_composite_index_cbond")
async def bond_new_composite_index_cbond(request: NewCompositeIndexCbond):
    """
    债券-中债指数-总指数-综合类指数-新综合指数

    接口: bond_new_composite_index_cbond

    目标地址: https://yield.chinabond.com.cn/cbweb-mn/indices/single_index_query

    描述: 中国债券信息网-中债指数-中债指数族系-总指数-综合类指数-中债-新综合指数
    """
    try:
        bond_new_composite_index_cbond = ak.bond_new_composite_index_cbond(
            indicator=request.indicator,
            period=request.period
        )
        bond_new_composite_index_cbond_df = sanitize_data_pandas(bond_new_composite_index_cbond)

        return bond_new_composite_index_cbond_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-中债指数-总指数-综合类指数-综合指数
@router.post("/bond_composite_index_cbond",
             operation_id="bond_composite_index_cbond")
async def bond_composite_index_cbond(request: NewCompositeIndexCbond):
    """
    债券-中债指数-总指数-综合类指数-综合指数

    接口: bond_composite_index_cbond

    目标地址: https://yield.chinabond.com.cn/cbweb-mn/indices/single_index_query

    描述: 中国债券信息网-中债指数-中债指数族系-总指数-综合类指数-中债-综合指数
    """
    try:
        bond_composite_index_cbond = ak.bond_composite_index_cbond(
            indicator=request.indicator,
            period=request.period
        )
        bond_composite_index_cbond_df = sanitize_data_pandas(bond_composite_index_cbond)

        return bond_composite_index_cbond_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
