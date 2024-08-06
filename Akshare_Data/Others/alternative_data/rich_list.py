import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FortuneRank(BaseModel):
    year: str = Field(..., title="指定年份", description="例：2023")


# 另类数据-财富排行榜-中文
@router.post("/fortune_rank", operation_id="post_fortune_rank")
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
