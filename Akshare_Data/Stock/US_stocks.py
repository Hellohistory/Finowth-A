import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 东方财富-美股-实时行情
@router.get("/stock_us_spot_em", operation_id="get_stock_us_spot_em")
def get_stock_us_spot_em():
    """
    东方财富-美股-实时行情

    接口: stock_us_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#us_stocks

    描述: 东方财富-美股-实时行情

    限量: 单次返回美股所有上市公司的实时行情数据
    """
    try:
        stock_us_spot_em = ak.stock_us_spot_em()
        stock_us_spot_em_df = sanitize_data_pandas(stock_us_spot_em)
        return stock_us_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-美股-实时行情
@router.get("/stock_us_spot", operation_id="get_stock_us_spot")
def get_stock_us_spot():
    """
    新浪财经-美股-实时行情

    接口: stock_us_spot

    目标地址: https://finance.sina.com.cn/stock/usstock/sector.shtml

    描述: 新浪财经-美股; 获取的数据有 15 分钟延迟; 建议使用 stock_us_spot_em 端口来获取数据

    限量: 单次返回美股所有上市公司的实时行情数据，需要注意该端口数据量较大，获取时间较长，需要耐心等待
    """
    try:
        us_stock_current = ak.stock_us_spot()
        columns_mapping = {
            "name": "公司名称",
            "cname": "中文名称",
            "category": "行业类别",
            "symbol": "股票代码",
            "price": "当前价格",
            "diff": "价格变动",
            "chg": "涨跌幅",
            "preclose": "前收盘价",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "amplitude": "振幅",
            "volume": "成交量",
            "mktcap": "市值",
            "pe": "市盈率",
            "market": "市场",
            "category_id": "行业类别ID"
        }
        us_stock_current.rename(columns=columns_mapping, inplace=True)

        stock_hk_hot_rank_latest_em_df = sanitize_data_pandas(us_stock_current)
        return stock_hk_hot_rank_latest_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class UStockDayHistoryRequest(BaseModel):
    symbol: str = Field(..., title="美股代码(可请求stock_us_spot_em获取)",
                        description="例：106.TTE")
    period: str = Field(..., title="时间周期",
                        description="例：daily; 所有可选参数为：daily(日), weekly(周), monthly(月)")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据")


