import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富-行情中心-盘口异动数据
@router.post("/stock_changes_em", operation_id="post_stock_changes_em")
async def post_stock_changes_em(request: SymbolRequest):
    """
    描述: 东方财富-行情中心-盘口异动数据
    限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间
    """
    try:

        stock_changes_em_df = ak.stock_changes_em(symbol=request.symbol)

        stock_changes_em_df = sanitize_data(stock_changes_em_df)

        return stock_changes_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_board_change_em", operation_id="get_stock_hsgt_fund_flow_summary_em")
def get_stock_hsgt_fund_flow_summary_em():
    """
    描述: 东方财富-行情中心-当日板块异动详情
    限量: 返回最近交易日的数据
    """
    try:
        stock_board_change_em_df = ak.stock_hsgt_fund_flow_summary_em()
        data = stock_board_change_em_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
