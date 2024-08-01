import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 另类数据-视频播映-电视剧集
@router.get("/stock_js_weibo_nlp_time", operation_id="get_stock_js_weibo_nlp_time")
def get_stock_js_weibo_nlp_time():
    """
    另类数据-微博股票舆情报告

    接口: stock_js_weibo_nlp_time
    """
    try:
        stock_js_weibo_nlp_time = ak.stock_js_weibo_nlp_time()
        stock_js_weibo_nlp_time_df = sanitize_data_pandas(stock_js_weibo_nlp_time)
        return stock_js_weibo_nlp_time_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockWeiboReport(BaseModel):
    time_period: str = Field(..., title="时间周期",
                             description="详见time_period参数一览表, 可通过调用 stock_js_weibo_nlp_time 获取")


# 另类数据-微博股票舆情报告
@router.post("/stock_js_weibo_report", operation_id="post_stock_js_weibo_report")
def post_stock_js_weibo_report(request: StockWeiboReport):
    """
    另类数据-微博股票舆情报告

    接口: stock_js_weibo_report

    目标地址: https://datacenter.jin10.com/market

    描述: 微博舆情报告中近期受关注的股票

    限量: 单次返回指定时间内微博舆情报告中近期受关注的股票

    time_period参数一览表:
    参数: CNHOUR2; 说明: 2小时
    参数: CNHOUR6; 说明: 6小时
    参数: CNHOUR12; 说明: 12小时
    参数: CNHOUR24; 说明: 1天
    参数: CNDAY7; 说明: 1周
    参数: CNDAY30; 说明: 1月
    """
    try:
        stock_js_weibo_report = ak.stock_js_weibo_report(
            time_period=request.time_period
        )
        stock_js_weibo_report_df = sanitize_data_pandas(stock_js_weibo_report)

        return stock_js_weibo_report_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
