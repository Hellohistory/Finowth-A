import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DongCaiNewsSymbolRequest(BaseModel):
    symbol: str = Field(..., title="股票代码或其他关键词", description="例：300059")


# 东方财富指定个股的新闻资讯数据
@router.post("/stock_news_em", operation_id="post_stock_news_em")
async def post_stock_news_em(request: DongCaiNewsSymbolRequest):
    """
    东方财富指定个股的新闻资讯数据

    接口: stock_news_em

    目标地址: https://so.eastmoney.com/news/s

    描述: 东方财富指定个股的新闻资讯数据

    限量: 指定个股当日最近 100 条新闻资讯数据
    """
    try:
        stock_news_em_df = ak.stock_news_em(symbol=request.symbol)
        return stock_news_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BaiduDateRequest(BaseModel):
    date: str = Field(..., title="指定日期", description="例：20230808")


# 百度股市通-财报发行
@router.post("/news_report_time_baidu", operation_id="post_news_report_time_baidu")
async def post_news_report_time_baidu(request: BaiduDateRequest):
    """
    百度股市通-财报发行

    接口: news_report_time_baidu

    目标地址: https://gushitong.baidu.com/calendar

    描述: 百度股市通-财报发行

    限量: 单次获取指定时间的财报发行, 提供港股的财报发行数据
    """
    try:
        news_report_time_baidu_df = ak.news_report_time_baidu(date=request.date)
        return news_report_time_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class AnnualDateRequest(BaseModel):
    date: str = Field(..., title="指定日期",
                      description="数据从20100331开始，可从四个时间节点中选择：'XXXX0331', 'XXXX0630', 'XXXX0930', 'XXXX1231'")


# 东方财富-数据中心-年报季报-业绩报表
@router.post("/stock_yjbb_em", operation_id="post_stock_yjbb_em")
async def post_stock_yjbb_em(request: AnnualDateRequest):
    """
    东方财富-年报季报-业绩报表

    接口: stock_yjbb_em

    目标地址: http://data.eastmoney.com/bbsj/202003/yjbb.html

    描述: 东方财富-数据中心-年报季报-业绩报表

    限量: 单次获取指定时间的业绩报告数据
    """
    try:
        stock_yjbb_em_df = ak.stock_yjbb_em(date=request.date)
        stock_yjbb_em_df = sanitize_data_pandas(stock_yjbb_em_df)

        return stock_yjbb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩快报
@router.post("/stock_yjkb_em", operation_id="post_stock_yjkb_em")
async def post_stock_yjkb_em(request: AnnualDateRequest):
    """
    东方财富-年报季报-业绩快报

    接口: stock_yjkb_em

    目标地址: https://data.eastmoney.com/bbsj/202003/yjkb.html

    描述: 东方财富-数据中心-年报季报-业绩快报

    限量: 单次获取指定时间的业绩快报数据
    """
    try:
        stock_yjkb_em_df = ak.stock_yjkb_em(date=request.date)
        stock_yjkb_em_df = sanitize_data_pandas(stock_yjkb_em_df)

        return stock_yjkb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩预告
@router.post("/stock_yjyg_em", operation_id="post_stock_yjyg_em")
async def post_stock_yjyg_em(request: AnnualDateRequest):
    """
    东方财富-年报季报-业绩预告

    接口: stock_yjyg_em

    目标地址: https://data.eastmoney.com/bbsj/202003/yjyg.html

    描述: 东方财富-数据中心-年报季报-业绩预告

    限量: 单次获取指定时间的业绩预告数据
    """
    try:
        stock_yjyg_em_df = ak.stock_yjyg_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_yjyg_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiAnnualSymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="指定市场",
                        description="可选择'沪深A股', '沪市A股', '科创板', '深市A股', '创业板', '京市A股', 'ST板'")
    date: str = Field(..., title="指定时间",
                      description="数据从20081231开始，可从四个时间节点中选择：'XXXX0331', 'XXXX0630', 'XXXX0930', 'XXXX1231'")


# 东方财富-数据中心-年报季报-预约披露时间
@router.post("/stock_yysj_em", operation_id="stock_yysj_em")
async def post_stock_yysj_em(request: DongCaiAnnualSymbolDateRequest):
    """
    东方财富-年报季报-预约披露时间

    接口: stock_yysj_em

    目标地址: https://data.eastmoney.com/bbsj/202003/yysj.html

    描述: 东方财富-数据中心-年报季报-预约披露时间

    限量: 单次获取指定个股和指定时间的预约披露时间数据
    """
    try:
        stock_yysj_em_df = ak.stock_yysj_em(symbol=request.symbol, date=request.date)
        return stock_yysj_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoMarketPeriodRequest(BaseModel):
    market: str = Field(..., title="市场",
                        description="可选择'沪深京', '深市', '深主板', '创业板', '沪市', '沪主板', '科创板', '北交所'")
    period: str = Field(..., title="时间段",
                        description="可选择四个部分'XXXX一季', 'XXXX半年报', 'XXXX三季', 'XXXX年报'")


