import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 东方财富网-数据中心-资金流向-沪深港通资金流向
@router.get("/stock_hsgt_fund_flow_summary_em",
            operation_id="get_stock_hsgt_fund_flow_summary_em")
def get_stock_hsgt_fund_flow_summary_em():
    """
    接口: stock_hsgt_fund_flow_summary_em

    目标地址: https://data.eastmoney.com/hsgt/index.html#lssj

    描述: 东方财富网-数据中心-资金流向-沪深港通资金流向

    限量: 单次获取沪深港通资金流向数据
    """
    try:
        stock_hsgt_fund_flow_summary_em_df = ak.stock_hsgt_fund_flow_summary_em()
        return stock_hsgt_fund_flow_summary_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深港通-港股通业务信息-结算汇率
@router.get("/stock_sgt_settlement_exchange_rate_szse",
            operation_id="get_stock_sgt_settlement_exchange_rate_szse")
def get_stock_sgt_settlement_exchange_rate_szse():
    """
    接口: stock_sgt_settlement_exchange_rate_szse

    目标地址: https://www.szse.cn/szhk/hkbussiness/exchangerate/index.html

    描述: 深港通-港股通业务信息-结算汇率

    限量: 单次获取所有深港通结算汇率数据
    """
    try:
        stock_sgt_settlement_exchange_rate_szse_df = ak.stock_sgt_settlement_exchange_rate_szse()
        return stock_sgt_settlement_exchange_rate_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 沪港通-港股通信息披露-结算汇兑
@router.get("/stock_sgt_settlement_exchange_rate_sse",
            operation_id="get_stock_sgt_settlement_exchange_rate_sse")
def get_stock_sgt_settlement_exchange_rate_sse():
    """
    接口: stock_sgt_settlement_exchange_rate_sse

    目标地址: http://www.sse.com.cn/services/hkexsc/disclo/ratios

    描述: 沪港通-港股通信息披露-结算汇兑

    限量: 单次获取所有沪港通结算汇率数据
    """
    try:
        stock_sgt_settlement_exchange_rate_sse_df = ak.stock_sgt_settlement_exchange_rate_sse()
        return stock_sgt_settlement_exchange_rate_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 深港通-港股通业务信息-参考汇率
@router.get("/stock_sgt_reference_exchange_rate_szse",
            operation_id="get_stock_sgt_reference_exchange_rate_szse")
def get_stock_sgt_reference_exchange_rate_szse():
    """
    接口: stock_sgt_reference_exchange_rate_szse

    目标地址: https://www.szse.cn/szhk/hkbussiness/exchangerate/index.html

    描述: 深港通-港股通业务信息-参考汇率

    限量: 单次获取所有深港通参考汇率数据
    """
    try:
        stock_sgt_reference_exchange_rate_szse_df = ak.stock_sgt_reference_exchange_rate_szse()
        return stock_sgt_reference_exchange_rate_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 沪港通-港股通信息披露-参考汇率
@router.get("/stock_sgt_reference_exchange_rate_sse",
            operation_id="get_stock_sgt_reference_exchange_rate_sse")
def get_stock_sgt_reference_exchange_rate_sse():
    """
    接口: stock_sgt_reference_exchange_rate_sse

    目标地址: http://www.sse.com.cn/services/hkexsc/disclo/ratios/

    描述: 沪港通-港股通信息披露-参考汇率

    限量: 单次获取所有沪港通参考汇率数据
    """
    try:
        stock_sgt_reference_exchange_rate_sse_df = ak.stock_sgt_reference_exchange_rate_sse()
        return stock_sgt_reference_exchange_rate_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-行情中心-港股市场-港股通成份股
@router.get("/stock_hk_ggt_components_em",
            operation_id="get_stock_hk_ggt_components_em")
def get_stock_hk_ggt_components_em():
    """
    接口: stock_hk_ggt_components_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_components

    描述: 东方财富网-行情中心-港股市场-港股通成份股

    限量: 单次获取所有港股通成份股数据
    """
    try:
        stock_hk_ggt_components_em_df = ak.stock_hk_ggt_components_em()
        return stock_hk_ggt_components_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSHKSymbolRequest(BaseModel):
    stock: str = Field(..., title="资金类型", description="可选择'北向资金', '南向资金'")


