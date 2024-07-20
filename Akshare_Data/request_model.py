from pydantic import BaseModel
from datetime import date as dt_date


class IndustryIndexRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class DtDateRequest(BaseModel):
    date: dt_date


class SymbolStockRequest(BaseModel):
    stock: str
    symbol: str


class SectorSummaryRequest(BaseModel):
    symbol: str
    ym_date: str


class AreaSummaryRequest(BaseModel):
    ym_date: str


class FinancialAnalysis(BaseModel):
    symbol: str
    start_year: str


class SymolIndicatorRequest(BaseModel):
    symbol: str
    indicator: str


class StockRequest(BaseModel):
    stock: str
    start_date: str
    end_date: str


class OnlyStockRequest(BaseModel):
    stock: str


class RequestModel(BaseModel):
    symbol: str
    indicator: str


class StockReportRequest(BaseModel):
    from_page: int
    to_page: int


class DateRequest(BaseModel):
    date: str


class IndustryHistRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    period: str
    adjust: str


class IndustryHistMinRequest(BaseModel):
    symbol: str
    period: str


class SymbolDateRequest(BaseModel):
    symbol: str
    date: str


class DateRangeRequest(BaseModel):
    start_date: str
    end_date: str


class SymbolIndicatorRequest(BaseModel):
    symbol: str
    indicator: str


class DividendDetailRequest(BaseModel):
    symbol: str
    indicator: str
    date: str = None


class ConceptHistRequest(BaseModel):
    symbol: str
    period: str
    start_date: str
    end_date: str
    adjust: str


class ConceptHistMinRequest(BaseModel):
    symbol: str
    period: str


class SingleDateRequest(BaseModel):
    date: str


class SymbolMarketRequest(BaseModel):
    stock: str
    market: str


class IndicatorRequest(BaseModel):
    indicator: str


class SectorRequest(BaseModel):
    indicator: str
    sector_type: str


class SymbolDateRangeRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class YearRequest(BaseModel):
    year: str


class AnalystDetailRequest(BaseModel):
    analyst_id: str
    indicator: str


class SymbolRequest(BaseModel):
    symbol: str


class MarketPeriodRequest(BaseModel):
    market: str
    period: str


class DisclosureRequest(BaseModel):
    symbol: str
    market: str
    category: str
    start_date: str
    end_date: str


class StockAHDailyRequest(BaseModel):
    symbol: str
    start_year: str
    end_year: str
    adjust: str = ""


class SymbolFlagDateRequest(BaseModel):
    symbol: str
    date: str
    flag: str


class RestrictedReleaseSummaryRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class StockQuarterRequest(BaseModel):
    stock: str
    quarter: str


class StockHistoryRequest(BaseModel):
    symbol: str
    period: str
    start_date: str
    end_date: str
    adjust: str = ""


class StockMinuteRequest(BaseModel):
    symbol: str
    period: str
    adjust: str
    start_date: str
    end_date: str


class StockDailyRequest(BaseModel):
    symbol: str
    adjust: str = ""


class FinancialRequest(BaseModel):
    stock: str
    symbol: str
    indicator: str


class FinancialDebt(BaseModel):
    symbol: str
    indicator: str


class SymbolIndicatorPeriodRequest(BaseModel):
    symbol: str
    indicator: str
    period: str


class SymbolPeriodAdjust(BaseModel):
    symbol: str
    period: str
    adjust: str = ""


class StockZhVoteBaiduRequest(BaseModel):
    symbol: str
    indicator: str


class HoldingDetailRequest(BaseModel):
    date: str
    indicator: str
    symbol: str


class SymbolAndNameRequest(BaseModel):
    symbol: str
    name: str


class SectorSpotRequest(BaseModel):
    indicator: str
