from typing import List, Dict, Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

# 数据来源：Akshare
# 基金数据
# # 私募基金数据
from Akshare_Data.Fund.private_equity_funds import router as router54
# # 公募基金数据
from Akshare_Data.Fund.public_fund.basic_info import router as router117
from Akshare_Data.Fund.public_fund.dividend_distribution import router as router118
from Akshare_Data.Fund.public_fund.fund_announcement import router as router119
from Akshare_Data.Fund.public_fund.fund_individual_achievement_xq import router as router120
from Akshare_Data.Fund.public_fund.fund_market import router as router121
from Akshare_Data.Fund.public_fund.fund_net_value import router as router122
from Akshare_Data.Fund.public_fund.fund_position import router as router123
from Akshare_Data.Fund.public_fund.fund_ranking import router as router124
from Akshare_Data.Fund.public_fund.fund_rating import router as router131
from Akshare_Data.Fund.public_fund.fund_report import router as router125
from Akshare_Data.Fund.public_fund.fund_size import router as router126
from Akshare_Data.Fund.public_fund.fund_value_estimation_em import router as router127
from Akshare_Data.Fund.public_fund.reits_realtime_em import router as router128
from Akshare_Data.Fund.public_fund.scale_of_fund_company import router as router129
from Akshare_Data.Fund.public_fund.scale_share import router as router130
# 期货数据
from Akshare_Data.Futures.basic_data import router as router55
# 利率数据
from Akshare_Data.InterestRate.main_central_bank_interest_rates import router as router43
from Akshare_Data.InterestRate.fixing_repo_rate import router as router49
from Akshare_Data.InterestRate.interbank_lending_rate import router as router47
# 现货数据
from Akshare_Data.Spot.spot_trend import router as router53
from Akshare_Data.Spot.variety_list import router as router39
# 股票数据
from Akshare_Data.Stock.AH_data import router as router1
from Akshare_Data.Stock.A_stocksother_data import router as router2
from Akshare_Data.Stock.Basic_Data.AUH_index import router as router50
from Akshare_Data.Stock.Basic_Data.IPO_review import router as router52
from Akshare_Data.Stock.Basic_Data.basic import router as router32
from Akshare_Data.Stock.Basic_Data.executive_info import router as router28
from Akshare_Data.Stock.Basic_Data.financial_research_report import router as router23
from Akshare_Data.Stock.Basic_Data.fund import router as router30
from Akshare_Data.Stock.Basic_Data.institutional_info import router as router27
from Akshare_Data.Stock.Basic_Data.shareholder_info import router as router24
from Akshare_Data.Stock.Basic_Data.special_topic_tatistics import router as router29
from Akshare_Data.Stock.Basic_Data.stock_info import router as router26
from Akshare_Data.Stock.Basic_Data.unlock_data import router as router25
from Akshare_Data.Stock.Basic_Data.winners_list import router as router31
from Akshare_Data.Stock.ESG_rating import router as router42
from Akshare_Data.Stock.HK_stocks import router as router9
from Akshare_Data.Stock.SHK_stock_connect import router as router16
from Akshare_Data.Stock.US_stocks import router as router8
from Akshare_Data.Stock.basic_market import router as router11
from Akshare_Data.Stock.capital_flows import router as router21
from Akshare_Data.Stock.concept_section import router as router36
from Akshare_Data.Stock.daily_limit import router as router40
from Akshare_Data.Stock.dividend import router as router20
from Akshare_Data.Stock.featured_data import router as router17
from Akshare_Data.Stock.financial_report_issuance import router as router19
from Akshare_Data.Stock.goodwill import router as router12
from Akshare_Data.Stock.historical_data import router as router6
from Akshare_Data.Stock.industry_sector import router as router37
from Akshare_Data.Stock.info_data import router as router45
from Akshare_Data.Stock.large_transactions import router as router33
from Akshare_Data.Stock.margin_margin_trading import router as router34
from Akshare_Data.Stock.new_shares import router as router18
from Akshare_Data.Stock.other import router as router22
from Akshare_Data.Stock.profit_prediction import router as router35
from Akshare_Data.Stock.real_time_quotes import router as router5
from Akshare_Data.Stock.research import router as router10
from Akshare_Data.Stock.science_and_technology_innovation_board_data import router as router7
from Akshare_Data.Stock.stock_a_indicator_lg import router as router48
from Akshare_Data.Stock.stock_account_statistics import router as router13
from Akshare_Data.Stock.stock_changes_em import router as router44
from Akshare_Data.Stock.stock_evaluation import router as router15
from Akshare_Data.Stock.stock_financial_abstract import router as router46
from Akshare_Data.Stock.stock_hk_indicator_eniu import router as router51
from Akshare_Data.Stock.stock_market_overview import router as router3
from Akshare_Data.Stock.stock_pledge import router as router14
from Akshare_Data.Stock.stock_popularity import router as router38
from Akshare_Data.Stock.technical_indicators import router as router41
from Akshare_Data.Stock.time_sharing_data import router as router4
# 迁徙数据
from Akshare_Data.Migration.migration import router as router56
# 能源数据
from Akshare_Data.Energy.carbon_emission_rights import router as router57
from Akshare_Data.Energy.China_oil_price import router as router58
# 宏观数据
# # 中国宏观数据
from Akshare_Data.Macro.China.China_macro_leverage_ratio import router as router59
from Akshare_Data.Macro.China.economic_status import router as router60
from Akshare_Data.Macro.China.financial_indicators import router as router61
from Akshare_Data.Macro.China.industry_index import router as router62
from Akshare_Data.Macro.China.industry_indicators import router as router63
from Akshare_Data.Macro.China.oil_transportation import router as router64
from Akshare_Data.Macro.China.price_level import router as router65
from Akshare_Data.Macro.China.shipping_index import router as router66
from Akshare_Data.Macro.China.trade_status import router as router67
from Akshare_Data.Macro.China.transportation_index import router as router68
from Akshare_Data.Macro.China.banking_industry_indicators import router as router69
from Akshare_Data.Macro.China.financing_and_securities_lending import router as router70
from Akshare_Data.Macro.China.other_indicators import router as router71
from Akshare_Data.Macro.China.national_bureau_of_statistics import router as router72
from Akshare_Data.Macro.China.financial_market import router as router73
# # 中国香港宏观数据
from Akshare_Data.Macro.HongKong.building_index import router as router74
from Akshare_Data.Macro.HongKong.consumer_index import router as router75
from Akshare_Data.Macro.HongKong.gdp_index import router as router76
from Akshare_Data.Macro.HongKong.other_index import router as router77
# # 美国宏观数据
from Akshare_Data.Macro.America.consumer_income_and_expenditure import router as router78
from Akshare_Data.Macro.America.economic_situation import router as router79
from Akshare_Data.Macro.America.industry_indicators_industry import router as router80
from Akshare_Data.Macro.America.industry_indicators_manufacturing import router as router81
from Akshare_Data.Macro.America.industry_indicators_real_estate import router as router82
from Akshare_Data.Macro.America.industry_indicators_service_industry import router as router83
from Akshare_Data.Macro.America.labour_market import router as router84
from Akshare_Data.Macro.America.leading_indicators import router as router85
from Akshare_Data.Macro.America.other import router as router86
from Akshare_Data.Macro.America.price_level import router as router87
from Akshare_Data.Macro.America.trade_situation import router as router88
# # 欧元区宏观数据
from Akshare_Data.Macro.Eurozone.economic_situation import router as router89
from Akshare_Data.Macro.Eurozone.industry_indicators import router as router90
from Akshare_Data.Macro.Eurozone.leading_indicators import router as router91
# # 德国宏观数据
from Akshare_Data.Macro.Germany.macro_germany import router as router92
# # 瑞士宏观数据
from Akshare_Data.Macro.Switzerland.macro_swiss import router as router93
# # 日本宏观数据
from Akshare_Data.Macro.Japan.macro_japan import router as router94
# # 英国宏观数据
from Akshare_Data.Macro.England.macro_england import router as router95
# # 澳大利亚宏观数据
from Akshare_Data.Macro.Australia.macro_australia import router as router96
# # 加拿大宏观数据
from Akshare_Data.Macro.Canada.macro_canada import router as router97
# # 重要机构宏观数据
from Akshare_Data.Macro.ImportantInstitutions.macro_important_institutions import router as router98
# # 全球宏观数据
from Akshare_Data.Macro.Global.macro_global import router as router99
# 债券数据
from Akshare_Data.Bond.bond_info import router as router100
from Akshare_Data.Bond.bond_sh import router as router101
from Akshare_Data.Bond.bond_basic_data import router as router102
from Akshare_Data.Bond.bond_hs import router as router103
from Akshare_Data.Bond.bond_hs_convertible_bonds import router as router104
from Akshare_Data.Bond.bond_issuance import router as router105
from Akshare_Data.Bond.china_bond_index import router as router106
from Akshare_Data.Bond.bond_china_close_return_map import router as router107
# 期权数据
from Akshare_Data.Option.exchange_commodity_info import router as router108
# # 商品期权
from Akshare_Data.Option.commodity_options.market_data import router as router109
from Akshare_Data.Option.commodity_options.contract_info import router as router110
# # 金融期权
from Akshare_Data.Option.financial_options.market_data import router as router111
from Akshare_Data.Option.financial_options.contract_info import router as router112
from Akshare_Data.Option.financial_options.risk_indicators.zhong_jin_suo import router as router113
from Akshare_Data.Option.financial_options.risk_indicators.three_major_exchanges import router as router114
# 外汇数据
from Akshare_Data.ForeignExchange.foreign_exchange import router as router115
# 指数数据
from Akshare_Data.Index.actual_index import router as router132
from Akshare_Data.Index.Ashare_stock_index_data import router as router133
from Akshare_Data.Index.caixin_index import router as router134
from Akshare_Data.Index.CH_stock_index import router as router135
from Akshare_Data.Index.commodity_spot_price_index import router as router136
from Akshare_Data.Index.guozheng_index import router as router137
from Akshare_Data.Index.highway_logistics_index import router as router138
from Akshare_Data.Index.historical_market_data import router as router139
from Akshare_Data.Index.HK_stock_index import router as router140
from Akshare_Data.Index.index_valuation import router as router141
from Akshare_Data.Index.market_sentiment_index import router as router142
from Akshare_Data.Index.option_volatility_index import router as router143
from Akshare_Data.Index.shenwan_hongyuan_research import router as router144
from Akshare_Data.Index.shenwan_industry_index import router as router145
from Akshare_Data.Index.sugar_index import router as router146
from Akshare_Data.Index.US_stock_index import router as router147
# 其他数据
# # 政策不确定性数据
from Akshare_Data.Others.article_epu_index import router as router148
# # 银行数据
from Akshare_Data.Others.futures_czce_warehouse_receipt import router as router149
# # 交易日历
from Akshare_Data.Others.tool_trade_date_hist_sina import router as router150
# 数据来源：自编写
# 新闻模块
from News.xinwenlianbo import router as router116

