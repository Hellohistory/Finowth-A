import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 澳大利亚宏观-零售销售月率
@router.get("/macro_australia_retail_rate_monthly",
            operation_id="get_macro_australia_retail_rate_monthly")
async def get_macro_australia_retail_rate_monthly():
    """
    澳大利亚宏观-零售销售月率

    接口: macro_australia_retail_rate_monthly

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_0.html

    描述: 东方财富-经济数据-澳大利亚-零售销售月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_retail_rate_monthly = ak.macro_australia_retail_rate_monthly()
        macro_australia_retail_rate_monthly_df = sanitize_data_pandas(macro_australia_retail_rate_monthly)
        return macro_australia_retail_rate_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 澳大利亚宏观-贸易帐
@router.get("/macro_australia_trade",
            operation_id="get_macro_australia_trade")
async def get_macro_australia_trade():
    """
    澳大利亚宏观-贸易帐

    接口: macro_australia_trade

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_1.html

    描述: 东方财富-经济数据-澳大利亚-贸易帐

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_trade = ak.macro_australia_trade()
        macro_australia_trade_df = sanitize_data_pandas(macro_australia_trade)
        return macro_australia_trade_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 澳大利亚宏观-失业率
@router.get("/macro_australia_unemployment_rate",
            operation_id="get_macro_australia_unemployment_rate")
async def get_macro_australia_unemployment_rate():
    """
    澳大利亚宏观-失业率

    接口: macro_australia_unemployment_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_2.html

    描述: 东方财富-经济数据-澳大利亚-失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_unemployment_rate = ak.macro_australia_unemployment_rate()
        macro_australia_unemployment_rate_df = sanitize_data_pandas(macro_australia_unemployment_rate)
        return macro_australia_unemployment_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 澳大利亚宏观-生产者物价指数季率
@router.get("/macro_australia_ppi_quarterly",
            operation_id="get_macro_australia_ppi_quarterly")
async def get_macro_australia_ppi_quarterly():
    """
    澳大利亚宏观-生产者物价指数季率

    接口: macro_australia_ppi_quarterly

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_3.html

    描述: 东方财富-经济数据-澳大利亚-生产者物价指数季率

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_ppi_quarterly = ak.macro_australia_ppi_quarterly()
        macro_australia_ppi_quarterly_df = sanitize_data_pandas(macro_australia_ppi_quarterly)
        return macro_australia_ppi_quarterly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 澳大利亚宏观-消费者物价指数季率
@router.get("/macro_australia_cpi_quarterly",
            operation_id="get_macro_australia_cpi_quarterly")
async def get_macro_australia_cpi_quarterly():
    """
    澳大利亚宏观-消费者物价指数季率

    接口: macro_australia_cpi_quarterly

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_4.html

    描述: 东方财富-经济数据-澳大利亚-消费者物价指数季率

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_cpi_quarterly = ak.macro_australia_cpi_quarterly()
        macro_australia_cpi_quarterly_df = sanitize_data_pandas(macro_australia_cpi_quarterly)
        return macro_australia_cpi_quarterly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 澳大利亚宏观-消费者物价指数年率
@router.get("/macro_australia_cpi_yearly",
            operation_id="get_macro_australia_cpi_yearly")
async def get_macro_australia_cpi_yearly():
    """
    澳大利亚宏观-消费者物价指数年率

    接口: macro_australia_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_5.html

    描述: 东方财富-经济数据-澳大利亚-消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_cpi_yearly = ak.macro_australia_cpi_yearly()
        macro_australia_cpi_yearly_df = sanitize_data_pandas(macro_australia_cpi_yearly)
        return macro_australia_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 澳大利亚宏观-央行公布利率决议
@router.get("/macro_australia_bank_rate",
            operation_id="get_macro_australia_bank_rate")
async def get_macro_australia_bank_rate():
    """
    澳大利亚宏观-央行公布利率决议

    接口: macro_australia_bank_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_5_6.html

    描述: 东方财富-经济数据-澳大利亚-央行公布利率决议

    限量: 单次返回所有历史数据
    """
    try:
        macro_australia_bank_rate = ak.macro_australia_bank_rate()
        macro_australia_bank_rate_df = sanitize_data_pandas(macro_australia_bank_rate)
        return macro_australia_bank_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
