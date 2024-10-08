import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class OptionCommodityContractSina(BaseModel):
    symbol: str = Field(..., title="合约类型",
                        description="例：黄金期权，可通过 option_commodity_contract_table_sina 获取")


# 期权-商品期权-新浪财经-历史行情
@router.post("/option_commodity_contract_sina",
             operation_id="option_commodity_contract_sina")
def option_commodity_contract_sina(request: OptionCommodityContractSina):
    """
    期权-商品期权-新浪财经-当前合约

    接口: option_commodity_contract_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsDP.php

    描述: 新浪财经-商品期权当前在交易的合约

    限量: 单次返回指定期权名称的所有合约数据
    """
    try:
        option_commodity_contract_sina = ak.option_commodity_contract_sina(
            symbol=request.symbol
        )
        option_commodity_contract_sina_df = sanitize_data_pandas(option_commodity_contract_sina)

        return option_commodity_contract_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
