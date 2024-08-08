import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FundRating(BaseModel):
    symbol: str = Field(..., title="指定类型",
                        description="可选择 股票型基金, 混合型基金, 债券型基金, 货币型基金, QDII基金")


# 公募基金数据-东方财富-基金规模-开放式基金
@router.post("/fund_scale_open_sina",
             operation_id="post_fund_scale_open_sina")
def post_fund_scale_open_sina(request: FundRating):
    """
    公募基金数据-东方财富-基金规模-开放式基金

    接口: fund_scale_open_sina

    目标地址: https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf

    描述: 基金数据中心-基金规模-开放式基金

    限量: 单次返回指定类型的基金规模数据
    """
    try:
        fund_scale_open_sina = ak.fund_scale_open_sina(
            symbol=request.symbol
        )
        fund_scale_open_sina_df = sanitize_data_pandas(fund_scale_open_sina)

        return fund_scale_open_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-东方财富-基金规模-封闭式基金
@router.get("/fund_scale_close_sina",
            operation_id="get_fund_scale_close_sina")
async def get_fund_scale_close_sina():
    """
    公募基金数据-东方财富-基金规模-封闭式基金

    接口: fund_scale_close_sina

    目标地址: https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjhqetf

    描述: 基金数据中心-基金规模-封闭式基金

    限量: 单次返回所有封闭式基金的基金规模数据
    """
    try:
        fund_scale_close_sina = ak.fund_scale_close_sina()
        fund_scale_close_sina_df = sanitize_data_pandas(fund_scale_close_sina)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_scale_close_sina_df.to_dict(orient="records")


# 公募基金数据-东方财富-基金规模-分级子基金
@router.get("/fund_scale_structured_sina",
            operation_id="get_fund_scale_structured_sina")
async def get_fund_scale_structured_sina():
    """
    公募基金数据-东方财富-基金规模-分级子基金

    接口: fund_scale_structured_sina

    目标地址: https://vip.stock.finance.sina.com.cn/fund_center/index.html#jjgmfjall

    描述: 基金数据中心-基金规模-分级子基金

    限量: 单次返回所有分级子基金的基金规模数据
    """
    try:
        fund_scale_structured_sina = ak.fund_scale_structured_sina()
        fund_scale_structured_sina_df = sanitize_data_pandas(fund_scale_structured_sina)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_scale_structured_sina_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
