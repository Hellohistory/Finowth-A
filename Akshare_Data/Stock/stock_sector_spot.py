import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SectorSpotRequest(BaseModel):
    indicator: str


# 东方财富网-数据中心-限售股解禁-解禁详情一览
@router.post("/stock_sector_spot")
def get_stock_restricted_release_detail_em(request: SectorSpotRequest):
    """
    描述: 东方财富网-数据中心-限售股解禁-解禁详情一览
    限量: 单次获取指定时间段限售股解禁数据
    """
    try:
        stock_sector_spot_df = ak.stock_sector_spot(indicator=request.indicator)
        stock_sector_spot_df = sanitize_data_pandas(stock_sector_spot_df)

        return stock_sector_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
