import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class Sunrise(BaseModel):
    symbol: str = Field(..., title="指定城市", description="例：定州市")


# 另类数据-空气质量-河北-近期空气质量
@router.post("/air_quality_hebei",
             operation_id="post_air_quality_hebei")
def post_air_quality_hebei(request: Sunrise):
    """
    另类数据-空气质量-河北-近期空气质量

    接口: air_quality_hebei

    目标地址: https://110.249.223.67/publish/

    描述: 河北省指定城市的最近 6 天空气质量数据

    注释:

    注释-等级划分

    空气污染指数为0－50，空气质量级别为一级，空气质量状况属于优。此时，空气质量令人满意，基本无空气污染，各类人群可正常活动。

    空气污染指数为51－100，空气质量级别为二级，空气质量状况属于良。此时空气质量可接受，但某些污染物可能对极少数异常敏感人群健康有较弱影响，建议极少数异常敏感人群应减少户外活动。

    空气污染指数为101－150，空气质量级别为三级，空气质量状况属于轻度污染。此时，易感人群症状有轻度加剧，健康人群出现刺激症状。建议儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼。

    空气污染指数为151－200，空气质量级别为四级，空气质量状况属于中度污染。此时，进一步加剧易感人群症状，可能对健康人群心脏、呼吸系统有影响，建议疾病患者避免长时间、高强度的户外锻练，一般人群适量减少户外运动。

    空气污染指数为201－300，空气质量级别为五级，空气质量状况属于重度污染。此时，心脏病和肺病患者症状显著加剧，运动耐受力降低，健康人群普遍出现症状，建议儿童、老年人和心脏病、肺病患者应停留在室内，停止户外运动，一般人群减少户外运动。

    空气污染指数大于300，空气质量级别为六级，空气质量状况属于严重污染。此时，健康人群运动耐受力降低，有明显强烈症状，提前出现某些疾病，建议儿童、老年人和病人应当留在室内，避免体力消耗，一般人群应避免户外活动。

    注释-发布单位

    河北省环境应急与重污染天气预警中心

    注释-技术支持

    中国科学院大气物理研究所, 中科三清科技有限公司

    限量: 单次指定城市的最近 6 天的数据
    """
    try:
        air_quality_hebei = ak.air_quality_hebei(
            symbol=request.symbol
        )
        air_quality_hebei_df = sanitize_data_pandas(air_quality_hebei)

        return air_quality_hebei_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-空气质量-全国-城市列表
@router.get("/air_city_table", operation_id="get_air_city_table")
def get_air_city_table():
    """
    另类数据-空气质量-全国-城市列表

    接口: air_city_table

    目标地址: https://www.aqistudy.cn/

    描述: 所有能获取空气质量数据的城市表

    限量: 单次返回所有可以获取的城市表数据
    """
    try:
        air_city_table = ak.air_city_table()
        air_city_table_df = sanitize_data_pandas(air_city_table)
        return air_city_table_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class AirQualityHist(BaseModel):
    city: str = Field(..., title="指定城市", description="例：定州市，调用 air_city_table 接口获取所有城市列表")
    period: str = Field(..., title="数据频率",
                        description="hour: 每小时一个数据, 由于数据量比较大, 下载较慢; day: 每天一个数据; month: 每个月一个数据")
    start_date: str = Field(..., title="开始日期", description="例：20240717，需注意时间跨度不宜过长")
    end_date: str = Field(..., title="结束日期", description="例：20240717，需注意时间跨度不宜过长")


# 另类数据-空气质量-空气质量历史数据
@router.post("/air_quality_hist", operation_id="post_air_quality_hist")
def post_air_quality_hist(request: AirQualityHist):
    """
    另类数据-空气质量-空气质量历史数据

    接口: air_quality_hist

    目标地址: https://www.zq12369.com/

    描述: 指定城市和数据频率下并且在指定时间段内的空气质量数据

    限量: 单次返回所有的数据, 在提取一小时频率数据时请注意时间跨度不宜过长, 提取日频率数据的早年数据请分段提取
    """
    try:
        air_quality_hist = ak.air_quality_hist(
            city=request.city,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date
        )
        air_quality_hist_df = sanitize_data_pandas(air_quality_hist)

        return air_quality_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class AirQualityRank(BaseModel):
    date: str = Field(..., title="指定时间",
                      description="默认为空，返回当前时刻空气质量排名; 20200312: 当日空气质量排名; 202003: 当月空气质量排名; 2019: 当年空气质量排名;")


# 另类数据-空气质量-空气质量排名
@router.post("/air_quality_rank", operation_id="post_air_quality_rank")
def post_air_quality_rank(request: AirQualityRank):
    """
    另类数据-空气质量-空气质量排名

    接口: air_quality_rank

    目标地址: https://www.zq12369.com/environment.php

    描述: 获取指定时间点上所有城市(168个)的空气质量数据

    限量: 单次返回所有的数据
    """
    try:
        air_quality_rank = ak.air_quality_rank(
            date=request.date
        )
        air_quality_rank_df = sanitize_data_pandas(air_quality_rank)

        return air_quality_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class AirQualityHist(BaseModel):
    city: str = Field(..., title="指定城市", description="例：定州市，调用 air_city_table 接口获取所有城市列表")
    start_date: str = Field(..., title="开始日期", description="例：20240717，需注意时间跨度不宜过长")
    end_date: str = Field(..., title="结束日期", description="例：20240717，需注意时间跨度不宜过长")


# 另类数据-空气质量-监测点空气质量
@router.post("/air_quality_watch_point", operation_id="post_air_quality_watch_point")
def post_air_quality_watch_point(request: AirQualityHist):
    """
    另类数据-空气质量-监测点空气质量

    接口: air_quality_watch_point

    目标地址: https://www.zq12369.com/environment.php

    描述: 获取每个城市的所有空气质量监测点的数据

    限量: 单次返回指定城市指定日期区间的所有监测点的空气质量数据
    """
    try:
        air_quality_watch_point = ak.air_quality_watch_point(
            city=request.city,
            start_date=request.start_date,
            end_date=request.end_date
        )
        air_quality_watch_point_df = sanitize_data_pandas(air_quality_watch_point)

        return air_quality_watch_point_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
