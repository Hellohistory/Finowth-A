import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class BondZHSpot(BaseModel):
    start_page: str = Field(..., title="开始获取的页面", description="例：1")
    end_page: str = Field(..., title="结束获取的页面", description="例：10")


# 债券-沪深债券-实时行情数据
@router.post("/bond_zh_hs_spot", operation_id="post_bond_zh_hs_spot")
async def post_bond_zh_hs_spot(request: BondZHSpot):
    """
    债券-沪深债券-实时行情数据

    接口: bond_zh_hs_spot

    目标地址: https://vip.stock.finance.sina.com.cn/mkt/#hs_z

    描述: 新浪财经-债券-沪深债券-实时行情数据

    限量: 单次返回所有沪深债券的实时行情数据
    """
    try:
        bond_zh_hs_spot = ak.bond_zh_hs_spot(start_page=request.start_page,
                                             end_page=request.end_page
                                             )
        bond_zh_hs_spot_df = sanitize_data_pandas(bond_zh_hs_spot)

        return bond_zh_hs_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BondSymbolSpot(BaseModel):
    symbol: str = Field(..., title="带市场标识的债券代码",
                        description="例：sh010107")


# 债券-沪深债券-实时行情数据
@router.post("/bond_zh_hs_daily", operation_id="post_bond_zh_hs_daily")
async def post_bond_zh_hs_daily(request: BondSymbolSpot):
    """
    债券-沪深债券-历史行情数据

    接口: bond_zh_hs_daily

    目标地址: https://money.finance.sina.com.cn/bond/quotes/sh019315.html

    描述: 新浪财经-债券-沪深债券-历史行情数据, 历史数据按日频率更新

    限量: 单次返回具体某个沪深转债的所有历史行情数据
    """
    try:
        bond_zh_hs_daily = ak.bond_zh_hs_daily(symbol=request.symbol)
        bond_zh_hs_daily_df = sanitize_data_pandas(bond_zh_hs_daily)

        return bond_zh_hs_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
