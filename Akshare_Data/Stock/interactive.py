import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class IrmSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：002594")


# 互动易-提问
@router.post("/stock_irm_cninfo", operation_id="post_stock_irm_cninfo")
async def post_stock_irm_cninfo(request: IrmSymbolRequest):
    """
    互动易-提问

    接口: stock_irm_cninfo

    目标地址: https://irm.cninfo.com.cn/

    描述: 互动易-提问

    限量: 单次返回近期 10000 条提问数据
    """
    try:
        stock_irm_cninfo = ak.stock_irm_cninfo(symbol=request.symbol)
        stock_irm_cninfo_df = sanitize_data_pandas(stock_irm_cninfo)
        return stock_irm_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IrmAnsSymbolRequest(BaseModel):
    symbol: str = Field(..., title="提问者编号",
                        description="通过stock_irm_cninfo来获取具体的提问者编号")


# 互动易-回答
@router.post("/stock_irm_ans_cninfo", operation_id="post_stock_irm_ans_cninfo")
async def post_stock_irm_ans_cninfo(request: IrmAnsSymbolRequest):
    """
    互动易-回答

    接口: stock_irm_ans_cninfo

    目标地址: https://irm.cninfo.com.cn/

    描述: 互动易-回答

    限量: 单次返回指定个股的回答数据
    """
    try:
        stock_irm_ans_cninfo = ak.stock_irm_ans_cninfo(symbol=request.symbol)
        stock_irm_ans_cninfo_df = sanitize_data_pandas(stock_irm_ans_cninfo)
        return stock_irm_ans_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ShESymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：603119")


# 上证e互动-提问与回答
@router.post("/stock_sns_sseinfo", operation_id="post_stock_sns_sseinfo")
async def post_stock_sns_sseinfo(request: ShESymbolRequest):
    """
    上证e互动-提问与回答

    接口: stock_sns_sseinfo

    目标地址: https://sns.sseinfo.com/company.do?uid=65

    描述: 上证e互动-提问与回答

    限量: 单次返回指定个股的提问与回答数据
    """
    try:
        stock_sns_sseinfo = ak.stock_sns_sseinfo(symbol=request.symbol)
        stock_sns_sseinfo_df = sanitize_data_pandas(stock_sns_sseinfo)
        return stock_sns_sseinfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
