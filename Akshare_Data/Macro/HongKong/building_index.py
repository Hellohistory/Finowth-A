import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 中国香港-楼宇指数-香港楼宇买卖合约数量
@router.get("/macro_china_hk_building_volume",
            operation_id="macro_china_hk_building_volume")
async def macro_china_hk_building_volume():
    """
    中国香港-楼宇指数-香港楼宇买卖合约数量

    接口: macro_china_hk_building_volume

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_5.html

    描述: 东方财富-经济数据一览-中国香港-香港楼宇买卖合约数量

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_building_volume = ak.macro_china_hk_building_volume()
        macro_china_hk_building_volume_df = sanitize_data_pandas(macro_china_hk_building_volume)
        return macro_china_hk_building_volume_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 中国香港-楼宇指数-香港楼宇买卖合约成交金额
@router.get("/macro_china_hk_building_amount",
            operation_id="macro_china_hk_building_amount")
async def macro_china_hk_building_amount():
    """
    中国香港-楼宇指数-香港楼宇买卖合约成交金额

    接口: macro_china_hk_building_amount

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_6.html

    描述: 东方财富-经济数据一览-中国香港-香港楼宇买卖合约成交金额

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_building_amount = ak.macro_china_hk_building_amount()
        macro_china_hk_building_amount_df = sanitize_data_pandas(macro_china_hk_building_amount)
        return macro_china_hk_building_amount_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
