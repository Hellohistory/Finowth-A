import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-物价水平-美国CPI月率报告
@router.get("/macro_usa_cpi_monthly", operation_id="macro_usa_cpi_monthly")
async def macro_usa_cpi_monthly():
    """
    美国-物价水平-美国CPI月率报告

    接口: macro_usa_cpi_monthly

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_cpi

    描述: 美国 CPI 月率报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cpi_monthly = ak.macro_usa_cpi_monthly()
        macro_usa_cpi_monthly_df = sanitize_data_pandas(macro_usa_cpi_monthly)
        return macro_usa_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-物价水平-美国CPI年率报告
@router.get("/macro_usa_cpi_yoy", operation_id="macro_usa_cpi_yoy")
async def macro_usa_cpi_yoy():
    """
    美国-物价水平-美国CPI年率报告

    接口: macro_usa_cpi_yoy

    目标地址: https://data.eastmoney.com/cjsj/foreign_0_12.html

    描述: 东方财富-经济数据一览-美国-CPI年率, 数据区间从2008-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cpi_yoy = ak.macro_usa_cpi_yoy()
        macro_usa_cpi_yoy_df = sanitize_data_pandas(macro_usa_cpi_yoy)
        return macro_usa_cpi_yoy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-物价水平-美国核心CPI月率报告
@router.get("/macro_usa_core_cpi_monthly",
            operation_id="macro_usa_core_cpi_monthly")
async def macro_usa_core_cpi_monthly():
    """
    美国-物价水平-美国核心CPI月率报告

    接口: macro_usa_core_cpi_monthly

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_core_cpi

    描述: 美国核心 CPI 月率报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_core_cpi_monthly = ak.macro_usa_core_cpi_monthly()
        macro_usa_core_cpi_monthly_df = sanitize_data_pandas(macro_usa_core_cpi_monthly)
        return macro_usa_core_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-物价水平-美国零售销售月率报告
@router.get("/macro_usa_retail_sales",
            operation_id="macro_usa_retail_sales")
async def macro_usa_retail_sales():
    """
    美国-物价水平-美国零售销售月率报告

    接口: macro_usa_retail_sales

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_retail_sales

    描述: 美国零售销售月率报告, 数据区间从 19920301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_retail_sales = ak.macro_usa_retail_sales()
        macro_usa_retail_sales_df = sanitize_data_pandas(macro_usa_retail_sales)
        return macro_usa_retail_sales_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-物价水平-美国进口物价指数报告
@router.get("/macro_usa_import_price",
            operation_id="macro_usa_import_price")
async def macro_usa_import_price():
    """
    美国-物价水平-美国进口物价指数报告

    接口: macro_usa_import_price

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_import_price

    描述: 美国进口物价指数报告, 数据区间从 19890201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_import_price = ak.macro_usa_import_price()
        macro_usa_import_price_df = sanitize_data_pandas(macro_usa_import_price)
        return macro_usa_import_price_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-物价水平-美国出口价格指数报告
@router.get("/macro_usa_export_price",
            operation_id="macro_usa_export_price")
async def macro_usa_export_price():
    """
    美国-物价水平-美国出口价格指数报告

    接口: macro_usa_export_price

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_export_price

    描述: 美国出口价格指数报告, 数据区间从 19890201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_export_price = ak.macro_usa_export_price()
        macro_usa_export_price_df = sanitize_data_pandas(macro_usa_export_price)
        return macro_usa_export_price_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
