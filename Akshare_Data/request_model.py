from pydantic import BaseModel, Field


class IndustryIndexRequest(BaseModel):
    symbol: str
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


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



class RequestModel(BaseModel):
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")


class StockAdjustFactorRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    adjust: str = Field(..., title="", description="")


class StockReportRequest(BaseModel):
    from_page: int = Field(..., title="开始获取的页码", description="例如1")
    to_page: int = Field(..., title="结束获取的页码", description="例如100")


class DateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20230808")


class IndustryHistRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    start_date: str = Field(..., title="", description="")
    end_date: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")
    adjust: str = Field(..., title="", description="")


class IndustryHistMinRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")


class SymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    date: str = Field(..., title="", description="")


class DateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


class SymbolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")


class DividendDetailRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")
    date: str = Field(..., title="", description="")


class ConceptHistRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")
    adjust: str = Field(..., title="", description="")


class ConceptHistMinRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")


class SingleDateRequest(BaseModel):
    date: str = Field(..., title="", description="")


class SymbolMarketRequest(BaseModel):
    stock: str = Field(..., title="", description="")
    market: str = Field(..., title="", description="")


class IndicatorRequest(BaseModel):
    indicator: str = Field(..., title="", description="")


class SectorRequest(BaseModel):
    indicator: str = Field(..., title="", description="")
    sector_type: str = Field(..., title="", description="")


class SymbolDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


class YearRequest(BaseModel):
    year: str = Field(..., title="", description="")


class AnalystDetailRequest(BaseModel):
    analyst_id: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


class MarketPeriodRequest(BaseModel):
    market: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")


class DisclosureRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    market: str = Field(..., title="", description="")
    category: str = Field(..., title="", description="")
    start_date: str = Field(..., title="", description="")
    end_date: str = Field(..., title="", description="")


class StockAHDailyRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    start_year: str = Field(..., title="", description="")
    end_year: str = Field(..., title="", description="")
    adjust: str = Field(..., title="", description="")


class SymbolFlagDateRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    date: str = Field(..., title="", description="")
    flag: str = Field(..., title="", description="")


class RestrictedReleaseSummaryRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


class StockQuarterRequest(BaseModel):
    stock: str = Field(..., title="", description="")
    quarter: str = Field(..., title="", description="")


class StockHistoryRequest(BaseModel):
    symbol: str = Field(..., title="指定个股", description="例如2024-07-12; 当前交易日的数据需要交易所收盘后统计")
    period: str = Field(..., title="时间周期",
                        description="例如daily; 所有可选参数为：daily(日), weekly(周), monthly(月)")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据")


class StockMinuteRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")
    adjust: str = Field(..., title="", description="")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


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
    symbol: str = Field(..., title="", description="")
    period: str = Field(..., title="", description="")
    adjust: str = Field(..., title="", description="")


class StockZhVoteBaiduRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")


class HoldingDetailRequest(BaseModel):
    date: str = Field(..., title="", description="")
    indicator: str = Field(..., title="", description="")
    symbol: str = Field(..., title="", description="")


class SymbolAndNameRequest(BaseModel):
    symbol: str = Field(..., title="", description="")
    name: str = Field(..., title="", description="")


class SectorSpotRequest(BaseModel):
    indicator: str = Field(..., title="", description="")
