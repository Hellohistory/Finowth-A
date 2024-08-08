import json

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()

JSON_FILE_PATH_1 = 'Akshare_Data/Others/alternative_data/Json/福布斯中国指标一览表.json'


# 另类数据-财富排行-福布斯中国榜单
@router.get("/forbes_rank_info", operation_id="get_forbes_rank_info")
async def get_forbes_rank_info():
    """
    另类数据-财富排行-福布斯中国榜单一览表

    获取福布斯中国榜单一览表
    """
    try:
        with open(JSON_FILE_PATH_1, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="文件未找到")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 解码错误")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")


class ForbesRank(BaseModel):
    symbol: str = Field(..., title="指定榜单", description="例：2020年福布斯中国400富豪榜，通过 forbes_rank_info 获取")


# 另类数据-财富排行-福布斯中国榜单
@router.post("/forbes_rank", operation_id="post_forbes_rank")
def post_forbes_rank(request: ForbesRank):
    """
    另类数据-财富排行-福布斯中国榜单

    接口: forbes_rank

    目标地址: https://www.forbeschina.com/lists

    描述: 福布斯中国-榜单数据, 一共 87 个指标的数据可以获取

    限量: 单次返回指定榜单的数据

    """
    try:
        forbes_rank = ak.forbes_rank(
            symbol=request.symbol
        )
        forbes_rank_df = sanitize_data_pandas(forbes_rank)

        return forbes_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XincaifuRank(BaseModel):
    year: str = Field(..., title="指定年份", description="例：2020")


# 另类数据-财富排行-新财富富豪榜
@router.post("/xincaifu_rank", operation_id="post_xincaifu_rank")
def post_xincaifu_rank(request: XincaifuRank):
    """
    另类数据-财富排行-新财富富豪榜

    接口: xincaifu_rank

    目标地址: http://www.xcf.cn/zhuanti/ztzz/hdzt1/500frb/index.html

    描述: 新财富 500 富豪榜, 从 2003 年至今

    限量: 单次返回指定年份的富豪榜数据
    """
    try:
        xincaifu_rank = ak.xincaifu_rank(
            year=request.year
        )
        xincaifu_rank_df = sanitize_data_pandas(xincaifu_rank)

        return xincaifu_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XincaifuRank(BaseModel):
    indicator: str = Field(..., title="指定榜单",
                           description="可选值: 胡润百富榜, 胡润全球富豪榜 , 胡润印度榜 , "
                                       "胡润全球独角兽榜, 全球瞪羚企业榜 , "
                                       "胡润Under30s创业领袖榜 , 胡润世界500强 , 胡润艺术榜")
    year: str = Field(..., title="指定年份", description="例：2020，需注意各个榜单的时间，"
                                                         "胡润百富榜: 2014-至今, 胡润全球富豪榜: 2019-至今, "
                                                         "胡润印度榜: 2018-至今, 胡润全球独角兽榜: 2019-至今, "
                                                         "全球瞪羚企业榜: 2021-至今, 胡润Under30s创业领袖榜: 2019-至今, "
                                                         "胡润世界500强: 2020-至今, 胡润艺术榜: 2019-至今")


# 另类数据-财富排行-胡润排行榜
@router.post("/hurun_rank", operation_id="post_hurun_rank")
def post_hurun_rank(request: XincaifuRank):
    """
    另类数据-财富排行-胡润排行榜

    接口: hurun_rank

    目标地址: https://www.hurun.net/zh-CN/Rank/HsRankDetails?num=QWDD234E

    描述: 胡润百富榜单；富豪榜系列，创业系列，500强系列，特色系列

    限量: 单次返回指定榜单和年份的榜单数据
    """
    try:
        hurun_rank = ak.hurun_rank(
            indicator=request.indicator,
            year=request.year
        )
        hurun_rank_df = sanitize_data_pandas(hurun_rank)

        return hurun_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
