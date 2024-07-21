import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import DateRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-数据中心-特色数据-商誉-A股商誉市场概况
@router.get("/stock_sy_profile_em", operation_id="get_stock_sy_profile_em")
def get_stock_sy_profile_em():
    """
    接口: stock_sy_profile_em

    目标地址:  https://data.eastmoney.com/sy/scgk.html

    描述: 东方财富网-数据中心-特色数据-商誉-A股商誉市场概况

    限量: 单次所有历史数据
    """
    try:
        stock_sy_profile_em_df = ak.stock_sy_profile_em()
        sanitized_data = stock_sy_profile_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-商誉-商誉减值预期明细
@router.post("/stock_sy_yq_em", operation_id="get_stock_sy_yq_em")
async def post_stock_sy_yq_em(request: DateRequest):
    """
    接口: stock_sy_yq_em

    目标地址: https://data.eastmoney.com/sy/yqlist.html

    描述: 东方财富网-数据中心-特色数据-商誉-商誉减值预期明细

    限量: 单次所有历史数据
    """
    try:
        stock_sy_yq_em_df = ak.stock_sy_yq_em(date=request.date)
        sanitized_data = stock_sy_yq_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-商誉-个股商誉减值明细
@router.post("/stock_sy_jz_em", operation_id="get_stock_sy_jz_em")
async def post_stock_sy_jz_em(request: DateRequest):
    """
    接口: stock_sy_jz_em

    目标地址: https://data.eastmoney.com/sy/jzlist.html

    描述: 东方财富网-数据中心-特色数据-商誉-个股商誉减值明细

    限量: 单次返回所有历史数据
    """
    try:
        stock_sy_jz_em_df = ak.stock_sy_jz_em(date=request.date)
        sanitized_data = stock_sy_jz_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-商誉-行业商誉
@router.post("/stock_sy_hy_em", operation_id="get_stock_sy_hy_em")
async def post_stock_sy_hy_em(request: DateRequest):
    """
    接口: stock_sy_hy_em

    目标地址: https://data.eastmoney.com/sy/hylist.html

    描述: 东方财富网-数据中心-特色数据-商誉-行业商誉

    限量: 单次返回所有历史数据
    """
    try:
        stock_sy_hy_em_df = ak.stock_sy_hy_em(date=request.date)
        return stock_sy_hy_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
