import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-产业指标-服务业-美国Markit服务业PMI初值报告
@router.get("/macro_usa_services_pmi",
            operation_id="macro_usa_services_pmi")
async def macro_usa_services_pmi():
    """
    美国-产业指标-服务业-美国Markit服务业PMI初值报告

    接口: macro_usa_services_pmi

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_services_pmi

    描述: 美国Markit服务业PMI初值报告, 数据区间从 20120701-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_services_pmi = ak.macro_usa_services_pmi()
        macro_usa_services_pmi_df = sanitize_data_pandas(macro_usa_services_pmi)
        return macro_usa_services_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-服务业-美国商业库存月率报告
@router.get("/macro_usa_business_inventories",
            operation_id="macro_usa_business_inventories")
async def macro_usa_business_inventories():
    """
    美国-产业指标-服务业-美国商业库存月率报告

    接口: macro_usa_business_inventories

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_business_inventories

    描述: 美国商业库存月率报告, 数据区间从 19920301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_business_inventories = ak.macro_usa_business_inventories()
        macro_usa_business_inventories_df = sanitize_data_pandas(macro_usa_business_inventories)
        return macro_usa_business_inventories_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-服务业-美国ISM非制造业PMI报告
@router.get("/macro_usa_ism_non_pmi",
            operation_id="macro_usa_ism_non_pmi")
async def macro_usa_ism_non_pmi():
    """
    美国-产业指标-服务业-美国ISM非制造业PMI报告

    接口: macro_usa_ism_non_pmi

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_ism_non_pmi

    描述: 美国 ISM 非制造业 PMI 报告, 数据区间从 19970801-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_ism_non_pmi = ak.macro_usa_ism_non_pmi()
        macro_usa_ism_non_pmi_df = sanitize_data_pandas(macro_usa_ism_non_pmi)
        return macro_usa_ism_non_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
