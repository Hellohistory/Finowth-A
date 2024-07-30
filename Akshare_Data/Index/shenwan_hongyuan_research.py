import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class IndexRealtimeFundSW(BaseModel):
    symbol: str = Field(..., title="基金指数类型",
                        description="可选择：基础一级, 基础二级, 基础三级, 特色指数")


# 指数数据-申万宏源研究-基金指数实时行情
@router.post("/index_realtime_fund_sw",
             operation_id="post_index_realtime_fund_sw")
def post_index_realtime_fund_sw(request: IndexRealtimeFundSW):
    """
    指数数据-申万宏源研究-基金指数实时行情

    接口: index_realtime_fund_sw

    目标地址: https://www.swsresearch.com/institute_sw/allIndex/releasedIndex

    描述: 申万宏源研究-申万指数-指数发布-基金指数-实时行情

    限量: 该接口返回指定基金指数类型的数据
    """
    try:
        index_realtime_fund_sw = ak.index_realtime_fund_sw(
            symbol=request.symbol
        )
        index_realtime_fund_sw_df = sanitize_data_pandas(index_realtime_fund_sw)

        return index_realtime_fund_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexHistFundSW(BaseModel):
    symbol: str = Field(..., title="基金指数代码", description="例：807200")
    period: str = Field(..., title="时间周期",
                        description="可选择：日：day，周：week，月：month")


# 指数数据-申万宏源研究-基金指数历史行情
@router.post("/index_hist_fund_sw",
             operation_id="post_index_hist_fund_sw")
def post_index_hist_fund_sw(request: IndexHistFundSW):
    """
    指数数据-申万宏源研究-基金指数历史行情

    接口: index_hist_fund_sw

    目标地址: https://www.swsresearch.com/institute_sw/allIndex/releasedIndex/fundDetail?code=807100

    描述: 申万宏源研究-申万指数-指数发布-基金指数-历史行情

    限量: 该接口返回指定基金指数类型的数据
    """
    try:
        index_hist_fund_sw = ak.index_hist_fund_sw(
            symbol=request.symbol,
            period=request.period
        )
        index_hist_fund_sw_df = sanitize_data_pandas(index_hist_fund_sw)

        return index_hist_fund_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexRealtimeSW(BaseModel):
    symbol: str = Field(..., title="基金指数类型",
                        description="可选择：市场表征, 一级行业, 二级行业, 风格指数, 大类风格指数, 金创指数")


# 指数数据-申万宏源研究-申万指数实时行情
@router.post("/index_realtime_sw",
             operation_id="post_index_realtime_sw")
def post_index_realtime_sw(request: IndexRealtimeSW):
    """
    指数数据-申万宏源研究-基金指数实时行情

    接口: index_realtime_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/releasedIndex

    描述: 申万宏源研究-指数系列; 注意其中大类风格指数和金创指数的字段

    限量: 该接口返回指定 symbol 的数据
    """
    try:
        index_realtime_sw = ak.index_realtime_sw(
            symbol=request.symbol
        )
        index_realtime_sw_df = sanitize_data_pandas(index_realtime_sw)

        return index_realtime_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-申万宏源研究-申万指数历史行情
@router.post("/index_hist_sw",
             operation_id="post_index_hist_sw")
def post_index_hist_sw(request: IndexHistFundSW):
    """
    指数数据-申万宏源研究-申万指数历史行情

    接口: index_hist_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/releasedIndex/releasedetail?code=801002&name=申万中小

    描述: 申万宏源研究-指数发布-指数详情-指数历史数据

    限量: 该接口返回指定基金指数类型的数据
    """
    try:
        index_hist_sw = ak.index_hist_sw(
            symbol=request.symbol,
            period=request.period
        )
        index_hist_sw_df = sanitize_data_pandas(index_hist_sw)

        return index_hist_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexMinSW(BaseModel):
    symbol: str = Field(..., title="基金代码", description="例：801030")


# 指数数据-申万宏源研究-申万指数分时行情
@router.post("/index_min_sw",
             operation_id="post_index_min_sw")
