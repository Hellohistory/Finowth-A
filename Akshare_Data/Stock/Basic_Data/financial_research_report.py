import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas, sanitize_data

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


class DateRequest(BaseModel):
    date: str


class StockRequest(BaseModel):
    stock: str
    symbol: str


class FinancialRequest(BaseModel):
    stock: str
    symbol: str
    indicator: str


class FinancialDebt(BaseModel):
    symbol: str
    indicator: str


# 东方财富网-数据中心-研究报告-个股研报
@router.post("/stock_research_report_em",
             operation_id="post_post_stock_research_report_em")
def get_stock_research_report_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-研究报告-个股研报
    限量: 单次返回指定 symbol 的所有数据
    """
    try:
        stock_research_report_em_df = ak.stock_research_report_em(symbol=request.symbol)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_research_report_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-公告大全-沪深京 A 股公告
@router.post("/stock_notice_report",
             operation_id="post_stock_notice_report")
def get_stock_notice_report(request: DateRequest):
    """
    描述: 东方财富网-数据中心-公告大全-沪深京 A 股公告
    限量: 单次获取指定 symbol 和 symbol 的数据
    """
    try:
        stock_notice_report_df = ak.stock_notice_report(symbol='财务报告', date=request.date)
        return stock_notice_report_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-财务报表-三大报表
@router.post("/stock_financial_report_sina",
             operation_id="post_stock_financial_report_sina")
def get_stock_financial_report_sina(request: StockRequest):
    """
    描述: 新浪财经-财务报表-三大报表
    限量: 单次获取指定报表的所有年份数据的历史数据
    """
    try:
        stock_financial_report_sina_df = ak.stock_financial_report_sina(stock=request.stock, symbol=request.symbol)
        stock_financial_report_sina_df = sanitize_data_pandas(stock_financial_report_sina_df)

        return stock_financial_report_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-资产负债表-按报告期
@router.post("/stock_balance_sheet_by_report_em",
             operation_id="post_stock_balance_sheet_by_report_em")
def get_stock_balance_sheet_by_report_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-资产负债表-按报告期
    限量: 单次获取指定 symbol 的资产负债表-按报告期数据
    """
    try:
        stock_balance_sheet_by_report_em_df = ak.stock_balance_sheet_by_report_em(symbol=request.symbol)
        stock_balance_sheet_by_report_em_df = sanitize_data_pandas(stock_balance_sheet_by_report_em_df)

        return stock_balance_sheet_by_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-资产负债表-按年度
@router.post("/stock_balance_sheet_by_yearly_em",
             operation_id="post_stock_balance_sheet_by_yearly_em")
def get_stock_balance_sheet_by_yearly_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-资产负债表-按年度
    限量: 单次获取指定 symbol 的资产负债表-按年度数据
    """
    try:
        stock_balance_sheet_by_yearly_em_df = ak.stock_balance_sheet_by_yearly_em(symbol=request.symbol)
        stock_balance_sheet_by_yearly_em_df = sanitize_data_pandas(stock_balance_sheet_by_yearly_em_df)

        return stock_balance_sheet_by_yearly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-报告期
@router.post("/stock_profit_sheet_by_report_em",
             operation_id="post_stock_profit_sheet_by_report_em")
def get_stock_profit_sheet_by_report_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-利润表-报告期
    限量: 单次获取指定 symbol 的利润表-报告期数据
    """
    try:
        stock_profit_sheet_by_report_em_df = ak.stock_profit_sheet_by_report_em(symbol=request.symbol)
        stock_profit_sheet_by_report_em_df = sanitize_data_pandas(stock_profit_sheet_by_report_em_df)

        return stock_profit_sheet_by_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-按年度
@router.post("/stock_profit_sheet_by_yearly_em",
             operation_id="post_stock_profit_sheet_by_yearly_em")
def get_stock_profit_sheet_by_yearly_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-利润表-按年度
    限量: 单次获取指定 symbol 的利润表-按年度数据
    """
    try:
        stock_profit_sheet_by_yearly_em_df = ak.stock_profit_sheet_by_yearly_em(symbol=request.symbol)
        stock_profit_sheet_by_yearly_em_df = sanitize_data_pandas(stock_profit_sheet_by_yearly_em_df)

        return stock_profit_sheet_by_yearly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-按单季度
@router.post("/stock_profit_sheet_by_quarterly_em",
             operation_id="post_stock_profit_sheet_by_quarterly_em")
def get_stock_profit_sheet_by_quarterly_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-利润表-按单季度
    限量: 单次获取指定 symbol 的利润表-按单季度数据
    """
    try:
        stock_profit_sheet_by_quarterly_em_df = ak.stock_profit_sheet_by_quarterly_em(symbol=request.symbol)
        stock_profit_sheet_by_quarterly_em_df = sanitize_data_pandas(stock_profit_sheet_by_quarterly_em_df)

        return stock_profit_sheet_by_quarterly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-按报告期
@router.post("/stock_cash_flow_sheet_by_report_em",
             operation_id="post_stock_cash_flow_sheet_by_report_em")
