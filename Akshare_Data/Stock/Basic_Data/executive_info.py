import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


class ShSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码或全部", description="可输入全部或者指定个股代码, 例：600000")


# 上海证券交易所-董监高人员股份变动
@router.post("/stock_share_hold_change_sse", operation_id="post_stock_share_hold_change_sse")
async def post_stock_share_hold_change_sse(request: ShSymbolRequest):
    """
    上海证券交易所-公司监管-董董监高人员股份变动

    接口: stock_share_hold_change_sse

    目标地址: http://www.sse.com.cn/disclosure/credibility/supervision/change/

    描述: 上海证券交易所-披露-监管信息公开-公司监管-董董监高人员股份变动

    限量: 单次获取指定个股的数据
    """
    try:
        stock_share_hold_change_sse_df = ak.stock_share_hold_change_sse(symbol=request.symbol)
        return stock_share_hold_change_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深圳证券交易所-董监高人员股份变动
@router.post("/stock_share_hold_change_szse", operation_id="post_stock_share_hold_change_szse")
async def post_stock_share_hold_change_szse(request: ShSymbolRequest):
    """
    深圳证券交易所-监管信息公开-董监高人员股份变动

    接口: stock_share_hold_change_szse

    目标地址: http://www.szse.cn/disclosure/supervision/change/index.html

    描述: 深圳证券交易所-信息披露-监管信息公开-董监高人员股份变动

    限量: 单次获取指定个股的数据
    """
    try:
        stock_share_hold_change_szse_df = ak.stock_share_hold_change_szse(symbol=request.symbol)
        return stock_share_hold_change_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 北京证券交易所-董监高及相关人员持股变动
@router.post("/stock_share_hold_change_bse", operation_id="post_stock_share_hold_change_bse")
async def post_stock_share_hold_change_bse(request: ShSymbolRequest):
    """
    北京证券交易所-监管信息-董监高及相关人员持股变动

    接口: stock_share_hold_change_bse

    目标地址: https://www.bse.cn/disclosure/djg_sharehold_change.html

    描述: 北京证券交易所-信息披露-监管信息-董监高及相关人员持股变动

    限量: 单次获取指定个股的数据
    """
    try:
        stock_share_hold_change_bse_df = ak.stock_share_hold_change_bse(symbol=request.symbol)
        return stock_share_hold_change_bse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoGaoGuanSymbolRequest(BaseModel):
    symbol: str = Field(..., title="获取指定类型", description="可选择'增持', '减持'")


# 巨潮资讯-高管持股变动明细
@router.post("/stock_hold_management_detail_cninfo", operation_id="post_stock_hold_management_detail_cninfo")
async def post_stock_hold_management_detail_cninfo(request: JuChaoGaoGuanSymbolRequest):
    """
    巨潮资讯-股东股本-高管持股变动明细

    接口: stock_hold_management_detail_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-股东股本-高管持股变动明细

    限量: 单次指定类型的高管持股变动明细数据, 返回近一年的数据
    """
    try:
        stock_hold_management_detail_cninfo_df = ak.stock_hold_management_detail_cninfo(symbol=request.symbol)
        return stock_hold_management_detail_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-董监高及相关人员持股变动明细
@router.get("/stock_hold_management_detail_em", operation_id="get_stock_hold_management_detail_em")
def get_stock_hold_management_detail_em():
    """
    东方财富-高管持股-董监高及相关人员持股变动明细

    接口: stock_hold_management_detail_em

    目标地址: https://data.eastmoney.com/executive/list.html

    描述: 东方财富-数据中心-特色数据-高管持股-董监高及相关人员持股变动明细

    限量: 单次返回所有数据
    """
    try:
        stock_hold_management_detail_em_df = ak.stock_hold_management_detail_em()
        return stock_hold_management_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
