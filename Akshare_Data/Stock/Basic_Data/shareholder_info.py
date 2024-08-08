import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class JuChaoGuDongDateRequest(BaseModel):
    date: str = Field(..., title="指定披露时间",
                      description="数据从20170331开始。可选择'XXXX0331', 'XXXX0630', 'XXXX0930', 'XXXX1231'")


# 巨潮资讯-数据中心-专题统计-股东股本-股东人数及持股集中度
@router.post("/stock_hold_num_cninfo", operation_id="post_stock_hold_num_cninfo")
async def post_stock_hold_num_cninfo(request: JuChaoGuDongDateRequest):
    """
    巨潮资讯-股东股本-股东人数及持股集中度

    接口: stock_hold_num_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-股东股本-股东人数及持股集中度

    限量: 单次指定时间的股东人数及持股集中度数据, 从 20170331 开始
    """
    try:
        stock_hold_num_cninfo_df = ak.stock_hold_num_cninfo(date=request.date)
        return stock_hold_num_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolAndNameRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：001308")
    name: str = Field(..., title="高管名称", description="例：吴远")


# 东方财富-数据中心-特色数据-高管持股-人员增减持股变动明细
@router.post("/stock_hold_management_person_em", operation_id="post_stock_hold_management_person_em")
async def post_stock_hold_management_person_em(request: DongCaiSymbolAndNameRequest):
    """
    东方财富-高管持股-人员增减持股变动明细

    接口: stock_hold_management_person_em

    目标地址: https://data.eastmoney.com/executive/personinfo.html?name=%E5%90%B4%E8%BF%9C&code=001308

    描述: 东方财富-数据中心-特色数据-高管持股-人员增减持股变动明细

    限量: 单次返回指定个股和指定高管的数据
    """
    try:
        stock_hold_management_person_em = ak.stock_hold_management_person_em(symbol=request.symbol, name=request.name)
        stock_hold_management_person_em_df = sanitize_data_pandas(stock_hold_management_person_em)
        return stock_hold_management_person_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东大会
@router.get("/stock_gddh_em", operation_id="get_stock_gddh_em")
def get_stock_gddh_em():
    """
    东方财富-数据中心-股东大会

    接口: stock_gddh_em

    目标地址: https://data.eastmoney.com/gddh/

    描述: 东方财富-数据中心-股东大会

    限量: 单次返回所有数据
    """
    try:
        stock_gddh_em = ak.stock_gddh_em()
        stock_gddh_em_df = sanitize_data_pandas(stock_gddh_em)
        return stock_gddh_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiDateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# 东方财富-数据中心-重大合同-重大合同明细
@router.post("/stock_zdhtmx_em", operation_id="post_stock_zdhtmx_em")
async def post_stock_zdhtmx_em(request: DongCaiDateRangeRequest):
    """
    东方财富-重大合同-重大合同明细

    接口: stock_zdhtmx_em

    目标地址: https://data.eastmoney.com/zdht/mx.html

    描述: 东方财富-数据中心-重大合同-重大合同明细

    限量: 单次返回指定开始查询的日期和结束查询的日期的所有数据
    """
    try:
        stock_zdhtmx_em = ak.stock_zdhtmx_em(start_date=request.start_date, end_date=request.end_date)
        stock_zdhtmx_em_df = sanitize_data_pandas(stock_zdhtmx_em)
        return stock_zdhtmx_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 新浪财经-股本股东-主要股东
@router.post("/stock_main_stock_holder", operation_id="post_stock_main_stock_holder")
async def post_stock_main_stock_holder(request: SymbolRequest):
    """
    新浪财经-股本股东-主要股东

    接口: stock_main_stock_holder

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/600004.phtml

    描述: 新浪财经-股本股东-主要股东

    限量: 单次获取所有历史数据
    """
    try:
        stock_main_stock_holder = ak.stock_main_stock_holder(stock=request.symbol)
        stock_main_stock_holder_df = sanitize_data_pandas(stock_main_stock_holder)
        return stock_main_stock_holder_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-股东股本-流通股东
