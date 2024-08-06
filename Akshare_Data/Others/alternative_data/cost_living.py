import json

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()

JSON_FILE_PATH_1 = 'Akshare_Data/Others/alternative_data/Json/城市一览表.json'


# 另类数据-生活成本-城市一览表
@router.get("/cost_living_info",
            operation_id="get_cost_living_info")
async def get_cost_living_info():
    """
    另类数据-生活成本-城市一览表

    获取城市一览表
    """
    try:
        with open(JSON_FILE_PATH_1, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="文件未找到")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 解码错误")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")


class CostLiving(BaseModel):
    symbol: str = Field(..., title="城市名称", description="通过 cost_living_info 获取城市名称")


# 另类数据-生活成本
@router.post("/cost_living",
             operation_id="post_cost_living")
def post_cost_living(request: CostLiving):
    """
    另类数据-生活成本

    接口: cost_living

    目标地址: https://expatistan.com/cost-of-living/index

    描述: 世界各大城市生活成本数据

    限量: 返回当前时点所有数据
    """
    try:
        cost_living = ak.cost_living(
            symbol=request.symbol
        )
        cost_living_df = sanitize_data_pandas(cost_living)

        return cost_living_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
