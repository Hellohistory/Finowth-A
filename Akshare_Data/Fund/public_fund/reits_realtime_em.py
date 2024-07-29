import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-东方财富-REITs-REITs-行情
@router.get("/reits_realtime_em", operation_id="get_reits_realtime_em")
async def get_reits_realtime_em():
    """
    公募基金数据-东方财富-REITs-REITs-行情

    接口: reits_realtime_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#fund_reits_all

    描述: 东方财富网-行情中心-REITs-沪深 REITs

    限量: 单次返回所有 REITs 的实时行情数据
    """
    try:
        reits_realtime_em = ak.reits_realtime_em()
        reits_realtime_em_df = sanitize_data_pandas(reits_realtime_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return reits_realtime_em_df.to_dict(orient="records")
