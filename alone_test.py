import logging

import akshare as ak
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
@app.post("/stock_zh_a_disclosure_report_cninfo",
          operation_id="stock_zh_a_disclosure_report_cninfo")
async def stock_zh_a_disclosure_report_cninfo(request: JuChaoDisclosureRequest):
    """
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=36925, log_level="info")
