import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 另类数据-视频播映-电视剧集
@router.get("/video_tv", operation_id="get_video_tv")
def get_video_tv():
    """
    另类数据-视频播映-电视剧集

    接口: video_tv

    目标地址: https://www.endata.com.cn/Video/index.html

    描述: 艺恩-视频放映-电视剧集

    限量: 返回前一日的电视剧播映数据
    """
    try:
        video_tv = ak.video_tv()
        video_tv_df = sanitize_data_pandas(video_tv)
        return video_tv_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-视频播映-综艺节目
@router.get("/video_variety_show", operation_id="get_video_variety_show")
def get_video_variety_show():
    """
    另类数据-视频播映-综艺节目

    接口: video_variety_show

    目标地址: https://www.endata.com.cn/Video/index.html

    描述: 艺恩-视频放映-综艺节目

    限量: 返回前一日的综艺播映数据
    """
    try:
        video_variety_show = ak.video_variety_show()
        video_variety_show_df = sanitize_data_pandas(video_variety_show)
        return video_variety_show_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
