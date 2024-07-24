import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas, sanitize_data

router = APIRouter()


class DongCaiWinnerListDateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


# 东方财富-龙虎榜单-龙虎榜详情
@router.post("/stock_lhb_detail_em", operation_id="post_stock_lhb_detail_em")
async def post_stock_lhb_detail_em(request: DongCaiWinnerListDateRangeRequest):
    """
    东方财富-龙虎榜单-龙虎榜详情

    接口: stock_lhb_detail_em

    目标地址: https://data.eastmoney.com/stock/tradedetail.html

    描述: 东方财富-数据中心-龙虎榜单-龙虎榜详情

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_detail_em_df = ak.stock_lhb_detail_em(start_date=request.start_date, end_date=request.end_date)
        stock_lhb_detail_em_df = sanitize_data_pandas(stock_lhb_detail_em_df)

        return stock_lhb_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiWinnerListSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期", description="可选择'近一月', '近三月', '近六月', '近一年'")


# 东方财富-龙虎榜单-个股上榜统计
@router.post("/stock_lhb_stock_statistic_em", operation_id="post_stock_lhb_stock_statistic_em")
async def post_stock_lhb_stock_statistic_em(request: DongCaiWinnerListSymbolRequest):
    """
    东方财富-龙虎榜单-个股上榜统计

    接口: stock_lhb_stock_statistic_em

    目标地址: https://data.eastmoney.com/stock/tradedetail.html

    描述: 东方财富-数据中心-龙虎榜单-个股上榜统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_stock_statistic_em_df = ak.stock_lhb_stock_statistic_em(symbol=request.symbol)
        return stock_lhb_stock_statistic_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiWinnerListDateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


# 东方财富-龙虎榜单-机构买卖每日统计
@router.post("/stock_lhb_jgmmtj_em", operation_id="post_stock_lhb_jgmmtj_em")
async def post_stock_lhb_jgmmtj_em(request: DongCaiWinnerListDateRangeRequest):
    """
    东方财富-龙虎榜单-机构买卖每日统计

    接口: stock_lhb_jgmmtj_em

    目标地址: https://data.eastmoney.com/stock/jgmmtj.html

    描述: 东方财富-数据中心-龙虎榜单-机构买卖每日统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_jgmmtj_em_df = ak.stock_lhb_jgmmtj_em(start_date=request.start_date, end_date=request.end_date)
        return stock_lhb_jgmmtj_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-龙虎榜单-机构席位追踪
@router.post("/stock_lhb_jgstatistic_em", operation_id="post_stock_lhb_jgstatistic_em")
async def post_stock_lhb_jgstatistic_em(request: DongCaiWinnerListSymbolRequest):
    """
    东方财富-龙虎榜单-机构席位追踪

    接口: stock_lhb_jgstatistic_em

    目标地址: https://data.eastmoney.com/stock/jgstatistic.html

    描述: 东方财富-数据中心-龙虎榜单-机构席位追踪

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_jgstatistic_em_df = ak.stock_lhb_jgstatistic_em(symbol=request.symbol)
        stock_lhb_jgstatistic_em_df = sanitize_data_pandas(stock_lhb_jgstatistic_em_df)

        return stock_lhb_jgstatistic_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-龙虎榜单-每日活跃营业部
