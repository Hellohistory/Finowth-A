import akshare as ak
from fastapi import APIRouter

router = APIRouter()


@router.get("/spot_price_table_qh", operation_id="spot_price_table_qh")
async def spot_price_table_qh():
    """
    接口：spot_price

    描述：获取品种类型
    """
    spot_price_table_qh = ak.spot_price_table_qh()
    data = spot_price_table_qh.to_dict(orient="records")
    return data


@router.get("/spot_symbol_table_sge", operation_id="spot_symbol_table_sge")
async def spot_symbol_table_sge():
    """
    接口：spot_symbol_table_sge

    描述：获取现货品种代码
    """
    spot_symbol_table_sge = ak.spot_symbol_table_sge()
    data = spot_symbol_table_sge.to_dict(orient="records")
    return data

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
