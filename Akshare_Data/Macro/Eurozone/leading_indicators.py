import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 欧元区宏观-领先指标-欧元区ZEW经济景气指数报告
@router.get("/macro_euro_zew_economic_sentiment",
            operation_id="get_macro_euro_zew_economic_sentiment")
async def get_macro_euro_zew_economic_sentiment():
    """
    欧元区宏观-领先指标-欧元区ZEW经济景气指数报告

    接口: macro_euro_zew_economic_sentiment

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_zew_economic_sentiment

    描述: 欧元区 ZEW 经济景气指数报告, 数据区间从 20080212-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_zew_economic_sentiment = ak.macro_euro_zew_economic_sentiment()
        macro_euro_zew_economic_sentiment_df = sanitize_data_pandas(macro_euro_zew_economic_sentiment)
        return macro_euro_zew_economic_sentiment_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 欧元区宏观-领先指标-欧元区Sentix投资者信心指数报告
@router.get("/macro_euro_sentix_investor_confidence",
            operation_id="get_macro_euro_sentix_investor_confidence")
async def get_macro_euro_sentix_investor_confidence():
    """
    欧元区宏观-领先指标-欧元区Sentix投资者信心指数报告

    接口: macro_euro_sentix_investor_confidence

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_sentix_investor_confidence

    描述: 欧元区 Sentix 投资者信心指数报告, 数据区间从 20020801-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_sentix_investor_confidence = ak.macro_euro_sentix_investor_confidence()
        macro_euro_sentix_investor_confidence_df = sanitize_data_pandas(macro_euro_sentix_investor_confidence)
        return macro_euro_sentix_investor_confidence_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