@router.post("/stock_lhb_hyyyb_em", operation_id="post_stock_lhb_hyyyb_em")
async def post_stock_lhb_hyyyb_em(request: DongCaiWinnerListDateRangeRequest):
    """
    东方财富-龙虎榜单-每日活跃营业部

    接口: stock_lhb_hyyyb_em

    目标地址: https://data.eastmoney.com/stock/hyyyb.html

    描述: 东方财富-数据中心-龙虎榜单-每日活跃营业部

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_hyyyb_em_df = ak.stock_lhb_hyyyb_em(start_date=request.start_date, end_date=request.end_date)
        stock_lhb_hyyyb_em_df = sanitize_data_pandas(stock_lhb_hyyyb_em_df)

        return stock_lhb_hyyyb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-龙虎榜单-营业部排行
@router.post("/stock_lhb_yybph_em", operation_id="post_stock_lhb_yybph_em")
async def post_stock_lhb_yybph_em(request: DongCaiWinnerListSymbolRequest):
    """
    东方财富-龙虎榜单-营业部排行

    接口: stock_lhb_yybph_em

    目标地址: https://data.eastmoney.com/stock/yybph.html

    描述: 东方财富-数据中心-龙虎榜单-营业部排行

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_yybph_em_df = ak.stock_lhb_yybph_em(symbol=request.symbol)
        return stock_lhb_yybph_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-龙虎榜单-营业部统计
@router.post("/stock_lhb_traderstatistic_em", operation_id="post_stock_lhb_traderstatistic_em")
async def post_stock_lhb_traderstatistic_em(request: DongCaiWinnerListSymbolRequest):
    """
    东方财富-龙虎榜单-营业部统计

    接口: stock_lhb_traderstatistic_em

    目标地址: https://data.eastmoney.com/stock/traderstatistic.html

    描述: 东方财富-数据中心-龙虎榜单-营业部统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_traderstatistic_em_df = ak.stock_lhb_traderstatistic_em(symbol=request.symbol)
        return stock_lhb_traderstatistic_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiWinnerListSymbolFlagDateRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：600077")
    date: str = Field(..., title="相应股票的有龙虎榜详情数据的日期",
                      description="需要通过stock_lhb_stock_detail_date_em接口获取")
    flag: str = Field(..., title="资金行为", description="可选择'买入', '卖出'")


# 东方财富-龙虎榜单-个股龙虎榜详情
@router.post("/stock_lhb_stock_detail_em", operation_id="post_stock_lhb_stock_detail_em")
async def post_stock_lhb_stock_detail_em(request: DongCaiWinnerListSymbolFlagDateRequest):
    """
    东方财富-龙虎榜单-个股龙虎榜详情

    接口: stock_lhb_stock_detail_em

    目标地址: https://data.eastmoney.com/stock/lhb/600077.html

    描述: 东方财富-数据中心-龙虎榜单-个股龙虎榜详情

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_stock_detail_em_df = ak.stock_lhb_stock_detail_em(symbol=request.symbol, date=request.date,
                                                                    flag=request.flag)
        stock_lhb_stock_detail_em_df = sanitize_data_pandas(stock_lhb_stock_detail_em_df)

        return stock_lhb_stock_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 龙虎榜-营业部排行-上榜次数最多
@router.get("/stock_lh_yyb_most", operation_id="get_stock_lh_yyb_most")
def get_stock_lh_yyb_most():
    """
    龙虎榜-营业部排行-上榜次数最多

    接口: stock_lh_yyb_most

    目标地址: https://data.10jqka.com.cn/market/longhu/

    描述: 龙虎榜-营业部排行-上榜次数最多

    限量: 单次返回所有历史数据
    """
    try:
        stock_lh_yyb_most_df = ak.stock_lh_yyb_most()
        return stock_lh_yyb_most_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 龙虎榜-营业部排行-资金实力最强
@router.get("/stock_lh_yyb_capital", operation_id="get_stock_lh_yyb_capital")
def get_stock_lh_yyb_capital():
    """
    龙虎榜-营业部排行-资金实力最强

    接口: stock_lh_yyb_capital

    目标地址: https://data.10jqka.com.cn/market/longhu/

    描述: 龙虎榜-营业部排行-资金实力最强

    限量: 单次返回所有历史数据
    """
    try:
        stock_lh_yyb_capital_df = ak.stock_lh_yyb_capital()
        return stock_lh_yyb_capital_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 龙虎榜-营业部排行-抱团操作实力
