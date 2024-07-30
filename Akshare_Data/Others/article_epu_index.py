import json

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()

JSON_FILE_PATH_1 = 'Akshare_Data/Others/Json/政策不确定性数据_国家和地区指数_国家和地区一览表.json'


class ArticleEpuIndex(BaseModel):
    symbol: str = Field(..., title="国家和地区一览表-英文名词",
                        description="例：China，可通过 article_epu_index_info 请求")


# 政策不确定性数据-国家和地区指数
@router.post("/article_epu_index",
             operation_id="post_article_epu_index")
def post_article_epu_index(request: ArticleEpuIndex):
    """
    政策不确定性数据-国家和地区指数

    接口: article_epu_index

    目标地址: https://www.policyuncertainty.com/index.html

    描述: 国家或地区的经济政策不确定性(EPU)数据

    限量: 单次返回某个具体国家或地区的所有月度经济政策不确定性数据
    """
    try:
        article_epu_index = ak.article_epu_index(
            symbol=request.symbol,
        )
        article_epu_index_df = sanitize_data_pandas(article_epu_index)

        return article_epu_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 政策不确定性数据-国家和地区指数-国家和地区一览表
@router.get("/article_epu_index_info",
            operation_id="get_article_epu_index_info")
async def get_article_epu_index_info():
    """
    政策不确定性数据-国家和地区指数-国家和地区一览表

    获取期货交易所信息一览表
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