# 东方财富-数据中心-沪深港通-市场概括-分时数据
@router.post("/stock_hsgt_fund_min_em",
             operation_id="post_stock_hsgt_fund_min_em")
async def post_stock_hsgt_fund_min_em(request: DongCaiSHKSymbolRequest):
    """
    接口: stock_hsgt_fund_min_em

    目标地址: https://data.eastmoney.com/hsgt/hsgtDetail/scgk.html

    描述: 东方财富-数据中心-沪深港通-市场概括-分时数据

    限量: 单次返回指定个股的所有数据
    """
    try:
        stock_hsgt_fund_min_em_df = ak.stock_hsgt_fund_min_em(symbol=request.symbol)
        return stock_hsgt_fund_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSHKSymolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="类型",
                        description="可选择'北向资金增持行业板块排行', '北向资金增持概念板块排行', '北向资金增持地域板块排行'")
    indicator: str = Field(..., title="时间周期",
                           description="可选择'今日', '3日', '5日', '10日', '1月', '1季', '1年'")


# 东方财富网-数据中心-沪深港通持股-板块排行
@router.post("/stock_hsgt_board_rank_em",
             operation_id="post_stock_hsgt_board_rank_em")
async def post_stock_hsgt_board_rank_em(data: DongCaiSHKSymolIndicatorRequest):
    """
    接口: stock_hsgt_board_rank_em

    目标地址: https://data.eastmoney.com/hsgtcg/bk.html

    描述: 东方财富网-数据中心-沪深港通持股-板块排行

    限量: 单次获取指定个股和指定时间段的所有数据
    """
    try:
        df = ak.stock_hsgt_board_rank_em(symbol=data.symbol, indicator=data.indicator)
        df.columns = [
            "序号", "名称", "最新涨跌幅", "北向资金今日持股-股票只数", "北向资金今日持股-市值",
            "北向资金今日持股-占板块比", "北向资金今日持股-占北向资金比", "北向资金今日增持估计-股票只数",
            "北向资金今日增持估计-市值", "北向资金今日增持估计-市值增幅", "北向资金今日增持估计-占板块比",
            "北向资金今日增持估计-占北向资金比", "今日增持最大股-市值", "今日增持最大股-占股本比",
            "今日减持最大股-占股本比", "今日减持最大股-市值", "报告时间"
        ]
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class DongCaiSHKMarketRequest(BaseModel):
    market: str = Field(..., title="市场", description="可选择'北向', '沪股通', '深股通'")
    indicator: str = Field(..., title="时间周期",
                           description="可选择'今日排行', '3日排行', '5日排行', '10日排行', '月排行', '季排行', '年排行'")


# 东方财富网-数据中心-沪深港通持股-个股排行
@router.post("/stock_hsgt_hold_stock_em",
             operation_id="post_stock_hsgt_hold_stock_em")
def post_stock_hsgt_hold_stock_em(data: DongCaiSHKMarketRequest):
    """
    接口: stock_hsgt_hold_stock_em

    目标地址: https://data.eastmoney.com/hsgtcg/list.html

    描述: 东方财富网-数据中心-沪深港通持股-个股排行

    限量: 单次获取指定市场和指定时间段的所有数据
    """
    try:
        stock_em_hsgt_hold_stock_df = ak.stock_hsgt_hold_stock_em(market=data.market, indicator=data.indicator)
        return stock_em_hsgt_hold_stock_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="市场", description="'北向持股', '沪股通持股', '深股通持股', '南向持股'")
    start_date: str = Field(..., title="起始时间(需近期交易日)", description="例：20240701")
    end_date: str = Field(..., title="终止时间(需近期交易日)", description="例：20240701")


# 东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计
@router.post("/stock_hsgt_stock_statistics_em",
             operation_id="post_stock_hsgt_stock_statistics_em")
