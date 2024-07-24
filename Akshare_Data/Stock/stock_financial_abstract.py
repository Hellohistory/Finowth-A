import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：600004")


# 新浪财经-财务报表-关键指标
@router.post("/stock_financial_abstract", operation_id="post_stock_financial_abstract")
async def post_stock_financial_abstract(request: SymbolRequest):
    """
    新浪财经-财务报表-关键指标

    接口: stock_financial_abstract

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600004.phtml

    描述: 新浪财经-财务报表-关键指标

    限量: 单次获取关键指标所有历史数据
    """
    try:
        stock_financial_abstract_df = ak.stock_financial_abstract(symbol=request.symbol)
        stock_financial_abstract_df = sanitize_data_pandas(stock_financial_abstract_df)

        return stock_financial_abstract_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取关键指标数据失败: {str(e)}")


class TongHuaShunSymbolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：000063")
    indicator: str = Field(..., title="报表周期", description="'按报告期', '按年度', '按单季度'")


# 同花顺-财务指标-主要指标
@router.post("/stock_financial_abstract_ths", operation_id="post_stock_financial_abstract_ths")
async def post_stock_financial_abstract_ths(request: TongHuaShunSymbolIndicatorRequest):
    """
    同花顺-财务指标-主要指标

    接口: stock_financial_abstract_ths

    目标地址: https://basic.10jqka.com.cn/new/000063/finance.html

    描述: 同花顺-财务指标-主要指标

    限量: 单次获取主要指标所有历史数据
    """
    try:
        stock_financial_abstract_ths_df = ak.stock_financial_abstract_ths(symbol=request.symbol,
                                                                          indicator=request.indicator)
        stock_financial_abstract_ths_df = sanitize_data_pandas(stock_financial_abstract_ths_df)

        return stock_financial_abstract_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取财务摘要数据失败: {str(e)}")


class XinLangFinancialAnalysis(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：600004")
    start_year: str = Field(..., title="开始查询的年份", description="例：2020")


# 新浪财经-财务分析-财务指标
@router.post("/stock_financial_analysis_indicator",
             operation_id="post_stock_financial_analysis_indicator")
async def post_stock_financial_analysis_indicator(request: XinLangFinancialAnalysis):
    """
    新浪财经-财务分析-财务指标

    接口: stock_financial_analysis_indicator

    目标地址: https://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/600004/ctrl/2019/displaytype/4.phtml

    描述: 新浪财经-财务分析-财务指标

    限量: 单次获取指定个股和指定年份的所有财务指标历史数据
    """
    try:
        stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol=request.symbol,
                                                                                      start_year=request.start_year)
        stock_financial_analysis_indicator_df = sanitize_data_pandas(stock_financial_analysis_indicator_df)

        return stock_financial_analysis_indicator_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取财务分析指标数据失败: {str(e)}")


class DongCaiSymolIndicatorRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：00700")
    indicator: str = Field(..., title="报告类型", description="可选择'年度', '报告期'")


# 东方财富-港股-财务分析-主要指标
@router.post("/stock_financial_hk_analysis_indicator_em",
             operation_id="post_stock_financial_hk_analysis_indicator_em")
async def post_stock_financial_hk_analysis_indicator_em(request: DongCaiSymolIndicatorRequest):
    """
    东方财富-港股-财务分析-主要指标

    接口: stock_financial_hk_analysis_indicator_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/NewFinancialAnalysis/index?type=web&code=00700

    描述: 东方财富-港股-财务分析-主要指标

    限量: 单次获取财务指标所有历史数据
    """
    try:
        stock_financial_hk_analysis_indicator_em_df = (
            ak.stock_financial_hk_analysis_indicator_em(symbol=request.symbol,
                                                        indicator=request.indicator))
        stock_financial_hk_analysis_indicator_em_df = sanitize_data_pandas(stock_financial_hk_analysis_indicator_em_df)

        return stock_financial_hk_analysis_indicator_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取财务分析指标数据失败: {str(e)}")
