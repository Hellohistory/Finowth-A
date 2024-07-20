import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, DateRequest, SymbolDateRequest, MarketPeriodRequest, \
    DisclosureRequest, SymbolDateRangeRequest
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 东方财富指定个股的新闻资讯数据
@router.post("/stock_news_em", operation_id="post_stock_news_em")
async def post_stock_news_em(request: SymbolRequest):
    """
    描述: 东方财富指定个股的新闻资讯数据
    限量: 指定 symbol 当日最近 100 条新闻资讯数据
    """
    try:
        stock_news_em_df = ak.stock_news_em(symbol=request.symbol)
        return stock_news_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 百度股市通-财报发行
@router.post("/news_report_time_baidu", operation_id="post_news_report_time_baidu")
async def post_news_report_time_baidu(request: DateRequest):
    """
    描述: 百度股市通-财报发行
    限量: 单次获取指定 symbol 的财报发行, 提供港股的财报发行数据
    """
    try:
        news_report_time_baidu_df = ak.news_report_time_baidu(date=request.date)
        return news_report_time_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩报表
@router.post("/stock_yjbb_em", operation_id="post_stock_yjbb_em")
async def post_stock_yjbb_em(request: DateRequest):
    """
    描述: 东方财富-数据中心-年报季报-业绩报表
    限量: 单次获取指定 symbol 的业绩报告数据
    """
    try:
        stock_yjbb_em_df = ak.stock_yjbb_em(date=request.date)
        stock_yjbb_em_df = sanitize_data_pandas(stock_yjbb_em_df)

        return stock_yjbb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩快报
@router.post("/stock_yjkb_em", operation_id="post_stock_yjkb_em")
async def post_stock_yjkb_em(request: DateRequest):
    """
    描述: 东方财富-数据中心-年报季报-业绩快报
    限量: 单次获取指定 symbol 的业绩快报数据
    """
    try:
        stock_yjkb_em_df = ak.stock_yjkb_em(date=request.date)
        stock_yjkb_em_df = sanitize_data_pandas(stock_yjkb_em_df)

        return stock_yjkb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩预告
@router.post("/stock_yjyg_em", operation_id="post_stock_yjyg_em")
async def post_stock_yjyg_em(request: DateRequest):
    """
    描述: 东方财富-数据中心-年报季报-业绩预告
    限量: 单次获取指定 symbol 的业绩预告数据
    """
    try:
        stock_yjyg_em_df = ak.stock_yjyg_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_yjyg_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-预约披露时间
@router.post("/stock_yysj_em", operation_id="stock_yysj_em")
async def post_stock_yysj_em(request: SymbolDateRequest):
    """
    描述: 东方财富-数据中心-年报季报-预约披露时间
    限量: 单次获取指定 symbol 和 symbol 的预约披露时间数据
    """
    try:
        stock_yysj_em_df = ak.stock_yysj_em(symbol=request.symbol, date=request.date)
        return stock_yysj_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据-预约披露的数据
@router.post("/stock_report_disclosure", operation_id="post_stock_report_disclosure")
async def post_stock_report_disclosure(request: MarketPeriodRequest):
    """
    描述: 巨潮资讯-数据-预约披露的数据
    限量: 单次获取指定 market 和 period 的预约披露数据
    """
    try:
        stock_report_disclosure_df = ak.stock_report_disclosure(market=request.market, period=request.period)
        return stock_report_disclosure_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-首页-公告查询-信息披露公告-沪深京
@router.post("/stock_zh_a_disclosure_report_cninfo",
             operation_id="post_stock_zh_a_disclosure_report_cninfo")
async def post_stock_zh_a_disclosure_report_cninfo(request: DisclosureRequest):
    """
    描述: 巨潮资讯-首页-公告查询-信息披露公告-沪深京
    限量: 单次获取指定 symbol 的信息披露公告数据
    """
    try:
        stock_zh_a_disclosure_report_cninfo_df = ak.stock_zh_a_disclosure_report_cninfo(
            symbol=request.symbol, market=request.market, category=request.category, start_date=request.start_date,
            end_date=request.end_date)
        return stock_zh_a_disclosure_report_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-首页-公告查询-信息披露调研-沪深京
@router.post("/stock_zh_a_disclosure_relation_cninfo",
             operation_id="post_stock_zh_a_disclosure_relation_cninfo")