def post_index_min_sw(request: IndexMinSW):
    """
    指数数据-申万宏源研究-申万指数分时行情

    接口: index_min_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/releasedIndex/releasedetail?code=801001&name=申万中小

    描述: 申万宏源研究-指数发布-指数详情-指数分时数据

    限量: 该接口返回指定基金代码的数据
    """
    try:
        index_min_sw = ak.index_min_sw(
            symbol=request.symbol
        )
        index_min_sw_df = sanitize_data_pandas(index_min_sw)

        return index_min_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-申万宏源研究-申万指数分时行情
@router.post("/index_component_sw",
             operation_id="post_index_component_sw")
def post_index_component_sw(request: IndexMinSW):
    """
    指数数据-申万宏源研究-申万指数分时行情

    接口: index_component_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/releasedIndex/releasedetail?code=801001&name=申万中小

    描述: 申万宏源研究-指数发布-指数详情-成分股

    限量: 该接口返回指定基金代码的数据
    """
    try:
        index_component_sw = ak.index_component_sw(
            symbol=request.symbol
        )
        index_component_sw_df = sanitize_data_pandas(index_component_sw)

        return index_component_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexAnalysisDailySW(BaseModel):
    symbol: str = Field(..., title="请求类型",
                        description="可选择：市场表征, 一级行业, 二级行业, 风格指数")
    start_date: str = Field(..., title="开始日期", description="例：20200101")
    end_date: str = Field(..., title="结束日期", description="例：20200101")


# 指数数据-申万宏源研究-申万指数分析-日报表
@router.post("/index_analysis_daily_sw",
             operation_id="post_index_analysis_daily_sw")
def post_index_analysis_daily_sw(request: IndexAnalysisDailySW):
    """
    指数数据-申万宏源研究-申万指数分析-日报表

    接口: index_analysis_daily_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/analysisIndex

    描述: 申万宏源研究-指数分析-日报表

    限量: 该接口返回指定参数的数据
    """
    try:
        index_analysis_daily_sw = ak.index_analysis_daily_sw(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )
        index_analysis_daily_sw_df = sanitize_data_pandas(index_analysis_daily_sw)

        return index_analysis_daily_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexAnalysisDailySW(BaseModel):
    symbol: str = Field(..., title="请求类型",
                        description="可选择：市场表征, 一级行业, 二级行业, 风格指数")
    date: str = Field(..., title="指定日期",
                      description="例：20221104，可通过 index_analysis_week_month_sw 获取")


# 指数数据-申万宏源研究-申万指数分析-周报表
@router.post("/index_analysis_weekly_sw",
             operation_id="post_index_analysis_weekly_sw")
def post_index_analysis_weekly_sw(request: IndexAnalysisDailySW):
    """
    指数数据-申万宏源研究-申万指数分析-周报表

    接口: index_analysis_weekly_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/analysisIndex

    描述: 申万宏源研究-指数分析-周报表

    限量: 该接口返回指定参数的数据
    """
    try:
        index_analysis_weekly_sw = ak.index_analysis_weekly_sw(
            symbol=request.symbol,
            date=request.date
        )
        index_analysis_weekly_sw_df = sanitize_data_pandas(index_analysis_weekly_sw)

        return index_analysis_weekly_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-申万宏源研究-申万指数分析-月报表
@router.post("/index_analysis_monthly_sw",
             operation_id="post_index_analysis_monthly_sw")
def post_index_analysis_monthly_sw(request: IndexAnalysisDailySW):
    """
    指数数据-申万宏源研究-申万指数分析-月报表

    接口: index_analysis_monthly_sw

    目标地址: https://www.swhyresearch.com/institute_sw/allIndex/analysisIndex

    描述: 申万宏源研究-指数分析-月报表

    限量: 该接口返回指定参数的数据
    """
    try:
        index_analysis_monthly_sw = ak.index_analysis_monthly_sw(
            symbol=request.symbol,
            date=request.date
        )
        index_analysis_monthly_sw_df = sanitize_data_pandas(index_analysis_monthly_sw)

        return index_analysis_monthly_sw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
