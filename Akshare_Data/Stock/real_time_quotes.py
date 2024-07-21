import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.Stock.stock_market_overview import sanitize_data
from Akshare_Data.request_model import SymbolRequest

router = APIRouter()


# 雪球-行情中心-个股
@router.post("/stock_individual_spot_xq", operation_id="post_stock_individual_spot_xq")
async def post_stock_individual_spot_xq(request: SymbolRequest):
    """
    接口: stock_individual_spot_xq

    目标地址: https://xueqiu.com/S/SH513520

    描述: 雪球-行情中心-个股

    限量: 单次获取指定个股的最新行情数据
    """
    try:
        stock_individual_spot_xq_df = ak.stock_individual_spot_xq(symbol=request.symbol)
        return stock_individual_spot_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-个股-股票信息
@router.post("/stock_individual_info_em", operation_id="post_stock_individual_info_em")
async def post_stock_individual_info_em(request: SymbolRequest):
    """
    接口: stock_individual_info_em

    目标地址: http://quote.eastmoney.com/concept/sh603777.html?from=classic

    描述: 东方财富-个股-股票信息

    限量: 单次返回指定个股的个股信息
    """
    try:
        stock_individual_info_em_df = ak.stock_individual_info_em(symbol=request.symbol)
        return stock_individual_info_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-行情报价
@router.post("/stock_bid_ask_em", operation_id="post_stock_bid_ask_em")
async def post_stock_bid_ask_em(request: SymbolRequest):
    """
    接口: stock_bid_ask_em

    目标地址: https://quote.eastmoney.com/sz000001.html

    描述: 东方财富-行情报价

    限量: 单次返回指定股票的行情报价数据
    """
    try:
        stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol=request.symbol)
        return stock_bid_ask_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_zh_a_spot_em", operation_id="get_stock_zh_a_spot_em")
def get_stock_zh_a_spot_em():
    """
    接口: stock_zh_a_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#hs_a_board

    描述: 东方财富网-沪深京 A 股-实时行情数据

    限量: 单次返回所有沪深京 A 股上市公司的实时行情数据
    """
    try:
        stock_zh_a_spot_em_data = ak.stock_zh_a_spot_em().to_dict(orient="records")

        # 处理字典中的非法浮点数值
        def sanitize_value(value):
            if isinstance(value, float):
                if not (float('-inf') < value < float('inf')):
                    return None
            return value

        sanitized_data = [
            {key: sanitize_value(value) for key, value in record.items()}
            for record in stock_zh_a_spot_em_data
        ]

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_sh_a_spot_em", operation_id="get_stock_sh_a_spot_em")
def get_stock_sh_a_spot_em():
    """
    接口: stock_sh_a_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#sh_a_board

    描述: 东方财富网-沪 A 股-实时行情数据

    限量: 单次返回所有沪 A 股上市公司的实时行情数据
    """
    try:
        stock_sh_a_spot_em_df = ak.stock_sh_a_spot_em()
        data = stock_sh_a_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-深 A 股-实时行情数据
@router.get("/stock_sz_a_spot_em", operation_id="get_stock_sz_a_spot_em")
def get_stock_sz_a_spot_em():
    """
    接口: stock_sz_a_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#sz_a_board

    描述: 东方财富网-深 A 股-实时行情数据

    限量: 单次返回所有深 A 股上市公司的实时行情数据
    """
    try:
        stock_sz_a_spot_em_df = ak.stock_sz_a_spot_em()
        data = stock_sz_a_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-京 A 股-实时行情数据
@router.get("/stock_bj_a_spot_em", operation_id="get_stock_bj_a_spot_em")
def get_stock_bj_a_spot_em():
    """
    接口: stock_bj_a_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#bj_a_board

    描述: 东方财富网-京 A 股-实时行情数据

    限量: 单次返回所有京 A 股上市公司的实时行情数据
    """
    try:
        stock_bj_a_spot_em_df = ak.stock_bj_a_spot_em()
        data = stock_bj_a_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-新股-实时行情数据
@router.get("/stock_new_a_spot_em", operation_id="get_stock_new_a_spot_em")
def get_stock_new_a_spot_em():
    """
    接口: stock_new_a_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#newshares

    描述: 东方财富网-新股-实时行情数据

    限量: 单次返回所有新股上市公司的实时行情数据
    """
    try:
        stock_new_a_spot_em_df = ak.stock_new_a_spot_em()
        data = stock_new_a_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-创业板-实时行情
@router.get("/stock_cy_a_spot_em", operation_id="get_stock_cy_a_spot_em")
def get_stock_cy_a_spot_em():
    """
    接口: stock_cy_a_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#gem_board

    描述: 东方财富网-创业板-实时行情

    限量: 单次返回所有创业板的实时行情数据
    """
    try:
        stock_cy_a_spot_em_df = ak.stock_cy_a_spot_em()
        data = stock_cy_a_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-科创板-实时行情
@router.get("/stock_kc_a_spot_em", operation_id="get_stock_kc_a_spot_em")
def get_stock_kc_a_spot_em():
    """
    接口: stock_kc_a_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#kcb_board

    描述: 东方财富网-科创板-实时行情

    限量: 单次返回所有科创板的实时行情数据
    """
    try:
        stock_kc_a_spot_em_df = ak.stock_kc_a_spot_em()
        data = stock_kc_a_spot_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-沪深京 A 股数据
@router.get("/stock_zh_a_spot", operation_id="get_stock_zh_a_spot")
def get_stock_zh_a_spot():
    """
    接口: stock_zh_a_spot

    目标地址: https://vip.stock.finance.sina.com.cn/mkt/#hs_a

    描述: 新浪财经-沪深京 A 股数据, 重复运行本函数会被新浪暂时封 IP, 建议增加时间间隔

    限量: 单次返回沪深京 A 股上市公司的实时行情数据
    """
    try:
        stock_zh_a_spot_df = ak.stock_zh_a_spot()
        return stock_zh_a_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
