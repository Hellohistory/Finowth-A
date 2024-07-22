import akshare as ak
from fastapi import FastAPI, HTTPException

app = FastAPI()


# B 股行情数据-新浪财经-实时行情数据
@app.get("/stock_zh_b_spot", operation_id="get_stock_zh_b_spot")
def get_stock_zh_b_spot():
    """
    接口: stock_zh_b_spot

    目标地址: http://vip.stock.finance.sina.com.cn/mkt/#hs_b

    描述: B 股数据是从新浪财经获取的数据, 重复运行本函数会被新浪暂时封 IP, 建议增加时间间隔

    限量: 单次返回所有 B 股上市公司的实时行情数据
    """
    try:
        stock_zh_b_spot_df = ak.stock_zh_b_spot()
        return stock_zh_b_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 运行 FastAPI 应用
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=36925, log_level="info")