async def post_stock_hsgt_stock_statistics_em(request: DongCaiSymbolDateRangeRequest):
    """
    接口: stock_hsgt_stock_statistics_em

    目标地址: http://data.eastmoney.com/hsgtcg/StockStatistics.aspx

    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计

    限量: 单次获取指定市场的起始时间和终止时间之间的所有数据, 该接口只能获取近期的数据
    """
    try:
        stock_hsgt_stock_statistics_em_df = ak.stock_hsgt_stock_statistics_em(symbol=request.symbol,
                                                                              start_date=request.start_date,
                                                                              end_date=request.end_date)
        return stock_hsgt_stock_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiMarketDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="市场", description="'北向持股', '沪股通持股', '深股通持股', '南向持股'")
    start_date: str = Field(..., title="起始时间(需近期交易日)", description="例：20240701")
    end_date: str = Field(..., title="终止时间(需近期交易日)", description="例：20240701")


# 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行
@router.post("/stock_hsgt_institution_statistics_em",
             operation_id="post_stock_hsgt_institution_statistics_em")
async def post_stock_hsgt_institution_statistics_em(request: DongCaiMarketDateRangeRequest):
    """
    接口: stock_hsgt_institution_statistics_em

    目标地址: http://data.eastmoney.com/hsgtcg/InstitutionStatistics.aspx

    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行

    限量: 单次获取指定市场的所有数据, 该接口只能获取近期的数据
    """
    try:
        stock_hsgt_institution_statistics_em_df = ak.stock_hsgt_institution_statistics_em(market=request.market,
                                                                                          start_date=request.start_date,
                                                                                          end_date=request.end_date)
        return stock_hsgt_institution_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSHKHistorySymbolRequest(BaseModel):
    symbol: str = Field(..., title="市场",
                        description="'北向资金', '沪股通', '深股通', '南向资金', '港股通沪', '港股通深'")


# 东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据
@router.post("/stock_hsgt_hist_em",
             operation_id="post_stock_hsgt_hist_em")
async def post_stock_hsgt_hist_em(request: DongCaiSHKHistorySymbolRequest):
    """
    接口: stock_hsgt_hist_em

    目标地址: https://data.eastmoney.com/hsgt/index.html

    描述: 东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据

    限量: 单次获取指定个股的所有数据
    """
    try:

        stock_hsgt_hist_em_df = ak.stock_hsgt_hist_em(symbol=request.symbol)
        stock_hsgt_hist_em_df = sanitize_data_pandas(stock_hsgt_hist_em_df)
        return stock_hsgt_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OnlyStockRequest(BaseModel):
    stock: str = Field(..., title="个股", description="例：002008")


# 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票
@router.post("/stock_hsgt_individual_em",
             operation_id="post_stock_hsgt_individual_em")
async def post_stock_hsgt_individual_em(request: OnlyStockRequest):
    """
    接口: stock_hsgt_individual_em

    目标地址: https://data.eastmoney.com/hsgtcg/StockHdStatistics/002008.html

    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票

    限量: 单次获取指定个股的近期数据
    """
    try:
        stock_hsgt_individual_em_df = ak.stock_hsgt_individual_em(stock=request.stock)
        return stock_hsgt_individual_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiStockRequest(BaseModel):
    stock: str = Field(..., title="个股", description="例：002008")
    start_date: str = Field(..., title="起始时间(需近90个交易日内)", description="例：20240701")
    end_date: str = Field(..., title="终止时间(需近90个交易日内)", description="例：20240715")


# 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票-个股详情
@router.post("/stock_hsgt_individual_detail_em",
             operation_id="post_stock_hsgt_individual_detail_em")
async def post_stock_hsgt_individual_detail_em(request: DongCaiStockRequest):
    """
    接口: stock_hsgt_individual_detail_em

    目标地址: http://data.eastmoney.com/hsgtcg/StockHdStatistics/002008.html

    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票-个股详情

    限量: 单次获取指定个股的在起始时间和终止时间之间的所有数据; 注意只能返回 90 个交易日内的数据
    """
    try:
        stock_hsgt_individual_detail_em_df = ak.stock_hsgt_individual_detail_em(symbol=request.stock,
                                                                                start_date=request.start_date,
                                                                                end_date=request.end_date)
        return stock_hsgt_individual_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
