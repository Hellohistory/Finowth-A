import json

from fastapi import APIRouter, HTTPException

router = APIRouter()

JSON_FILE_PATH_1 = 'Akshare_Data/Option/json/期货交易所信息.json'


@router.get("/futures_exchange_info",
            operation_id="get_futures_exchange_info")
async def get_futures_exchange_info():
    """
    期货数据-期货基础信息-期货交易所

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
