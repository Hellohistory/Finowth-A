import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


class SectorRequest(BaseModel):
    sector: str


class StockInfoRequest(BaseModel):
    symbol: str


# 新浪行业-板块行情-成份详情
@router.post("/stock_sector_detail", operation_id="post_stock_sector_detail")
def get_stock_sector_detail(request: SectorRequest):
    """
    描述: 新浪行业-板块行情-成份详情
    限量: 单次获取指定的新浪行业-板块行情-成份详情
    """
    try:
        stock_sector_detail_df = ak.stock_sector_detail(sector=request.sector)
        return stock_sector_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 沪深京 A 股股票代码和股票简称数据
@router.get("/stock_info_a_code_name", operation_id="post_stock_info_a_code_name")
def get_stock_info_a_code_name():
    """
    描述: 沪深京 A 股股票代码和股票简称数据
    限量: 单次获取所有 A 股股票代码和简称数据
    """
    try:
        stock_info_a_code_name_df = ak.stock_info_a_code_name()
        return stock_info_a_code_name_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 上海证券交易所股票代码和简称数据
@router.post("/stock_info_sh_name_code", operation_id="post_stock_info_sh_name_code")
def get_stock_info_sh_name_code(request: StockInfoRequest):
    """
    描述: 上海证券交易所股票代码和简称数据
    限量: 单次获取所有上海证券交易所股票代码和简称数据
    """
    try:
        stock_info_sh_name_code_df = ak.stock_info_sh_name_code(symbol=request.symbol)
        return stock_info_sh_name_code_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深证证券交易所股票代码和股票简称数据
@router.post("/stock_info_sz_name_code", operation_id="post_stock_info_sz_name_code")
def get_stock_info_sz_name_code(request: StockInfoRequest):
    """
    描述: 深证证券交易所股票代码和股票简称数据
    限量: 单次获取深证证券交易所股票代码和简称数据
    """
    try:
        stock_info_sz_name_code_df = ak.stock_info_sz_name_code(symbol=request.symbol)
        return stock_info_sz_name_code_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 北京证券交易所股票代码和简称数据
@router.get("/stock_info_bj_name_code", operation_id="post_stock_info_bj_name_code")
def get_stock_info_bj_name_code():
    """
    描述: 北京证券交易所股票代码和简称数据
    限量: 单次获取北京证券交易所所有的股票代码和简称数据
    """
    try:
        stock_info_bj_name_code_df = ak.stock_info_bj_name_code()
        return stock_info_bj_name_code_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深证证券交易所终止/暂停上市股票
@router.post("/stock_info_sz_delist", operation_id="post_stock_info_sz_delist")
def get_stock_info_sz_delist(request: StockInfoRequest):
    """
    描述: 深证证券交易所终止/暂停上市股票
    限量: 单次获取深证证券交易所终止/暂停上市数据
    """
    try:
        stock_info_sz_delist_df = ak.stock_info_sz_delist(symbol=request.symbol)
        return stock_info_sz_delist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-行情中心-沪深个股-两网及退市
@router.get("/stock_staq_net_stop", operation_id="post_stock_staq_net_stop")
def get_stock_staq_net_stop():
    """
    描述: 东方财富网-行情中心-沪深个股-两网及退市
    限量: 单次获取所有两网及退市的股票数据
    """
    try:
        stock_staq_net_stop_df = ak.stock_staq_net_stop()
        return stock_staq_net_stop_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 上海证券交易所暂停/终止上市股票
@router.post("/stock_info_sh_delist", operation_id="post_stock_info_sh_delist")
def get_stock_info_sh_delist(request: StockInfoRequest):
    """
    描述: 上海证券交易所暂停/终止上市股票
    限量: 单次获取上海证券交易所暂停/终止上市股票
    """
    try:
        stock_info_sh_delist_df = ak.stock_info_sh_delist(symbol=request.symbol)
        return stock_info_sh_delist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-股票曾用名
@router.post("/stock_info_change_name", operation_id="post_stock_info_change_name")
def get_stock_info_change_name(request: SymbolRequest):
    """
    描述: 新浪财经-股票曾用名
    限量: 单次指定 symbol 的所有历史曾用名称
    """
    try:
        stock_info_change_name_list = ak.stock_info_change_name(symbol=request.symbol)
        return stock_info_change_name_list.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深证证券交易所-市场数据-股票数据-名称变更
@router.post("/stock_info_sz_change_name", operation_id="post_stock_info_sz_change_name")
def get_stock_info_sz_change_name(request: StockInfoRequest):
    """
    描述: 深证证券交易所-市场数据-股票数据-名称变更
    限量: 单次获取所有历史数据
    """
    try:
        stock_info_sz_change_name_df = ak.stock_info_sz_change_name(symbol=request.symbol)
        return stock_info_sz_change_name_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
