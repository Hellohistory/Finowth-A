import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-消费者收入与支出-美国核心PCE物价指数年率报告
@router.get("/macro_usa_core_pce_price",
            operation_id="get_macro_usa_core_pce_price")
async def get_macro_usa_core_pce_price():
    """
    美国-消费者收入与支出-美国核心PCE物价指数年率报告

    接口: macro_usa_core_pce_price

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_core_pce_price

    描述: 美国核心 PCE 物价指数年率报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_core_pce_price = ak.macro_usa_core_pce_price()
        macro_usa_core_pce_price_df = sanitize_data_pandas(macro_usa_core_pce_price)
        return macro_usa_core_pce_price_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-消费者收入与支出-美国实际个人消费支出季率初值报告
@router.get("/macro_usa_real_consumer_spending",
            operation_id="get_macro_usa_real_consumer_spending")
async def get_macro_usa_real_consumer_spending():
    """
    美国-消费者收入与支出-美国核心PCE物价指数年率报告

    接口: macro_usa_real_consumer_spending

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_real_consumer_spending

    描述: 美国实际个人消费支出季率初值报告, 数据区间从 20131107-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_real_consumer_spending = ak.macro_usa_real_consumer_spending()
        macro_usa_real_consumer_spending_df = sanitize_data_pandas(macro_usa_real_consumer_spending)
        return macro_usa_real_consumer_spending_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
