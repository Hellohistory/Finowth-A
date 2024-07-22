from pydantic import BaseModel, Field


class IndustryIndexRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class SymbolStockRequest(BaseModel):
    stock: str
    symbol: str


class SectorSummaryRequest(BaseModel):
    symbol: str = Field(..., title="指定个股", description="例如2024-07-12; 当前交易日的数据需要交易所收盘后统计")
    ym_date: str = Field(..., title="指定交易日", description="例如2024-07-12; 当前交易日的数据需要交易所收盘后统计")


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


class StockAdjustFactorRequest(BaseModel):
    symbol: str
    adjust: str


class StockReportRequest(BaseModel):
    from_page: int = Field(..., title="开始获取的页码", description="例如1")
    to_page: int = Field(..., title="结束获取的页码", description="例如100")


class DateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20230808")


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
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


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
    adjust: str


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
    symbol: str = Field(..., title="指定个股", description="例如2024-07-12; 当前交易日的数据需要交易所收盘后统计")
    period: str = Field(..., title="时间周期",
                        description="例如daily; 所有可选参数为：daily(日), weekly(周), monthly(月)")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据")


class StockMinuteRequest(BaseModel):
    symbol: str
    period: str
    adjust: str
    start_date: str
    end_date: str


class StockDailyRequest(BaseModel):
    symbol: str = Field(..., title="指定个股(需带市场标识)", description="例如sh688008")
    adjust: str = Field(..., title="复权类型", description="qfq: 返回前复权后的数据; "
                                                           "hfq: 返回后复权后的数据; "
                                                           "hfq-factor: 返回后复权因子; "
                                                           "qfq-factor: 返回前复权因子")


class FinancialRequest(BaseModel):
    stock: str = Field(..., title="", description="")
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")


class FinancialDebt(BaseModel):
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")


class SymbolIndicatorPeriodRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")


class SymbolPeriodAdjust(BaseModel):
    symbol: str
    period: str
    adjust: str


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
