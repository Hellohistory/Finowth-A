import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymolIndicatorRequest

router = APIRouter()


@router.post("/stock_hk_indicator_eniu", operation_id="post_stock_hk_indicator_eniu")
async def post_stock_hk_indicator_eniu(request: SymolIndicatorRequest):
    """
    获取香港股票某一指标的数据
    单次获取指定 symbol 和 indicator 的所有历史数据
    """
    try:
        stock_hk_indicator_eniu_df = ak.stock_hk_indicator_eniu(symbol=request.symbol, indicator=request.indicator)
        return stock_hk_indicator_eniu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
