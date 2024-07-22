# 盈利预测

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


class DongCaiSymbolRequest(BaseModel):
    symbol: str = Field(..., title="板块信息",
                        description="默认为获取全部数据，行业板块可以通过 stock_board_industry_name_em接口获取")


# 东方财富网-数据中心-研究报告-盈利预测
@router.post("/stock_profit_forecast_em", operation_id="post_stock_profit_forecast_em")
def post_stock_profit_forecast_em(request: DongCaiSymbolRequest):
    """
    接口: stock_profit_forecast_em

    目标地址: http://data.eastmoney.com/report/profitforecast.jshtml

    描述: 东方财富网-数据中心-研究报告-盈利预测; 该数据源网页端返回数据有异常, 本接口已修复该异常

    限量: 单次返回指定个股的数据
    """
    try:
        stock_profit_forecast_em_df = ak.stock_profit_forecast_em(symbol=request.symbol)
        return stock_profit_forecast_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JingJiTongHKSymbolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="港股代码", description="例：09999")
    indicator: str = Field(..., title="类型",
                           description="可选择'评级总览', '去年度业绩表现', '综合盈利预测', '盈利预测概览'")


# 经济通-公司资料-盈利预测
@router.post("/stock_hk_profit_forecast_et", operation_id="post_stock_hk_profit_forecast_et")
async def post_stock_hk_profit_forecast_et(request: JingJiTongHKSymbolIndicatorRequest):
    """
    接口: stock_hk_profit_forecast_et

    目标地址: https://www.etnet.com.hk/www/sc/stocks/realtime/quote_profit.php?code=9999

    描述: 经济通-公司资料-盈利预测

    限量: 单次返回指定个股和指定时间段的数据
    """
    try:
        stock_hk_profit_forecast_et_df = ak.stock_hk_profit_forecast_et(symbol=request.symbol,
                                                                        indicator=request.indicator)
        return stock_hk_profit_forecast_et_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class TongHuaShunSymbolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：600519")
    indicator: str = Field(..., title="类型",
                           description="可选择'预测年报每股收益', '预测年报净利润', '业绩预测详表-机构', '业绩预测详表-详细指标预测'")


# 同花顺-盈利预测
@router.post("/stock_profit_forecast_ths", operation_id="post_stock_profit_forecast_ths")
async def post_stock_profit_forecast_ths(request: TongHuaShunSymbolIndicatorRequest):
    """
    接口: stock_profit_forecast_ths

    目标地址: http://basic.10jqka.com.cn/new/600519/worth.html

    描述: 同花顺-盈利预测

    限量: 单次返回指定个股和指定时间段的数据
    """
    try:
        stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol=request.symbol, indicator=request.indicator)
        return stock_profit_forecast_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
