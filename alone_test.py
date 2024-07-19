import logging
import akshare as ak
from fastapi import HTTPException, FastAPI
from pydantic import BaseModel

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建 FastAPI 应用实例
app = FastAPI()


class StockDailyRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    adjust: str


@app.post("/stock_zh_b_daily")
def get_stock_zh_b_daily(request: StockDailyRequest):
    """
    描述: B 股数据是从新浪财经获取的数据, 历史数据按日频率更新
    限量: 单次返回指定 B 股上市公司指定日期间的历史行情日频率数据
    """
    try:
        logger.info("Received request: %s", request.json())
        stock_zh_b_daily_df = ak.stock_zh_b_daily(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        logger.info("Successfully fetched data from akshare")
        return stock_zh_b_daily_df.to_dict(orient="records")
    except Exception as e:
        logger.error("Error fetching data: %s", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=36925, log_level="info")
