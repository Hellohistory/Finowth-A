import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class JuChaoSymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="分类类别", description="可选择'证监会行业分类', '国证行业分类'")
    date: str = Field(..., title="指定交易日(只能获取近一年内的数据)", description="例：20240617")


# 巨潮资讯-数据中心-行业分析-行业市盈率
@router.post("/stock_industry_pe_ratio_cninfo", operation_id="stock_industry_pe_ratio_cninfo")
async def gstock_industry_pe_ratio_cninfo(request: JuChaoSymbolDateRequest):
    """
    巨潮资讯-行业市盈率

    接口: stock_industry_pe_ratio_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-行业分析-行业市盈率

    限量: 单次获取指定个股在指定交易日的所有数据; 只能获取近期的数据
    """
    try:
        stock_industry_pe_ratio_cninfo_df = ak.stock_industry_pe_ratio_cninfo(symbol=request.symbol, date=request.date)
        stock_industry_pe_ratio_cninfo_df = sanitize_data_pandas(stock_industry_pe_ratio_cninfo_df)

        return stock_industry_pe_ratio_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class LeGuSymbolRequest(BaseModel):
    symbol: str = Field(..., title="市场类型", description="可选择'上证A股', '深证A股', '创业板', '科创板'")


# 乐咕乐股-股息率-A 股股息率
@router.post("/stock_a_gxl_lg", operation_id="stock_a_gxl_lg")
async def stock_a_gxl_lg(request: LeGuSymbolRequest):
    """
    乐咕乐股-A 股股息率

    接口: stock_a_gxl_lg

    目标地址: https://legulegu.com/stockdata/guxilv

    描述: 乐咕乐股-股息率-A 股股息率

    限量: 单次获取指定类型市场的所有历史数据
    """
    try:
        stock_a_gxl_lg = ak.stock_a_gxl_lg(symbol=request.symbol)
        stock_a_gxl_lg_df = sanitize_data_pandas(stock_a_gxl_lg)
        return stock_a_gxl_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-股息率-恒生指数股息率
@router.get("/stock_hk_gxl_lg", operation_id="stock_hk_gxl_lg")
def stock_hk_gxl_lg():
    """
    乐咕乐股-股息率-恒生指数股息率

    接口: stock_hk_gxl_lg

    目标地址: https://legulegu.com/stockdata/market/hk/dv/hsi

    描述: 乐咕乐股-股息率-恒生指数股息率

    限量: 单次获取所有月度历史数据
    """
    try:
        stock_hk_gxl_lg = ak.stock_hk_gxl_lg()
        stock_hk_gxl_lg_df = sanitize_data_pandas(stock_hk_gxl_lg)
        return stock_hk_gxl_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-大盘拥挤度
@router.get("/stock_a_congestion_lg", operation_id="stock_a_congestion_lg")
def stock_a_congestion_lg():
    """
    乐咕乐股-大盘拥挤度

    接口: stock_a_congestion_lg

    目标地址: https://legulegu.com/stockdata/ashares-congestion

    描述: 乐咕乐股-大盘拥挤度

    限量: 单次获取近 4 年的历史数据
    """
    try:
        stock_a_congestion_lg = ak.stock_a_congestion_lg()
        stock_a_congestion_lg.rename(columns={
            'date': '日期',
            'close': '收盘价',
            'congestion': '拥挤度'
        }, inplace=True)
        stock_a_congestion_lg_df = sanitize_data_pandas(stock_a_congestion_lg)
        return stock_a_congestion_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-股债利差
@router.get("/stock_ebs_lg", operation_id="stock_ebs_lg")
def stock_ebs_lg():
    """
    乐咕乐股-股债利差

    接口: stock_ebs_lg

    目标地址: https://legulegu.com/stockdata/equity-bond-spread

    描述: 乐咕乐股-股债利差

    限量: 单次所有历史数据
    """
    try:
        stock_ebs_lg = ak.stock_ebs_lg()
        stock_ebs_lg_df = sanitize_data_pandas(stock_ebs_lg)
        return stock_ebs_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐估乐股-底部研究-巴菲特指标
