import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-产业指标-工业-美国工业产出月率报告
@router.get("/macro_usa_industrial_production",
            operation_id="get_macro_usa_industrial_production")
async def get_macro_usa_industrial_production():
    """
    美国-产业指标-制造业-美国工业产出月率报告

    接口: macro_usa_industrial_production

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_industrial_production

    描述: 美国工业产出月率报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_industrial_production = ak.macro_usa_industrial_production()
        macro_usa_industrial_production_df = sanitize_data_pandas(macro_usa_industrial_production)
        return macro_usa_industrial_production_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-工业-美国耐用品订单月率报告
@router.get("/macro_usa_durable_goods_orders",
            operation_id="get_macro_usa_durable_goods_orders")
async def get_macro_usa_durable_goods_orders():
    """
    美国-产业指标-制造业-美国耐用品订单月率报告

    接口: macro_usa_durable_goods_orders

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_durable_goods_orders

    描述: 美国耐用品订单月率报告, 数据区间从 20080227-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_durable_goods_orders = ak.macro_usa_durable_goods_orders()
        macro_usa_durable_goods_orders_df = sanitize_data_pandas(macro_usa_durable_goods_orders)
        return macro_usa_durable_goods_orders_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-工业-美国工厂订单月率报告
@router.get("/macro_usa_factory_orders",
            operation_id="get_macro_usa_factory_orders")
async def get_macro_usa_factory_orders():
    """
    美国-产业指标-制造业-美国工厂订单月率报告

    接口: macro_usa_factory_orders

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_factory_orders

    描述: 美国工厂订单月率报告, 数据区间从 19920401-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_factory_orders = ak.macro_usa_factory_orders()
        macro_usa_factory_orders_df = sanitize_data_pandas(macro_usa_factory_orders)
        return macro_usa_factory_orders_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
