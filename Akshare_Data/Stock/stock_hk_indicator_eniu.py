import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymolIndicatorRequest

router = APIRouter()


@router.post("/stock_hk_indicator_eniu", operation_id="post_stock_hk_indicator_eniu")
async def post_stock_hk_indicator_eniu(request: SymolIndicatorRequest):
    """
    P.S. 该数据源暂未更新数据

    接口: stock_hk_indicator_eniu

    目标地址: https://eniu.com/gu/hk01093/roe

    描述: 亿牛网-港股个股指标: 市盈率, 市净率, 股息率, ROE, 市值

    限量: 单次获取指定个股和指定时间段的所有历史数据
    """
    try:
        stock_hk_indicator_eniu_df = ak.stock_hk_indicator_eniu(symbol=request.symbol, indicator=request.indicator)
        return stock_hk_indicator_eniu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
