import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 英国宏观-Halifax 房价指数月率
@router.get("/macro_uk_halifax_monthly",
            operation_id="get_macro_uk_halifax_monthly")
async def get_macro_uk_halifax_monthly():
    """
    英国宏观-Halifax 房价指数月率

    接口: macro_uk_halifax_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_0.html

    描述: 东方财富-经济数据-英国-Halifax 房价指数月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_halifax_monthly = ak.macro_uk_halifax_monthly()
        macro_uk_halifax_monthly_df = sanitize_data_pandas(macro_uk_halifax_monthly)
        return macro_uk_halifax_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-Halifax 房价指数年率
@router.get("/macro_uk_halifax_yearly",
            operation_id="get_macro_uk_halifax_yearly")
async def get_macro_uk_halifax_yearly():
    """
    英国宏观-Halifax 房价指数年率

    接口: macro_uk_halifax_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_1.html

    描述: 东方财富-经济数据-英国-Halifax 房价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_halifax_yearly = ak.macro_uk_halifax_yearly()
        macro_uk_halifax_yearly_df = sanitize_data_pandas(macro_uk_halifax_yearly)
        return macro_uk_halifax_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-贸易帐
@router.get("/macro_uk_trade",
            operation_id="get_macro_uk_trade")
async def get_macro_uk_trade():
    """
    英国宏观-贸易帐

    接口: macro_uk_trade

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_2.html

    描述: 东方财富-经济数据-英国-贸易帐

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_trade = ak.macro_uk_trade()
        macro_uk_trade_df = sanitize_data_pandas(macro_uk_trade)
        return macro_uk_trade_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-央行公布利率决议
@router.get("/macro_uk_bank_rate",
            operation_id="get_macro_uk_bank_rate")
async def get_macro_uk_bank_rate():
    """
    英国宏观-央行公布利率决议

    接口: macro_uk_bank_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_3.html

    描述: 东方财富-经济数据-英国-央行公布利率决议

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_bank_rate = ak.macro_uk_bank_rate()
        macro_uk_bank_rate_df = sanitize_data_pandas(macro_uk_bank_rate)
        return macro_uk_bank_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-核心消费者物价指数年率
@router.get("/macro_uk_core_cpi_yearly",
            operation_id="get_macro_uk_core_cpi_yearly")
async def get_macro_uk_core_cpi_yearly():
    """
    英国宏观-核心消费者物价指数年率

    接口: macro_uk_core_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_4.html

    描述: 东方财富-经济数据-英国-核心消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_core_cpi_yearly = ak.macro_uk_core_cpi_yearly()
        macro_uk_core_cpi_yearly_df = sanitize_data_pandas(macro_uk_core_cpi_yearly)
        return macro_uk_core_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-核心消费者物价指数月率
@router.get("/macro_uk_core_cpi_monthly",
            operation_id="get_macro_uk_core_cpi_monthly")
async def get_macro_uk_core_cpi_monthly():
    """
    英国宏观-核心消费者物价指数月率

    接口: macro_uk_core_cpi_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_7.html

    描述: 东方财富-经济数据-英国-核心消费者物价指数月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_core_cpi_monthly = ak.macro_uk_core_cpi_monthly()
        macro_uk_core_cpi_monthly_df = sanitize_data_pandas(macro_uk_core_cpi_monthly)
        return macro_uk_core_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-消费者物价指数年率
@router.get("/macro_uk_cpi_yearly",
            operation_id="get_macro_uk_cpi_yearly")
async def get_macro_uk_cpi_yearly():
    """
    英国宏观-消费者物价指数年率

    接口: macro_uk_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_6.html

    描述: 东方财富-经济数据-英国-消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_cpi_yearly = ak.macro_uk_cpi_yearly()
        macro_uk_cpi_yearly_df = sanitize_data_pandas(macro_uk_cpi_yearly)
        return macro_uk_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-消费者物价指数月率
@router.get("/macro_uk_cpi_monthly",
            operation_id="get_macro_uk_cpi_monthly")
async def get_macro_uk_cpi_monthly():
    """
    英国宏观-消费者物价指数月率

    接口: macro_uk_cpi_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_7.html

    描述: 东方财富-经济数据-英国-消费者物价指数月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_cpi_monthly = ak.macro_uk_cpi_monthly()
        macro_uk_cpi_monthly_df = sanitize_data_pandas(macro_uk_cpi_monthly)
        return macro_uk_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-零售销售月率