@router.post("/stock_circulate_stock_holder", operation_id="post_stock_circulate_stock_holder")
async def post_stock_circulate_stock_holder(request: SymbolRequest):
    """
    新浪财经-股东股本-流通股东

    接口: stock_circulate_stock_holder

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/600000.phtml

    描述: 新浪财经-股东股本-流通股东

    限量: 单次获取指定个股的流通股东数据
    """
    try:
        stock_circulate_stock_holder = ak.stock_circulate_stock_holder(symbol=request.symbol)
        stock_circulate_stock_holder_df = sanitize_data_pandas(stock_circulate_stock_holder)
        return stock_circulate_stock_holder_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="带市场标识的股票代码", description="例：sh688686")
    date: str = Field(..., title="财报发布季度最后日", description="例：20210630")


# 东方财富-个股-十大流通股东
@router.post("/stock_gdfx_free_top_10_em", operation_id="post_stock_gdfx_free_top_10_em")
async def post_stock_gdfx_free_top_10_em(request: DongCaiSymbolDateRequest):
    """
    东方财富-个股-十大流通股东

    接口: stock_gdfx_free_top_10_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=SH688686#sdltgd-0

    描述: 东方财富-个股-十大流通股东

    限量: 单次返回指定个股和 date 的所有数据
    """
    try:
        stock_gdfx_free_top_10_em = ak.stock_gdfx_free_top_10_em(symbol=request.symbol, date=request.date)
        stock_gdfx_free_top_10_em_df = sanitize_data_pandas(stock_gdfx_free_top_10_em)
        return stock_gdfx_free_top_10_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-个股-十大股东
@router.post("/stock_gdfx_top_10_em", operation_id="post_stock_gdfx_top_10_em")
async def post_stock_gdfx_top_10_em(request: DongCaiSymbolDateRequest):
    """
    东方财富-个股-十大股东

    接口: stock_gdfx_top_10_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=SH688686#sdltgd-0

    描述: 东方财富-个股-十大股东

    限量: 单次返回指定个股和 date 的所有数据
    """
    try:
        stock_gdfx_top_10_em = ak.stock_gdfx_top_10_em(symbol=request.symbol, date=request.date)
        stock_gdfx_top_10_em_df = sanitize_data_pandas(stock_gdfx_top_10_em)
        return stock_gdfx_top_10_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiDateRequest(BaseModel):
    date: str = Field(..., title="财报发布季度最后日", description="例：20210930")


# 东方财富-数据中心-股东分析-股东持股变动统计-十大流通股东
@router.post("/stock_gdfx_free_holding_change_em", operation_id="post_stock_gdfx_free_holding_change_em")
async def post_stock_gdfx_free_holding_change_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股变动统计-十大流通股东

    接口: stock_gdfx_free_holding_change_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股变动统计-十大流通股东

    限量: 单次返回指定时间的所有数据
    """
    try:
        stock_gdfx_free_holding_change_em = ak.stock_gdfx_free_holding_change_em(date=request.date)
        stock_gdfx_free_holding_change_em_df = sanitize_data_pandas(stock_gdfx_free_holding_change_em)
        return stock_gdfx_free_holding_change_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东持股变动统计-十大股东
@router.post("/stock_gdfx_holding_change_em", operation_id="post_stock_gdfx_holding_change_em")
async def post_stock_gdfx_holding_change_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股变动统计-十大股东

    接口: stock_gdfx_holding_change_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股变动统计-十大股东

    限量: 单次返回指定时间的所有数据
    """
    try:
        stock_gdfx_holding_change_em = ak.stock_gdfx_holding_change_em(date=request.date)
        stock_gdfx_holding_change_em_df = sanitize_data_pandas(stock_gdfx_holding_change_em)
        return stock_gdfx_holding_change_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东持股分析-十大流通股东
