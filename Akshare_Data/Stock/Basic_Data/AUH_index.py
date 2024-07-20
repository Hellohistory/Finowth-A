import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.request_model import SymbolDateRequest, SymbolRequest, SymbolIndicatorPeriodRequest
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 巨潮资讯-数据中心-行业分析-行业市盈率
@router.post("/stock_industry_pe_ratio_cninfo", operation_id="post_stock_industry_pe_ratio_cninfo")
async def gpost_stock_industry_pe_ratio_cninfo(request: SymbolDateRequest):
    """
    接口: stock_industry_pe_ratio_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-行业分析-行业市盈率

    限量: 单次获取指定个股在指定交易日的所有数据; 只能获取近期的数据

    请求类型: `POST`
    """
    try:
        stock_industry_pe_ratio_cninfo_df = ak.stock_industry_pe_ratio_cninfo(symbol=request.symbol, date=request.date)
        stock_industry_pe_ratio_cninfo_df = sanitize_data_pandas(stock_industry_pe_ratio_cninfo_df)

        return stock_industry_pe_ratio_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-A 股个股指标: 市盈率, 市净率, 股息率
@router.post("/stock_a_indicator_lg", operation_id="post_stock_a_indicator_lg")
async def post_stock_a_indicator_lg(request: SymbolRequest):
    """
    描述: 乐咕乐股-A 股个股指标: 市盈率, 市净率, 股息率
    限量: 单次获取指定 symbol 的所有历史数据
    """
    try:
        stock_a_indicator_lg_df = ak.stock_a_indicator_lg(symbol=request.symbol)
        return stock_a_indicator_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-股息率-A 股股息率
@router.post("/stock_a_gxl_lg", operation_id="post_stock_a_gxl_lg")
async def post_stock_a_gxl_lg(request: SymbolRequest):
    """
    接口: stock_a_gxl_lg

    目标地址: https://legulegu.com/stockdata/guxilv

    描述: 乐咕乐股-股息率-A 股股息率

    限量: 单次获取指定个股的所有历史数据

    请求类型: `POST`
    """
    try:
        stock_a_gxl_lg_df = ak.stock_a_gxl_lg(symbol=request.symbol)
        return stock_a_gxl_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-股息率-恒生指数股息率
@router.get("/stock_hk_gxl_lg", operation_id="get_stock_hk_gxl_lg")
def get_stock_hk_gxl_lg():
    """
    接口: stock_hk_gxl_lg

    目标地址: https://legulegu.com/stockdata/market/hk/dv/hsi

    描述: 乐咕乐股-股息率-恒生指数股息率

    限量: 单次获取所有月度历史数据

    请求类型: `GET`
    """
    try:
        stock_hk_gxl_lg_df = ak.stock_hk_gxl_lg()
        return stock_hk_gxl_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-大盘拥挤度
@router.get("/stock_a_congestion_lg", operation_id="get_stock_a_congestion_lg")
def get_stock_a_congestion_lg():
    """
    接口: stock_a_congestion_lg

    目标地址: https://legulegu.com/stockdata/ashares-congestion

    描述: 乐咕乐股-大盘拥挤度

    限量: 单次获取近 4 年的历史数据

    请求类型: `GET`
    """
    try:
        stock_a_congestion_lg_df = ak.stock_a_congestion_lg()
        stock_a_congestion_lg_df.rename(columns={
            'date': '日期',
            'close': '收盘价',
            'congestion': '拥挤度'
        }, inplace=True)
        return stock_a_congestion_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-股债利差
@router.get("/stock_ebs_lg", operation_id="get_stock_ebs_lg")
def get_stock_ebs_lg():
    """
    接口: stock_ebs_lg

    目标地址: https://legulegu.com/stockdata/equity-bond-spread

    描述: 乐咕乐股-股债利差

    限量: 单次所有历史数据

    请求类型: `GET`
    """
    try:
        stock_ebs_lg_df = ak.stock_ebs_lg()
        return stock_ebs_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐估乐股-底部研究-巴菲特指标
@router.get("/stock_buffett_index_lg", operation_id="get_stock_buffett_index_lg")
def get_stock_buffett_index_lg():
    """
    接口: stock_buffett_index_lg

    目标地址: https://legulegu.com/stockdata/marketcap-gdp

    描述: 乐估乐股-底部研究-巴菲特指标

    限量: 单次获取所有历史数据

    请求类型: `GET`
    """
    try:
        stock_buffett_index_lg_df = ak.stock_buffett_index_lg()
        return stock_buffett_index_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-A 股等权重市盈率与中位数市盈率