@router.get("/macro_uk_retail_monthly",
            operation_id="get_macro_uk_retail_monthly")
async def get_macro_uk_retail_monthly():
    """
    英国宏观-零售销售月率

    接口: macro_uk_retail_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_8.html

    描述: 东方财富-经济数据-英国-零售销售月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_retail_monthly = ak.macro_uk_retail_monthly()
        macro_uk_retail_monthly_df = sanitize_data_pandas(macro_uk_retail_monthly)
        return macro_uk_retail_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-零售销售年率
@router.get("/macro_uk_retail_yearly",
            operation_id="get_macro_uk_retail_yearly")
async def get_macro_uk_retail_yearly():
    """
    英国宏观-零售销售年率

    接口: macro_uk_retail_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_9.html

    描述: 东方财富-经济数据-英国-零售销售年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_retail_yearly = ak.macro_uk_retail_yearly()
        macro_uk_retail_yearly_df = sanitize_data_pandas(macro_uk_retail_yearly)
        return macro_uk_retail_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-Rightmove 房价指数年率
@router.get("/macro_uk_rightmove_yearly",
            operation_id="get_macro_uk_rightmove_yearly")
async def get_macro_uk_rightmove_yearly():
    """
    英国宏观-Rightmove 房价指数年率

    接口: macro_uk_rightmove_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_10.html

    描述: 东方财富-经济数据-英国-Rightmove 房价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_rightmove_yearly = ak.macro_uk_rightmove_yearly()
        macro_uk_rightmove_yearly_df = sanitize_data_pandas(macro_uk_rightmove_yearly)
        return macro_uk_rightmove_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-Rightmove 房价指数月率
@router.get("/macro_uk_rightmove_monthly",
            operation_id="get_macro_uk_rightmove_monthly")
async def get_macro_uk_rightmove_monthly():
    """
    英国宏观-Rightmove 房价指数月率

    接口: macro_uk_rightmove_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_11.html

    描述: 东方财富-经济数据-英国-Rightmove 房价指数月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_rightmove_monthly = ak.macro_uk_rightmove_monthly()
        macro_uk_rightmove_monthly_df = sanitize_data_pandas(macro_uk_rightmove_monthly)
        return macro_uk_rightmove_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-GDP 季率初值
@router.get("/macro_uk_gdp_quarterly",
            operation_id="get_macro_uk_gdp_quarterly")
async def get_macro_uk_gdp_quarterly():
    """
    英国宏观-GDP 季率初值

    接口: macro_uk_gdp_quarterly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_12.html

    描述: 东方财富-经济数据-英国-GDP 季率初值

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_gdp_quarterly = ak.macro_uk_gdp_quarterly()
        macro_uk_gdp_quarterly_df = sanitize_data_pandas(macro_uk_gdp_quarterly)
        return macro_uk_gdp_quarterly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-GDP 年率初值
@router.get("/macro_uk_gdp_yearly",
            operation_id="get_macro_uk_gdp_yearly")
async def get_macro_uk_gdp_yearly():
    """
    英国宏观-GDP 年率初值

    接口: macro_uk_gdp_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_13.html

    描述: 东方财富-经济数据-英国-GDP 年率初值

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_gdp_yearly = ak.macro_uk_gdp_yearly()
        macro_uk_gdp_yearly_df = sanitize_data_pandas(macro_uk_gdp_yearly)
        return macro_uk_gdp_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 英国宏观-失业率
@router.get("/macro_uk_unemployment_rate",
            operation_id="get_macro_uk_unemployment_rate")
async def get_macro_uk_unemployment_rate():
    """
    英国宏观-失业率

    接口: macro_uk_unemployment_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_4_14.html

    描述: 东方财富-经济数据-英国-失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_uk_unemployment_rate = ak.macro_uk_unemployment_rate()
        macro_uk_unemployment_rate_df = sanitize_data_pandas(macro_uk_unemployment_rate)
        return macro_uk_unemployment_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