def get_stock_cash_flow_sheet_by_report_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-现金流量表-按报告期
    限量: 单次获取指定 symbol 的现金流量表-按报告期数据
    """
    try:
        stock_cash_flow_sheet_by_report_em_df = ak.stock_cash_flow_sheet_by_report_em(symbol=request.symbol)
        return stock_cash_flow_sheet_by_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-按年度
@router.post("/stock_cash_flow_sheet_by_yearly_em",
             operation_id="post_stock_cash_flow_sheet_by_yearly_em")
def get_stock_cash_flow_sheet_by_yearly_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-现金流量表-按年度
    限量: 单次获取指定 symbol 的现金流量表-按年度数据
    """
    try:
        stock_cash_flow_sheet_by_yearly_em_df = ak.stock_cash_flow_sheet_by_yearly_em(symbol=request.symbol)

        stock_cash_flow_sheet_by_yearly_em_df = sanitize_data(stock_cash_flow_sheet_by_yearly_em_df)

        return stock_cash_flow_sheet_by_yearly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-按单季度
@router.post("/stock_cash_flow_sheet_by_quarterly_em",
             operation_id="post_stock_cash_flow_sheet_by_quarterly_em")
def get_stock_cash_flow_sheet_by_quarterly_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-现金流量表-按单季度
    限量: 单次获取指定 symbol 的现金流量表-按单季度数据
    """
    try:
        stock_cash_flow_sheet_by_quarterly_em_df = ak.stock_cash_flow_sheet_by_quarterly_em(symbol=request.symbol)
        return stock_cash_flow_sheet_by_quarterly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-财务指标-资产负债表
@router.post("/stock_financial_debt_ths",
             operation_id="post_stock_financial_debt_ths")
def get_stock_financial_debt_ths(request: FinancialDebt):
    """
    描述: 同花顺-财务指标-资产负债表
    限量: 单次获取资产负债表所有历史数据
    """
    try:
        stock_financial_debt_ths_df = ak.stock_financial_debt_ths(symbol=request.symbol, indicator=request.indicator)
        return stock_financial_debt_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-财务指标-利润表
@router.post("/stock_financial_benefit_ths",
             operation_id="post_stock_financial_benefit_ths")
def get_stock_financial_benefit_ths(request: FinancialDebt):
    """
    描述: 同花顺-财务指标-利润表
    限量: 单次获取利润表所有历史数据
    """
    try:
        stock_financial_benefit_ths_df = ak.stock_financial_benefit_ths(symbol=request.symbol,
                                                                        indicator=request.indicator)
        return stock_financial_benefit_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-财务指标-现金流量表
@router.post("/stock_financial_cash_ths",
             operation_id="post_stock_financial_cash_ths")
def get_stock_financial_cash_ths(request: FinancialDebt):
    """
    描述: 同花顺-财务指标-现金流量表
    限量: 单次获取现金流量表所有历史数据
    """
    try:
        stock_financial_cash_ths_df = ak.stock_financial_cash_ths(symbol=request.symbol, indicator=request.indicator)
        return stock_financial_cash_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-资产负债表-已退市股票-按报告期
@router.post("/stock_balance_sheet_by_report_delisted_em",
             operation_id="stock_balance_sheet_by_report_delisted_em")
def get_stock_balance_sheet_by_report_delisted_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-资产负债表-已退市股票-按报告期
    限量: 单次获取指定 symbol 的资产负债表-按报告期数据
    """
    try:
        stock_balance_sheet_by_report_delisted_em_df = ak.stock_balance_sheet_by_report_delisted_em(
            symbol=request.symbol)
        stock_balance_sheet_by_report_delisted_em_df = sanitize_data_pandas(
            stock_balance_sheet_by_report_delisted_em_df)

        return stock_balance_sheet_by_report_delisted_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-已退市股票-按报告期
@router.post("/stock_profit_sheet_by_report_delisted_em",
             operation_id="post_stock_profit_sheet_by_report_delisted_em")
def get_stock_profit_sheet_by_report_delisted_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-利润表-已退市股票-按报告期
    限量: 单次获取指定 symbol 的利润表-按报告期数据
    """
    try:
        stock_profit_sheet_by_report_delisted_em_df = ak.stock_profit_sheet_by_report_delisted_em(symbol=request.symbol)
        return stock_profit_sheet_by_report_delisted_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-已退市股票-按报告期
@router.post("/stock_cash_flow_sheet_by_report_delisted_em",
             operation_id="post_stock_cash_flow_sheet_by_report_delisted_em")
def get_stock_cash_flow_sheet_by_report_delisted_em(request: SymbolRequest):
    """
    描述: 东方财富-股票-财务分析-现金流量表-已退市股票-按报告期
    限量: 单次获取指定 symbol 的现金流量表-按报告期数据
    """
    try:
        stock_cash_flow_sheet_by_report_delisted_em_df = ak.stock_cash_flow_sheet_by_report_delisted_em(
            symbol=request.symbol)
        return stock_cash_flow_sheet_by_report_delisted_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-港股-财务报表-三大报表
@router.post("/stock_financial_hk_report_em",
             operation_id="post_stock_financial_hk_report_em")
def get_stock_financial_hk_report_em(request: FinancialRequest):
    """
    描述: 东方财富-港股-财务报表-三大报表
    限量: 单次获取指定报表的所有年份数据
    """
    try:
        stock_financial_hk_report_em_df = ak.stock_financial_hk_report_em(stock=request.stock, symbol=request.symbol,
                                                                          indicator=request.indicator)
        return stock_financial_hk_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