# 巨潮资讯-数据-预约披露的数据
@router.post("/stock_report_disclosure", operation_id="post_stock_report_disclosure")
async def post_stock_report_disclosure(request: JuChaoMarketPeriodRequest):
    """
    巨潮资讯-预约披露的数据

    接口: stock_report_disclosure

    目标地址: http://www.cninfo.com.cn/new/commonUrl?url=data/yypl

    描述: 巨潮资讯-数据-预约披露的数据

    限量: 单次获取指定市场和指定时期的预约披露数据
    """
    try:
        stock_report_disclosure_df = ak.stock_report_disclosure(market=request.market, period=request.period)
        return stock_report_disclosure_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoDisclosureRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：000001")
    market: str = Field(..., title="市场类型",
                        description="'沪深京', '港股', '三板', '基金', '债券', '监管', '预披露'")
    keyword: str = Field(..., title="关键词", description="可选参数，默认为空")
    category: str = Field(..., title="公告类型",
                          description="'年报', '半年报', '一季报', '三季报', "
                                      "'业绩预告', '权益分派', '董事会', '监事会', "
                                      "'股东大会', '日常经营', '公司治理', '中介报告', "
                                      "'首发', '增发', '股权激励', '配股', '解禁', '公司债', "
                                      "'可转债', '其他融资', '股权变动', '补充更正', '澄清致歉', "
                                      "'风险提示', '特别处理和退市', '退市整理期'")
    start_date: str = Field(..., title="开始时间", description="例：20230618")
    end_date: str = Field(..., title="终止时间", description="例：20231219")


# 巨潮资讯-首页-公告查询-信息披露公告-沪深京
@router.post("/stock_zh_a_disclosure_report_cninfo",
             operation_id="post_stock_zh_a_disclosure_report_cninfo")
async def post_stock_zh_a_disclosure_report_cninfo(request: JuChaoDisclosureRequest):
    """
    巨潮资讯-信息披露公告-沪深京

    接口: stock_zh_a_disclosure_report_cninfo

    目标地址: http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search

    描述: 巨潮资讯-首页-公告查询-信息披露公告-沪深京

    限量: 单次获取指定个股的信息披露公告数据
    """
    try:
        stock_zh_a_disclosure_report_cninfo_df = ak.stock_zh_a_disclosure_report_cninfo(
            symbol=request.symbol,
            market=request.market,
            keyword=request.keyword,
            category=request.category,
            start_date=request.start_date,
            end_date=request.end_date)
        return stock_zh_a_disclosure_report_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoSymbolDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：000001")
    market: str = Field(..., title="市场类型",
                        description="'沪深京', '港股', '三板', '基金', '债券', '监管', '预披露'")
    start_date: str = Field(..., title="开始时间", description="例：20230618")
    end_date: str = Field(..., title="终止时间", description="例：20231219")


# 巨潮资讯-首页-公告查询-信息披露调研-沪深京
@router.post("/stock_zh_a_disclosure_relation_cninfo",
             operation_id="post_stock_zh_a_disclosure_relation_cninfo")
async def post_stock_zh_a_disclosure_relation_cninfo(request: JuChaoSymbolDateRangeRequest):
    """
    巨潮资讯-信息披露调研-沪深京

    接口: stock_zh_a_disclosure_relation_cninfo

    目标地址: http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search

    描述: 巨潮资讯-首页-公告查询-信息披露调研-沪深京

    限量: 单次获取指定个股的信息披露调研数据
    """
    try:
        stock_zh_a_disclosure_relation_cninfo_df = ak.stock_zh_a_disclosure_relation_cninfo(
            symbol=request.symbol, market=request.market, start_date=request.start_date, end_date=request.end_date)
        return stock_zh_a_disclosure_relation_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoDataSymbolRequest(BaseModel):
    symbol: str = Field(..., title="分类标准",
                        description="可选择'证监会行业分类标准', '巨潮行业分类标准', '申银万国行业分类标准', "
                                    "'新财富行业分类标准', '国资委行业分类标准', '巨潮产业细分标准', "
                                    "'天相行业分类标准', '全球行业分类标准'")


# 巨潮资讯-数据-行业分类数据
@router.post("/stock_industry_category_cninfo", operation_id="post_stock_industry_category_cninfo")
async def post_stock_industry_category_cninfo(request: JuChaoDataSymbolRequest):
    """
    巨潮资讯-行业分类数据

    接口: stock_industry_category_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/apiDoc

    描述: 巨潮资讯-数据-行业分类数据

    限量: 单次获取指定个股的行业分类数据
    """
    try:
        stock_industry_category_cninfo_df = ak.stock_industry_category_cninfo(symbol=request.symbol)
        return stock_industry_category_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoDataSymbolDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="股票代码", description="例：000001")
    start_date: str = Field(..., title="开始时间", description="例：20230618")
    end_date: str = Field(..., title="终止时间", description="例：20231219")


