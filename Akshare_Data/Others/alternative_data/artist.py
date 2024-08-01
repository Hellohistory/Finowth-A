import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 另类数据-艺人-艺人商业价值
@router.get("/business_value_artist", operation_id="get_business_value_artist")
def get_business_value_artist():
    """
    另类数据-艺人-艺人商业价值

    接口: business_value_artist

    目标地址: https://www.endata.com.cn/Marketing/Artist/business.html

    描述: 艺恩-艺人-艺人商业价值

    限量: 返回当前的艺人商业价值数据
    """
    try:
        business_value_artist = ak.business_value_artist()
        business_value_artist_df = sanitize_data_pandas(business_value_artist)
        return business_value_artist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-艺人-艺人流量价值
@router.get("/online_value_artist", operation_id="get_online_value_artist")
def get_online_value_artist():
    """
    另类数据-艺人-艺人流量价值

    接口: online_value_artist

    目标地址: https://www.endata.com.cn/Marketing/Artist/business.html

    描述: 艺恩-艺人-艺人流量价值

    限量: 返回当前的艺人流量价值数据
    """
    try:
        online_value_artist = ak.online_value_artist()
        online_value_artist_df = sanitize_data_pandas(online_value_artist)
        return online_value_artist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
