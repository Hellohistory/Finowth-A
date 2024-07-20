import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, SymbolIndicatorRequest, FinancialAnalysis
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


@router.post("/stock_financial_abstract", operation_id="post_stock_financial_abstract")
async def post_stock_financial_abstract(request: SymbolRequest):
    """
    获取股票的财务摘要数据
    :param request: 包含股票代码的请求体
    :return: 财务摘要数据的JSON格式
    """
    try:
        # 使用akshare获取财务摘要数据
        stock_financial_abstract_df = ak.stock_financial_abstract(symbol=request.symbol)
        stock_financial_abstract_df = sanitize_data_pandas(stock_financial_abstract_df)

        return stock_financial_abstract_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取财务摘要数据失败: {str(e)}")


@router.post("/stock_financial_abstract_ths", operation_id="post_stock_financial_abstract_ths")
async def post_stock_financial_abstract_ths(request: SymbolIndicatorRequest):
    """
    获取股票的财务摘要数据（包含指标）
    :param request: 包含股票代码和指标的请求体
    :return: 财务摘要数据的JSON格式
    """
    try:
        stock_financial_abstract_ths_df = ak.stock_financial_abstract_ths(symbol=request.symbol,
                                                                          indicator=request.indicator)
        stock_financial_abstract_ths_df = sanitize_data_pandas(stock_financial_abstract_ths_df)

        return stock_financial_abstract_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取财务摘要数据失败: {str(e)}")


@router.post("/stock_financial_analysis_indicator",
             operation_id="post_stock_financial_analysis_indicator")
async def post_stock_financial_analysis_indicator(request: FinancialAnalysis):
    """
    获取股票的财务摘要数据（包含起始年份）
    :param request: 包含股票代码和起始年份的请求体
    :return: 财务摘要数据的JSON格式
    """
    try:
        # 使用akshare获取财务分析指标数据
        stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol=request.symbol,
                                                                                      start_year=request.start_year)
        stock_financial_analysis_indicator_df = sanitize_data_pandas(stock_financial_analysis_indicator_df)

        # 返回处理后的数据
        return stock_financial_analysis_indicator_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取财务分析指标数据失败: {str(e)}")
