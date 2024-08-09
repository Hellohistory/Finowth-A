import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-经济状况-欧元区季度GDP年率报告
@router.get("/macro_euro_gdp_yoy",
            operation_id="macro_euro_gdp_yoy")
async def macro_euro_gdp_yoy():
    """
    国民经济运行状况-经济状况-欧元区季度GDP年率报告

    接口: macro_euro_gdp_yoy

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_gdp_yoy

    描述: 欧元区季度 GDP 年率报告, 数据区间从 20131114-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_gdp_yoy = ak.macro_euro_gdp_yoy()
        macro_euro_gdp_yoy_df = sanitize_data_pandas(macro_euro_gdp_yoy)
        return macro_euro_gdp_yoy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-欧元区CPI月率报告
@router.get("/macro_euro_cpi_mom",
            operation_id="macro_euro_cpi_mom")
async def macro_euro_cpi_mom():
    """
    国民经济运行状况-物价水平-欧元区CPI月率报告

    接口: macro_euro_cpi_mom

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_cpi_mom

    描述: 欧元区 CPI 月率报告, 数据区间从 19900301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_cpi_mom = ak.macro_euro_cpi_mom()
        macro_euro_cpi_mom_df = sanitize_data_pandas(macro_euro_cpi_mom)
        return macro_euro_cpi_mom_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-欧元区CPI年率报告
@router.get("/macro_euro_cpi_yoy",
            operation_id="macro_euro_cpi_yoy")
async def macro_euro_cpi_yoy():
    """
    国民经济运行状况-物价水平-欧元区CPI年率报告

    接口: macro_euro_cpi_yoy

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_cpi_yoy

    描述: 欧元区 CPI 年率报告, 数据区间从 19910201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_cpi_yoy = ak.macro_euro_cpi_yoy()
        macro_euro_cpi_yoy_df = sanitize_data_pandas(macro_euro_cpi_yoy)
        return macro_euro_cpi_yoy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-欧元区PPI月率报告
@router.get("/macro_euro_ppi_mom",
            operation_id="macro_euro_ppi_mom")
async def macro_euro_ppi_mom():
    """
    国民经济运行状况-物价水平-欧元区PPI月率报告

    接口: macro_euro_ppi_mom

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_ppi_mom

    描述: 欧元区 PPI 月率报告, 数据区间从 19810301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_ppi_mom = ak.macro_euro_ppi_mom()
        macro_euro_ppi_mom_df = sanitize_data_pandas(macro_euro_ppi_mom)
        return macro_euro_ppi_mom_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-欧元区零售销售月率报告
@router.get("/macro_euro_retail_sales_mom",
            operation_id="macro_euro_retail_sales_mom")
async def macro_euro_retail_sales_mom():
    """
    国民经济运行状况-物价水平-欧元区零售销售月率报告

    接口: macro_euro_retail_sales_mom

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_retail_sales_mom

    描述: 欧元区零售销售月率报告, 数据区间从 20000301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_retail_sales_mom = ak.macro_euro_retail_sales_mom()
        macro_euro_retail_sales_mom_df = sanitize_data_pandas(macro_euro_retail_sales_mom)
        return macro_euro_retail_sales_mom_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-劳动力市场-欧元区季调后就业人数季率报告
@router.get("/macro_euro_employment_change_qoq",
            operation_id="macro_euro_employment_change_qoq")
async def macro_euro_employment_change_qoq():
    """
    国民经济运行状况-劳动力市场-欧元区季调后就业人数季率报告

    接口: macro_euro_employment_change_qoq

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_employment_change_qoq

    描述: 欧元区季调后就业人数季率报告, 数据区间从 20083017-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_employment_change_qoq = ak.macro_euro_employment_change_qoq()
        macro_euro_employment_change_qoq_df = sanitize_data_pandas(macro_euro_employment_change_qoq)
        return macro_euro_employment_change_qoq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-劳动力市场-欧元区失业率报告
@router.get("/macro_euro_unemployment_rate_mom",
            operation_id="macro_euro_unemployment_rate_mom")
async def macro_euro_unemployment_rate_mom():
    """
    国民经济运行状况-劳动力市场-欧元区失业率报告

    接口: macro_euro_unemployment_rate_mom

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_unemployment_rate_mom

    描述: 欧元区失业率报告, 数据区间从 19980501-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_unemployment_rate_mom = ak.macro_euro_unemployment_rate_mom()
        macro_euro_unemployment_rate_mom_df = sanitize_data_pandas(macro_euro_unemployment_rate_mom)
        return macro_euro_unemployment_rate_mom_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-贸易状况-欧元区未季调贸易帐报告
@router.get("/macro_euro_trade_balance",
            operation_id="macro_euro_trade_balance")
async def macro_euro_trade_balance():
    """
    国民经济运行状况-劳动力市场-欧元区失业率报告

    接口: macro_euro_trade_balance

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_trade_balance_mom

    描述: 欧元区未季调贸易帐报告, 数据区间从 19990201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_trade_balance = ak.macro_euro_trade_balance()
        macro_euro_trade_balance_df = sanitize_data_pandas(macro_euro_trade_balance)
        return macro_euro_trade_balance_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-贸易状况-欧元区经常帐报告
@router.get("/macro_euro_current_account_mom",
            operation_id="macro_euro_current_account_mom")
async def macro_euro_current_account_mom():
    """
    国民经济运行状况-劳动力市场-欧元区经常帐报告

    接口: macro_euro_current_account_mom

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_current_account_mom

    描述: 欧元区经常帐报告, 数据区间从 20080221-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_current_account_mom = ak.macro_euro_current_account_mom()
        macro_euro_current_account_mom_df = sanitize_data_pandas(macro_euro_current_account_mom)
        return macro_euro_current_account_mom_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
