import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import DateRequest
from Akshare_Data.utility_function import sanitize_data, sanitize_data_pandas

router = APIRouter()


# 东方财富网-数据中心-特色数据-股权质押-股权质押市场概况
@router.get("/stock_gpzy_profile_em", operation_id="get_stock_gpzy_profile_em")
def get_stock_gpzy_profile_em():
    """
    描述: 东方财富网-数据中心-特色数据-股权质押-股权质押市场概况
    限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间
    """
    try:
        stock_gpzy_profile_em_df = ak.stock_gpzy_profile_em()
        return stock_gpzy_profile_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-股权质押-上市公司质押比例
@router.post("/stock_gpzy_pledge_ratio_em", operation_id="post_stock_gpzy_pledge_ratio_em")
async def post_stock_gpzy_pledge_ratio_em(request: DateRequest):
    """
    描述: 东方财富网-数据中心-特色数据-股权质押-上市公司质押比例
    限量: 单次返回指定交易日的所有历史数据
    """
    try:
        stock_gpzy_pledge_ratio_em_df = ak.stock_gpzy_pledge_ratio_em(date=request.date)
        # 清洗数据
        stock_gpzy_pledge_ratio_em_df = sanitize_data_pandas(stock_gpzy_pledge_ratio_em_df)
        return stock_gpzy_pledge_ratio_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_gpzy_pledge_ratio_detail_em", operation_id="get_stock_gpzy_pledge_ratio_detail_em")
def get_stock_gpzy_pledge_ratio_detail_em():
    """
    描述: 东方财富网-数据中心-特色数据-股权质押-重要股东股权质押明细
    限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间
    """
    try:
        stock_gpzy_pledge_ratio_detail_em_df = ak.stock_gpzy_pledge_ratio_detail_em()
        sanitized_data = stock_gpzy_pledge_ratio_detail_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-证券公司
@router.get("/stock_gpzy_distribute_statistics_company_em",
            operation_id="get_stock_gpzy_distribute_statistics_company_em")
def get_stock_gpzy_distribute_statistics_company_em():
    """
    描述: 东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-证券公司
    限量: 单次返回当前时点所有历史数据
    """
    try:
        stock_gpzy_distribute_statistics_company_em_df = ak.stock_gpzy_distribute_statistics_company_em()
        return stock_gpzy_distribute_statistics_company_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-银行
@router.get("/stock_gpzy_distribute_statistics_bank_em",
            operation_id="get_stock_gpzy_distribute_statistics_bank_em")
def get_stock_gpzy_distribute_statistics_bank_em():
    """
    描述: 东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-银行
    限量: 单次返回当前时点所有历史数据
    """
    try:
        stock_gpzy_distribute_statistics_bank_em_df = ak.stock_gpzy_distribute_statistics_bank_em()
        return stock_gpzy_distribute_statistics_bank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
@router.get("/stock_gpzy_industry_data_em", operation_id="get_stock_gpzy_industry_data_em")
def get_stock_gpzy_industry_data_em():
    """
    描述: 东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
    限量: 单次返回所有历史数据
    """
    try:
        stock_gpzy_industry_data_em_df = ak.stock_gpzy_industry_data_em()
        return stock_gpzy_industry_data_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
