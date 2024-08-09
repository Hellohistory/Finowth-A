import akshare as ak
from fastapi import HTTPException, APIRouter

router = APIRouter()


# 工具箱-新浪财经-交易日历
@router.get("/tool_trade_date_hist_sina", operation_id="tool_trade_date_hist_sina")
def tool_trade_date_hist_sina():
    """
    工具箱-新浪财经-交易日历

    接口: tool_trade_date_hist_sina

    目标地址: https://finance.sina.com.cn

    描述: 新浪财经-股票交易日历数据

    限量: 单次返回从 1990-12-19 到 2024-12-31 之间的股票交易日历数据, 这里补充 1992-05-04 进入交易日
    """
    try:
        tool_trade_date_hist_sina = ak.tool_trade_date_hist_sina()
        columns_mapping = {
            "trade_date": "交易日"
        }
        tool_trade_date_hist_sina.rename(columns=columns_mapping, inplace=True)
        return tool_trade_date_hist_sina.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
