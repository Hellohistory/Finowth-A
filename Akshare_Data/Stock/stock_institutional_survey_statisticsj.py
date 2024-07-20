import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


class DateRequest(BaseModel):
    date: str


# 东方财富网-数据中心-特色数据-机构调研-机构调研统计
@router.post("/stock_jgdy_tj_em", operation_id="post_stock_jgdy_tj_em")
async def post_stock_jgdy_tj_em(request: DateRequest):
    """
    描述: 东方财富网-数据中心-特色数据-机构调研-机构调研统计
    限量: 单次返回所有历史数据
    """
    try:
        stock_jgdy_tj_em_df = ak.stock_jgdy_tj_em(date=request.date)

        stock_jgdy_tj_em_df = sanitize_data(stock_jgdy_tj_em_df)

        return stock_jgdy_tj_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
