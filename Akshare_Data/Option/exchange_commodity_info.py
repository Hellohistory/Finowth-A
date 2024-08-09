import json

from fastapi import APIRouter, HTTPException

router = APIRouter()

JSON_FILE_PATH_1 = 'Akshare_Data/Option/json/上期所商品期权品种.json'
JSON_FILE_PATH_2 = 'Akshare_Data/Option/json/大商所商品期权品种.json'
JSON_FILE_PATH_3 = 'Akshare_Data/Option/json/郑商所商品期权品种.json'
JSON_FILE_PATH_4 = 'Akshare_Data/Option/json/广商所商品期权品种.json'
JSON_FILE_PATH_5 = 'Akshare_Data/Option/json/金融期权合约名称一览表.json'


@router.get("/options_of_the_previous_stock_exchange",
            operation_id="options_of_the_previous_stock_exchange")
async def options_of_the_previous_stock_exchange():
    """
    期权-金融期权-金融期权合约名称一览表

    获取金融期权合约名称一览表
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


@router.get("/options_dalian_commodity_exchange",
            operation_id="options_dalian_commodity_exchange")
async def options_dalian_commodity_exchange():
    """
    期权-大商所-商品期权-商品期权合约名称一览表

    获取金融期权合约名称一览表
    """
    try:
        with open(JSON_FILE_PATH_2, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="文件未找到")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 解码错误")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")


@router.get("/options_zhengzhou_commodity_exchange",
            operation_id="options_zhengzhou_commodity_exchange")
async def options_zhengzhou_commodity_exchange():
    """
    期权-郑商所-商品期权-商品期权合约名称一览表

    获取金融期权合约名称一览表
    """
    try:
        with open(JSON_FILE_PATH_3, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="文件未找到")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 解码错误")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")


@router.get("/options_guangzhou_commodity_exchange",
            operation_id="options_guangzhou_commodity_exchange")
async def options_guangzhou_commodity_exchange():
    """
    期权-郑商所-商品期权-商品期权合约名称一览表

    获取金融期权合约名称一览表
    """
    try:
        with open(JSON_FILE_PATH_4, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="文件未找到")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 解码错误")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")


@router.get("/option_list_of_financial_option_contract_names",
            operation_id="option_list_of_financial_option_contract_names")
async def option_list_of_financial_option_contract_names():
    """
    期权-金融期权-金融期权合约名称一览表

    获取金融期权合约名称一览表
    """
    try:
        with open(JSON_FILE_PATH_5, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="文件未找到")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="JSON 解码错误")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")
