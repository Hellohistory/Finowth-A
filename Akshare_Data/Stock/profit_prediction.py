# 盈利预测

import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.request_model import SymbolIndicatorRequest

router = APIRouter()


@router.get("/stock_profit_forecast_em", operation_id="get_stock_profit_forecast_em")
def get_stock_profit_forecast_em():
    """
    接口: stock_profit_forecast_em

    目标地址: http://data.eastmoney.com/report/profitforecast.jshtml

    描述: 东方财富网-数据中心-研究报告-盈利预测; 该数据源网页端返回数据有异常, 本接口已修复该异常

    限量: 单次返回指定个股的数据

    请求类型: `POST`
    """
    try:
        stock_profit_forecast_em_df = ak.stock_profit_forecast_em()
        return stock_profit_forecast_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_hk_profit_forecast_et", operation_id="post_stock_hk_profit_forecast_et")
async def post_stock_hk_profit_forecast_et(request: SymbolIndicatorRequest):
    """
    接口: stock_hk_profit_forecast_et

    目标地址: https://www.etnet.com.hk/www/sc/stocks/realtime/quote_profit.php?code=9999

    描述: 经济通-公司资料-盈利预测

    限量: 单次返回指定个股和指定时间段的数据

    请求类型: `POST`
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
    接口: stock_profit_forecast_ths

    目标地址: http://basic.10jqka.com.cn/new/600519/worth.html

    描述: 同花顺-盈利预测

    限量: 单次返回指定个股和指定时间段的数据

    请求类型: `POST`
    """
    try:
        stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol=request.symbol, indicator=request.indicator)
        return stock_profit_forecast_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
