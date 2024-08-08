import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 加拿大宏观-新屋开工
@router.get("/macro_canada_new_house_rate",
            operation_id="get_macro_canada_new_house_rate")
async def get_macro_canada_new_house_rate():
    """
    加拿大宏观-新屋开工

    接口: macro_canada_new_house_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_0.html

    描述: 东方财富-经济数据-加拿大-新屋开工

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_new_house_rate = ak.macro_canada_new_house_rate()
        macro_canada_new_house_rate_df = sanitize_data_pandas(macro_canada_new_house_rate)
        return macro_canada_new_house_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-失业率
@router.get("/macro_canada_unemployment_rate",
            operation_id="get_macro_canada_unemployment_rate")
async def get_macro_canada_unemployment_rate():
    """
    加拿大宏观-失业率

    接口: macro_canada_unemployment_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_1.html

    描述: 东方财富-经济数据-加拿大-失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_unemployment_rate = ak.macro_canada_unemployment_rate()
        macro_canada_unemployment_rate_df = sanitize_data_pandas(macro_canada_unemployment_rate)
        return macro_canada_unemployment_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-贸易帐
@router.get("/macro_canada_trade",
            operation_id="get_macro_canada_trade")
async def get_macro_canada_trade():
    """
    加拿大宏观-贸易帐

    接口: macro_canada_trade

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_2.html

    描述: 东方财富-经济数据-加拿大-贸易帐

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_trade = ak.macro_canada_trade()
        macro_canada_trade_df = sanitize_data_pandas(macro_canada_trade)
        return macro_canada_trade_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-零售销售月率
@router.get("/macro_canada_retail_rate_monthly",
            operation_id="get_macro_canada_retail_rate_monthly")
async def get_macro_canada_retail_rate_monthly():
    """
    加拿大宏观-零售销售月率

    接口: macro_canada_retail_rate_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_3.html

    描述: 东方财富-经济数据-加拿大-零售销售月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_retail_rate_monthly = ak.macro_canada_retail_rate_monthly()
        macro_canada_retail_rate_monthly_df = sanitize_data_pandas(macro_canada_retail_rate_monthly)
        return macro_canada_retail_rate_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-央行公布利率决议
@router.get("/macro_canada_bank_rate",
            operation_id="get_macro_canada_bank_rate")
async def get_macro_canada_bank_rate():
    """
    加拿大宏观-央行公布利率决议

    接口: macro_canada_bank_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_4.html

    描述: 东方财富-经济数据-加拿大-央行公布利率决议

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_bank_rate = ak.macro_canada_bank_rate()
        macro_canada_bank_rate_df = sanitize_data_pandas(macro_canada_bank_rate)
        return macro_canada_bank_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-核心消费者物价指数年率
@router.get("/macro_canada_core_cpi_yearly",
            operation_id="get_macro_canada_core_cpi_yearly")
async def get_macro_canada_core_cpi_yearly():
    """
    加拿大宏观-核心消费者物价指数年率

    接口: macro_canada_core_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_5.html

    描述: 东方财富-经济数据-加拿大-核心消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_core_cpi_yearly = ak.macro_canada_core_cpi_yearly()
        macro_canada_core_cpi_yearly_df = sanitize_data_pandas(macro_canada_core_cpi_yearly)
        return macro_canada_core_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-核心消费者物价指数月率
@router.get("/macro_canada_core_cpi_monthly",
            operation_id="get_macro_canada_core_cpi_monthly")
async def get_macro_canada_core_cpi_monthly():
    """
    加拿大宏观-核心消费者物价指数月率

    接口: macro_canada_core_cpi_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_6.html

    描述: 东方财富-经济数据-加拿大-核心消费者物价指数月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_core_cpi_monthly = ak.macro_canada_core_cpi_monthly()
        macro_canada_core_cpi_monthly_df = sanitize_data_pandas(macro_canada_core_cpi_monthly)
        return macro_canada_core_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-消费者物价指数年率
@router.get("/macro_canada_cpi_yearly",
            operation_id="get_macro_canada_cpi_yearly")
async def get_macro_canada_cpi_yearly():
    """
    加拿大宏观-核心消费者物价指数月率

    接口: macro_canada_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_7.html

    描述: 东方财富-经济数据-加拿大-消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_cpi_yearly = ak.macro_canada_cpi_yearly()
        macro_canada_cpi_yearly_df = sanitize_data_pandas(macro_canada_cpi_yearly)
        return macro_canada_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 加拿大宏观-GDP 月率
@router.get("/macro_canada_gdp_monthly",
            operation_id="get_macro_canada_gdp_monthly")
async def get_macro_canada_gdp_monthly():
    """
    加拿大宏观-GDP 月率

    接口: macro_canada_gdp_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_7_9.html

    描述: 东方财富-经济数据-加拿大-GDP 月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_canada_gdp_monthly = ak.macro_canada_gdp_monthly()
        macro_canada_gdp_monthly_df = sanitize_data_pandas(macro_canada_gdp_monthly)
        return macro_canada_gdp_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
