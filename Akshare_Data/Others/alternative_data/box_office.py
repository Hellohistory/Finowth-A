import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 另类数据-电影票房-实时票房
@router.get("/movie_boxoffice_realtime", operation_id="get_movie_boxoffice_realtime")
def get_movie_boxoffice_realtime():
    """
    另类数据-电影票房-实时票房

    接口: movie_boxoffice_realtime

    目标地址: https://ys.endata.cn/BoxOffice/Movie

    描述: 当前时刻的实时电影票房数据, 每 5 分钟更新一次数据, 实时票房包含今天未开映场次已售出的票房

    限量: 当前时刻的实时票房数据
    """
    try:
        movie_boxoffice_realtime = ak.movie_boxoffice_realtime()
        movie_boxoffice_realtime_df = sanitize_data_pandas(movie_boxoffice_realtime)
        return movie_boxoffice_realtime_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class MovieBoxoffice(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240219，只能选择最近的日期")


# 另类数据-电影票房-单日票房
@router.post("/movie_boxoffice_daily",
             operation_id="post_movie_boxoffice_daily")
def post_movie_boxoffice_daily(request: MovieBoxoffice):
    """
    另类数据-电影票房-单日票房

    接口: movie_boxoffice_daily

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Day/index.html

    描述: 指定日期的电影票房数据, 每日 10:30, 12:30更新日票房，16:30 同时补充前 7 日票房

    限量: 只能指定最近的日期
    """
    try:
        movie_boxoffice_daily = ak.movie_boxoffice_daily(
            date=request.date
        )
        movie_boxoffice_daily_df = sanitize_data_pandas(movie_boxoffice_daily)

        return movie_boxoffice_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-电影票房-单周票房
@router.post("/movie_boxoffice_weekly",
             operation_id="post_movie_boxoffice_weekly")
def post_movie_boxoffice_weekly(request: MovieBoxoffice):
    """
    另类数据-电影票房-单周票房

    接口: movie_boxoffice_weekly

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Week/oneWeek.html

    描述: 指定日期所在完整周的票房数据, 影片周票房数据初始更新周期为每周二，下周二补充数据

    限量: 指定日期所在完整周的票房数据
    """
    try:
        movie_boxoffice_weekly = ak.movie_boxoffice_weekly(
            date=request.date
        )
        movie_boxoffice_weekly_df = sanitize_data_pandas(movie_boxoffice_weekly)

        return movie_boxoffice_weekly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-电影票房-单月票房
@router.post("/movie_boxoffice_monthly",
             operation_id="post_movie_boxoffice_monthly")
def post_movie_boxoffice_monthly(request: MovieBoxoffice):
    """
    另类数据-电影票房-单月票房

    接口: movie_boxoffice_monthly

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Month/oneMonth.html

    描述: 获取指定日期所在月份的票房数据, 每月5号更新上月票房，并补充之前两个月票房

    限量: 指定日期所在月份的票房数据, 只能获取最近月份的数据
    """
    try:
        movie_boxoffice_monthly = ak.movie_boxoffice_monthly(
            date=request.date
        )
        movie_boxoffice_monthly_df = sanitize_data_pandas(movie_boxoffice_monthly)

        return movie_boxoffice_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-电影票房-年度票房
@router.post("/movie_boxoffice_yearly",
             operation_id="post_movie_boxoffice_yearly")
def post_movie_boxoffice_yearly(request: MovieBoxoffice):
    """
    另类数据-电影票房-年度票房

    接口: movie_boxoffice_yearly

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Year/index.html

    描述: 指定日期所在年度的票房数据

    限量: 指定日期所在年度的票房数据, 只能获取最近年度的数据
    """
    try:
        movie_boxoffice_yearly = ak.movie_boxoffice_yearly(
            date=request.date
        )
        movie_boxoffice_yearly_df = sanitize_data_pandas(movie_boxoffice_yearly)

        return movie_boxoffice_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-电影票房-年度票房
@router.post("/movie_boxoffice_yearly_first_week",
             operation_id="post_movie_boxoffice_yearly_first_week")
def post_movie_boxoffice_yearly_first_week(request: MovieBoxoffice):
    """
    另类数据-电影票房-年度票房

    接口: movie_boxoffice_yearly_first_week

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Year/firstWeek.html

    描述: 指定日期所在年度的年度首周票房数据

    限量: 指定日期所在年度的年度首周票房数据, 只能获取最近年度的数据
    """
    try:
        movie_boxoffice_yearly_first_week = ak.movie_boxoffice_yearly_first_week(
            date=request.date
        )
        movie_boxoffice_yearly_first_week_df = sanitize_data_pandas(movie_boxoffice_yearly_first_week)

        return movie_boxoffice_yearly_first_week_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-电影票房-影院票房-日票房排行
@router.post("/movie_boxoffice_cinema_daily",
             operation_id="post_movie_boxoffice_cinema_daily")
def post_movie_boxoffice_cinema_daily(request: MovieBoxoffice):
    """
    另类数据-电影票房-影院票房-日票房排行

    接口: movie_boxoffice_cinema_daily

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Cinema/day.html

    描述: 指定日期的每日各影院的票房数据

    限量: 指定日期各影院的票房数据, 注意当前日期的数据需要第二日才可以获取
    """
    try:
        movie_boxoffice_cinema_daily = ak.movie_boxoffice_cinema_daily(
            date=request.date
        )
        movie_boxoffice_cinema_daily_df = sanitize_data_pandas(movie_boxoffice_cinema_daily)

        return movie_boxoffice_cinema_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-电影票房-影院票房-周票房排行
@router.post("/movie_boxoffice_cinema_weekly",
             operation_id="post_movie_boxoffice_cinema_weekly")
def post_movie_boxoffice_cinema_weekly(request: MovieBoxoffice):
    """
    另类数据-电影票房-影院票房-周票房排行

    接口: movie_boxoffice_cinema_weekly

    目标地址: https://www.endata.com.cn/BoxOffice/BO/Cinema/week.html

    描述: 指定日期的完整周各影院的票房数据

    限量: 指定日期的完整周各影院的票房数据, 注意当前日期的数据只能返回上周的数据
    """
    try:
        movie_boxoffice_cinema_weekly = ak.movie_boxoffice_cinema_weekly(
            date=request.date
        )
        movie_boxoffice_cinema_weekly_df = sanitize_data_pandas(movie_boxoffice_cinema_weekly)

        return movie_boxoffice_cinema_weekly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