@router.get("/stock_buffett_index_lg", operation_id="stock_buffett_index_lg")
def stock_buffett_index_lg():
    """
    乐估乐股-底部研究-巴菲特指标

    接口: stock_buffett_index_lg

    目标地址: https://legulegu.com/stockdata/marketcap-gdp

    描述: 乐估乐股-底部研究-巴菲特指标

    限量: 单次获取所有历史数据
    """
    try:
        stock_buffett_index_lg = ak.stock_buffett_index_lg()
        stock_buffett_index_lg_df = sanitize_data_pandas(stock_buffett_index_lg)
        return stock_buffett_index_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_a_ttm_lyr", operation_id="stock_a_ttm_lyr")
def stock_a_ttm_lyr():
    """
    乐咕乐股-A 股等权重市盈率与中位数市盈率

    接口: stock_a_ttm_lyr

    目标地址: https://www.legulegu.com/stockdata/a-ttm-lyr

    描述: 乐咕乐股-A 股等权重市盈率与中位数市盈率

    限量: 单次返回所有数据
    """
    try:
        stock_a_ttm_lyr = ak.stock_a_ttm_lyr()

        stock_a_ttm_lyr.rename(columns={
            "date": "日期",
            "middlePETTM": "全A股滚动市盈率(TTM)中位数",
            "averagePETTM": "全A股滚动市盈率(TTM)等权平均",
            "middlePELYR": "全A股静态市盈率(LYR)中位数",
            "averagePELYR": "全A股静态市盈率(LYR)等权平均",
            "quantileInAllHistoryMiddlePeTtm": "当前TTM中位数在历史数据上的分位数",
            "quantileInRecent10YearsMiddlePeTtm": "当前TTM中位数在最近10年数据上的分位数",
            "quantileInAllHistoryAveragePeTtm": "当前TTM等权平均在历史数据上的分位数",
            "quantileInRecent10YearsAveragePeTtm": "当前TTM等权平均在最近10年数据上的分位数",
            "quantileInAllHistoryMiddlePeLyr": "当前LYR中位数在历史数据上的分位数",
            "quantileInRecent10YearsMiddlePeLyr": "当前LYR中位数在最近10年数据上的分位数",
            "quantileInAllHistoryAveragePeLyr": "当前LYR等权平均在历史数据上的分位数",
            "quantileInRecent10YearsAveragePeLyr": "当前LYR等权平均在最近10年数据上的分位数",
            "close": "沪深300指数"
        }, inplace=True)

        stock_a_ttm_lyr_df = sanitize_data_pandas(stock_a_ttm_lyr)
        return stock_a_ttm_lyr_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-A 股等权重与中位数市净率
@router.get("/stock_a_all_pb", operation_id="stock_a_all_pb")
def stock_a_all_pb():
    """
    乐咕乐股-A 股等权重与中位数市净率

    接口: stock_a_all_pb

    目标地址: https://www.legulegu.com/stockdata/all-pb

    描述: 乐咕乐股-A 股等权重与中位数市净率

    限量: 单次返回所有数据
    """
    try:
        stock_a_all_pb = ak.stock_a_all_pb()

        stock_a_all_pb.rename(columns={
            "date": "日期",
            "middlePB": "全部A股市净率中位数",
            "equalWeightAveragePB": "全部A股市净率等权平均",
            "close": "上证指数",
            "quantileInAllHistoryMiddlePB": "当前市净率中位数在历史数据上的分位数",
            "quantileInRecent10YearsMiddlePB": "当前市净率中位数在最近10年数据上的分位数",
            "quantileInAllHistoryEqualWeightAveragePB": "当前市净率等权平均在历史数据上的分位数",
            "quantileInRecent10YearsEqualWeightAveragePB": "当前市净率等权平均在最近10年数据上的分位数"
        }, inplace=True)

        stock_a_all_pb_df = sanitize_data_pandas(stock_a_all_pb)
        return stock_a_all_pb_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class LeGuZhuBanSymbolRequest(BaseModel):
    symbol: str = Field(..., title="市场类型", description="可选择'上证', '深证', '创业板', '科创版'")


