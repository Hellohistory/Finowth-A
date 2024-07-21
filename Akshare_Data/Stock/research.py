import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import DateRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-数据中心-特色数据-机构调研-机构调研详细
@router.post("/stock_jgdy_detail_em", operation_id="post_stock_jgdy_detail_em")
async def post_stock_jgdy_detail_em(request: DateRequest):
    """
    接口: stock_jgdy_detail_em

    目标地址: http://data.eastmoney.com/jgdy/xx.html

    描述: 东方财富网-数据中心-特色数据-机构调研-机构调研详细

    限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间
    """
    try:
        stock_jgdy_detail_em_df = ak.stock_jgdy_detail_em(date=request.date)

        # 使用 sanitize_data 函数清理数据
        stock_jgdy_detail_em_df = sanitize_data(stock_jgdy_detail_em_df)

        return stock_jgdy_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
