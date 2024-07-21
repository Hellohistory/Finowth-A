import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import StockAHDailyRequest

router = APIRouter()


# 腾讯财经-A+H 股实时行情数据
@router.get("/stock_zh_ah_spot", operation_id="get_stock_zh_ah_spot")
def get_stock_zh_ah_spot():
    """
    接口: stock_zh_ah_spot

    目标地址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH

    描述: A+H 股数据是从腾讯财经获取的数据, 延迟 15 分钟更新

    限量: 单次返回所有 A+H 上市公司的实时行情数据
    """
    try:
        stock_zh_ah_spot_df = ak.stock_zh_ah_spot()
        return stock_zh_ah_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 腾讯财经-A+H 股历史行情数据
@router.post("/stock_zh_ah_daily", operation_id="post_stock_zh_ah_daily")
async def post_stock_zh_ah_daily(request: StockAHDailyRequest):
    """
    接口: stock_zh_ah_daily

    目标地址: https://gu.qq.com/hk02359/gp

    描述: 腾讯财经-A+H 股数据

    限量: 单次返回指定参数的 A+H 上市公司的历史行情数据
    """
    try:
        stock_zh_ah_daily_df = ak.stock_zh_ah_daily(
            symbol=request.symbol,
            start_year=request.start_year,
            end_year=request.end_year,
            adjust=request.adjust
        )
        return stock_zh_ah_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# A+H 股票字典
@router.get("/stock_zh_ah_name", operation_id="get_stock_zh_ah_name")
def get_stock_zh_ah_name():
    """
    接口: stock_zh_ah_name

    目标地址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH

    描述: A+H 股数据是从腾讯财经获取的数据, 历史数据按日频率更新

    限量: 单次返回所有 A+H 上市公司的代码和名称
    """
    try:
        stock_zh_ah_name_df = ak.stock_zh_ah_name()
        return stock_zh_ah_name_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
