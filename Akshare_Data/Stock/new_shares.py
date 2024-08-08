import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockRequest(BaseModel):
    stock: str = Field(..., title="指定个股代码", description="例：000066")


# 新浪财经-发行与分配-新股发行
@router.post("/stock_ipo_info", operation_id="post_stock_ipo_info")
def post_stock_ipo_info(request: StockRequest):
    """
    新浪财经-新股发行

    接口: stock_ipo_info

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/600004.phtml

    描述: 新浪财经-发行与分配-新股发行

    限量: 单次获取新股发行的基本信息数据
    """
    try:
        stock_ipo_info = ak.stock_ipo_info(stock=request.stock)
        stock_ipo_info_df = sanitize_data_pandas(stock_ipo_info)
        return stock_ipo_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据中心-新股数据-新股过会
@router.get("/stock_new_gh_cninfo", operation_id="get_stock_new_gh_cninfo")
def get_stock_new_gh_cninfo():
    """
    巨潮资讯-新股过会

    接口: stock_new_gh_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/xinguList

    描述: 巨潮资讯-数据中心-新股数据-新股过会

    限量: 单次获取近一年所有新股过会的数据
    """
    try:
        stock_new_gh_cninfo = ak.stock_new_gh_cninfo()
        stock_new_gh_cninfo_df = sanitize_data_pandas(stock_new_gh_cninfo)
        return stock_new_gh_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据中心-新股数据-新股发行
@router.get("/stock_new_ipo_cninfo", operation_id="get_stock_new_ipo_cninfo")
def get_stock_new_ipo_cninfo():
    """
    巨潮资讯-新股发行

    接口: stock_new_ipo_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/xinguList

    描述: 巨潮资讯-数据中心-新股数据-新股发行

    限量: 单次获取近三年所有新股发行的数据
    """
    try:
        stock_new_ipo_cninfo = ak.stock_new_ipo_cninfo()
        stock_margin_ratio_pa_df = sanitize_data_pandas(stock_new_ipo_cninfo)
        return stock_margin_ratio_pa_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-新股申购-打新收益率
@router.get("/stock_dxsyl_em", operation_id="get_stock_dxsyl_em")
def get_stock_dxsyl_em():
    """
    东方财富-打新收益率

    接口: stock_dxsyl_em

    目标地址: https://data.eastmoney.com/xg/xg/dxsyl.html

    描述: 东方财富-数据中心-新股申购-打新收益率

    限量: 单次获取所有打新收益率数据
    """
    try:
        stock_dxsyl_em = ak.stock_dxsyl_em()
        stock_dxsyl_em_df = sanitize_data_pandas(stock_dxsyl_em)
        return stock_dxsyl_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolRequest(BaseModel):
    symbol: str = Field(..., title="市场类型",
                        description="可选择：'全部股票', '沪市主板', '科创板', '深市主板', '创业板', '北交所'")


# 东方财富-数据中心-新股数据-新股申购-新股申购与中签查询
@router.post("/stock_xgsglb_em", operation_id="post_stock_xgsglb_em")
async def post_stock_xgsglb_em(request: DongCaiSymbolRequest):
    """
    东方财富-新股申购与中签查询

    接口: stock_xgsglb_em

    目标地址: https://data.eastmoney.com/xg/xg/default_2.html

    描述: 东方财富-数据中心-新股数据-新股申购-新股申购与中签查询

    限量: 单次获取指定市场的新股申购与中签查询数据
    """
    try:
        stock_xgsglb_em = ak.stock_xgsglb_em(symbol=request.symbol)

        stock_xgsglb_em_df = sanitize_data_pandas(stock_xgsglb_em)
        return stock_xgsglb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