# 乐咕乐股-主板市盈率
@router.post("/stock_market_pe_lg", operation_id="stock_market_pe_lg")
async def stock_market_pe_lg(request: LeGuZhuBanSymbolRequest):
    """
    乐咕乐股-主板市盈率

    接口: stock_market_pe_lg

    目标地址: https://legulegu.com/stockdata/shanghaiPE

    描述: 乐咕乐股-主板市盈率

    限量: 单次获取指定个股的所有数据
    """
    try:
        stock_market_pe_lg = ak.stock_market_pe_lg(symbol=request.symbol)
        stock_market_pe_lg_df = sanitize_data_pandas(stock_market_pe_lg)
        return stock_market_pe_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class LeGuZhiShuSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指数类型",
                        description="可选择'上证50', '沪深300', '上证380', '创业板50', '中证500', '上证180', "
                                    "'深证红利', '深证100', '中证1000', '上证红利', '中证100', '中证800'")


# 乐咕乐股-指数市盈率
@router.post("/stock_index_pe_lg", operation_id="stock_index_pe_lg")
async def stock_index_pe_lg(request: LeGuZhiShuSymbolRequest):
    """
    乐咕乐股-指数市盈率

    接口: stock_index_pe_lg

    目标地址: https://legulegu.com/stockdata/sz50-ttm-lyr

    描述: 乐咕乐股-指数市盈率

    限量: 单次获取指定类型的所有数据
    """
    try:
        stock_index_pe_lg = ak.stock_index_pe_lg(symbol=request.symbol)
        stock_index_pe_lg_df = sanitize_data_pandas(stock_index_pe_lg)
        return stock_index_pe_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-主板市净率
@router.post("/stock_market_pb_lg", operation_id="stock_market_pb_lg")
async def stock_market_pb_lg(request: LeGuZhuBanSymbolRequest):
    """
    乐咕乐股-主板市净率

    接口: stock_market_pb_lg

    目标地址: https://legulegu.com/stockdata/shanghaiPB

    描述: 乐咕乐股-主板市净率

    限量: 单次获取指定类型的所有数据
    """
    try:
        stock_market_pb_lg = ak.stock_market_pb_lg(symbol=request.symbol)
        stock_market_pb_lg_df = sanitize_data_pandas(stock_market_pb_lg)
        return stock_market_pb_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 乐咕乐股-指数市净率
@router.post("/stock_index_pb_lg", operation_id="stock_index_pb_lg")
async def stock_index_pb_lg(request: LeGuZhiShuSymbolRequest):
    """
    乐咕乐股-指数市净率

    接口: stock_index_pb_lg

    目标地址: https://legulegu.com/stockdata/sz50-pb

    描述: 乐咕乐股-指数市净率

    限量: 单次获取指定类型的所有数据
    """
    try:
        stock_index_pb_lg = ak.stock_index_pb_lg(symbol=request.symbol)
        stock_index_pb_lg_df = sanitize_data_pandas(stock_index_pb_lg)
        return stock_index_pb_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolIndicatorPeriodRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：002044")
    indicator: str = Field(..., title="数据类型",
                           description="可选择'总市值', '市盈率(TTM)', '市盈率(静)', '市净率', '市现率'")
    period: str = Field(..., title="时间类型", description="可选择'近一年', '近三年', '近五年', '近十年', '全部'")


# 百度股市通-A 股-财务报表-估值数据
@router.post("/stock_zh_valuation_baidu", operation_id="stock_zh_valuation_baidu")
async def stock_zh_valuation_baidu(request: SymbolIndicatorPeriodRequest):
    """
    百度股市通-A 股-财务报表-估值数据

    接口: stock_zh_valuation_baidu

    目标地址: https://gushitong.baidu.com/stock/ab-002044

    描述: 百度股市通-A 股-财务报表-估值数据

    限量: 单次获取指定个股和指定时间段的所有历史数据
    """
    try:
        stock_zh_valuation_baidu = ak.stock_zh_valuation_baidu(
            symbol=request.symbol, indicator=request.indicator, period=request.period
        )
        stock_zh_valuation_baidu_df = sanitize_data_pandas(stock_zh_valuation_baidu)
        return stock_zh_valuation_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
