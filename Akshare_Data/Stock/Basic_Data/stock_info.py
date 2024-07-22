import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class XinLangSectorRequest(BaseModel):
    sector: str = Field(..., title="行业代码", description="通过stock_sector_spot返回数据的 label 字段选择 sector")


# 新浪行业-板块行情-成份详情
@router.post("/stock_sector_detail", operation_id="post_stock_sector_detail")
async def post_stock_sector_detail(request: XinLangSectorRequest):
    """
    接口: stock_sector_detail

    目标地址: http://finance.sina.com.cn/stock/sl/#area_1

    描述: 新浪行业-板块行情-成份详情, 由于新浪网页提供的统计数据有误, 部分行业数量大于统计数

    限量: 单次获取指定的新浪行业-板块行情-成份详情
    """
    try:
        stock_sector_detail_df = ak.stock_sector_detail(sector=request.sector)

        stock_sector_detail_df.rename(columns={
            "symbol": "带市场标识股票代码",
            "code": "代码",
            "name": "名称",
            "trade": "交易",
            "pricechange": "价格变动",
            "changepercent": "涨跌幅",
            "buy": "买入",
            "sell": "卖出",
            "settlement": "结算",
            "open": "开盘价",
            "high": "最高价",
            "low": "最低价",
            "volume": "成交量",
            "amount": "成交金额",
            "ticktime": "时间",
            "per": "市盈率",
            "pb": "市净率",
            "mktcap": "总市值",
            "nmc": "流通市值",
            "turnoverratio": "换手率"
        }, inplace=True)

        return stock_sector_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 沪深京 A 股股票代码和股票简称数据
@router.get("/stock_info_a_code_name", operation_id="post_stock_info_a_code_name")
def get_stock_info_a_code_name():
    """
    接口: stock_info_a_code_name

    目标地址: 沪深京三个交易所

    描述: 沪深京 A 股股票代码和股票简称数据

    限量: 单次获取所有 A 股股票代码和简称数据
    """
    try:
        stock_info_a_code_name_df = ak.stock_info_a_code_name()
        return stock_info_a_code_name_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ShSymbolRequest(BaseModel):
    symbol: str = Field(..., title="市场类型", description="可选择'主板A股', '主板B股', '科创板'")


# 上海证券交易所股票代码和简称数据
@router.post("/stock_info_sh_name_code", operation_id="post_stock_info_sh_name_code")
async def post_stock_info_sh_name_code(request: ShSymbolRequest):
    """
    接口: stock_info_sh_name_code

    目标地址: https://www.sse.com.cn/assortment/stock/list/share/

    描述: 上海证券交易所股票代码和简称数据

    限量: 单次获取所有上海证券交易所股票代码和简称数据
    """
    try:
        stock_info_sh_name_code_df = ak.stock_info_sh_name_code(symbol=request.symbol)
        return stock_info_sh_name_code_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SzSymbolRequest(BaseModel):
    symbol: str = Field(..., title="市场类型", description="可选择'A股列表', 'B股列表', 'CDR列表', 'AB股列表'")


# 深证证券交易所股票代码和股票简称数据
@router.post("/stock_info_sz_name_code", operation_id="post_stock_info_sz_name_code")
async def post_stock_info_sz_name_code(request: SzSymbolRequest):
    """
    接口: stock_info_sz_name_code

    目标地址: https://www.szse.cn/market/product/stock/list/index.html

    描述: 深证证券交易所股票代码和股票简称数据

    限量: 单次获取深证证券交易所股票代码和简称数据
    """
    try:
        stock_info_sz_name_code_df = ak.stock_info_sz_name_code(symbol=request.symbol)
        return stock_info_sz_name_code_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 北京证券交易所股票代码和简称数据
@router.get("/stock_info_bj_name_code", operation_id="post_stock_info_bj_name_code")
def get_stock_info_bj_name_code():
    """
    接口: stock_info_bj_name_code

    目标地址: https://www.bse.cn/nq/listedcompany.html

    描述: 北京证券交易所股票代码和简称数据

    限量: 单次获取北京证券交易所所有的股票代码和简称数据
    """
    try:
        stock_info_bj_name_code_df = ak.stock_info_bj_name_code()
        return stock_info_bj_name_code_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SzTsSymbolRequest(BaseModel):
    symbol: str = Field(..., title="数据类型",
                        description="可选择'暂停上市公司', '终止上市公司'")


# 深证证券交易所终止/暂停上市股票
@router.post("/stock_info_sz_delist", operation_id="post_stock_info_sz_delist")
async def post_stock_info_sz_delist(request: SzTsSymbolRequest):
    """
    接口: stock_info_sz_delist

    目标地址: https://www.szse.cn/market/stock/suspend/index.html

    描述: 深证证券交易所终止/暂停上市股票

    限量: 单次获取深证证券交易所终止/暂停上市数据
    """
    try:
        stock_info_sz_delist_df = ak.stock_info_sz_delist(symbol=request.symbol)
        return stock_info_sz_delist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-行情中心-沪深个股-两网及退市
@router.get("/stock_staq_net_stop", operation_id="post_stock_staq_net_stop")
def get_stock_staq_net_stop():
    """
    接口: stock_staq_net_stop

    目标地址: https://quote.eastmoney.com/center/gridlist.html#staq_net_board

    描述: 东方财富网-行情中心-沪深个股-两网及退市

    限量: 单次获取所有两网及退市的股票数据
    """
    try:
        stock_staq_net_stop_df = ak.stock_staq_net_stop()
        return stock_staq_net_stop_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ShTsSymbolRequest(BaseModel):
    symbol: str = Field(..., title="数据类型",
                        description="可选择'全部', '沪市', '科创板'")


# 上海证券交易所暂停/终止上市股票
@router.post("/stock_info_sh_delist", operation_id="post_stock_info_sh_delist")
async def post_stock_info_sh_delist(request: ShTsSymbolRequest):
    """
    接口: stock_info_sh_delist

    目标地址: https://www.sse.com.cn/assortment/stock/list/delisting/

    描述: 上海证券交易所暂停/终止上市股票

    限量: 单次获取上海证券交易所暂停/终止上市股票
    """
    try:
        stock_info_sh_delist_df = ak.stock_info_sh_delist(symbol=request.symbol)
        return stock_info_sh_delist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 新浪财经-股票曾用名
@router.post("/stock_info_change_name", operation_id="post_stock_info_change_name")
async def post_stock_info_change_name(request: XinLangSymbolRequest):
    """
    接口: stock_info_change_name

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/300378.phtml

    描述: 新浪财经-股票曾用名

    限量: 单次指定个股的所有历史曾用名称
    """
    try:
        stock_info_change_name_list = ak.stock_info_change_name(symbol=request.symbol)
        return stock_info_change_name_list.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SzSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定类型", description="可选择'全称变更', '简称变更'")


# 深证证券交易所-市场数据-股票数据-名称变更
@router.post("/stock_info_sz_change_name", operation_id="post_stock_info_sz_change_name")
async def post_stock_info_sz_change_name(request: SzSymbolRequest):
    """
    接口: stock_info_sz_change_name

    目标地址: https://www.szse.cn/www/market/stock/changename/index.html

    描述: 深证证券交易所-市场数据-股票数据-名称变更

    限量: 单次获取所有历史数据
    """
    try:
        stock_info_sz_change_name_df = ak.stock_info_sz_change_name(symbol=request.symbol)
        return stock_info_sz_change_name_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
