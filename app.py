import uvicorn
from fastapi import FastAPI
from Akshare_Data.Stock.AH_data import router as router1
from Akshare_Data.Stock.A_stocksother_data import router as router2
from Akshare_Data.Stock.stock_market_overview import router as router3
from Akshare_Data.Stock.time_sharing_data import router as router4
from Akshare_Data.Stock.real_time_quotes import router as router5
from Akshare_Data.Stock.historical_data import router as router6
from Akshare_Data.Stock.science_and_technology_innovation_board_data import router as router7
from Akshare_Data.Stock.US_stocks import router as router8
from Akshare_Data.Stock.HK_stocks import router as router9
from Akshare_Data.Stock.basic_market import router as router11
from Akshare_Data.Stock.goodwill import router as router12
from Akshare_Data.Stock.stock_account_statistics import router as router13
from Akshare_Data.Stock.stock_pledge import router as router14
from Akshare_Data.Stock.stock_evaluation import router as router15
from Akshare_Data.Stock.SHK_stock_connect import router as router16
from Akshare_Data.Stock.featured_data import router as router17
from Akshare_Data.Stock.new_shares import router as router18
from Akshare_Data.Stock.financial_report_issuance import router as router19
from Akshare_Data.Stock.dividend import router as router20
from Akshare_Data.Stock.capital_flows import router as router21
from Akshare_Data.Stock.other import router as router22
from Akshare_Data.Stock.Basic_Data.financial_research_report import router as router23
from Akshare_Data.Stock.Basic_Data.shareholder_info import router as router24
from Akshare_Data.Stock.Basic_Data.unlock_data import router as router25
from Akshare_Data.Stock.Basic_Data.stock_info import router as router26
from Akshare_Data.Stock.Basic_Data.institutional_info import router as router27
from Akshare_Data.Stock.Basic_Data.executive_info import router as router28
from Akshare_Data.Stock.Basic_Data.special_topic_tatistics import router as router29
from Akshare_Data.Stock.Basic_Data.fund import router as router30
from Akshare_Data.Stock.Basic_Data.winners_list import router as router31
from Akshare_Data.Stock.Basic_Data.basic import router as router32
from Akshare_Data.Stock.large_transactions import router as router33
from Akshare_Data.Stock.margin_margin_trading import router as router34
from Akshare_Data.Stock.profit_prediction import router as router35
from Akshare_Data.Stock.concept_section import router as router36
from Akshare_Data.Stock.industry_sector import router as router37
from Akshare_Data.Stock.stock_popularity import router as router38
from Akshare_Data.Stock.his_trends_fan_char import router as router39
from Akshare_Data.Stock.daily_limit import router as router40
from Akshare_Data.Stock.technical_indicators import router as router41
from Akshare_Data.Stock.ESG_rating import router as router42
from Akshare_Data.Stock.stock_institutional_survey_statisticsj import router as router43
from Akshare_Data.Stock.stock_changes_em import router as router44
from Akshare_Data.Stock.info_data import router as router45
from Akshare_Data.Stock.stock_financial_abstract import router as router46
from Akshare_Data.Stock.stock_sector_spot import router as router47
from Akshare_Data.Stock.stock_a_indicator_lg import router as router48
from Akshare_Data.doc import router as router49
from Akshare_Data.Stock.Basic_Data.AUH_index import router as router50
from Akshare_Data.Stock.stock_hk_indicator_eniu import router as router51
from Akshare_Data.Stock.Basic_Data.IPO_review import router as router52

app = FastAPI()

app.include_router(router1)
app.include_router(router2)
app.include_router(router3)
app.include_router(router4)
app.include_router(router5)
app.include_router(router6)
app.include_router(router7)
app.include_router(router8)
app.include_router(router9)
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=36925)
