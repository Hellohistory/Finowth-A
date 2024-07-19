import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_numpy, sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


class DateRequest(BaseModel):
    date: str


# 东方财富-数据中心-年报季报-分红配送
@router.post("/stock_fhps_em")
def get_stock_fhps_em(request: DateRequest):
    """
    接口: stock_fhps_em
    目标地址: https://data.eastmoney.com/yjfp/
    描述: 东方财富-数据中心-年报季报-分红配送
    限量: 单次获取指定日期的分红配送数据
    """
    try:
        stock_fhps_em_df = ak.stock_fhps_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_numpy(stock_fhps_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-分红送配-分红送配详情
@router.post("/stock_fhps_detail_em")
def get_stock_fhps_detail_em(request: SymbolRequest):
    """
    接口: stock_fhps_detail_em
    目标地址: https://data.eastmoney.com/yjfp/detail/300073.html
    描述: 东方财富网-数据中心-分红送配-分红送配详情
    限量: 单次获取指定 symbol 的分红配送详情数据
    """
    try:
        stock_fhps_detail_em_df = ak.stock_fhps_detail_em(symbol=request.symbol)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_fhps_detail_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-分红情况
@router.post("/stock_fhps_detail_ths")
def get_stock_fhps_detail_ths(request: SymbolRequest):
    """
    接口: stock_fhps_detail_ths
    目标地址: https://basic.10jqka.com.cn/new/603444/bonus.html
    描述: 同花顺-分红情况
    限量: 单次获取指定 symbol 的分红情况数据
    """
    try:
        stock_fhps_detail_ths_df = ak.stock_fhps_detail_ths(symbol=request.symbol)
        return stock_fhps_detail_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-港股-分红派息
@router.post("/stock_hk_fhpx_detail_ths")
def get_stock_hk_fhpx_detail_ths(request: SymbolRequest):
    """
    接口: stock_hk_fhpx_detail_ths
    目标地址: https://stockpage.10jqka.com.cn/HK0700/bonus/
    描述: 同花顺-港股-分红派息
    限量: 单次获取指定股票的分红派息数据
    """
    try:
        stock_hk_fhpx_detail_ths_df = ak.stock_hk_fhpx_detail_ths(symbol=request.symbol)
        return stock_hk_fhpx_detail_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolRequest(BaseModel):
    symbol: str


class SymbolIndicatorRequest(BaseModel):
    symbol: str
    indicator: str


class DividendDetailRequest(BaseModel):
    symbol: str
    indicator: str
    date: str = None


# 新浪财经-发行与分配-历史分红
@router.get("/stock_history_dividend")
def get_stock_history_dividend():
    """
    描述: 新浪财经-发行与分配-历史分红
    限量: 单次获取所有股票的历史分红数据
    """
    try:
        stock_history_dividend_df = ak.stock_history_dividend()
        return stock_history_dividend_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-发行与分配-分红配股
@router.post("/stock_history_dividend_detail")
def get_stock_history_dividend_detail(request: DividendDetailRequest):
    """
    描述: 新浪财经-发行与分配-分红配股
    限量: 单次获取指定股票的新浪财经-发行与分配-分红配股详情
    """
    try:
        if request.date:
            stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol=request.symbol,
                                                                                indicator=request.indicator,
                                                                                date=request.date)
        else:
            stock_history_dividend_detail_df = ak.stock_history_dividend_detail(symbol=request.symbol,
                                                                                indicator=request.indicator)
        return stock_history_dividend_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-个股-历史分红
@router.post("/stock_dividend_cninfo")
def get_stock_dividend_cninfo(request: SymbolRequest):
    """
    描述: 巨潮资讯-个股-历史分红
    限量: 单次获取指定股票的历史分红数据
    """
    try:
        stock_dividend_cninfo_df = ak.stock_dividend_cninfo(symbol=request.symbol)
        stock_dividend_cninfo_df = sanitize_data_pandas(stock_dividend_cninfo_df)

        return stock_dividend_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
