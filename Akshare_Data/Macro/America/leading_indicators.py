import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-领先指标-未决房屋销售月率
@router.get("/macro_usa_phs",
            operation_id="get_macro_usa_phs")
async def get_macro_usa_phs():
    """
    美国-领先指标-未决房屋销售月率

    接口: macro_usa_phs

    目标地址: http://data.eastmoney.com/cjsj/foreign_0_5.html

    描述: 东方财富-经济数据一览-美国-未决房屋销售月率, 数据区间从 20080201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_phs = ak.macro_usa_phs()
        macro_usa_phs_df = sanitize_data_pandas(macro_usa_phs)
        return macro_usa_phs_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-领先指标-美国谘商会消费者信心指数报告
@router.get("/macro_usa_cb_consumer_confidence",
            operation_id="get_macro_usa_cb_consumer_confidence")
async def get_macro_usa_cb_consumer_confidence():
    """
    美国-领先指标-美国谘商会消费者信心指数报告

    接口: macro_usa_cb_consumer_confidence

    目标地址: https://cdn.jin10.com/dc/reports/dc_usa_cb_consumer_confidence_all.js?v=1578576859

    描述: 美国谘商会消费者信心指数报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cb_consumer_confidence = ak.macro_usa_cb_consumer_confidence()
        macro_usa_cb_consumer_confidence_df = sanitize_data_pandas(macro_usa_cb_consumer_confidence)
        return macro_usa_cb_consumer_confidence_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-领先指标-美国NFIB小型企业信心指数报告
@router.get("/macro_usa_nfib_small_business",
            operation_id="get_macro_usa_nfib_small_business")
async def get_macro_usa_nfib_small_business():
    """
    美国-领先指标-美国NFIB小型企业信心指数报告

    接口: macro_usa_nfib_small_business

    目标地址: https://cdn.jin10.com/dc/reports/dc_usa_nfib_small_business_all.js?v=1578576631

    描述: 美国NFIB小型企业信心指数报告, 数据区间从 19750201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_nfib_small_business = ak.macro_usa_nfib_small_business()
        macro_usa_nfib_small_business_df = sanitize_data_pandas(macro_usa_nfib_small_business)
        return macro_usa_nfib_small_business_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-领先指标-美国密歇根大学消费者信心指数初值报告
@router.get("/macro_usa_michigan_consumer_sentiment",
            operation_id="get_macro_usa_michigan_consumer_sentiment")
async def get_macro_usa_michigan_consumer_sentiment():
    """
    美国-领先指标-美国密歇根大学消费者信心指数初值报告

    接口: macro_usa_michigan_consumer_sentiment

    目标地址: https://cdn.jin10.com/dc/reports/dc_usa_michigan_consumer_sentiment_all.js?v=1578576228

    描述: 美国密歇根大学消费者信心指数初值报告, 数据区间从 19700301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_michigan_consumer_sentiment = ak.macro_usa_michigan_consumer_sentiment()
        macro_usa_michigan_consumer_sentiment_df = sanitize_data_pandas(macro_usa_michigan_consumer_sentiment)
        return macro_usa_michigan_consumer_sentiment_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
