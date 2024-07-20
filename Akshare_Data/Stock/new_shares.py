import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import DateRequest, StockRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 新浪财经-发行与分配-新股发行
@router.post("/stock_ipo_info", operation_id="post_stock_ipo_info")
def post_stock_ipo_info(request: StockRequest):
    """
    接口: stock_ipo_info

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/600004.phtml

    描述: 新浪财经-发行与分配-新股发行

    限量: 单次获取新股发行的基本信息数据

    请求类型: `POST`
    """
    try:
        stock_ipo_info_df = ak.stock_ipo_info(stock=request.stock)
        return stock_ipo_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据中心-新股数据-新股过会
@router.get("/stock_new_gh_cninfo", operation_id="get_stock_new_gh_cninfo")
def get_stock_new_gh_cninfo():
    """
    接口: stock_new_gh_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/xinguList

    描述: 巨潮资讯-数据中心-新股数据-新股过会

    限量: 单次获取近一年所有新股过会的数据

    请求类型: `GET`
    """
    try:
        stock_new_gh_cninfo_df = ak.stock_new_gh_cninfo()
        return stock_new_gh_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据中心-新股数据-新股发行
@router.get("/stock_new_ipo_cninfo", operation_id="get_stock_new_ipo_cninfo")
def get_stock_new_ipo_cninfo():
    """
    描述: 巨潮资讯-数据中心-新股数据-新股发行
    限量: 单次获取近三年所有新股发行的数据
    """
    try:
        stock_new_ipo_cninfo_df = ak.stock_new_ipo_cninfo()
        return stock_new_ipo_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-新股申购-打新收益率
@router.get("/stock_dxsyl_em", operation_id="get_stock_dxsyl_em")
def get_stock_dxsyl_em():
    """
    接口: stock_dxsyl_em

    目标地址: https://data.eastmoney.com/xg/xg/dxsyl.html

    描述: 东方财富网-数据中心-新股申购-打新收益率

    限量: 单次获取所有打新收益率数据

    请求类型: `GET`
    """
    try:
        stock_dxsyl_em_df = ak.stock_dxsyl_em()
        data = stock_dxsyl_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-新股数据-新股申购-新股申购与中签查询
@router.post("/stock_xgsglb_em", operation_id="post_stock_xgsglb_em")
async def post_stock_xgsglb_em(request: DateRequest):
    """
    接口: stock_xgsglb_em

    目标地址: https://data.eastmoney.com/xg/xg/default_2.html

    描述: 东方财富网-数据中心-新股数据-新股申购-新股申购与中签查询

    限量: 单次获取指定市场的新股申购与中签查询数据

    请求类型: `POST`
    """
    try:
        stock_xgsglb_em_df = ak.stock_xgsglb_em(symbol=request.symbol)

        return stock_xgsglb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
