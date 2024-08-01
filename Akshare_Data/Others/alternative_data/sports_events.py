import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 另类数据-体育赛事-奥运奖牌
@router.get("/sport_olympic_hist", operation_id="get_sport_olympic_hist")
def get_sport_olympic_hist():
    """
    另类数据-体育赛事-奥运奖牌

    接口: sport_olympic_hist

    目标地址: https://www.kaggle.com/marcogdepinto/let-s-discover-more-about-the-olympic-games

    描述: 奥运会-奖牌数据

    限量: 单次返回 1896-2016 年度的奥运奖牌数据
    """
    try:
        sport_olympic_hist = ak.sport_olympic_hist()
        sport_olympic_hist_df = sanitize_data_pandas(sport_olympic_hist)
        return sport_olympic_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-体育赛事-冬奥会历届奖牌榜
@router.get("/sport_olympic_winter_hist", operation_id="get_sport_olympic_winter_hist")
def get_sport_olympic_winter_hist():
    """
    另类数据-体育赛事-冬奥会历届奖牌榜

    接口: sport_olympic_winter_hist

    目标地址: https://m.sports.qq.com/g/sv3/winter-oly22/winter-olympic-rank.htm?type=0

    描述: 腾讯运动-冬奥会-历届奖牌榜

    限量: 单次返回 1924-2018 年度的冬奥会历届奖牌榜数据
    """
    try:
        sport_olympic_winter_hist = ak.sport_olympic_winter_hist()
        sport_olympic_winter_hist_df = sanitize_data_pandas(sport_olympic_winter_hist)
        return sport_olympic_winter_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
