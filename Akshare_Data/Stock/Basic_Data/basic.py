import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data, sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 股票增发
@router.post("/stock_add_stock", operation_id="post_stock_add_stock")
async def post_stock_add_stock(request: SymbolRequest):
    """
    新浪财经-发行与分配-增发

    接口: stock_add_stock

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_AddStock/stockid/600004.phtml

    描述: 新浪财经-发行与分配-增发

    限量: 单次指定个股的股票增发详情数据
    """
    try:
        stock_add_stock_df = ak.stock_add_stock(symbol=request.symbol)
        return stock_add_stock_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BaiDuStockZhVoteBaiduRequest(BaseModel):
    symbol: str = Field(..., title="A 股股票或指数代码", description="例：000001")
    indicator: str = Field(..., title="指数或股票", description="可选择'指数', '股票'")


# 涨跌投票
@router.post("/stock_zh_vote_baidu", operation_id="post_stock_zh_vote_baidu")
async def post_stock_zh_vote_baidu(request: BaiDuStockZhVoteBaiduRequest):
    """
    百度股市通- A 股或指数-股评-投票

    接口: stock_zh_vote_baidu

    目标地址: https://gushitong.baidu.com/index/ab-000001

    描述: 百度股市通- A 股或指数-股评-投票

    限量: 单次获取指定个股和指定时间段的所有数据
    """
    try:
        stock_zh_vote_baidu_df = ak.stock_zh_vote_baidu(symbol=request.symbol, indicator=request.indicator)
        return stock_zh_vote_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BaiDuHKSymbolIndicatorPeriodRequest(BaseModel):
    symbol: str = Field(..., title="港股代码", description="例：02358")
    indicator: str = Field(..., title="估值类型",
                           description="可选择'总市值', '市盈率(TTM)', '市盈率(静)', '市净率', '市现率'")
    period: str = Field(..., title="时间类型", description="可选择'近一年', '近三年', '近五年', '近十年', '全部'")


# 港股估值指标
@router.post("/stock_hk_valuation_baidu", operation_id="post_stock_hk_valuation_baidu")
async def post_stock_hk_valuation_baidu(request: BaiDuHKSymbolIndicatorPeriodRequest):
    """
    百度股市通-港股-财务报表-估值数据

    接口: stock_hk_valuation_baidu

    目标地址: https://gushitong.baidu.com/stock/hk-06969

    描述: 百度股市通-港股-财务报表-估值数据

    限量: 单次获取指定个股的指定指定时间段的特定 period 的历史数据
    """
    try:
        stock_hk_valuation_baidu_df = ak.stock_hk_valuation_baidu(symbol=request.symbol, indicator=request.indicator,
                                                                  period=request.period)
        return stock_hk_valuation_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定查询代码",
                        description="可选择all : 全部A股, sz50 : 上证50, hs300 : 沪深300, zz500 : 中证500")


# 创新高和新低的股票数量
@router.post("/stock_a_high_low_statistics", operation_id="post_stock_a_high_low_statistics")
async def post_stock_a_high_low_statistics(request: XSymbolRequest):
    """
    不同市场的创新高和新低的股票数量

    接口: stock_a_high_low_statistics

    目标地址: https://www.legulegu.com/stockdata/high-low-statistics

    描述: 不同市场的创新高和新低的股票数量

    限量: 单次获取指定市场的近两年的历史数据
    """
    try:
        stock_a_high_low_statistics_df = ak.stock_a_high_low_statistics(symbol=request.symbol)
        # 更改列名为中文
        stock_a_high_low_statistics_df.rename(columns={
            'date': '交易日',
            'close': '相关指数收盘价',
            'high20': '20日新高',
            'low20': '20日新低',
            'high60': '60日新高',
            'low60': '60日新低',
            'high120': '120日新高',
            'low120': '120日新低'
        }, inplace=True)
        return stock_a_high_low_statistics_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class PSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定查询代码",
                        description="可选择 全部A股,  沪深300,  上证50, 中证500")


# 破净股统计
@router.post("/stock_a_below_net_asset_statistics", operation_id="post_stock_a_below_net_asset_statistics")
async def post_stock_a_below_net_asset_statistics(request: PSymbolRequest):
    """
    乐咕乐股-A 股破净股统计数据

    接口: stock_a_below_net_asset_statistics

    目标地址: https://www.legulegu.com/stockdata/below-net-asset-statistics

    描述: 乐咕乐股-A 股破净股统计数据

    限量: 单次获取指定类型的所有历史数据
    """
    try:
        stock_a_below_net_asset_statistics_df = ak.stock_a_below_net_asset_statistics(symbol=request.symbol)
        # 更改列名为中文
        stock_a_below_net_asset_statistics_df.rename(columns={
            'date': '交易日',
            'below_net_asset': '破净股家数',
            'total_company': '总公司数',
            'below_net_asset_ratio': '破净股比率'
        }, inplace=True)
        return stock_a_below_net_asset_statistics_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-首发申报信息-首发申报企业信息
@router.get("/stock_ipo_declare", operation_id="get_stock_ipo_declare")
def get_stock_ipo_declare():
    """
    东方财富-首发申报信息-首发申报企业信息

    接口: stock_ipo_declare

    目标地址: https://data.eastmoney.com/xg/xg/sbqy.html

    描述: 东方财富-数据中心-新股申购-首发申报信息-首发申报企业信息

    限量: 单次返回所有历史数据
    """
    try:
        stock_ipo_declare_df = ak.stock_ipo_declare()
        data = stock_ipo_declare_df.to_dict(orient="records")
        sanitized_data = sanitize_data(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 增发
@router.get("/stock_qbzf_em", operation_id="get_stock_qbzf_em")
def get_stock_qbzf_em():
    """
    东方财富-新股数据-增发-全部增发

    接口: stock_qbzf_em

    目标地址: https://data.eastmoney.com/other/gkzf.html

    描述: 东方财富-数据中心-新股数据-增发-全部增发

    限量: 单次返回所有历史数据
    """
    try:
        stock_qbzf_em_df = ak.stock_qbzf_em()
        stock_qbzf_em_df = sanitize_data_pandas(stock_qbzf_em_df)

        return stock_qbzf_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 配股
@router.get("/stock_pg_em", operation_id="get_stock_pg_em")
def get_stock_pg_em():
    """
    东方财富-新股数据-配股

    接口: stock_pg_em

    目标地址: https://data.eastmoney.com/xg/pg/

    描述: 东方财富-数据中心-新股数据-配股

    限量: 单次返回所有历史数据
    """
    try:
        stock_pg_em_df = ak.stock_pg_em()
        stock_pg_em_df = sanitize_data_pandas(stock_pg_em_df)

        return stock_pg_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 股票回购数据
@router.get("/stock_repurchase_em", operation_id="get_stock_repurchase_em")
def get_stock_repurchase_em():
    """
    东方财富-股票回购-股票回购数据

    接口: stock_repurchase_em

    目标地址: https://data.eastmoney.com/gphg/hglist.html

    描述: 东方财富-数据中心-股票回购-股票回购数据

    限量: 单次返回所有历史数据
    """
    try:
        stock_repurchase_em = ak.stock_repurchase_em()
        stock_repurchase_em_df = sanitize_data_pandas(stock_repurchase_em)

        return stock_repurchase_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
