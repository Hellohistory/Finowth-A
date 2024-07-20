import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import DateRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-数据中心-股市日历-公司动态
@router.post("/stock_gsrl_gsdt_em", operation_id="post_stock_gsrl_gsdt_em")
async def post_stock_gsrl_gsdt_em(request: DateRequest):
    """
    描述: 东方财富网-数据中心-股市日历-公司动态
    限量: 单次返回指定交易日的数据
    """
    try:
        stock_gsrl_gsdt_em_df = ak.stock_gsrl_gsdt_em(date=request.date)
        return stock_gsrl_gsdt_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-行情中心-沪深个股-风险警示板
@router.get("/stock_zh_a_st_em", operation_id="get_stock_zh_a_st_em")
def get_stock_zh_a_st_em():
    """
    描述: 东方财富网-行情中心-沪深个股-风险警示板
    限量: 单次返回当前交易日风险警示板的所有股票的行情数据
    """
    try:
        stock_zh_a_st_em_df = ak.stock_zh_a_st_em()
        data = stock_zh_a_st_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-行情中心-沪深个股-新股
@router.get("/stock_zh_a_new_em", operation_id="get_stock_zh_a_new_em")
def get_stock_zh_a_new_em():
    """
    描述: 东方财富网-行情中心-沪深个股-新股
    限量: 单次返回当前交易日新股板块的所有股票的行情数据
    """
    try:
        stock_zh_a_new_em_df = ak.stock_zh_a_new_em()
        return stock_zh_a_new_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-数据中心-新股数据-IPO受益股
@router.get("/stock_ipo_benefit_ths", operation_id="get_stock_ipo_benefit_ths")
def get_stock_ipo_benefit_ths():
    """
    描述: 同花顺-数据中心-新股数据-IPO受益股
    限量: 单次返回当前交易日的所有数据; 该数据每周更新一次, 返回最近一周的数据
    """
    try:
        result = ak.stock_ipo_benefit_ths()
        if isinstance(result, str) and result == "当前没有数据，请稍后再试。":
            return {"message": result}
        return result.to_dict(orient="records")
    except AttributeError as e:
        if "'NoneType' object has no attribute 'text'" in str(e):
            return {"message": "当前没有数据，请稍后再试。"}
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-行情中心-沪深个股-两网及退市
@router.get("/stock_zh_a_stop_em", operation_id="get_stock_zh_a_stop_em")
def get_stock_zh_a_stop_em():
    """
    描述: 东方财富网-行情中心-沪深个股-两网及退市
    限量: 单次返回当前交易日两网及退市的所有股票的行情数据
    """
    try:
        stock_zh_a_stop_em_df = ak.stock_zh_a_stop_em()
        data = stock_zh_a_stop_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
