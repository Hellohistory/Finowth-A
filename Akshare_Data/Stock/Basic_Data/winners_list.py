import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.request_model import DateRangeRequest, SymbolRequest, SymbolFlagDateRequest, DateRequest
from Akshare_Data.utility_function import sanitize_data_pandas, sanitize_data, sanitize_data_numpy

router = APIRouter()


# 东方财富网-龙虎榜单-龙虎榜详情
@router.post("/stock_lhb_detail_em", operation_id="post_stock_lhb_detail_em")
async def post_stock_lhb_detail_em(request: DateRangeRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-龙虎榜详情
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_detail_em_df = ak.stock_lhb_detail_em(start_date=request.start_date, end_date=request.end_date)
        stock_lhb_detail_em_df = sanitize_data_numpy(stock_lhb_detail_em_df)

        return stock_lhb_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-个股上榜统计
@router.post("/stock_lhb_stock_statistic_em", operation_id="post_stock_lhb_stock_statistic_em")
async def post_stock_lhb_stock_statistic_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-个股上榜统计
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_stock_statistic_em_df = ak.stock_lhb_stock_statistic_em(symbol=request.symbol)
        return stock_lhb_stock_statistic_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-机构买卖每日统计
@router.post("/stock_lhb_jgmmtj_em", operation_id="post_stock_lhb_jgmmtj_em")
async def post_stock_lhb_jgmmtj_em(request: DateRangeRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-机构买卖每日统计
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_jgmmtj_em_df = ak.stock_lhb_jgmmtj_em(start_date=request.start_date, end_date=request.end_date)
        return stock_lhb_jgmmtj_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-机构席位追踪
@router.post("/stock_lhb_jgstatistic_em", operation_id="post_stock_lhb_jgstatistic_em")
async def post_stock_lhb_jgstatistic_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-机构席位追踪
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_jgstatistic_em_df = ak.stock_lhb_jgstatistic_em(symbol=request.symbol)
        stock_lhb_jgstatistic_em_df = sanitize_data_pandas(stock_lhb_jgstatistic_em_df)

        return stock_lhb_jgstatistic_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-每日活跃营业部
@router.post("/stock_lhb_hyyyb_em", operation_id="post_stock_lhb_hyyyb_em")
async def post_stock_lhb_hyyyb_em(request: DateRangeRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-每日活跃营业部
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_hyyyb_em_df = ak.stock_lhb_hyyyb_em(start_date=request.start_date, end_date=request.end_date)
        stock_lhb_hyyyb_em_df = sanitize_data_pandas(stock_lhb_hyyyb_em_df)

        return stock_lhb_hyyyb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-营业部排行
@router.post("/stock_lhb_yybph_em", operation_id="post_stock_lhb_yybph_em")
async def post_stock_lhb_yybph_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-营业部排行
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_yybph_em_df = ak.stock_lhb_yybph_em(symbol=request.symbol)
        return stock_lhb_yybph_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-营业部统计
@router.post("/stock_lhb_traderstatistic_em", operation_id="post_stock_lhb_traderstatistic_em")
async def post_stock_lhb_traderstatistic_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-营业部统计
    限量: 单次返回所有历史数据
    """
    try:
        stock_lhb_traderstatistic_em_df = ak.stock_lhb_traderstatistic_em(symbol=request.symbol)
        return stock_lhb_traderstatistic_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-龙虎榜单-个股龙虎榜详情
@router.post("/stock_lhb_stock_detail_em", operation_id="post_stock_lhb_stock_detail_em")
async def post_stock_lhb_stock_detail_em(request: SymbolFlagDateRequest):
    """
    描述: 东方财富网-数据中心-龙虎榜单-个股龙虎榜详情
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
    描述: 龙虎榜-营业部排行-抱团操作实力
    限量: 单次返回所有历史数据
    """
    try:
        stock_lh_yyb_control_df = ak.stock_lh_yyb_control()
        return stock_lh_yyb_control_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-每日详情
@router.post("/stock_lhb_detail_daily_sina", operation_id="post_stock_lhb_detail_daily_sina")
async def post_stock_lhb_detail_daily_sina(request: DateRequest):
    """
    描述: 新浪财经-龙虎榜-每日详情
    限量: 单次返回指定 symbol 的所有数据
    """
    try:
        stock_lhb_detail_daily_sina_df = ak.stock_lhb_detail_daily_sina(date=request.date)
        stock_lhb_detail_daily_sina_df = sanitize_data_pandas(stock_lhb_detail_daily_sina_df)

        return stock_lhb_detail_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-个股上榜统计
@router.post("/stock_lhb_ggtj_sina", operation_id="post_stock_lhb_ggtj_sina")
async def post_stock_lhb_ggtj_sina(request: SymbolRequest):
    """
    描述: 新浪财经-龙虎榜-个股上榜统计
    限量: 单次返回指定 symbol 的所有历史数据
    """
    try:
        stock_lhb_ggtj_sina_df = ak.stock_lhb_ggtj_sina(symbol=request.symbol)
        return stock_lhb_ggtj_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-营业上榜统计
@router.post("/stock_lhb_yytj_sina", operation_id="post_stock_lhb_yytj_sina")
async def post_stock_lhb_yytj_sina(request: SymbolRequest):
    """
    描述: 新浪财经-龙虎榜-营业上榜统计
    限量: 单次返回指定 symbol 的所有历史数据
    """
    try:
        stock_lhb_yytj_sina_df = ak.stock_lhb_yytj_sina(symbol=request.symbol)
        return stock_lhb_yytj_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-龙虎榜-机构席位追踪
@router.post("/stock_lhb_jgzz_sina", operation_id="post_stock_lhb_jgzz_sina")
async def post_stock_lhb_jgzz_sina(request: SymbolRequest):
    """
    描述: 新浪财经-龙虎榜-机构席位追踪
    限量: 单次返回指定 symbol 的所有历史数据
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
