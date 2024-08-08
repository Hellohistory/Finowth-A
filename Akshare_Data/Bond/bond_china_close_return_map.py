import akshare as ak
from fastapi import APIRouter

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 查询债券名称
@router.get("/bond_china_close_return_map", operation_id="get_bond_china_close_return_map")
async def get_bond_china_close_return_map():
    """
    查询债券名称

    接口: bond_china_close_return_map
    """
    bond_china_close_return_map = ak.bond_china_close_return_map()
    bond_china_close_return_map_df = sanitize_data_pandas(bond_china_close_return_map)
    bond_china_close_return_map_df.rename(columns={
        "value": "债券代码",
        "cnLabel": "中文名称",
        "enLabel": "英文名称"
    }, inplace=True)
    return bond_china_close_return_map_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
