import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class ActualIndex(BaseModel):
    symbol: str = Field(..., title="实际指数参数", description="可选择 月度, 季度")


# 指数数据-排污权指数
@router.post("/index_eri", operation_id="post_index_eri")
def post_index_eri(request: ActualIndex):
    """
    指数数据-排污权指数

    接口: index_eri

    目标地址: https://zs.zjpwq.net/

    描述: 浙江省排污权交易指数的数据
    """
    try:
        index_eri = ak.index_eri(
            symbol=request.symbol
        )
        index_eri_df = sanitize_data_pandas(index_eri)

        return index_eri_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DrewryWCIndex(BaseModel):
    symbol: str = Field(..., title="实际指数参数",
                        description="可选择 composite, shanghai-rotterdam, "
                                    "rotterdam-shanghai, shanghai-los angeles, "
                                    "los angeles-shanghai, shanghai-genoa, "
                                    "new york-rotterdam, rotterdam-new york")


# 指数数据-集装箱指数
@router.post("/drewry_wci_index", operation_id="post_drewry_wci_index")
def post_drewry_wci_index(request: DrewryWCIndex):
    """
    指数数据-集装箱指数

    接口: drewry_wci_index

    目标地址: https://infogram.com/world-container-index-1h17493095xl4zj

    描述: Drewry 集装箱指数的数据

    限量: 返回指定类型的数据
    """
    try:
        drewry_wci_index = ak.drewry_wci_index(
            symbol=request.symbol
        )
        drewry_wci_index_df = sanitize_data_pandas(drewry_wci_index)

        return drewry_wci_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
