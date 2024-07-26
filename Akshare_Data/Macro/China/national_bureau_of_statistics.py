from typing import Literal, Optional

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class MacroChinaNbsNation(BaseModel):
    kind: Literal["月度数据", "季度数据", "年度数据"] = Field(..., title="数据类别",
                                                              description="例：月度数据，季度数据，年度数据")
    path: str = Field(..., title="数据路径",
                      description="例：需与kind参数匹配，具体见官网，多层级之间使用 > 连接 。示例：国民经济核算 > 支出法国内生产总值; 人口 > 总人口;金融业 > 保险系统机构、人员数 "
                                  "> 保险系统机构数")
    period: str = Field(..., title="时间区间", description="例：参考格式如下(英文逗号分割，且不能有多余空格)：月：201201,201205；"
                                                           "季：2012A,2012B,2012C,2012D；年：2012,2013；"
                                                           "至今：2013-；最近：last10")


# 国民经济运行状况-国家统计局-国家统计局全国数据
@router.post("/macro_china_nbs_nation", operation_id="post_macro_china_nbs_nation")
async def post_macro_china_nbs_nation(request: MacroChinaNbsNation):
    """
    国民经济运行状况-国家统计局-国家统计局全国数据

    接口: macro_china_nbs_nation

    目标地址: https://data.stats.gov.cn/easyquery.htm

    描述: 国家统计局全国数据通用接口，包括月度数据、季度数据、年度数据，具体指标见数据官网。

    限量: 根据参数返回指定数据
    """
    try:
        macro_china_nbs_nation = ak.macro_china_nbs_nation(
            kind=request.kind,
            path=request.path,
            period=request.period
        )
        macro_china_nbs_nation_df = sanitize_data_pandas(macro_china_nbs_nation)

        return macro_china_nbs_nation_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class MacroChinaNbsRegion(BaseModel):
    kind: Literal[
        "分省月度数据", "分省季度数据", "分省年度数据", "主要城市月度价格", "主要城市年度数据", "港澳台月度数据", "港澳台年度数据"] = Field(
        ..., title="数据类别",
        description="数据类别，包括：分省月度数据、分省季度数据、分省年度数据、主要城市月度价格、主要城市年度数据、港澳台月度数据、港澳台年度数据。"
    )
    path: str = Field(..., title="数据路径", description="数据路径，需与kind匹配，具体见官网，多层级之间使用 '>' 连接。")
    indicator: Optional[str] = Field(None, title="指定指标",
                                     description="在指定region参数的情况下，此参数可以设置为None，此时将获取指定地区下所有可选指标的值。indicator和region参数不能同时为None。")
    region: Optional[str] = Field(None, title="指定地区", description="指定时表示仅获取当前地区下的数据。")
    period: str = Field(..., title="时间区间",
                        description="时间区间格式如下：月：201201,201205；季：2012A,2012B,2012C,2012D；年：2012,2013；至今：2013-；最近：last10。")


# 国民经济运行状况-国家统计局-国家统计局地区数据接口
@router.post("/macro_china_nbs_region", operation_id="post_macro_china_nbs_region")
async def post_macro_china_nbs_region(request: MacroChinaNbsRegion):
    """
    国民经济运行状况-国家统计局-国家统计局地区数据接口

    接口: macro_china_nbs_region

    目标地址: https://data.stats.gov.cn/easyquery.htm

    描述: 国家统计局地区数据通用接口，包括分省月度数据、分省季度数据、分省年度数据、主要城市月度价格、主要城市年度数据、港澳台月度数据、港澳台年度数据，具体指标见数据官网。

    限量: 根据参数返回指定数据
    """
    try:
        macro_china_nbs_region = ak.macro_china_nbs_region(
            kind=request.kind,
            path=request.path,
            indicator=request.indicator,
            region=request.region,
            period=request.period
        )
        macro_china_nbs_region_df = sanitize_data_pandas(macro_china_nbs_region)

        return macro_china_nbs_region_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
