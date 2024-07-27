import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class EnergyCarbonDomestic(BaseModel):
    symbol: str = Field(..., title="需查询的省份",
                        description="可选择'湖北', '上海', '北京', '重庆', '广东', '天津', '深圳', '福建")


# 碳排放权-国内
@router.post("/energy_carbon_domestic", operation_id="post_energy_carbon_domestic")
async def post_energy_carbon_domestic(request: EnergyCarbonDomestic):
    """
    碳排放权-国内

    接口: energy_carbon_domestic

    目标地址: http://www.tanjiaoyi.com/

    描述: 碳交易网-行情信息

    限量: 返回指定省份的所有历史数据
    """
    try:
        energy_carbon_domestic = ak.energy_carbon_domestic(symbol=request.symbol)

        return energy_carbon_domestic.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 碳排放权-北京
@router.get("/energy_carbon_bj", operation_id="get_energy_carbon_bj")
async def get_energy_carbon_bj():
    try:
        energy_carbon_bj = ak.energy_carbon_bj()
        energy_carbon_bj_df = sanitize_data_pandas(energy_carbon_bj)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return energy_carbon_bj_df.to_dict(orient="records")


# 碳排放权-深圳
@router.get("/energy_carbon_sz", operation_id="get_energy_carbon_sz")
async def get_energy_carbon_sz():
    try:
        energy_carbon_sz = ak.energy_carbon_sz()
        energy_carbon_sz_df = sanitize_data_pandas(energy_carbon_sz)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return energy_carbon_sz_df.to_dict(orient="records")


# 碳排放权-国际
@router.get("/energy_carbon_eu", operation_id="get_energy_carbon_eu")
async def get_energy_carbon_eu():
    try:
        energy_carbon_eu = ak.energy_carbon_eu()
        energy_carbon_eu_df = sanitize_data_pandas(energy_carbon_eu)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return energy_carbon_eu_df.to_dict(orient="records")


# 碳排放权-湖北
@router.get("/energy_carbon_hb", operation_id="get_energy_carbon_hb")
async def get_energy_carbon_hb():
    try:
        energy_carbon_hb = ak.energy_carbon_hb()
        energy_carbon_hb_df = sanitize_data_pandas(energy_carbon_hb)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return energy_carbon_hb_df.to_dict(orient="records")


# 碳排放权-广州
@router.get("/energy_carbon_gz", operation_id="get_energy_carbon_gz")
async def get_energy_carbon_gz():
    try:
        energy_carbon_gz = ak.energy_carbon_gz()
        energy_carbon_gz_df = sanitize_data_pandas(energy_carbon_gz)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return energy_carbon_gz_df.to_dict(orient="records")
