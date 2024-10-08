import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 新浪财经-科创板股票实时行情数据
@router.get("/stock_zh_kcb_spot", operation_id="stock_zh_kcb_spot")
async def stock_zh_kcb_spot():
    """
    新浪财经-科创板股票实时行情数据

    接口: stock_zh_kcb_spot

    目标地址: http://vip.stock.finance.sina.com.cn/mkt/#kcb

    描述: 新浪财经-科创板股票实时行情数据

    限量: 单次返回所有科创板上市公司的实时行情数据; 请控制采集的频率, 大量抓取容易封IP
    """
    try:
        stock_zh_kcb_spot = ak.stock_zh_kcb_spot()
        stock_zh_kcb_spot_df = sanitize_data_pandas(stock_zh_kcb_spot)
        return stock_zh_kcb_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockDailyRequest(BaseModel):
    symbol: str = Field(..., title="指定个股(需带市场标识)", description="例：sh688008")
    adjust: str = Field(..., title="复权类型", description="默认为空: 返回不复权的数据;"
                                                           "qfq: 返回前复权后的数据; "
                                                           "hfq: 返回后复权后的数据; "
                                                           "hfq-factor: 返回后复权因子; "
                                                           "hfq-factor: 返回前复权因子")


# 新浪财经-科创板股票历史行情数据
@router.post("/stock_zh_kcb_daily", operation_id="stock_zh_kcb_daily")
async def stock_zh_kcb_daily(request: StockDailyRequest):
    """
    新浪财经-科创板股票历史行情数据

    接口: stock_zh_kcb_daily

    目标地址: https://finance.sina.com.cn/realstock/company/sh688001/nc.shtml (示例)

    描述: 新浪财经-科创板股票历史行情数据

    限量: 单次返回指定个股和 adjust 的所有历史行情数据; 请控制采集的频率, 大量抓取容易封IP

    补充描述：API返回的“公告代码”一项可以用来获取公告详情: http://data.eastmoney.com/notices/detail/688595/{替换到此处}.html
    """
    try:
        stock_zh_kcb_daily = ak.stock_zh_kcb_daily(symbol=request.symbol, adjust=request.adjust)

        stock_zh_kcb_daily.rename(columns={
            "date": "日期",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "close": "收盘价",
            "volume": "成交量",
            "after_volume": "盘后成交量",
            "after_amount": "盘后成交金额",
            "outstanding_share": "流通股本",
            "turnover": "换手率"
        }, inplace=True)

        stock_zh_kcb_daily_df = sanitize_data_pandas(stock_zh_kcb_daily)
        return stock_zh_kcb_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockReportRequest(BaseModel):
    from_page: int = Field(..., title="开始获取的页码", description="例：1")
    to_page: int = Field(..., title="结束获取的页码", description="例：100")


# 东方财富-科创板报告数据
@router.post("/stock_zh_kcb_report_em", operation_id="stock_zh_kcb_report_em")
async def stock_zh_kcb_report_em(request: StockReportRequest):
    """
    有概率能获取，有概率无法获取，需排查问题

    东方财富-科创板报告数据

    接口: stock_zh_kcb_report_em

    目标地址: https://data.eastmoney.com/notices/kcb.html

    描述: 东方财富-科创板报告数据

    限量: 单次返回所有科创板上市公司的报告数据
    """
    try:
        stock_zh_kcb_report_em = ak.stock_zh_kcb_report_em(
            from_page=request.from_page,
            to_page=request.to_page
        )
        stock_zh_kcb_report_em_df = sanitize_data_pandas(stock_zh_kcb_report_em)
        return stock_zh_kcb_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
