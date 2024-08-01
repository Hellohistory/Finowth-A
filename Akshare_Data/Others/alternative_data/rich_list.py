import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FortuneRank(BaseModel):
    year: str = Field(..., title="指定年份", description="例：2023")


# 另类数据-财富排行榜-中文
@router.post("/fortune_rank",
             operation_id="post_fortune_rank")
def post_fortune_rank(request: FortuneRank):
    """
    另类数据-财富排行榜-中文

    接口: fortune_rank

    目标地址: https://www.fortunechina.com/fortune500/node_65.htm

    描述: 指定年份财富世界 500 强公司排行榜

    限量: 单次返回某一个年份的所有历史数据

    """
    try:
        fortune_rank = ak.fortune_rank(
            year=request.year
        )
        fortune_rank_df = sanitize_data_pandas(fortune_rank)

        return fortune_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-财富排行榜-英文
@router.post("/fortune_rank_eng",
             operation_id="post_fortune_rank_eng")
def post_fortune_rank_eng(request: FortuneRank):
    """
    另类数据-财富排行榜-英文

    接口: fortune_rank_eng

    目标地址: https://fortune.com/global500/

    描述: 指定年份财富世界 500 强公司排行榜-英文版本, 从 1995 年开始, 数据和格式较中文版本完整

    限量: 单次返回某一个年份的所有历史数据, 早期数据可能不足 500 家公司

    """
    try:
        fortune_rank_eng = ak.fortune_rank_eng(
            year=request.year
        )
        fortune_rank_eng_df = sanitize_data_pandas(fortune_rank_eng)

        return fortune_rank_eng_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ForbesRank(BaseModel):
    symbol: str = Field(..., title="指定年份", description="例：2023")


# 另类数据-财富排行榜-中文
@router.post("/forbes_rank",
             operation_id="post_fortune_rank")
def post_fortune_rank(request: ForbesRank):
    """
    另类数据-财富排行榜-中文

    接口: fortune_rank

    目标地址: https://www.fortunechina.com/fortune500/node_65.htm

    描述: 指定年份财富世界 500 强公司排行榜

    限量: 单次返回某一个年份的所有历史数据

    """
    try:
        fortune_rank = ak.fortune_rank(
            year=request.year
        )
        fortune_rank_df = sanitize_data_pandas(fortune_rank)

        return fortune_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
