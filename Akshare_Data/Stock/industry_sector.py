import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


@router.get("/stock_board_industry_name_em", operation_id="get_stock_board_industry_name_em")
def get_stock_board_industry_name_em():
    """
    东方财富-沪深京板块-行业板块

    接口: stock_board_industry_name_em

    目标地址: https://quote.eastmoney.com/center/boardlist.html#industry_board

    描述: 东方财富-沪深京板块-行业板块

    限量: 单次返回当前时刻所有行业板块数据
    """
    try:
        stock_board_industry_name_em_df = ak.stock_board_industry_name_em()
        return stock_board_industry_name_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_board_industry_summary_ths", operation_id="get_stock_board_industry_summary_ths")
def get_stock_board_industry_summary_ths():
    """
    同花顺-同花顺行业一览表

    接口: stock_board_industry_summary_ths

    目标地址: https://q.10jqka.com.cn/thshy/

    描述: 同花顺-同花顺行业一览表

    限量: 单次返回当前时刻同花顺行业一览表
    """
    try:
        stock_board_industry_summary_ths_df = ak.stock_board_industry_summary_ths()
        return stock_board_industry_summary_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndustryIndexRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：元件，可以通过调用stock_board_industry_name_ths查看同花顺的所有行业名称")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# 同花顺-板块-行业板块-指数日频率数据
@router.post("/stock_board_industry_index_ths", operation_id="post_stock_board_industry_index_ths")
async def post_stock_board_industry_index_ths(request: IndustryIndexRequest):
    """
    同花顺-行业板块-指数日频率数据

    接口: stock_board_industry_index_ths

    目标地址: https://q.10jqka.com.cn/thshy/detail/code/881270/

    描述: 同花顺-板块-行业板块-指数日频率数据

    限量: 单次返回所有日频指数数据
    """
    try:
        stock_board_industry_index_ths_df = ak.stock_board_industry_index_ths(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )
        return stock_board_industry_index_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：小金属，可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有概念名称")


# 东方财富-沪深板块-行业板块-板块成份
@router.post("/stock_board_industry_cons_em", operation_id="post_stock_board_industry_cons_em")
async def post_stock_board_industry_cons_em(request: SymbolRequest):
    """
    东方财富-沪深板块-行业板块-板块成份

    接口: stock_board_industry_cons_em

    目标地址: https://data.eastmoney.com/bkzj/BK1027.html

    描述: 东方财富-沪深板块-行业板块-板块成份

    限量: 单次返回指定概念板块的所有成份股
    """
    try:
        stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol=request.symbol)
        return stock_board_industry_cons_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndustryHistRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：小金属，可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有概念名称")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")
    period: str = Field(..., title="时间周期", description="可选择'日k', '周k', '月k'")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据")


# 东方财富-沪深板块-行业板块-历史行情数据
@router.post("/stock_board_industry_hist_em", operation_id="post_stock_board_industry_hist_em")
async def post_stock_board_industry_hist_em(request: IndustryHistRequest):
    """
    东方财富-沪深板块-行业板块-历史行情数据

    接口: stock_board_industry_hist_em

    目标地址: https://quote.eastmoney.com/bk/90.BK1027.html

    描述: 东方财富-沪深板块-行业板块-历史行情数据

    限量: 单次返回指定个股和指定复权类型的所有历史数据
    """
    try:
        stock_board_industry_hist_em_df = ak.stock_board_industry_hist_em(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            period=request.period,
            adjust=request.adjust
        )
        return stock_board_industry_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndustryHistMinRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：小金属，可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有概念名称")
    period: str = Field(..., title="时间周期",
                        description="可选择1分钟:'1',5分钟:'5',15分钟:'15',30分钟:'30',60分钟:'60'")


# 东方财富-沪深板块-行业板块-分时历史行情数据
@router.post("/stock_board_industry_hist_min_em", operation_id="post_stock_board_industry_hist_min_em")
async def post_stock_board_industry_hist_min_em(request: IndustryHistMinRequest):
    """
    东方财富-沪深板块-行业板块-分时历史行情数据

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
