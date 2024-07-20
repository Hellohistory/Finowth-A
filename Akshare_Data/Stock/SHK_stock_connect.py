import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    stock: str
    symbol: str


class DateRequest(BaseModel):
    date: str


class DateRangeRequest(BaseModel):
    start_date: str
    end_date: str


class StockRequest(BaseModel):
    stock: str
    start_date: str
    end_date: str


class StockHSGTRequest(BaseModel):
    stock: str


class RequestModel(BaseModel):
    symbol: str
    indicator: str


# 东方财富网-数据中心-资金流向-沪深港通资金流向
@router.get("/stock_hsgt_fund_flow_summary_em",
            operation_id="get_stock_hsgt_fund_flow_summary_em")
async def get_stock_hsgt_fund_flow_summary_em():
    """
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
async def get_stock_sgt_settlement_exchange_rate_szse():
    """
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
async def get_stock_sgt_settlement_exchange_rate_sse():
    """
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
async def get_stock_sgt_reference_exchange_rate_szse():
    """
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
async def get_stock_sgt_reference_exchange_rate_sse():
    """
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
async def get_stock_hk_ggt_components_em():
    """
    描述: 东方财富网-行情中心-港股市场-港股通成份股
    限量: 单次获取所有港股通成份股数据
    """
    try:
        stock_hk_ggt_components_em_df = ak.stock_hk_ggt_components_em()
        return stock_hk_ggt_components_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-沪深港通-市场概括-分时数据
@router.post("/stock_hsgt_fund_min_em",
             operation_id="post_stock_hsgt_fund_min_em")
async def post_stock_hsgt_fund_min_em(request: SymbolRequest):
    """
    描述: 东方财富-数据中心-沪深港通-市场概括-分时数据
    限量: 单次返回指定 symbol 的所有数据
    """
    try:
        stock_hsgt_fund_min_em_df = ak.stock_hsgt_fund_min_em(symbol=request.symbol)
        return stock_hsgt_fund_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-沪深港通持股-板块排行
@router.post("/stock_hsgt_board_rank_em",
             operation_id="post_stock_hsgt_board_rank_em")
async def post_stock_hsgt_board_rank_em(data: RequestModel):
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


# 东方财富网-数据中心-沪深港通持股-个股排行
@router.post("/stock_hsgt_hold_stock_em",
             operation_id="post_stock_hsgt_hold_stock_em")
def post_stock_hsgt_hold_stock_em():
    """
    描述: 东方财富网-数据中心-沪深港通持股-个股排行
    限量: 单次获取指定 market 和 indicator 的所有数据
    """
    try:
        stock_em_hsgt_hold_stock_df = ak.stock_hsgt_hold_stock_em(market="北向", indicator="今日排行")
        return stock_em_hsgt_hold_stock_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计
@router.post("/stock_hsgt_stock_statistics_em",
             operation_id="post_stock_hsgt_stock_statistics_em")
async def post_stock_hsgt_stock_statistics_em(request: DateRangeRequest):
    """
    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计
    限量: 单次获取指定 market 的 start_date 和 indicator 之间的所有数据
    """
    try:
        stock_hsgt_stock_statistics_em_df = ak.stock_hsgt_stock_statistics_em(symbol="北向持股",
                                                                              start_date=request.start_date,
                                                                              end_date=request.end_date)
        return stock_hsgt_stock_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行
@router.post("/stock_hsgt_institution_statistics_em",
             operation_id="post_stock_hsgt_institution_statistics_em")
async def post_stock_hsgt_institution_statistics_em(request: DateRangeRequest):
    """
    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行
    限量: 单次获取指定 market 的所有数据
    """
    try:
        stock_hsgt_institution_statistics_em_df = ak.stock_hsgt_institution_statistics_em(market="北向持股",
                                                                                          start_date=request.start_date,
                                                                                          end_date=request.end_date)
        return stock_hsgt_institution_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据
@router.post("/stock_hsgt_hist_em",
             operation_id="post_stock_hsgt_hist_em")
async def post_stock_hsgt_hist_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据
    限量: 单次获取指定 symbol 的所有数据
    """
    try:

        stock_hsgt_hist_em_df = ak.stock_hsgt_hist_em(symbol=request.symbol)
        # 清洗数据
        stock_hsgt_hist_em_df = sanitize_data_pandas(stock_hsgt_hist_em_df)
        return stock_hsgt_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票
@router.post("/stock_hsgt_individual_em",
             operation_id="post_stock_hsgt_individual_em")
async def post_stock_hsgt_individual_em(request: StockHSGTRequest):
    """
    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票
    限量: 单次获取指定 symbol 的近期数据
    """
    try:
        stock_hsgt_individual_em_df = ak.stock_hsgt_individual_em(stock=request.stock)
        return stock_hsgt_individual_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票-个股详情
@router.post("/stock_hsgt_individual_detail_em",
             operation_id="post_stock_hsgt_individual_detail_em")
async def post_stock_hsgt_individual_detail_em(request: StockRequest):
    """
    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-具体股票-个股详情
    限量: 单次获取指定 symbol 的在 start_date 和 indicator 之间的所有数据
    """
    try:
        stock_hsgt_individual_detail_em_df = ak.stock_hsgt_individual_detail_em(symbol=request.stock,
                                                                                start_date=request.start_date,
                                                                                end_date=request.end_date)
        return stock_hsgt_individual_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
