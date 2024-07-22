import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="异动类型",
                        description="可选择'火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', "
                                    "'有大买盘', '竞价上涨', '高开5日线', '向上缺口', '60日新高', '60日大幅上涨', "
                                    "'加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘', "
                                    "'竞价下跌', '低开5日线', '向下缺口', '60日新低', '60日大幅下跌'")


# 东方财富-行情中心-盘口异动数据
@router.post("/stock_changes_em", operation_id="post_stock_changes_em")
async def post_stock_changes_em(request: SymbolRequest):
    """
    接口: stock_changes_em

    目标地址: http://quote.eastmoney.com/changes/

    描述: 东方财富-行情中心-盘口异动数据

    限量: 单次指定个股的最近交易日的盘口异动数据
    """
    try:

        stock_changes_em_df = ak.stock_changes_em(symbol=request.symbol)

        stock_changes_em_df = sanitize_data(stock_changes_em_df)

        return stock_changes_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_board_change_em", operation_id="get_stock_board_change_em")
def get_stock_board_change_em():
    """
    接口: stock_board_change_em

    目标地址: https://quote.eastmoney.com/changes/

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