@router.get("/stock_a_ttm_lyr", operation_id="get_stock_a_ttm_lyr")
def get_stock_a_ttm_lyr():
    """
    接口: stock_a_ttm_lyr

    目标地址: https://www.legulegu.com/stockdata/a-ttm-lyr

    描述: 乐咕乐股-A 股等权重市盈率与中位数市盈率

    限量: 单次返回所有数据

    请求类型: `GET`
    """
    try:
        stock_a_ttm_lyr_df = ak.stock_a_ttm_lyr()
        return stock_a_ttm_lyr_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-A 股等权重与中位数市净率
@router.get("/stock_a_all_pb", operation_id="get_stock_a_all_pb")
def get_stock_a_all_pb():
    """
    接口: stock_a_all_pb

    目标地址: https://www.legulegu.com/stockdata/all-pb

    描述: 乐咕乐股-A 股等权重与中位数市净率

    限量: 单次返回所有数据

    请求类型: `GET`
    """
    try:
        stock_a_all_pb_df = ak.stock_a_all_pb()
        return stock_a_all_pb_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-主板市盈率
@router.post("/stock_market_pe_lg", operation_id="post_stock_market_pe_lg")
async def post_stock_market_pe_lg(request: SymbolRequest):
    """
    接口: stock_market_pe_lg

    目标地址: https://legulegu.com/stockdata/shanghaiPE

    描述: 乐咕乐股-主板市盈率

    限量: 单次获取指定个股的所有数据

    请求类型: `POST`
    """
    try:
        stock_market_pe_lg_df = ak.stock_market_pe_lg(symbol=request.symbol)
        return stock_market_pe_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-指数市盈率
@router.post("/stock_index_pe_lg", operation_id="post_stock_index_pe_lg")
async def post_stock_index_pe_lg(request: SymbolRequest):
    """
    接口: stock_index_pe_lg

    目标地址: https://legulegu.com/stockdata/sz50-ttm-lyr

    描述: 乐咕乐股-指数市盈率

    限量: 单次获取指定个股的所有数据

    请求类型: `POST`
    """
    try:
        stock_index_pe_lg_df = ak.stock_index_pe_lg(symbol=request.symbol)
        return stock_index_pe_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-主板市净率
@router.post("/stock_market_pb_lg", operation_id="post_stock_market_pb_lg")
async def post_stock_market_pb_lg(request: SymbolRequest):
    """
    接口: stock_market_pb_lg

    目标地址: https://legulegu.com/stockdata/shanghaiPB

    描述: 乐咕乐股-主板市净率

    限量: 单次获取指定个股的所有数据

    请求类型: `POST`
    """
    try:
        stock_market_pb_lg_df = ak.stock_market_pb_lg(symbol=request.symbol)
        return stock_market_pb_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-指数市净率
@router.post("/stock_index_pb_lg", operation_id="post_stock_index_pb_lg")
async def post_stock_index_pb_lg(request: SymbolRequest):
    """
    接口: stock_index_pb_lg

    目标地址: https://legulegu.com/stockdata/sz50-pb

    描述: 乐咕乐股-指数市净率

    限量: 单次获取指定个股的所有数据

    请求类型: `POST`
    """
    try:
        stock_index_pb_lg_df = ak.stock_index_pb_lg(symbol=request.symbol)
        return stock_index_pb_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 百度股市通-A 股-财务报表-估值数据
@router.post("/stock_zh_valuation_baidu", operation_id="post_stock_zh_valuation_baidu")
async def post_stock_zh_valuation_baidu(request: SymbolIndicatorPeriodRequest):
    """
    接口: stock_zh_valuation_baidu

    目标地址: https://gushitong.baidu.com/stock/ab-002044

    描述: 百度股市通-A 股-财务报表-估值数据

    限量: 单次获取指定个股和指定时间段的所有历史数据

    请求类型: `POST`
    """
    try:
        stock_zh_valuation_baidu_df = ak.stock_zh_valuation_baidu(
            symbol=request.symbol, indicator=request.indicator, period=request.period
        )
        return stock_zh_valuation_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