@router.post("/stock_gdfx_free_holding_analyse_em", operation_id="post_stock_gdfx_free_holding_analyse_em")
async def post_stock_gdfx_free_holding_analyse_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股分析-十大流通股东

    接口: stock_gdfx_free_holding_analyse_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股分析-十大流通股东

    限量: 单次获取返回所有数据
    """
    try:
        stock_gdfx_free_holding_analyse_em = ak.stock_gdfx_free_holding_analyse_em(date=request.date)
        stock_gdfx_free_holding_analyse_em_df = sanitize_data_pandas(stock_gdfx_free_holding_analyse_em)
        return stock_gdfx_free_holding_analyse_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东持股分析-十大股东
@router.post("/stock_gdfx_holding_analyse_em", operation_id="post_stock_gdfx_holding_analyse_em")
async def post_stock_gdfx_holding_analyse_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股分析-十大股东

    接口: stock_gdfx_holding_analyse_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股分析-十大股东

    限量: 单次获取返回所有数据
    """
    try:
        stock_gdfx_holding_analyse_em = ak.stock_gdfx_holding_analyse_em(date=request.date)
        stock_gdfx_holding_analyse_em_df = sanitize_data_pandas(stock_gdfx_holding_analyse_em)
        return stock_gdfx_holding_analyse_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东持股明细-十大流通股东
@router.post("/stock_gdfx_free_holding_detail_em", operation_id="post_stock_gdfx_free_holding_detail_em")
async def post_stock_gdfx_free_holding_detail_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股明细-十大流通股东

    接口: stock_gdfx_free_holding_detail_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股明细-十大流通股东

    限量: 单次返回指定时间的所有数据
    """
    try:
        stock_gdfx_free_holding_detail_em = ak.stock_gdfx_free_holding_detail_em(date=request.date)
        stock_gdfx_free_holding_detail_em_df = sanitize_data_pandas(stock_gdfx_free_holding_detail_em)
        return stock_gdfx_free_holding_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiHoldingDetailRequest(BaseModel):
    date: str = Field(..., title="财报发布季度最后日", description="例：20230331")
    indicator: str = Field(..., title="数据类型", description="可选择'个人', '基金', 'QFII', '社保', '券商', '信托'")
    symbol: str = Field(..., title="转变类型", description="可选择'新进', '增加', '不变', '减少'")


# 东方财富-数据中心-股东分析-股东持股明细-十大股东
@router.post("/stock_gdfx_holding_detail_em", operation_id="post_stock_gdfx_holding_detail_em")
async def post_stock_gdfx_holding_detail_em(request: DongCaiHoldingDetailRequest):
    """
    东方财富-股东分析-股东持股明细-十大股东

    接口: stock_gdfx_holding_detail_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股明细-十大股东

    限量: 单次返回指定参数的所有数据
    """
    try:
        stock_gdfx_holding_detail_em = ak.stock_gdfx_holding_detail_em(date=request.date, indicator=request.indicator, symbol=request.symbol)
        stock_gdfx_holding_detail_em_df = sanitize_data_pandas(stock_gdfx_holding_detail_em)
        return stock_gdfx_holding_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东持股统计-十大流通股东
@router.post("/stock_gdfx_free_holding_statistics_em", operation_id="post_stock_gdfx_free_holding_statistics_em")
async def post_stock_gdfx_free_holding_statistics_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股统计-十大股东

    接口: stock_gdfx_free_holding_statistics_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股统计-十大股东

    限量: 单次返回指定时间的所有数据
    """
    try:
        stock_gdfx_free_holding_statistics_em = ak.stock_gdfx_free_holding_statistics_em(date=request.date)
        stock_gdfx_free_holding_statistics_em_df = sanitize_data_pandas(stock_gdfx_free_holding_statistics_em)
        return stock_gdfx_free_holding_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东持股统计-十大股东
