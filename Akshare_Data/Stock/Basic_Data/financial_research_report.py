import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 东方财富-数据中心-研究报告-个股研报
@router.post("/stock_research_report_em", operation_id="stock_research_report_em")
async def stock_research_report_em(request: SymbolRequest):
    """
    东方财富-研究报告-个股研报

    接口: stock_research_report_em

    目标地址: https://data.eastmoney.com/report/stock.jshtml

    描述: 东方财富-数据中心-研究报告-个股研报

    限量: 单次返回指定个股的所有数据
    """
    try:
        stock_research_report_em = ak.stock_research_report_em(symbol=request.symbol)
        stock_research_report_em_df = sanitize_data_pandas(stock_research_report_em)
        return stock_research_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="数据种类",
                        description="可选择 全部 , 重大事项 , 财务报告 , 融资公告 , 风险提示 , 资产重组 , "
                                    " 信息变更 , 持股变动")
    date: str = Field(..., title="指定日期", description="例：20220511")


# 东方财富-数据中心-公告大全-沪深京 A 股公告
@router.post("/stock_notice_report", operation_id="stock_notice_report")
async def stock_notice_report(request: DongCaiSymbolDateRequest):
    """
    东方财富-沪深京 A 股公告

    接口: stock_notice_report

    目标地址: https://data.eastmoney.com/notices/hsa/5.html

    描述: 东方财富-数据中心-公告大全-沪深京 A 股公告

    限量: 单次获取指定个股和指定日期的数据
    """
    try:
        stock_notice_report = ak.stock_notice_report(symbol=request.symbol, date=request.date)
        stock_notice_report_df = sanitize_data_pandas(stock_notice_report)
        return stock_notice_report_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangStockSymbolRequest(BaseModel):
    stock: str = Field(..., title="指定个股代码(需带市场标识)", description="例：sh600600")
    symbol: str = Field(..., title="报表类型", description="可选择 资产负债表 , 利润表 , 现金流量表 ")


# 新浪财经-财务报表-三大报表
@router.post("/stock_financial_report_sina", operation_id="stock_financial_report_sina")
async def stock_financial_report_sina(request: XinLangStockSymbolRequest):
    """
    新浪财经-财务报表-三大报表

    接口: stock_financial_report_sina

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600600/displaytype/4.phtml?source=fzb&qq-pf-to=pcqq.group

    描述: 新浪财经-财务报表-三大报表

    限量: 单次获取指定报表的所有年份数据的历史数据

    注意: 原始数据中有 `国内票证结算` 和 `内部应收款` 字段重, 返回数据中已经剔除
    """
    try:
        stock_financial_report_sina = ak.stock_financial_report_sina(stock=request.stock, symbol=request.symbol)
        stock_financial_report_sina_df = sanitize_data_pandas(stock_financial_report_sina)
        return stock_financial_report_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiZiChanSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码(需带市场标识)", description="例：SH600519")


# 东方财富-股票-财务分析-资产负债表-按报告期
@router.post("/stock_balance_sheet_by_report_em", operation_id="stock_balance_sheet_by_report_em")
async def stock_balance_sheet_by_report_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-资产负债表-按报告期

    接口: stock_balance_sheet_by_report_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-资产负债表-按报告期

    限量: 单次获取指定个股的资产负债表-按报告期数据
    """
    try:
        stock_balance_sheet_by_report_em = ak.stock_balance_sheet_by_report_em(symbol=request.symbol)
        stock_balance_sheet_by_report_em_df = sanitize_data_pandas(stock_balance_sheet_by_report_em)
        return stock_balance_sheet_by_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-资产负债表-按年度
@router.post("/stock_balance_sheet_by_yearly_em", operation_id="stock_balance_sheet_by_yearly_em")
async def stock_balance_sheet_by_yearly_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-资产负债表-按年度

    接口: stock_balance_sheet_by_yearly_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-资产负债表-按年度

    限量: 单次获取指定个股的资产负债表-按年度数据
    """
    try:
        stock_balance_sheet_by_yearly_em = ak.stock_balance_sheet_by_yearly_em(symbol=request.symbol)
        stock_balance_sheet_by_yearly_em_df = sanitize_data_pandas(stock_balance_sheet_by_yearly_em)
        return stock_balance_sheet_by_yearly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-报告期
@router.post("/stock_profit_sheet_by_report_em", operation_id="stock_profit_sheet_by_report_em")
async def stock_profit_sheet_by_report_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-利润表-报告期

    接口: stock_profit_sheet_by_report_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-利润表-报告期

    限量: 单次获取指定个股的利润表-报告期数据
    """
    try:
        stock_profit_sheet_by_report_em = ak.stock_profit_sheet_by_report_em(symbol=request.symbol)
        stock_profit_sheet_by_report_em_df = sanitize_data_pandas(stock_profit_sheet_by_report_em)
        return stock_profit_sheet_by_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-按年度
@router.post("/stock_profit_sheet_by_yearly_em", operation_id="stock_profit_sheet_by_yearly_em")
async def stock_profit_sheet_by_yearly_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-利润表-按年度

    接口: stock_profit_sheet_by_yearly_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-利润表-按年度

    限量: 单次获取指定个股的利润表-按年度数据
    """
    try:
        stock_profit_sheet_by_yearly_em = ak.stock_profit_sheet_by_yearly_em(symbol=request.symbol)
        stock_profit_sheet_by_yearly_em_df = sanitize_data_pandas(stock_profit_sheet_by_yearly_em)
        return stock_profit_sheet_by_yearly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-按单季度