async def post_stock_zh_a_disclosure_relation_cninfo(request: SymbolDateRangeRequest):
    """
    描述: 巨潮资讯-首页-公告查询-信息披露调研-沪深京
    限量: 单次获取指定 symbol 的信息披露调研数据
    """
    try:
        stock_zh_a_disclosure_relation_cninfo_df = ak.stock_zh_a_disclosure_relation_cninfo(
            symbol=request.symbol, market="沪深京", start_date=request.start_date, end_date=request.end_date)
        return stock_zh_a_disclosure_relation_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据-行业分类数据
@router.post("/stock_industry_category_cninfo", operation_id="post_stock_industry_category_cninfo")
async def post_stock_industry_category_cninfo(request: SymbolRequest):
    """
    描述: 巨潮资讯-数据-行业分类数据
    限量: 单次获取指定 symbol 的行业分类数据
    """
    try:
        stock_industry_category_cninfo_df = ak.stock_industry_category_cninfo(symbol=request.symbol)
        return stock_industry_category_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据-上市公司行业归属的变动情况
@router.post("/stock_industry_change_cninfo", operation_id="post_stock_industry_change_cninfo")
async def post_stock_industry_change_cninfo(request: SymbolDateRangeRequest):
    """
    描述: 巨潮资讯-数据-上市公司行业归属的变动情况
    限量: 单次获取指定 symbol 在 start_date 和 indicator 之间的上市公司行业归属的变动情况数据
    """
    try:
        # 获取数据
        stock_industry_change_cninfo_df = ak.stock_industry_change_cninfo(symbol=request.symbol,
                                                                          start_date=request.start_date,
                                                                          end_date=request.end_date)
        # 清洗数据
        sanitized_df = sanitize_data_pandas(stock_industry_change_cninfo_df)

        # 返回清洗后的数据
        return sanitized_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据-公司股本变动
@router.post("/stock_share_change_cninfo", operation_id="post_stock_share_change_cninfo")
async def post_stock_share_change_cninfo(request: SymbolDateRangeRequest):
    """
    描述: 巨潮资讯-数据-公司股本变动
    限量: 单次获取指定 symbol 在 start_date 和 indicator 之间的公司股本变动数据
    """
    try:
        stock_share_change_cninfo_df = ak.stock_share_change_cninfo(symbol=request.symbol,
                                                                    start_date=request.start_date,
                                                                    end_date=request.end_date)
        # 清洗数据
        sanitized_df = sanitize_data_pandas(stock_share_change_cninfo_df)

        # 返回清洗后的数据
        return sanitized_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-个股-配股实施方案
@router.post("/stock_allotment_cninfo", operation_id="post_stock_allotment_cninfo")
async def post_stock_allotment_cninfo(request: SymbolDateRangeRequest):
    """
    描述: 巨潮资讯-个股-配股实施方案
    限量: 单次获取指定 symbol 在 start_date 和 indicator 之间的公司股本变动数据
    """
    try:
        stock_allotment_cninfo_df = ak.stock_allotment_cninfo(symbol=request.symbol, start_date=request.start_date,
                                                              end_date=request.end_date)
        # 清洗数据
        sanitized_df = sanitize_data_pandas(stock_allotment_cninfo_df)

        # 返回清洗后的数据
        return sanitized_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩快报-资产负债表
@router.post("/stock_zcfz_em", operation_id="post_stock_zcfz_em")
async def post_stock_zcfz_em(request: DateRequest):
    """
    描述: 东方财富-数据中心-年报季报-业绩快报-资产负债表
    限量: 单次获取指定 symbol 的资产负债表数据
    """
    try:
        stock_zcfz_em_df = ak.stock_zcfz_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_zcfz_em_df)
        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩快报-利润表
@router.post("/stock_lrb_em", operation_id="post_stock_lrb_em")
async def post_stock_lrb_em(request: DateRequest):
    """
    描述: 东方财富-数据中心-年报季报-业绩快报-利润表
    限量: 单次获取指定 symbol 的利润表数据
    """
    try:
        stock_lrb_em_df = ak.stock_lrb_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_lrb_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩快报-现金流量表
@router.post("/stock_xjll_em", operation_id="post_stock_xjll_em")
async def post_stock_xjll_em(request: DateRequest):
    """
    描述: 东方财富-数据中心-年报季报-业绩快报-现金流量表
    限量: 单次获取指定 symbol 的现金流量表数据
    """
    try:
        stock_xjll_em_df = ak.stock_xjll_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_xjll_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
