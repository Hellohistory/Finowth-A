import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 汽柴油历史调价信息
@router.get("/energy_oil_hist", operation_id="get_energy_oil_hist")
async def get_energy_oil_hist():
    """
    汽柴油历史调价信息

    接口: energy_oil_hist

    目标地址: https://data.eastmoney.com/cjsj/oil_default.html

    描述: 东方财富-数据中心-中国油价-汽柴油历史调价信息

    限量: 单次返回中国油价的所有历史数据
    """
    energy_oil_hist = ak.energy_oil_hist()
    energy_oil_hist_df = sanitize_data_pandas(energy_oil_hist)

    return energy_oil_hist_df.to_dict(orient="records")


class EnergyOilDetail(BaseModel):
    date: str = Field(..., title="调价日期", description="通过调用 energy_oil_hist 可以获取历史调价日期")


# 碳排放权-国内
@router.post("/energy_oil_detail", operation_id="post_energy_oil_detail")
async def post_energy_oil_detail(request: EnergyOilDetail):
    """
    碳排放权-国内

    接口: energy_carbon_domestic

    目标地址: http://www.tanjiaoyi.com/

    描述: 碳交易网-行情信息

    限量: 返回指定省份的所有历史数据
    """
    try:
        energy_oil_detail = ak.energy_oil_detail(date=request.date)

        return energy_oil_detail.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
