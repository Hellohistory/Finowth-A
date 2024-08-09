import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 欧元区宏观-产业指标-欧元区工业产出月率报告
@router.get("/macro_euro_industrial_production_mom",
            operation_id="macro_euro_industrial_production_mom")
async def macro_euro_industrial_production_mom():
    """
    欧元区宏观-产业指标-欧元区工业产出月率报告

    接口: macro_euro_industrial_production_mom

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_industrial_production_mom

    描述: 欧元区工业产出月率报告, 数据区间从 19910301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_industrial_production_mom = ak.macro_euro_industrial_production_mom()
        macro_euro_industrial_production_mom_df = sanitize_data_pandas(macro_euro_industrial_production_mom)
        return macro_euro_industrial_production_mom_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 欧元区宏观-产业指标-欧元区制造业PMI初值报告
@router.get("/macro_euro_manufacturing_pmi",
            operation_id="macro_euro_manufacturing_pmi")
async def macro_euro_manufacturing_pmi():
    """
    欧元区宏观-产业指标-欧元区制造业PMI初值报告

    接口: macro_euro_manufacturing_pmi

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_manufacturing_pmi

    描述: 欧元区制造业 PMI 初值报告, 数据区间从 20080222-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_manufacturing_pmi = ak.macro_euro_manufacturing_pmi()
        macro_euro_manufacturing_pmi_df = sanitize_data_pandas(macro_euro_manufacturing_pmi)
        return macro_euro_manufacturing_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 欧元区宏观-产业指标-欧元区制造业PMI初值报告
@router.get("/macro_euro_services_pmi",
            operation_id="macro_euro_services_pmi")
async def macro_euro_services_pmi():
    """
    欧元区宏观-产业指标-欧元区制造业PMI初值报告

    接口: macro_euro_services_pmi

    目标地址: https://datacenter.jin10.com/reportType/dc_eurozone_services_pmi

    描述: 欧元区服务业 PMI 终值报告, 数据区间从 20080222-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_services_pmi = ak.macro_euro_services_pmi()
        macro_euro_services_pmi_df = sanitize_data_pandas(macro_euro_services_pmi)
        return macro_euro_services_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