@router.post("/stock_profit_sheet_by_quarterly_em", operation_id="stock_profit_sheet_by_quarterly_em")
async def stock_profit_sheet_by_quarterly_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-利润表-按单季度

    接口: stock_profit_sheet_by_quarterly_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-利润表-按单季度

    限量: 单次获取指定个股的利润表-按单季度数据
    """
    try:
        stock_profit_sheet_by_quarterly_em = ak.stock_profit_sheet_by_quarterly_em(symbol=request.symbol)
        stock_profit_sheet_by_quarterly_em_df = sanitize_data_pandas(stock_profit_sheet_by_quarterly_em)
        return stock_profit_sheet_by_quarterly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-按报告期
@router.post("/stock_cash_flow_sheet_by_report_em", operation_id="stock_cash_flow_sheet_by_report_em")
async def stock_cash_flow_sheet_by_report_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-现金流量表-按报告期

    接口: stock_cash_flow_sheet_by_report_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-现金流量表-按报告期

    限量: 单次获取指定个股的现金流量表-按报告期数据
    """
    try:
        stock_cash_flow_sheet_by_report_em = ak.stock_cash_flow_sheet_by_report_em(symbol=request.symbol)
        stock_cash_flow_sheet_by_report_em_df = sanitize_data_pandas(stock_cash_flow_sheet_by_report_em)

        return stock_cash_flow_sheet_by_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-按年度
