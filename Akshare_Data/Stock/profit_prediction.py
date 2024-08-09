# 盈利预测

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DongCaiSymbolRequest(BaseModel):
    symbol: str = Field(..., title="板块信息",
                        description="默认为获取全部数据，行业板块可以通过 stock_board_industry_name_em接口获取")


# 东方财富-数据中心-研究报告-盈利预测
@router.post("/stock_profit_forecast_em", operation_id="stock_profit_forecast_em")
def stock_profit_forecast_em(request: DongCaiSymbolRequest):
    """
    东方财富-研究报告-盈利预测

    接口: stock_profit_forecast_em

    目标地址: http://data.eastmoney.com/report/profitforecast.jshtml

    描述: 东方财富-数据中心-研究报告-盈利预测

    限量: 单次返回指定个股的数据
    """
    try:
        stock_profit_forecast_em = ak.stock_profit_forecast_em(symbol=request.symbol)
        stock_profit_forecast_em_df = sanitize_data_pandas(stock_profit_forecast_em)
        return stock_profit_forecast_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JingJiTongHKSymbolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="港股代码", description="例：09999")
    indicator: str = Field(..., title="类型",
                           description="可选择'评级总览', '去年度业绩表现', '综合盈利预测', '盈利预测概览'")


# 经济通-公司资料-盈利预测
@router.post("/stock_hk_profit_forecast_et", operation_id="stock_hk_profit_forecast_et")
async def stock_hk_profit_forecast_et(request: JingJiTongHKSymbolIndicatorRequest):
    """
    经济通-公司资料-盈利预测

    接口: stock_hk_profit_forecast_et

    目标地址: https://www.etnet.com.hk/www/sc/stocks/realtime/quote_profit.php?code=9999

    描述: 经济通-公司资料-盈利预测

    限量: 单次返回指定个股和指定时间段的数据
    """
    try:
        stock_hk_profit_forecast_et = ak.stock_hk_profit_forecast_et(symbol=request.symbol,
                                                                        indicator=request.indicator)
        stock_hk_profit_forecast_et_df = sanitize_data_pandas(stock_hk_profit_forecast_et)
        return stock_hk_profit_forecast_et_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class TongHuaShunSymbolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：600519")
    indicator: str = Field(..., title="类型",
                           description="可选择'预测年报每股收益', '预测年报净利润', '业绩预测详表-机构', '业绩预测详表-详细指标预测'")


# 同花顺-盈利预测
@router.post("/stock_profit_forecast_ths", operation_id="stock_profit_forecast_ths")
async def stock_profit_forecast_ths(request: TongHuaShunSymbolIndicatorRequest):
    """
    同花顺-盈利预测

    接口: stock_profit_forecast_ths

    目标地址: http://basic.10jqka.com.cn/new/600519/worth.html

    描述: 同花顺-盈利预测

    限量: 单次返回指定个股和指定时间段的数据
    """
    try:
        stock_profit_forecast_ths = ak.stock_profit_forecast_ths(
            symbol=request.symbol,
            indicator=request.indicator
        )
        stock_profit_forecast_ths_df = sanitize_data_pandas(stock_profit_forecast_ths)
        return stock_profit_forecast_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
