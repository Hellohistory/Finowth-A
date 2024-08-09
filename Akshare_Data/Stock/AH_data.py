import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 腾讯财经-A+H 股实时行情数据
@router.get("/stock_zh_ah_spot", operation_id="stock_zh_ah_spot")
def stock_zh_ah_spot():
    """
    腾讯财经-A+H 股数据

    接口: stock_zh_ah_spot

    目标地址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH

    描述: A+H 股数据是从腾讯财经获取的数据, 延迟 15 分钟更新

    限量: 单次返回所有 A+H 上市公司的实时行情数据
    """
    try:
        stock_zh_ah_spot = ak.stock_zh_ah_spot()
        stock_zh_ah_spot_df = sanitize_data_pandas(stock_zh_ah_spot)
        return stock_zh_ah_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockAHDailyRequest(BaseModel):
    symbol: str = Field(..., title="港股股票代码", description="例：02318，可通过stock_zh_ah_name获取")
    start_year: str = Field(..., title="开始年份", description="例：2000")
    end_year: str = Field(..., title="结束年份", description="例：2019")
    adjust: str = Field(..., title="复权形式", description="默认为空不复权; 'qfq': 前复权, 'hfq': 后复权")


# 腾讯财经-A+H 股历史行情数据
@router.post("/stock_zh_ah_daily", operation_id="stock_zh_ah_daily")
async def stock_zh_ah_daily(request: StockAHDailyRequest):
    """
    腾讯财经-A+H 股数据

    接口: stock_zh_ah_daily

    目标地址: https://gu.qq.com/hk02359/gp

    描述: 腾讯财经-A+H 股数据

    限量: 单次返回指定参数的 A+H 上市公司的历史行情数据
    """
    try:
        stock_zh_ah_daily = ak.stock_zh_ah_daily(
            symbol=request.symbol,
            start_year=request.start_year,
            end_year=request.end_year,
            adjust=request.adjust
        )
        stock_zh_ah_daily_df = sanitize_data_pandas(stock_zh_ah_daily)
        return stock_zh_ah_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# A+H 股票字典
@router.get("/stock_zh_ah_name", operation_id="stock_zh_ah_name")
def stock_zh_ah_name():
    """
    腾讯财经-A+H 股票字典

    接口: stock_zh_ah_name

    目标地址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH

    描述: A+H 股数据是从腾讯财经获取的数据, 历史数据按日频率更新

    限量: 单次返回所有 A+H 上市公司的代码和名称
    """
    try:
        stock_zh_ah_name = ak.stock_zh_ah_name()
        stock_zh_ah_name_df = sanitize_data_pandas(stock_zh_ah_name)
        return stock_zh_ah_name_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