app = FastAPI()

# 配置CORS
origins = [
    "http://localhost:36924",
    "http://localhost:36925",
    "http://192.168.1.18:36929",
    "http://192.168.1.18:36927"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class APIInfo(BaseModel):
    api_name: str
    api_path: str
    method: str
    description: str
    parameters: List[Dict[str, Any]]


def process_api_info() -> List[APIInfo]:
    openapi_json = get_openapi(
        title="FinDataAPI",
        version="0.0.1",
        routes=app.routes,
    )

    def resolve_ref(ref, spec):
        """解析$ref引用"""
        parts = ref.lstrip('#/').split('/')
        result = spec
        for part in parts:
            result = result.get(part, {})
        return result

    api_info_list = []

    for path, path_item in openapi_json.get('paths', {}).items():
        for method, operation in path_item.items():
            api_name = operation.get('operationId', '无操作ID')
            api_summary = operation.get('summary', '无描述信息')
            api_description = operation.get('description', '无详细描述')

            parameters = []

            if method == 'post':
                request_body = operation.get('requestBody', {})
                content = request_body.get('content', {})
                for media_type, media_type_object in content.items():
                    schema = media_type_object.get('schema', {})
                    if '$ref' in schema:
                        schema = resolve_ref(schema['$ref'], openapi_json)
                    properties = schema.get('properties', {})
                    required = schema.get('required', [])
                    for param_name, param_info in properties.items():
                        param_type = param_info.get('type', '未知类型')
                        param_description = param_info.get('description', '无描述')
                        param_title = param_info.get('title', '无标题')
                        is_required = param_name in required
                        parameters.append({
                            "name": param_name,
                            "type": param_type,
                            "required": is_required,
                            "description": param_description,
                            "title": param_title
                        })

            api_info = APIInfo(
                api_name=api_name,
                api_path=path,
                method=method,
                description=api_description,
                parameters=parameters
            )
            api_info_list.append(api_info)

    return api_info_list


@app.get("/api_info", response_model=List[APIInfo])
async def get_api_info():
    """
    获取API信息

    这个接口用于获取所有API的相关信息。返回值是一个包含多个API信息对象的列表。

    :return: 包含API信息对象的列表

    :rtype: List[APIInfo]
    """
    api_info = process_api_info()
    return api_info


@app.get("/openapi.json")
async def get_open_api_endpoint():
    """
    获取OpenAPI模式定义

    这个接口用于获取当前应用的OpenAPI模式定义。OpenAPI模式定义包含了应用中所有API的详细信息，包括路径、请求方法、请求参数、响应格式等。

    :return: 包含应用中所有API详细信息的OpenAPI模式定义

    :rtype: dict
    """
    openapi_schema = get_openapi(
        title="FinDataAPI",
        version="0.0.1",
        routes=app.routes,
    )
    return openapi_schema


app.include_router(router1)
app.include_router(router2)
app.include_router(router3)
app.include_router(router4)
app.include_router(router5)
app.include_router(router6)
app.include_router(router7)
app.include_router(router8)
app.include_router(router9)
app.include_router(router10)
app.include_router(router11)
app.include_router(router12)
app.include_router(router13)
app.include_router(router14)
app.include_router(router15)
app.include_router(router16)
app.include_router(router17)
app.include_router(router18)
app.include_router(router19)
app.include_router(router20)
app.include_router(router21)
app.include_router(router22)
app.include_router(router23)
app.include_router(router24)
app.include_router(router25)
app.include_router(router26)
app.include_router(router27)
app.include_router(router28)
app.include_router(router29)
app.include_router(router30)
app.include_router(router31)
app.include_router(router32)
app.include_router(router33)
app.include_router(router34)
app.include_router(router35)
app.include_router(router36)
app.include_router(router37)
app.include_router(router38)
app.include_router(router39)
app.include_router(router40)
app.include_router(router41)
app.include_router(router42)
app.include_router(router43)
app.include_router(router44)
app.include_router(router45)
app.include_router(router46)
app.include_router(router47)
app.include_router(router48)
app.include_router(router49)
app.include_router(router50)
app.include_router(router51)
app.include_router(router52)
app.include_router(router53)
app.include_router(router54)
app.include_router(router55)
app.include_router(router56)
app.include_router(router57)
app.include_router(router58)
app.include_router(router59)
app.include_router(router60)
app.include_router(router61)
app.include_router(router62)
app.include_router(router63)
app.include_router(router64)
app.include_router(router65)
app.include_router(router66)
app.include_router(router67)
app.include_router(router68)
app.include_router(router69)
app.include_router(router70)
app.include_router(router71)
app.include_router(router72)
app.include_router(router73)
app.include_router(router74)
app.include_router(router75)
app.include_router(router76)
app.include_router(router77)
app.include_router(router78)
app.include_router(router79)
app.include_router(router80)
app.include_router(router81)
app.include_router(router82)
app.include_router(router83)
app.include_router(router84)
app.include_router(router85)
app.include_router(router86)
app.include_router(router87)
app.include_router(router88)
app.include_router(router89)
app.include_router(router90)
app.include_router(router91)
app.include_router(router92)
app.include_router(router93)
app.include_router(router94)
app.include_router(router95)
app.include_router(router96)
app.include_router(router97)
app.include_router(router98)
app.include_router(router99)
app.include_router(router100)
app.include_router(router101)
app.include_router(router102)
app.include_router(router103)
app.include_router(router104)
app.include_router(router105)
app.include_router(router106)
app.include_router(router107)
app.include_router(router108)
app.include_router(router109)
app.include_router(router110)
app.include_router(router111)
app.include_router(router112)
app.include_router(router113)
app.include_router(router114)
app.include_router(router115)
app.include_router(router116)
app.include_router(router117)
app.include_router(router118)
app.include_router(router119)
app.include_router(router120)
app.include_router(router121)
app.include_router(router122)
app.include_router(router123)
app.include_router(router124)
app.include_router(router125)
app.include_router(router126)
app.include_router(router127)
app.include_router(router128)
app.include_router(router129)
app.include_router(router130)
app.include_router(router131)
app.include_router(router132)
app.include_router(router133)
app.include_router(router134)
app.include_router(router135)
app.include_router(router136)
app.include_router(router137)
app.include_router(router138)
app.include_router(router139)
app.include_router(router140)
app.include_router(router141)
app.include_router(router142)
app.include_router(router143)
app.include_router(router144)
app.include_router(router145)
app.include_router(router146)
app.include_router(router147)
app.include_router(router148)
app.include_router(router149)
app.include_router(router150)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=36925)