@router.get("/stock_lh_yyb_control", operation_id="get_stock_lh_yyb_control")
def get_stock_lh_yyb_control():
    """
    龙虎榜-营业部排行-抱团操作实力

    接口: stock_lh_yyb_control

    目标地址: https://data.10jqka.com.cn/market/longhu/

    描述: 龙虎榜-营业部排行-抱团操作实力

    限量: 单次返回所有历史数据
    """
    try:
        stock_lh_yyb_control_df = ak.stock_lh_yyb_control()
        return stock_lh_yyb_control_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangWinnerListDateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20240222")


# 新浪财经-龙虎榜-每日详情
@router.post("/stock_lhb_detail_daily_sina", operation_id="post_stock_lhb_detail_daily_sina")
async def post_stock_lhb_detail_daily_sina(request: XinLangWinnerListDateRequest):
    """
    新浪财经-龙虎榜-每日详情

    接口: stock_lhb_detail_daily_sina

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhb/index.phtml

    描述: 新浪财经-龙虎榜-每日详情

    限量: 单次返回指定时间的所有数据
    """
    try:
        stock_lhb_detail_daily_sina_df = ak.stock_lhb_detail_daily_sina(date=request.date)
        stock_lhb_detail_daily_sina_df = sanitize_data_pandas(stock_lhb_detail_daily_sina_df)

        return stock_lhb_detail_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-个股上榜统计
@router.post("/stock_lhb_ggtj_sina", operation_id="post_stock_lhb_ggtj_sina")
async def post_stock_lhb_ggtj_sina(request: XinLangWinnerListDateRequest):
    """
    新浪财经-龙虎榜-个股上榜统计

    接口: stock_lhb_ggtj_sina

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/ggtj/index.phtml

    描述: 新浪财经-龙虎榜-个股上榜统计

    限量: 单次返回指定个股的所有历史数据
    """
    try:
        stock_lhb_ggtj_sina_df = ak.stock_lhb_ggtj_sina(symbol=request.symbol)
        return stock_lhb_ggtj_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择'5': 最近 5 天; '10': 最近 10 天; '30': 最近 30 天; '60': 最近 60 天")


# 新浪财经-龙虎榜-营业上榜统计
@router.post("/stock_lhb_yytj_sina", operation_id="post_stock_lhb_yytj_sina")
async def post_stock_lhb_yytj_sina(request: XinLangSymbolRequest):
    """
    新浪财经-龙虎榜-营业上榜统计

    接口: stock_lhb_yytj_sina

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/yytj/index.phtml

    描述: 新浪财经-龙虎榜-营业上榜统计

    限量: 单次返回指定个股的所有历史数据
    """
    try:
        stock_lhb_yytj_sina_df = ak.stock_lhb_yytj_sina(symbol=request.symbol)
        return stock_lhb_yytj_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-机构席位追踪
@router.post("/stock_lhb_jgzz_sina", operation_id="post_stock_lhb_jgzz_sina")
async def post_stock_lhb_jgzz_sina(request: XinLangSymbolRequest):
    """
    新浪财经-龙虎榜-机构席位追踪

    接口: stock_lhb_jgzz_sina

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/jgzz/index.phtml

    描述: 新浪财经-龙虎榜-机构席位追踪

    限量: 单次返回指定个股的所有历史数据
    """
    try:
        stock_lhb_jgzz_sina_df = ak.stock_lhb_jgzz_sina(symbol=request.symbol)
        return stock_lhb_jgzz_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-机构席位成交明细
@router.get("/stock_lhb_jgmx_sina", operation_id="get_stock_lhb_jgmx_sina")
def get_stock_lhb_jgmx_sina():
    """
    新浪财经-龙虎榜-机构席位成交明细

    接口: stock_lhb_jgmx_sina

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/jgzz/index.phtml

    描述: 新浪财经-龙虎榜-机构席位成交明细

    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_jgmx_sina_df = ak.stock_lhb_jgmx_sina()
        data = stock_lhb_jgmx_sina_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
