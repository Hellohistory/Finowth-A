import logging

import akshare as ak
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DongCaiMarketDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="市场类型", description="'北向持股', '沪股通持股', '深股通持股', '南向持股'")
    start_date: str = Field(..., title="起始时间(需近期交易日)", description="例：20240701")
    end_date: str = Field(..., title="终止时间(需近期交易日)", description="例：20240701")


# 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行
@app.post("/stock_hsgt_institution_statistics_em", operation_id="post_stock_hsgt_institution_statistics_em")
async def post_stock_hsgt_institution_statistics_em(request: DongCaiMarketDateRangeRequest):
    """
    接口: stock_hsgt_institution_statistics_em

    目标地址: http://data.eastmoney.com/hsgtcg/InstitutionStatistics.aspx

    描述: 东方财富网-数据中心-沪深港通-沪深港通持股-机构排行

    限量: 单次获取指定市场的所有数据, 该接口只能获取近期的数据
    """
    logger.info(f"Received request: {request}")
    try:
        stock_hsgt_institution_statistics_em_df = ak.stock_hsgt_institution_statistics_em(
            market=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )

        if stock_hsgt_institution_statistics_em_df is None or stock_hsgt_institution_statistics_em_df.empty:
            logger.error("Received empty dataframe")
            raise HTTPException(status_code=404, detail="未找到相关数据")

        logger.info("Data retrieved successfully")
        return stock_hsgt_institution_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=36925, log_level="info")
