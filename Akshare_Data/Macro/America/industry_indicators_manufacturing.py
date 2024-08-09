import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-产业指标-制造业-贝克休斯钻井报告
@router.get("/macro_usa_rig_count",
            operation_id="macro_usa_rig_count")
async def macro_usa_rig_count():
    """
    美国-产业指标-制造业-贝克休斯钻井报告

    接口: macro_usa_rig_count

    目标地址: https://datacenter.jin10.com/reportType/dc_rig_count_summary

    描述: 贝克休斯钻井报告, 数据区间从 19870717-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_rig_count = ak.macro_usa_rig_count()
        macro_usa_rig_count_df = sanitize_data_pandas(macro_usa_rig_count)
        return macro_usa_rig_count_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-制造业-美国生产者物价指数(PPI)报告
@router.get("/macro_usa_ppi",
            operation_id="macro_usa_ppi")
async def macro_usa_ppi():
    """
    美国-产业指标-制造业-贝克休斯钻井报告

    接口: macro_usa_ppi

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_ppi

    描述: 美国生产者物价指数(PPI)报告, 数据区间从 20080226-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_ppi = ak.macro_usa_ppi()
        macro_usa_ppi_df = sanitize_data_pandas(macro_usa_ppi)
        return macro_usa_ppi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-制造业-美国核心生产者物价指数(PPI)报告
@router.get("/macro_usa_core_ppi",
            operation_id="macro_usa_core_ppi")
async def macro_usa_core_ppi():
    """
    美国-产业指标-制造业-美国核心生产者物价指数(PPI)报告

    接口: macro_usa_core_ppi

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_core_ppi

    描述: 美国核心生产者物价指数(PPI)报告, 数据区间从 20080318-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_core_ppi = ak.macro_usa_core_ppi()
        macro_usa_core_ppi_df = sanitize_data_pandas(macro_usa_core_ppi)
        return macro_usa_core_ppi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-制造业-美国 API 原油库存报告
@router.get("/macro_usa_api_crude_stock",
            operation_id="macro_usa_api_crude_stock")
async def macro_usa_api_crude_stock():
    """
    美国-产业指标-制造业-美国 API 原油库存报告

    接口: macro_usa_api_crude_stock

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_api_crude_stock

    描述: 美国 API 原油库存报告, 数据区间从 20120328-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_api_crude_stock = ak.macro_usa_api_crude_stock()
        macro_usa_api_crude_stock_df = sanitize_data_pandas(macro_usa_api_crude_stock)
        return macro_usa_api_crude_stock_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-制造业-美国ISM制造业PMI报告
@router.get("/macro_usa_ism_pmi",
            operation_id="macro_usa_ism_pmi")
async def macro_usa_ism_pmi():
    """
    美国-产业指标-制造业-美国ISM制造业PMI报告

    接口: macro_usa_ism_pmi

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_ism_pmi

    描述: 美国 ISM 制造业 PMI 报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_ism_pmi = ak.macro_usa_ism_pmi()
        macro_usa_ism_pmi_df = sanitize_data_pandas(macro_usa_ism_pmi)
        return macro_usa_ism_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
