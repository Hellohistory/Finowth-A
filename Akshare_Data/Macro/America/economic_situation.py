import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-经济状况-美国GDP
@router.get("/macro_usa_gdp_monthly",
            operation_id="macro_usa_gdp_monthly")
async def macro_usa_gdp_monthly():
    """
    美国-经济状况-美国GDP

    接口: macro_usa_gdp_monthly

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_gdp

    描述: 美国国内生产总值(GDP)报告, 数据区间从 20080228-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_gdp_monthly = ak.macro_usa_gdp_monthly()
        macro_usa_gdp_monthly_df = sanitize_data_pandas(macro_usa_gdp_monthly)
        return macro_usa_gdp_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-经济状况-美国个人支出月率报告
@router.get("/macro_usa_personal_spending",
            operation_id="macro_usa_personal_spending")
async def macro_usa_personal_spending():
    """
    美国-经济状况-美国个人支出月率报告

    接口: macro_usa_personal_spending

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_personal_spending

    描述: 美国个人支出月率报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_personal_spending = ak.macro_usa_personal_spending()
        macro_usa_personal_spending_df = sanitize_data_pandas(macro_usa_personal_spending)
        return macro_usa_personal_spending_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
