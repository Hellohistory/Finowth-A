import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 德国宏观-IFO商业景气指数
@router.get("/macro_germany_ifo",
            operation_id="get_macro_germany_ifo")
async def get_macro_germany_ifo():
    """
    德国宏观-IFO商业景气指数

    接口: macro_germany_ifo

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_0.html

    描述: 东方财富-数据中心-经济数据一览-IFO商业景气指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_ifo = ak.macro_germany_ifo()
        macro_germany_ifo_df = sanitize_data_pandas(macro_germany_ifo)
        return macro_germany_ifo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-消费者物价指数月率终值
@router.get("/macro_germany_cpi_monthly",
            operation_id="get_macro_germany_cpi_monthly")
async def get_macro_germany_cpi_monthly():
    """
    德国宏观-消费者物价指数月率终值

    接口: macro_germany_cpi_monthly

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_1.html

    描述: 东方财富-数据中心-经济数据一览-德国-消费者物价指数月率终值

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_cpi_monthly = ak.macro_germany_cpi_monthly()
        macro_germany_cpi_monthly_df = sanitize_data_pandas(macro_germany_cpi_monthly)
        return macro_germany_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-消费者物价指数年率终值
@router.get("/macro_germany_cpi_yearly",
            operation_id="get_macro_germany_cpi_yearly")
async def get_macro_germany_cpi_yearly():
    """
    德国宏观-消费者物价指数年率终值

    接口: macro_germany_cpi_yearly

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_2.html

    描述: 东方财富-数据中心-经济数据一览-德国-消费者物价指数年率终值

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_cpi_yearly = ak.macro_germany_cpi_yearly()
        macro_germany_cpi_yearly_df = sanitize_data_pandas(macro_germany_cpi_yearly)
        return macro_germany_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-贸易帐-季调后
@router.get("/macro_germany_trade_adjusted",
            operation_id="get_macro_germany_trade_adjusted")
async def get_macro_germany_trade_adjusted():
    """
    德国宏观-贸易帐-季调后

    接口: macro_germany_trade_adjusted

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_3.html

    描述: 东方财富-数据中心-经济数据一览-德国-贸易帐(季调后)

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_trade_adjusted = ak.macro_germany_trade_adjusted()
        macro_germany_trade_adjusted_df = sanitize_data_pandas(macro_germany_trade_adjusted)
        return macro_germany_trade_adjusted_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-贸易帐-GDP
@router.get("/macro_germany_gdp",
            operation_id="get_macro_germany_gdp")
async def get_macro_germany_gdp():
    """
    德国宏观-贸易帐-GDP

    接口: macro_germany_gdp

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_4.html

    描述: 东方财富-数据中心-经济数据一览-德国-GDP

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_gdp = ak.macro_germany_gdp()
        macro_germany_gdp_df = sanitize_data_pandas(macro_germany_gdp)
        return macro_germany_gdp_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-实际零售销售月率
@router.get("/macro_germany_retail_sale_monthly",
            operation_id="get_macro_germany_retail_sale_monthly")
async def get_macro_germany_retail_sale_monthly():
    """
    德国宏观-实际零售销售月率

    接口: macro_germany_retail_sale_monthly

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_5.html

    描述: 东方财富-数据中心-经济数据一览-德国-实际零售销售月率

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_retail_sale_monthly = ak.macro_germany_retail_sale_monthly()
        macro_germany_retail_sale_monthly_df = sanitize_data_pandas(macro_germany_retail_sale_monthly)
        return macro_germany_retail_sale_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-实际零售销售年率
@router.get("/macro_germany_retail_sale_yearly",
            operation_id="get_macro_germany_retail_sale_yearly")
async def get_macro_germany_retail_sale_yearly():
    """
    德国宏观-实际零售销售月率

    接口: macro_germany_retail_sale_yearly

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_6.html

    描述: 东方财富-数据中心-经济数据一览-德国-实际零售销售年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_retail_sale_yearly = ak.macro_germany_retail_sale_yearly()
        macro_germany_retail_sale_yearly_df = sanitize_data_pandas(macro_germany_retail_sale_yearly)
        return macro_germany_retail_sale_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 德国宏观-ZEW 经济景气指数
@router.get("/macro_germany_zew",
            operation_id="get_macro_germany_zew")
async def get_macro_germany_zew():
    """
    德国宏观-ZEW 经济景气指数

    接口: macro_germany_zew

    目标地址: https://data.eastmoney.com/cjsj/foreign_1_7.html

    描述: 东方财富-数据中心-经济数据一览-德国-ZEW 经济景气指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_germany_zew = ak.macro_germany_zew()
        macro_germany_zew_df = sanitize_data_pandas(macro_germany_zew)
        return macro_germany_zew_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))















