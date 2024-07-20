# 盈利预测

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


@router.get("/stock_profit_forecast_em", operation_id="get_stock_profit_forecast_em")
def get_stock_profit_forecast_em():
    """
    东方财富网-数据中心-研究报告-盈利预测
    """
    try:
        stock_profit_forecast_em_df = ak.stock_profit_forecast_em()
        return stock_profit_forecast_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolIndicatorRequest(BaseModel):
    symbol: str
    indicator: str


@router.post("/stock_hk_profit_forecast_et", operation_id="post_stock_hk_profit_forecast_et")
async def post_stock_hk_profit_forecast_et(request: SymbolIndicatorRequest):
    """
    经济通-公司资料-盈利预测
    """
    try:
        stock_hk_profit_forecast_et_df = ak.stock_hk_profit_forecast_et(symbol=request.symbol,
                                                                        indicator=request.indicator)
        return stock_hk_profit_forecast_et_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_profit_forecast_ths", operation_id="post_stock_profit_forecast_ths")
async def post_stock_profit_forecast_ths(request: SymbolIndicatorRequest):
    """
    同花顺-盈利预测
    """
    try:
        stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol=request.symbol, indicator=request.indicator)
        return stock_profit_forecast_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
