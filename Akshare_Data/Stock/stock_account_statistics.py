import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 东方财富-数据中心-特色数据-股票账户统计
@router.get("/stock_account_statistics_em",
            operation_id="get_stock_account_statistics_em")
def get_stock_account_statistics_em():
    """
    东方财富-特色数据-股票账户统计

    接口: stock_account_statistics_em

    目标地址: https://data.eastmoney.com/cjsj/gpkhsj.html

    描述: 东方财富-数据中心-特色数据-股票账户统计

    限量: 单次返回从 201504 开始 202308 的所有历史数据
    """
    try:
        stock_account_statistics_em = ak.stock_account_statistics_em()
        stock_account_statistics_em_df = sanitize_data_pandas(stock_account_statistics_em)
        return stock_account_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class YearRequest(BaseModel):
    year: str = Field(..., title="指定年份", description="例：2022，数据从 2013 年至今")


# 东方财富-数据中心-研究报告-东方财富分析师指数
@router.post("/stock_analyst_rank_em",
             operation_id="post_stock_analyst_rank_em")
async def post_stock_analyst_rank_em(request: YearRequest):
    """
    东方财富-研究报告-东方财富分析师指数

    接口: stock_analyst_rank_em

    目标地址: https://data.eastmoney.com/invest/invest/list.html

    描述: 东方财富-数据中心-研究报告-东方财富分析师指数

    限量: 单次获取指定年份的所有数据
    """
    try:
        stock_analyst_rank_em = ak.stock_analyst_rank_em(year=request.year)
        stock_analyst_rank_em_df = sanitize_data_pandas(stock_analyst_rank_em)
        return stock_analyst_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class AnalystDetailRequest(BaseModel):
    analyst_id: str = Field(..., title="分析师ID(从stock_analyst_rank_em获取)",
                            description="例：11000257131")
    indicator: str = Field(..., title="报告类型",
                           description="从'最新跟踪成分股', '历史跟踪成分股', '历史指数'当中选择")


# 东方财富-数据中心-研究报告-东方财富分析师指数-分析师详情
@router.post("/stock_analyst_detail_em",
             operation_id="post_stock_analyst_detail_em")
async def post_stock_analyst_detail_em(request: AnalystDetailRequest):
    """
    东方财富-研究报告-东方财富分析师指数-分析师详情

    接口: stock_analyst_detail_em

    目标地址: https://data.eastmoney.com/invest/invest/11000257131.html

    描述: 东方财富-数据中心-研究报告-东方财富分析师指数-分析师详情

    限量: 单次获取指定 indicator 指定的数据
    """
    try:
        stock_analyst_detail_em = ak.stock_analyst_detail_em(analyst_id=request.analyst_id,
                                                                indicator=request.indicator)
        stock_analyst_detail_em_df = sanitize_data_pandas(stock_analyst_detail_em)
        return stock_analyst_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