# 东方财富-美股-每日行情
@router.post("/stock_us_hist", operation_id="post_stock_us_hist")
async def post_stock_us_hist(request: UStockDayHistoryRequest):
    """
    东方财富-美股-每日行情

    接口: stock_us_hist

    目标地址: https://quote.eastmoney.com/us/ENTX.html#fullScreenChart

    描述: 东方财富-行情-美股-每日行情

    限量: 单次返回指定上市公司的指定复权类型的所有历史行情数据
    """
    try:
        stock_us_hist = ak.stock_us_hist(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        stock_us_hist_df = sanitize_data_pandas(stock_us_hist)
        return stock_us_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiUDayMinRequest(BaseModel):
    symbol: str = Field(..., title="美股代码(可请求stock_us_spot_em获取)",
                        description="例：106.TTE")
    start_date: str = Field(..., title="起始日期时间",
                            description="例2024-07-01 09:32:00，不填写则默认返回所有数据")
    end_date: str = Field(..., title="终止日期时间",
                          description="例2024-07-15 09:32:00，不填写则默认返回所有数据")


# 东方财富-美股-每日分时行情
@router.post("/stock_us_hist_min_em", operation_id="post_stock_us_hist_min_em")
async def post_stock_us_hist_min_em(request: DongCaiUDayMinRequest):
    """
    东方财富-美股-每日分时行情

    接口: stock_us_hist_min_em

    目标地址: https://quote.eastmoney.com/us/ATER.html

    描述: 东方财富-行情首页-美股-每日分时行情

    限量: 单次返回指定上市公司最近 5 个交易日分钟数据, 注意美股数据更新有延时
    """
    try:
        stock_us_hist_min_em = ak.stock_us_hist_min_em(symbol=request.symbol)
        stock_us_hist_min_em_df = sanitize_data_pandas(stock_us_hist_min_em)
        return stock_us_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangUStockHistoryRequest(BaseModel):
    symbol: str = Field(..., title="指定美股代码(可请求stock_us_spot_em获取)",
                        description="例：106.TTE")
    adjust: str = Field(..., title="复权类型",
                        description="默认为空则返回未复权的数据;qfq: 返回前复权后的数据;qfq-factor: 返回前复权因子")


# 新浪财经-美股-历史行情
@router.post("/stock_us_daily", operation_id="post_stock_us_daily")
async def post_stock_us_daily(request: XinLangUStockHistoryRequest):
    """
    新浪财经-美股-历史行情

    出现500错误待修复

    接口: stock_us_daily

    目标地址: http://finance.sina.com.cn/stock/usstock/sector.shtml

    描述: 美股历史行情数据，设定 adjust="qfq" 则返回前复权后的数据，默认 adjust="", 则返回未复权的数据，历史数据按日频率更新

    限量: 单次返回指定上市公司的指定复权类型后的所有历史行情数据
    """
    try:
        stock_us_daily = ak.stock_us_daily(symbol=request.symbol, adjust=request.adjust)

        stock_us_daily.rename(columns={
            "date": "时间",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "close": "收盘价",
            "volume": "成交量",
            "qfq_factor": "前复权因子",
            "adjust": "调整因子"
        }, inplace=True)

        stock_us_daily_df = sanitize_data_pandas(stock_us_daily)
        return stock_us_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美股粉单市场的实时行情数据
@router.get("/stock_us_pink_spot_em", operation_id="get_stock_us_pink_spot_em")
def get_stock_us_pink_spot_em():
    """
    东方财富-美股粉单市场-实时行情数据

    接口: stock_us_pink_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#us_pinksheet

    描述: 美股粉单市场的实时行情数据

    限量: 单次返回指定所有粉单市场的行情数据
    """
    try:
        stock_us_pink_spot_em = ak.stock_us_pink_spot_em()
        stock_us_pink_spot_em_df = sanitize_data_pandas(stock_us_pink_spot_em)
        return stock_us_pink_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class USFamouSpot(BaseModel):
    symbol: str = Field(..., title="指定种类知名美股",
                        description="可从'科技类', '金融类', '医药食品类', '媒体类', '汽车能源类', '制造零售类'选择请求")


# 东方财富-美股-知名美股-实时行情数据
@router.post("/stock_us_famous_spot_em", operation_id="post_stock_us_famous_spot_em")
async def post_stock_us_famous_spot_em(request: USFamouSpot):
    """
    东方财富-美股-知名美股-实时行情数据

    接口: stock_us_famous_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#us_wellknown

    描述: 东方财富-美股-知名美股-实时行情数据

    限量: 单次返回指定个股的行情数据
    """
    try:
        stock_us_famous_spot_em = ak.stock_us_famous_spot_em(symbol=request.symbol)

        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_us_famous_spot_em)

        return stock_us_famous_spot_em_df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-行情中心-港股市场-知名港股-实时行情数据
@router.get("/stock_hk_famous_spot_em", operation_id="get_stock_hk_famous_spot_em")
def get_stock_hk_famous_spot_em():
    """
    东方财富-行情中心-港股市场-知名港股-实时行情数据

    接口: stock_hk_famous_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_wellknown

    描述: 东方财富-行情中心-港股市场-知名港股-实时行情数据

    限量: 单次返回全部行情数据
    """
    try:
        stock_hk_famous_spot_em = ak.stock_hk_famous_spot_em()
        stock_hk_famous_spot_em_df = sanitize_data_pandas(stock_hk_famous_spot_em)
        return stock_hk_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
