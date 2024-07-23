import akshare as ak
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


# B 股行情数据-新浪财经-实时行情数据
class IndustryHistMinRequest(BaseModel):
    symbol: str = Field(..., title="板块类型",
                        description="可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有概念代码")
    period: str = Field(..., title="时间周期",
                        description="可选择1分钟:'1',5分钟:'5',15分钟:'15',30分钟:'30',60分钟:'60'")


# 东方财富-沪深板块-行业板块-分时历史行情数据
@app.post("/stock_board_industry_hist_min_em", operation_id="post_stock_board_industry_hist_min_em")
async def post_stock_board_industry_hist_min_em(request: IndustryHistMinRequest):
    """
    接口: stock_board_industry_hist_min_em

    目标地址: http://quote.eastmoney.com/bk/90.BK1027.html

    描述: 东方财富-沪深板块-行业板块-分时历史行情数据

    限量: 单次返回指定个股和 period 的所有历史数据
    """
    try:
        stock_board_industry_hist_min_em_df = ak.stock_board_industry_hist_min_em(
            symbol=request.symbol,
            period=request.period
        )
        return stock_board_industry_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=36925, log_level="info")
