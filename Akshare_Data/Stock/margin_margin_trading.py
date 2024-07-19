import akshare as ak
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/stock_margin_ratio_pa")
def get_stock_margin_ratio_pa(date: str):
    """
    融资融券-标的证券名单及保证金比例查询
    """
    try:
        stock_margin_ratio_pa_df = ak.stock_margin_ratio_pa(date=date)
        return stock_margin_ratio_pa_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 暂无法获取
# @router.get("/stock_margin_account_info")
# def get_stock_margin_account_info():
#     """
#     东方财富网-数据中心-融资融券-融资融券账户统计-两融账户信息
#     """
#     try:
#         stock_margin_account_info_df = ak.stock_margin_account_info()
#         return stock_margin_account_info_df.to_dict(orient="records")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_margin_sse")
def get_stock_margin_sse(start_date: str, end_date: str):
    """
    上海证券交易所-融资融券数据-融资融券汇总数据
    """
    try:
        stock_margin_sse_df = ak.stock_margin_sse(start_date=start_date, end_date=end_date)
        return stock_margin_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_margin_detail_sse")
def get_stock_margin_detail_sse(date: str):
    """
    上海证券交易所-融资融券数据-融资融券明细数据
    """
    try:
        stock_margin_detail_sse_df = ak.stock_margin_detail_sse(date=date)
        return stock_margin_detail_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_margin_szse")
def get_stock_margin_szse(date: str):
    """
    深圳证券交易所-融资融券数据-融资融券汇总数据
    """
    try:
        stock_margin_szse_df = ak.stock_margin_szse(date=date)
        return stock_margin_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_margin_detail_szse")
def get_stock_margin_detail_szse(date: str):
    """
    深证证券交易所-融资融券数据-融资融券交易明细数据
    """
    try:
        stock_margin_detail_szse_df = ak.stock_margin_detail_szse(date=date)
        return stock_margin_detail_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_margin_underlying_info_szse")
def get_stock_margin_underlying_info_szse(date: str):
    """
    深圳证券交易所-融资融券数据-标的证券信息
    """
    try:
        stock_margin_underlying_info_szse_df = ak.stock_margin_underlying_info_szse(date=date)
        return stock_margin_underlying_info_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
