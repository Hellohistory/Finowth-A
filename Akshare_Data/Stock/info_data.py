import akshare as ak
from fastapi import HTTPException, APIRouter

router = APIRouter()


@router.get("/stock_info_cjzc_em", operation_id="get_stock_info_cjzc_em")
def get_stock_info_cjzc_em():
    """
    接口：stock_info_cjzc_em

    目标地址：https://stock.eastmoney.com/a/czpnc.html

    描述：东方财富-财经早餐

    限量：单次返回全部历史数据
    """
    try:
        stock_info_cjzc_em_df = ak.stock_info_cjzc_em()
        return stock_info_cjzc_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 全球财经快讯-东财财富
@router.get("/stock_info_global_em", operation_id="get_stock_info_global_em")
def get_stock_info_global_em():
    """
    接口：stock_info_global_em

    目标地址：https://kuaixun.eastmoney.com/7_24.html

    描述：东方财富-全球财经快讯

    限量：单次返回最近 200 条新闻数据
    """
    try:
        stock_info_global_em_df = ak.stock_info_global_em()
        return stock_info_global_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 全球财经快讯-新浪财经
@router.get("/stock_info_global_sina", operation_id="get_stock_info_global_sina")
def get_stock_info_global_sina():
    """
    接口：stock_info_global_sina

    目标地址：https://finance.sina.com.cn/7x24

    描述：新浪财经-全球财经快讯

    限量：单次返回最近 20 条新闻数据
    """
    try:
        stock_info_global_sina_df = ak.stock_info_global_sina()
        return stock_info_global_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 快讯-富途牛牛
@router.get("/stock_info_global_futu", operation_id="get_stock_info_global_futu")
def get_stock_info_global_futu():
    """
    接口：stock_info_global_futu

    目标地址：https://news.futunn.com/main/live

    描述：富途牛牛-快讯

    限量：单次返回最近 50 条新闻数据
    """
    try:
        stock_info_global_futu_df = ak.stock_info_global_futu()
        return stock_info_global_futu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 全球财经直播-同花顺财经
@router.get("/stock_info_global_ths", operation_id="get_stock_info_global_ths")
def get_stock_info_global_ths():
    """
    接口：stock_info_global_ths

    目标地址：https://news.10jqka.com.cn/realtimenews.html

    描述：同花顺财经-全球财经直播

    限量：单次返回最近 20 条新闻数据
    """
    try:
        stock_info_global_ths_df = ak.stock_info_global_ths()
        return stock_info_global_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 电报-财联社
@router.get("/stock_info_global_cls/{symbol}", operation_id="get_stock_info_global_cls")
def get_stock_info_global_cls(symbol: str):
    """
    接口：stock_info_global_cls

    目标地址：https://www.cls.cn/telegraph

    描述：财联社-电报

    限量：单次返回指定个股的最近 300 条财联社-电报的数据
    """
    try:
        stock_info_global_cls_df = ak.stock_info_global_cls(symbol=symbol)
        return stock_info_global_cls_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 证券原创-新浪财经
@router.get("/stock_info_broker_sina/{page}", operation_id="get_stock_info_broker_sina")
def get_stock_info_broker_sina(page: str):
    """
    接口：stock_info_broker_sina

    目标地址：https://finance.sina.com.cn/roll/index.d.html?cid=221431

    描述：新浪财经-证券-证券原创

    限量：单次返回指定页面的数据
    """
    try:
        stock_info_broker_sina_df = ak.stock_info_broker_sina(page=page)
        return stock_info_broker_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