# 巨潮资讯-数据-上市公司行业归属的变动情况
@router.post("/stock_industry_change_cninfo", operation_id="post_stock_industry_change_cninfo")
async def post_stock_industry_change_cninfo(request: JuChaoDataSymbolDateRangeRequest):
    """
    巨潮资讯-上市公司行业归属的变动情况

    接口: stock_industry_change_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/apiDoc

    描述: 巨潮资讯-数据-上市公司行业归属的变动情况

    限量: 单次获取指定个股在指定起始时间和终止时间之间的上市公司行业归属的变动情况数据
    """
    try:
        stock_industry_change_cninfo_df = ak.stock_industry_change_cninfo(symbol=request.symbol,
                                                                          start_date=request.start_date,
                                                                          end_date=request.end_date)
        sanitized_df = sanitize_data_pandas(stock_industry_change_cninfo_df)

        return sanitized_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据-公司股本变动
@router.post("/stock_share_change_cninfo", operation_id="post_stock_share_change_cninfo")
async def post_stock_share_change_cninfo(request: JuChaoDataSymbolDateRangeRequest):
    """
    巨潮资讯-公司股本变动

    接口: stock_share_change_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/apiDoc

    描述: 巨潮资讯-数据-公司股本变动

    限量: 单次获取指定个股在起始时间和终止时间之间的公司股本变动数据
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
async def post_stock_allotment_cninfo(request: JuChaoDataSymbolDateRangeRequest):
    """
    巨潮资讯-配股实施方案

    接口: stock_allotment_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/dataBrowse

    描述: 巨潮资讯-个股-配股实施方案

    限量: 单次获取指定个股在起始时间和终止时间之间的公司股本变动数据
    """
    try:
        stock_allotment_cninfo_df = ak.stock_allotment_cninfo(symbol=request.symbol, start_date=request.start_date,
                                                              end_date=request.end_date)
        sanitized_df = sanitize_data_pandas(stock_allotment_cninfo_df)

        return sanitized_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiBalanceSheetRequest(BaseModel):
    date: str = Field(..., title="指定时间",
                      description="数据从20081231开始，可从四个时间节点中选择：'XXXX0331', 'XXXX0630', 'XXXX0930', 'XXXX1231'")


# 东方财富-数据中心-年报季报-业绩快报-资产负债表
@router.post("/stock_zcfz_em", operation_id="post_stock_zcfz_em")
async def post_stock_zcfz_em(request: DongCaiBalanceSheetRequest):
    """
    东方财富-年报季报-业绩快报-资产负债表

    接口: stock_zcfz_em

    目标地址: https://data.eastmoney.com/bbsj/202003/zcfz.html

    描述: 东方财富-数据中心-年报季报-业绩快报-资产负债表

    限量: 单次获取指定时间的资产负债表数据
    """
    try:
        stock_zcfz_em_df = ak.stock_zcfz_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_zcfz_em_df)
        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiIncomeStatementDateRequest(BaseModel):
    date: str = Field(..., title="指定时间",
                      description="数据从20120331开始，可从四个时间节点中选择：'XXXX0331', 'XXXX0630', 'XXXX0930', 'XXXX1231'")


# 东方财富-数据中心-年报季报-业绩快报-利润表
@router.post("/stock_lrb_em", operation_id="post_stock_lrb_em")
async def post_stock_lrb_em(request: DongCaiIncomeStatementDateRequest):
    """
    东方财富-年报季报-业绩快报-利润表

    接口: stock_lrb_em

    目标地址: http://data.eastmoney.com/bbsj/202003/lrb.html

    描述: 东方财富-数据中心-年报季报-业绩快报-利润表

    限量: 单次获取指定时间的利润表数据
    """
    try:
        stock_lrb_em_df = ak.stock_lrb_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_lrb_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-年报季报-业绩快报-现金流量表
@router.post("/stock_xjll_em", operation_id="post_stock_xjll_em")
async def post_stock_xjll_em(request: DongCaiBalanceSheetRequest):
    """
    东方财富-年报季报-业绩快报-现金流量表

    接口: stock_xjll_em

    目标地址: http://data.eastmoney.com/bbsj/202003/xjll.html

    描述: 东方财富-数据中心-年报季报-业绩快报-现金流量表

    限量: 单次获取指定时间的现金流量表数据
    """
    try:
        stock_xjll_em_df = ak.stock_xjll_em(date=request.date)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_xjll_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
