import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


class THSCXGSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择'创月新高','半年新高','一年新高','历史新高'")


# 创新高
@router.post("/stock_rank_cxg_ths", operation_id="post_stock_rank_cxg_ths")
async def post_stock_rank_cxg_ths(request: THSCXGSymbolRequest):
    """
    接口：stock_rank_cxg_ths

    目标地址：https://data.10jqka.com.cn/rank/cxg/

    描述：同花顺-数据中心-技术选股-创新高

    限量：单次指定个股的所有数据
    """
    try:
        stock_rank_cxg_ths_df = ak.stock_rank_cxg_ths(symbol=request.symbol)
        return stock_rank_cxg_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class THSCXDSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择'创月新低','半年新低','一年新低','历史新低'")


# 创新低
@router.post("/stock_rank_cxd_ths", operation_id="post_stock_rank_cxd_ths")
async def post_stock_rank_cxd_ths(request: THSCXDSymbolRequest):
    """
    接口：stock_rank_cxd_ths

    目标地址：https://data.10jqka.com.cn/rank/cxd/

    描述：同花顺-数据中心-技术选股-创新低

    限量：单次指定个股的所有数据
    """
    try:
        stock_rank_cxd_ths_df = ak.stock_rank_cxd_ths(symbol=request.symbol)
        return stock_rank_cxd_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 连续上涨
@router.get("/stock_rank_lxsz_ths", operation_id="get_stock_rank_lxsz_ths")
def get_stock_rank_lxsz_ths():
    """
    接口：stock_rank_lxsz_ths

    目标地址：https://data.10jqka.com.cn/rank/lxsz/

    描述：同花顺-数据中心-技术选股-连续上涨

    限量：单次返回所有数据
    """
    try:
        stock_rank_lxsz_ths_df = ak.stock_rank_lxsz_ths()
        return stock_rank_lxsz_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 连续下跌
@router.get("/stock_rank_lxxd_ths", operation_id="get_stock_rank_lxxd_ths")
def get_stock_rank_lxxd_ths():
    """
     接口：stock_rank_lxxd_ths

    目标地址：https://data.10jqka.com.cn/rank/lxxd/

    描述：同花顺-数据中心-技术选股-连续下跌

    限量：单次返回所有数据
    """
    try:
        stock_rank_lxxd_ths_df = ak.stock_rank_lxxd_ths()
        return stock_rank_lxxd_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 持续放量
@router.get("/stock_rank_cxfl_ths", operation_id="get_stock_rank_cxfl_ths")
def get_stock_rank_cxfl_ths():
    """
    接口: stock_rank_cxfl_ths

    目标地址: https://data.10jqka.com.cn/rank/cxfl/

    描述: 同花顺-数据中心-技术选股-持续放量

    限量: 单次返回所有数据
    """
    try:
        stock_rank_cxfl_ths_df = ak.stock_rank_cxfl_ths()
        return stock_rank_cxfl_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 持续缩量
@router.get("/stock_rank_cxsl_ths", operation_id="get_stock_rank_cxsl_ths")
def get_stock_rank_cxsl_ths():
    """
    接口: stock_rank_cxsl_ths

    目标地址: https://data.10jqka.com.cn/rank/cxsl/

    描述: 同花顺-数据中心-技术选股-持续缩量

    限量: 单次返回所有数据
    """
    try:
        stock_rank_cxsl_ths_df = ak.stock_rank_cxsl_ths()
        return stock_rank_cxsl_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class THSCXDSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择'5日均线', '10日均线','20日均线','30日均线','60日均线','90日均线','250日均线','500日均线'")


# 向上突破
@router.post("/stock_rank_xstp_ths", operation_id="post_stock_rank_xstp_ths")
async def post_stock_rank_xstp_ths(request: THSCXDSymbolRequest):
    """
    接口: stock_rank_xstp_ths

    目标地址: https://data.10jqka.com.cn/rank/xstp/

    描述: 同花顺-数据中心-技术选股-向上突破

    限量: 单次返回所有数据
    """
    try:
        stock_rank_xstp_ths_df = ak.stock_rank_xstp_ths(symbol=request.symbol)
        return stock_rank_xstp_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 向下突破
@router.post("/stock_rank_xxtp_ths", operation_id="post_stock_rank_xxtp_ths")
async def post_stock_rank_xxtp_ths(request: THSCXDSymbolRequest):
    """
    接口: stock_rank_xxtp_ths

    目标地址: https://data.10jqka.com.cn/rank/xxtp/

    描述: 同花顺-数据中心-技术选股-向下突破

    限量: 单次返回所有数据
    """
    try:
        stock_rank_xxtp_ths_df = ak.stock_rank_xxtp_ths(symbol=request.symbol)
        return stock_rank_xxtp_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 量价齐升
@router.get("/stock_rank_ljqs_ths", operation_id="get_stock_rank_ljqs_ths")
def get_stock_rank_ljqs_ths():
    """
    接口: stock_rank_ljqs_ths

    目标地址: https://data.10jqka.com.cn/rank/ljqs/

    描述: 同花顺-数据中心-技术选股-量价齐升

    限量: 单次返回所有数据
    """
    try:
        stock_rank_ljqs_ths_df = ak.stock_rank_ljqs_ths()
        return stock_rank_ljqs_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 量价齐跌
@router.get("/stock_rank_ljqd_ths", operation_id="get_stock_rank_ljqd_ths")
def get_stock_rank_ljqd_ths():
    """
    接口: stock_rank_ljqd_ths

    目标地址: https://data.10jqka.com.cn/rank/ljqd/

    描述: 同花顺-数据中心-技术选股-量价齐跌

    限量: 单次返回所有数据
    """
    try:
        stock_rank_ljqd_ths_df = ak.stock_rank_ljqd_ths()
        data = stock_rank_ljqd_ths_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500)


# 险资举牌
@router.get("/stock_rank_xzjp_ths", operation_id="get_stock_rank_xzjp_ths")
def get_stock_rank_xzjp_ths():
    """
    接口: stock_rank_xzjp_ths

    目标地址: https://data.10jqka.com.cn/financial/xzjp/

    描述: 同花顺-数据中心-技术选股-险资举牌

    限量: 单次返回所有数据
    """
    try:
        stock_rank_xzjp_ths_df = ak.stock_rank_xzjp_ths()
        return stock_rank_xzjp_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