@router.post("/stock_gdfx_holding_statistics_em", operation_id="post_stock_gdfx_holding_statistics_em")
async def post_stock_gdfx_holding_statistics_em(request: DongCaiDateRequest):
    """
    东方财富-股东分析-股东持股统计-十大股东

    接口: stock_gdfx_holding_statistics_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东持股统计-十大股东

    限量: 单次返回指定时间的所有数据
    """
    try:
        stock_gdfx_holding_statistics_em = ak.stock_gdfx_holding_statistics_em(date=request.date)
        stock_gdfx_holding_statistics_em_df = sanitize_data_pandas(stock_gdfx_holding_statistics_em)
        return stock_gdfx_holding_statistics_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiGuDongSymbolRequest(BaseModel):
    symbol: str = Field(..., title="数据类型",
                        description="可选择'全部','个人', '基金', 'QFII', '社保', '券商', '信托'")


# 东方财富-数据中心-股东分析-股东协同-十大流通股东
@router.post("/stock_gdfx_free_holding_teamwork_em", operation_id="post_stock_gdfx_free_holding_teamwork_em")
async def post_stock_gdfx_free_holding_teamwork_em(request: DongCaiGuDongSymbolRequest):
    """
    东方财富-股东分析-股东协同-十大流通股东

    接口: stock_gdfx_free_holding_teamwork_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东协同-十大流通股东

    限量: 单次返回所有数据
    """
    try:
        stock_gdfx_free_holding_teamwork_em = ak.stock_gdfx_free_holding_teamwork_em(symbol=request.symbol)
        stock_gdfx_free_holding_teamwork_em_df = sanitize_data_pandas(stock_gdfx_free_holding_teamwork_em)
        return stock_gdfx_free_holding_teamwork_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-股东分析-股东协同-十大股东
@router.post("/stock_gdfx_holding_teamwork_em", operation_id="post_stock_gdfx_holding_teamwork_em")
async def post_stock_gdfx_holding_teamwork_em(request: DongCaiGuDongSymbolRequest):
    """
    东方财富-股东分析-股东协同-十大股东

    接口: stock_gdfx_holding_teamwork_em

    目标地址: https://data.eastmoney.com/gdfx/HoldingAnalyse.html

    描述: 东方财富-数据中心-股东分析-股东协同-十大股东

    限量: 单次返回所有数据
    """
    try:
        stock_gdfx_holding_teamwork_em = ak.stock_gdfx_holding_teamwork_em(symbol=request.symbol)
        stock_gdfx_holding_teamwork_em_df = sanitize_data_pandas(stock_gdfx_holding_teamwork_em)
        return stock_gdfx_holding_teamwork_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiGuDongDateRequest(BaseModel):
    date: str = Field(..., title="数据时间",
                      description="可选择'最新', '每个季度末', 其中每个季度末需要写成 `20230930` 格式")


# 东方财富-数据中心-特色数据-股东户数数据
@router.post("/stock_zh_a_gdhs", operation_id="post_stock_zh_a_gdhs")
async def post_stock_zh_a_gdhs(request: DongCaiGuDongDateRequest):
    """
    东方财富-股东户数详情

    接口: stock_zh_a_gdhs

    目标地址: http://data.eastmoney.com/gdhs/

    描述: 东方财富-数据中心-特色数据-股东户数数据

    限量: 单次获取返回所有数据
    """
    try:
        stock_zh_a_gdhs = ak.stock_zh_a_gdhs(symbol=request.date)
        stock_zh_a_gdhs_df = sanitize_data_pandas(stock_zh_a_gdhs)
        return stock_zh_a_gdhs_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-特色数据-股东户数详情
@router.post("/stock_zh_a_gdhs_detail_em", operation_id="post_stock_zh_a_gdhs_detail_em")
async def post_stock_zh_a_gdhs_detail_em(request: SymbolRequest):
    """
    东方财富-股东户数详情

    接口: stock_zh_a_gdhs_detail_em

    目标地址: https://data.eastmoney.com/gdhs/detail/000002.html

    描述: 东方财富-数据中心-特色数据-股东户数详情

    限量: 单次获取指定个股的所有数据
    """
    try:
        stock_zh_a_gdhs_detail_em = ak.stock_zh_a_gdhs_detail_em(symbol=request.symbol)
        stock_zh_a_gdhs_detail_em_df = sanitize_data_pandas(stock_zh_a_gdhs_detail_em)
        return stock_zh_a_gdhs_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
