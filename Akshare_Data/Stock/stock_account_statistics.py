import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import YearRequest, AnalystDetailRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-数据中心-特色数据-股票账户统计
@router.get("/stock_account_statistics_em",
            operation_id="get_stock_account_statistics_em")
def get_stock_account_statistics_em():
    """
    接口: stock_account_statistics_em

    目标地址: https://data.eastmoney.com/cjsj/gpkhsj.html

    描述: 东方财富网-数据中心-特色数据-股票账户统计

    限量: 单次返回从 201504 开始 202308 的所有历史数据

    请求类型: `GET`
    """
    try:
        stock_account_statistics_em_df = ak.stock_account_statistics_em()
        sanitized_data = stock_account_statistics_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-研究报告-东方财富分析师指数
@router.post("/stock_analyst_rank_em",
             operation_id="post_stock_analyst_rank_em")
async def post_stock_analyst_rank_em(request: YearRequest):
    """
    接口: stock_analyst_rank_em

    目标地址: https://data.eastmoney.com/invest/invest/list.html

    描述: 东方财富网-数据中心-研究报告-东方财富分析师指数

    限量: 单次获取指定年份的所有数据

    请求类型: `POST`
    """
    try:
        stock_analyst_rank_em_df = ak.stock_analyst_rank_em(year=request.year)
        return stock_analyst_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-研究报告-东方财富分析师指数-分析师详情
@router.post("/stock_analyst_detail_em",
             operation_id="post_stock_analyst_detail_em")
async def post_stock_analyst_detail_em(request: AnalystDetailRequest):
    """
    接口: stock_analyst_detail_em

    目标地址: https://data.eastmoney.com/invest/invest/11000257131.html

    描述: 东方财富网-数据中心-研究报告-东方财富分析师指数-分析师详情

    限量: 单次获取指定 indicator 指定的数据

    请求类型: `POST`
    """
    try:
        stock_analyst_detail_em_df = ak.stock_analyst_detail_em(analyst_id=request.analyst_id,
                                                                indicator=request.indicator)
        return stock_analyst_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
