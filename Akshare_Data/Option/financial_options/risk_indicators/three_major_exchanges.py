import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class OptionRiskIndicator(BaseModel):
    date: str = Field(..., title="指定交易日",
                      description="例：20240626，数据从 20150209 开始")


# 期权-金融期权-风险指标-上海证券交易所
@router.post("/option_risk_indicator_sse",
             operation_id="option_risk_indicator_sse")
def option_risk_indicator_sse(request: OptionRiskIndicator):
    """
    期权-金融期权-风险指标-上海证券交易所

    接口: option_risk_indicator_sse

    目标地址: http://www.sse.com.cn/assortment/options/risk/

    描述: 上海证券交易所-产品-股票期权-期权风险指标数据

    限量: 单次返回指定交易日的数据
    """
    try:
        option_risk_indicator_sse = ak.option_risk_indicator_sse(date=request.date)
        option_risk_indicator_sse_df = sanitize_data_pandas(option_risk_indicator_sse)

        return option_risk_indicator_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-每日统计-上海证券交易所
@router.post("/option_daily_stats_sse",
             operation_id="option_daily_stats_sse")
def option_daily_stats_sse(request: OptionRiskIndicator):
    """
    期权-金融期权-每日统计-上海证券交易所

    接口: option_daily_stats_sse

    目标地址: http://www.sse.com.cn/assortment/options/date/

    描述: 上海证券交易所-产品-股票期权-每日统计

    限量: 单次返回指定交易日的数据
    """
    try:
        option_daily_stats_sse = ak.option_daily_stats_sse(date=request.date)
        option_daily_stats_sse_df = sanitize_data_pandas(option_daily_stats_sse)

        return option_daily_stats_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-每日统计-上海证券交易所
@router.post("/option_daily_stats_szse",
             operation_id="option_daily_stats_szse")
def option_daily_stats_szse(request: OptionRiskIndicator):
    """
    期权-金融期权-每日统计-深圳证券交易所

    接口: option_daily_stats_szse

    目标地址: https://investor.szse.cn/market/option/day/index.html

    描述: 深圳证券交易所-市场数据-期权数据-日度概况

    限量: 单次返回指定交易日的数据
    """
    try:
        option_daily_stats_szse = ak.option_daily_stats_sse(date=request.date)
        option_daily_stats_szse_df = sanitize_data_pandas(option_daily_stats_szse)

        return option_daily_stats_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