@router.post("/stock_cash_flow_sheet_by_yearly_em", operation_id="stock_cash_flow_sheet_by_yearly_em")
async def stock_cash_flow_sheet_by_yearly_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-现金流量表-按年度

    接口: stock_cash_flow_sheet_by_yearly_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-现金流量表-按年度

    限量: 单次获取指定个股的现金流量表-按年度数据
    """
    try:
        stock_cash_flow_sheet_by_yearly_em = ak.stock_cash_flow_sheet_by_yearly_em(symbol=request.symbol)

        stock_cash_flow_sheet_by_yearly_em_df = sanitize_data_pandas(stock_cash_flow_sheet_by_yearly_em)

        return stock_cash_flow_sheet_by_yearly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-按单季度
@router.post("/stock_cash_flow_sheet_by_quarterly_em", operation_id="stock_cash_flow_sheet_by_quarterly_em")
async def stock_cash_flow_sheet_by_quarterly_em(request: DongCaiZiChanSymbolRequest):
    """
    东方财富-财务分析-现金流量表-按单季度

    接口: stock_cash_flow_sheet_by_quarterly_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sh600519#lrb-0

    描述: 东方财富-股票-财务分析-现金流量表-按单季度

    限量: 单次获取指定个股的现金流量表-按单季度数据
    """
    try:
        stock_cash_flow_sheet_by_quarterly_em = ak.stock_cash_flow_sheet_by_quarterly_em(symbol=request.symbol)
        stock_cash_flow_sheet_by_quarterly_em_df = sanitize_data_pandas(stock_cash_flow_sheet_by_quarterly_em)

        return stock_cash_flow_sheet_by_quarterly_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class TongHuaShunFinancialDebt(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：000063")
    indicator: str = Field(..., title="报告类型", description="可选择'按报告期', '按年度', '按单季度'")


# 同花顺-财务指标-资产负债表
@router.post("/stock_financial_debt_ths", operation_id="stock_financial_debt_ths")
async def stock_financial_debt_ths(request: TongHuaShunFinancialDebt):
    """
    同花顺-财务指标-资产负债表

    接口: stock_financial_debt_ths

    目标地址: https://basic.10jqka.com.cn/new/000063/finance.html

    描述: 同花顺-财务指标-资产负债表

    限量: 单次获取资产负债表所有历史数据
    """
    try:
        stock_financial_debt_ths = ak.stock_financial_debt_ths(symbol=request.symbol, indicator=request.indicator)
        stock_financial_debt_ths_df = sanitize_data_pandas(stock_financial_debt_ths)
        return stock_financial_debt_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-财务指标-利润表
@router.post("/stock_financial_benefit_ths", operation_id="stock_financial_benefit_ths")
async def stock_financial_benefit_ths(request: TongHuaShunFinancialDebt):
    """
    同花顺-财务指标-利润表

    接口: stock_financial_benefit_ths

    目标地址: https://basic.10jqka.com.cn/new/000063/finance.html

    描述: 同花顺-财务指标-利润表

    限量: 单次获取利润表所有历史数据
    """
    try:
        stock_financial_benefit_ths = ak.stock_financial_benefit_ths(symbol=request.symbol, indicator=request.indicator)
        stock_financial_benefit_ths_df = sanitize_data_pandas(stock_financial_benefit_ths)
        return stock_financial_benefit_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-财务指标-现金流量表
@router.post("/stock_financial_cash_ths", operation_id="stock_financial_cash_ths")
async def stock_financial_cash_ths(request: TongHuaShunFinancialDebt):
    """
    同花顺-财务指标-现金流量表

    接口: stock_financial_cash_ths

    目标地址: https://basic.10jqka.com.cn/new/000063/finance.html

    描述: 同花顺-财务指标-现金流量表

    限量: 单次获取现金流量表所有历史数据
    """
    try:
        stock_financial_cash_ths = ak.stock_financial_cash_ths(symbol=request.symbol, indicator=request.indicator)
        stock_financial_cash_ths_df = sanitize_data_pandas(stock_financial_cash_ths)
        return stock_financial_cash_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class TuiShiSymbolRequest(BaseModel):
    symbol: str = Field(..., title="带市场标识的已退市股票代码", description="例：SZ000013")


# 东方财富-股票-财务分析-资产负债表-已退市股票-按报告期
@router.post("/stock_balance_sheet_by_report_delisted_em", operation_id="stock_balance_sheet_by_report_delisted_em")
async def stock_balance_sheet_by_report_delisted_em(request: TuiShiSymbolRequest):
    """
    东方财富-资产负债表-已退市股票-按报告期

    接口: stock_balance_sheet_by_report_delisted_em

    目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/zcfzb

    描述: 东方财富-股票-财务分析-资产负债表-已退市股票-按报告期

    限量: 单次获取指定个股的资产负债表-按报告期数据
    """
    try:
        stock_balance_sheet_by_report_delisted_em = ak.stock_balance_sheet_by_report_delisted_em(symbol=request.symbol)
        stock_balance_sheet_by_report_delisted_em_df = sanitize_data_pandas(stock_balance_sheet_by_report_delisted_em)
        return stock_balance_sheet_by_report_delisted_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-利润表-已退市股票-按报告期
@router.post("/stock_profit_sheet_by_report_delisted_em", operation_id="stock_profit_sheet_by_report_delisted_em")
async def stock_profit_sheet_by_report_delisted_em(request: TuiShiSymbolRequest):
    """
    东方财富-利润表-已退市股票-按报告期

    接口: stock_profit_sheet_by_report_delisted_em

    目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/lrb

    描述: 东方财富-股票-财务分析-利润表-已退市股票-按报告期

    限量: 单次获取指定个股的利润表-按报告期数据
    """
    try:
        stock_profit_sheet_by_report_delisted_em = ak.stock_profit_sheet_by_report_delisted_em(symbol=request.symbol)
        stock_profit_sheet_by_report_delisted_em_df = sanitize_data_pandas(stock_profit_sheet_by_report_delisted_em)
        return stock_profit_sheet_by_report_delisted_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-股票-财务分析-现金流量表-已退市股票-按报告期
@router.post("/stock_cash_flow_sheet_by_report_delisted_em", operation_id="stock_cash_flow_sheet_by_report_delisted_em")
async def stock_cash_flow_sheet_by_report_delisted_em(request: TuiShiSymbolRequest):
    """
    东方财富-现金流量表-已退市股票-按报告期

    接口: stock_cash_flow_sheet_by_report_delisted_em

    目标地址: https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=SZ000013#/cwfx/xjllb

    描述: 东方财富-股票-财务分析-现金流量表-已退市股票-按报告期

    限量: 单次获取指定个股的现金流量表-按报告期数据
    """
    try:
        stock_cash_flow_sheet_by_report_delisted_em = ak.stock_cash_flow_sheet_by_report_delisted_em(symbol=request.symbol)
        stock_cash_flow_sheet_by_report_delisted_em_df = sanitize_data_pandas(stock_cash_flow_sheet_by_report_delisted_em)
        return stock_cash_flow_sheet_by_report_delisted_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiHKFinancialRequest(BaseModel):
    stock: str = Field(..., title="港股代码", description="例：00700")
    symbol: str = Field(..., title="报表类型", description="可选择'资产负债表', '利润表', '现金流量表'")
    indicator: str = Field(..., title="报告周期", description="可选择'年度', '报告期'")


# 东方财富-港股-财务报表-三大报表
@router.post("/stock_financial_hk_report_em", operation_id="stock_financial_hk_report_em")
async def stock_financial_hk_report_em(request: DongCaiHKFinancialRequest):
    """
    东方财富-港股-财务报表-三大报表

    接口: stock_financial_hk_report_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HKF10/FinancialAnalysis/index?type=web&code=00700

    描述: 东方财富-港股-财务报表-三大报表

    限量: 单次获取指定报表的所有年份数据
    """
    try:
        stock_financial_hk_report_em = ak.stock_financial_hk_report_em(stock=request.stock, symbol=request.symbol,
                                                                       indicator=request.indicator)
        stock_financial_hk_report_em_df = sanitize_data_pandas(stock_financial_hk_report_em)
        return stock_financial_hk_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
