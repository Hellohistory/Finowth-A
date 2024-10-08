import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DateRequest(BaseModel):
    date: str = Field(..., title="指定日期", description="数据从19901231开始，从'XXXX0630', 'XXXX1231'选择")


# 东方财富-数据中心-年报季报-分红配送
@router.post("/stock_fhps_em", operation_id="stock_fhps_em")
async def stock_fhps_em(request: DateRequest):
    """
    东方财富-年报季报-分红配送

    接口: stock_fhps_em

    目标地址: https://data.eastmoney.com/yjfp/

    描述: 东方财富-数据中心-年报季报-分红配送

    限量: 单次获取指定日期的分红配送数据
    """
    try:
        stock_fhps_em = ak.stock_fhps_em(date=request.date)
        stock_fhps_em_df = sanitize_data_pandas(stock_fhps_em)
        return stock_fhps_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 东方财富-数据中心-分红送配-分红送配详情
@router.post("/stock_fhps_detail_em", operation_id="stock_fhps_detail_em")
async def stock_fhps_detail_em(request: SymbolRequest):
    """
    东方财富-分红送配-分红送配详情

    接口: stock_fhps_detail_em

    目标地址: https://data.eastmoney.com/yjfp/detail/300073.html

    描述: 东方财富-数据中心-分红送配-分红送配详情

    限量: 单次获取指定个股的分红配送详情数据
    """
    try:
        stock_fhps_detail_em = ak.stock_fhps_detail_em(symbol=request.symbol)
        stock_fhps_detail_em_df = sanitize_data_pandas(stock_fhps_detail_em)
        return stock_fhps_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-分红情况
@router.post("/stock_fhps_detail_ths", operation_id="stock_fhps_detail_ths")
async def stock_fhps_detail_ths(request: SymbolRequest):
    """
    同花顺-分红情况

    接口: stock_fhps_detail_ths

    目标地址: https://basic.10jqka.com.cn/new/603444/bonus.html

    描述: 同花顺-分红情况

    限量: 单次获取指定个股的分红情况数据
    """
    try:
        stock_fhps_detail_ths = ak.stock_fhps_detail_ths(symbol=request.symbol)
        stock_fhps_detail_ths_df = sanitize_data_pandas(stock_fhps_detail_ths)
        return stock_fhps_detail_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-港股-分红派息
@router.post("/stock_hk_fhpx_detail_ths", operation_id="stock_hk_fhpx_detail_ths")
async def stock_hk_fhpx_detail_ths(request: SymbolRequest):
    """
    同花顺-港股-分红派息

    接口: stock_hk_fhpx_detail_ths

    目标地址: https://stockpage.10jqka.com.cn/HK0700/bonus/

    描述: 同花顺-港股-分红派息

    限量: 单次获取指定股票的分红派息数据
    """
    try:
        stock_hk_fhpx_detail_ths = ak.stock_hk_fhpx_detail_ths(symbol=request.symbol)
        stock_hk_fhpx_detail_ths_df = sanitize_data_pandas(stock_hk_fhpx_detail_ths)
        return stock_hk_fhpx_detail_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-发行与分配-历史分红
@router.get("/stock_history_dividend", operation_id="stock_history_dividend")
def stock_history_dividend():
    """
    新浪财经-发行与分配-历史分红

    接口: stock_history_dividend

    目标地址: http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lsfh/index.phtml?p=1&num=5000

    描述: 新浪财经-发行与分配-历史分红

    限量: 单次获取所有股票的历史分红数据
    """
    try:
        stock_history_dividend = ak.stock_history_dividend()
        stock_history_dividend_df = sanitize_data_pandas(stock_history_dividend)
        return stock_history_dividend_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DividendDetailRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：600012")
    indicator: str = Field(..., title="分红配股", description="可选择'分红', '配股'")
    date: str = Field(..., title="分红配股的具体日期", description="例：2019-06-14，此为可选参数可不填")


# 新浪财经-发行与分配-分红配股
@router.post("/stock_history_dividend_detail", operation_id="stock_history_dividend_detail")
async def stock_history_dividend_detail(request: DividendDetailRequest):
    """
    新浪财经-发行与分配-分红配股

    接口: stock_history_dividend_detail

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/300670.phtml

    描述: 新浪财经-发行与分配-分红配股

    限量: 单次获取指定股票的新浪财经-发行与分配-分红配股详情
    """
    try:
        if request.date:
            stock_history_dividend_detail = ak.stock_history_dividend_detail(symbol=request.symbol,
                                                                                indicator=request.indicator,
                                                                                date=request.date)
        else:
            stock_history_dividend_detail = ak.stock_history_dividend_detail(symbol=request.symbol,
                                                                                indicator=request.indicator)
        stock_history_dividend_detail_df = sanitize_data_pandas(stock_history_dividend_detail)
        return stock_history_dividend_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-个股-历史分红
@router.post("/stock_dividend_cninfo", operation_id="stock_dividend_cninfo")
async def stock_dividend_cninfo(request: SymbolRequest):
    """
    巨潮资讯-个股-历史分红

    接口: stock_dividend_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/company?companyid=600009

    描述: 巨潮资讯-个股-历史分红

    限量: 单次获取指定股票的历史分红数据
    """
    try:
        stock_dividend_cninfo = ak.stock_dividend_cninfo(symbol=request.symbol)
        stock_dividend_cninfo_df = sanitize_data_pandas(stock_dividend_cninfo)

        return stock_dividend_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
