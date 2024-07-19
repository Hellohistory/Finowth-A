from fastapi import FastAPI, APIRouter, HTTPException
import akshare as ak

app = FastAPI()
router = APIRouter()


# 科创板
@router.get("/stock_register_kcb")
def get_stock_register_kcb():
    """
    描述: 东方财富网-数据中心-新股数据-IPO审核信息-科创板
    限量: 单次返回所有历史数据
    """
    try:
        stock_register_kcb_df = ak.stock_register_kcb()
        return stock_register_kcb_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 创业板
@router.get("/stock_register_cyb")
def get_stock_register_cyb():
    """
    描述: 东方财富网-数据中心-新股数据-IPO审核信息-创业板
    限量: 单次返回所有历史数据
    """
    try:
        stock_register_cyb_df = ak.stock_register_cyb()
        return stock_register_cyb_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 上海主板
@router.get("/stock_register_sh")
def get_stock_register_sh():
    """
    描述: 东方财富网-数据中心-新股数据-IPO审核信息-上海主板
    限量: 单次返回所有历史数据
    """
    try:
        stock_register_sh_df = ak.stock_register_sh()
        return stock_register_sh_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深圳主板
@router.get("/stock_register_sz")
def get_stock_register_sz():
    """
    描述: 东方财富网-数据中心-新股数据-IPO审核信息-深圳主板
    限量: 单次返回所有历史数据
    """
    try:
        stock_register_sz_df = ak.stock_register_sz()
        return stock_register_sz_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 北交所
@router.get("/stock_register_bj")
def get_stock_register_bj():
    """
    描述: 东方财富网-数据中心-新股数据-IPO审核信息-北交所
    限量: 单次返回所有历史数据
    """
    try:
        stock_register_bj_df = ak.stock_register_bj()
        return stock_register_bj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
