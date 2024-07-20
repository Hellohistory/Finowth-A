import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SectorSpotRequest
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 东方财富网-数据中心-限售股解禁-解禁详情一览
@router.post("/stock_sector_spot", operation_id="post_stock_restricted_release_detail_em")
async def post_stock_restricted_release_detail_em(request: SectorSpotRequest):
    """
    接口: stock_sector_spot

    目标地址: http://finance.sina.com.cn/stock/sl/

    描述: 新浪行业-板块行情

    限量: 单次获取指定的板块行情实时数据

    请求类型: `POST`
    """
    try:
        stock_sector_spot_df = ak.stock_sector_spot(indicator=request.indicator)
        stock_sector_spot_df = sanitize_data_pandas(stock_sector_spot_df)

        return stock_sector_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
