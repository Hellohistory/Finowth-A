import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-港股-实时行情
@router.get("/stock_hk_spot_em", operation_id="get_stock_hk_spot_em")
def get_stock_hk_spot_em():
    """
    接口: stock_hk_spot_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#hk_stocks

    描述: 所有港股的实时行情数据; 该数据有 15 分钟延时

    限量: 单次返回最近交易日的所有港股的数据
    """
    try:
        stock_hk_spot_em_df = ak.stock_hk_spot_em()
        sanitized_data = stock_hk_spot_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 港股主板实时行情数据-东财
@router.get("/stock_hk_main_board_spot_em", operation_id="get_stock_hk_main_board_spot_em")
def get_stock_hk_main_board_spot_em():
    """
    接口: stock_hk_main_board_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_mainboard

    描述: 港股主板的实时行情数据; 该数据有 15 分钟延时

    限量: 单次返回港股主板的数据
    """
    try:
        stock_hk_main_board_spot_em_df = ak.stock_hk_main_board_spot_em()
        sanitized_data = stock_hk_main_board_spot_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hk_spot", operation_id="get_stock_hk_spot")
def get_stock_hk_spot():
    """
    港股-实时行情数据是从新浪财经获取的数据, 更新频率为实时, 由于新浪服务器因素行情延时 15 分钟

    接口: stock_hk_spot

    目标地址: http://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk

    描述: 获取所有港股的实时行情数据 15 分钟延时

    限量: 单次返回当前时间戳的所有港股的数据
    """
    try:
        stock_hk_spot_df = ak.stock_hk_spot()
        stock_hk_spot_list = stock_hk_spot_df.to_dict(orient="records")

        # 将字段名转换为中文
        translated_list = []
        for item in stock_hk_spot_list:
            translated_item = {
                "股票代码": item.get("symbol"),
                "股票名称": item.get("name"),
                "英文名称": item.get("engname"),
                "交易类型": item.get("tradetype"),
                "最新成交价": item.get("lasttrade"),
                "前收盘价": item.get("prevclose"),
                "开盘价": item.get("open"),
                "最高价": item.get("high"),
                "最低价": item.get("low"),
                "成交量": item.get("volume"),
                "成交额": item.get("amount"),
                "时间戳": item.get("ticktime"),
                "买入价": item.get("buy"),
                "卖出价": item.get("sell"),
                "价格变动": item.get("pricechange"),
                "涨跌幅": item.get("changepercent")
            }
            translated_list.append(translated_item)

        return translated_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiHKStockMinuteRequest(BaseModel):
    symbol: str = Field(..., title="指定港股代码(可通过stock_hk_spot_em获取)",
                        description="例：01611")
    period: str = Field(..., title="时间周期",
                        description="可选择'1', '5', '15', '30', '60'; 其中 1 分钟数据返回近 5 个交易日数据且不复权")
    adjust: str = Field(..., title="复权形式",
                        description="可选择为空返回不复权信息,'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权")
    start_date: str = Field(..., title="开始时间", description="例：2024-07-01 09:32:00，默认返回所有数据")
    end_date: str = Field(..., title="结束时间", description="2024-07-15 09:32:00，默认返回所有数据")


# 东方财富网-港股-每日分时行情
@router.post("/stock_hk_hist_min_em", operation_id="post_stock_zh_ah_spot")
async def post_stock_hk_hist_min_em(request: DongCaiHKStockMinuteRequest):
    """
    接口: stock_hk_hist_min_em

    目标地址: http://quote.eastmoney.com/hk/00948.html

    描述: 东方财富网-行情首页-港股-每日分时行情

    限量: 单次返回指定上市公司最近 5 个交易日分钟数据, 注意港股有延时
    """
    try:
        stock_hk_hist_min_em_df = ak.stock_hk_hist_min_em(
            symbol=request.symbol,
            period=request.period,
            adjust=request.adjust,
            start_date=request.start_date,
            end_date=request.end_date
        )
        return stock_hk_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiHKStockHistoryRequest(BaseModel):
    symbol: str = Field(..., title="指定港股代码(可通过stock_hk_spot_em获取)",
                        description="例：01611")
    period: str = Field(..., title="时间周期",
                        description="例如daily; 所有可选参数为：daily(日), weekly(周), monthly(月)")
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")
    adjust: str = Field(..., title="复权形式",
                        description="默认返回不复权的数据，即此参数为空; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据")


# 东方财富网-港股-历史行情数据
@router.post("/stock_hk_hist", operation_id="post_stock_hk_hist")
async def post_stock_hk_hist(request: DongCaiHKStockHistoryRequest):
    """
    接口: stock_hk_hist

    目标地址: https://quote.eastmoney.com/hk/08367.html

    描述: 港股-历史行情数据, 可以选择返回复权后数据, 更新频率为日频

    限量: 单次返回指定上市公司的历史行情数据
    """
    try:
        stock_hk_hist_df = ak.stock_hk_hist(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_hk_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockDailyRequest(BaseModel):
    symbol: str = Field(..., title="指定港股代码(可通过stock_hk_spot_em获取)", description="例如01611")
    adjust: str = Field(..., title="复权类型", description="默认返回不复权的数据，即此参数为空;"
                                                           "qfq: 返回前复权后的数据; "
                                                           "hfq: 返回后复权后的数据; "
                                                           "hfq-factor: 返回后复权因子和调整因子; "
                                                           "qfq-factor: 返回前复权因子和调整因子")


# 新浪财经-港股-历史行情数据
@router.post("/stock_hk_daily", operation_id="post_stock_hk_daily")
async def post_stock_hk_daily(request: StockDailyRequest):
    """
    接口: stock_hk_daily

    目标地址: http://stock.finance.sina.com.cn/hkstock/quotes/01336.html(个例)

    描述: 港股-历史行情数据, 可以选择返回复权后数据,更新频率为日频

    限量: 单次返回指定上市公司的历史行情数据(包括前后复权因子), 提供新浪财经拥有的该股票的所有数据(
    并不等于该股票从上市至今的数据)
    """
    try:
        stock_hk_daily_df = ak.stock_hk_daily(symbol=request.symbol, adjust=request.adjust)

        # 重命名字段
        stock_hk_daily_df.rename(columns={
            "date": "日期",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "close": "收盘价",
            "volume": "成交量",
            "hfq_factor": "后复权因子",
            "cash": "现金分红"
        }, inplace=True)

        return stock_hk_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
