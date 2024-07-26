import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-行业指数-菜篮子产品批发价格指数
@router.get("/macro_china_vegetable_basket", operation_id="get_macro_china_vegetable_basket")
async def get_macro_china_vegetable_basket():
    """
    国民经济运行状况-行业指数-菜篮子产品批发价格指数

    接口: macro_china_vegetable_basket

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00009275.html

    描述: 菜篮子产品批发价格指数, 数据区间从 20050927-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_vegetable_basket = ak.macro_china_vegetable_basket()
        macro_china_vegetable_basket_df = sanitize_data_pandas(macro_china_vegetable_basket)
        return macro_china_vegetable_basket_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-农产品批发价格总指数
@router.get("/macro_china_agricultural_product", operation_id="get_macro_china_agricultural_product")
async def get_macro_china_agricultural_product():
    """
    国民经济运行状况-行业指数-农产品批发价格总指数

    接口: macro_china_agricultural_product

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00009274.html

    描述: 农产品批发价格总指数, 数据区间从 20050927-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_agricultural_product = ak.macro_china_agricultural_product()
        macro_china_agricultural_product_df = sanitize_data_pandas(macro_china_agricultural_product)
        return macro_china_agricultural_product_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-农副指数
@router.get("/macro_china_agricultural_index", operation_id="get_macro_china_agricultural_index")
async def get_macro_china_agricultural_index():
    """
    国民经济运行状况-行业指数-农副指数

    接口: macro_china_agricultural_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662543.html

    描述: 农副指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_agricultural_index = ak.macro_china_agricultural_index()
        macro_china_agricultural_index_df = sanitize_data_pandas(macro_china_agricultural_index)
        return macro_china_agricultural_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-能源指数
@router.get("/macro_china_energy_index", operation_id="get_macro_china_energy_index")
async def get_macro_china_energy_index():
    """
    国民经济运行状况-行业指数-能源指数

    接口: macro_china_agricultural_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662543.html

    描述: 农副指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_energy_index = ak.macro_china_energy_index()
        macro_china_energy_index_df = sanitize_data_pandas(macro_china_energy_index)
        return macro_china_energy_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-大宗商品价格
@router.get("/macro_china_commodity_price_index", operation_id="get_macro_china_commodity_price_index")
async def get_macro_china_commodity_price_index():
    """
    国民经济运行状况-行业指数-大宗商品价格

    接口: macro_china_agricultural_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662543.html

    描述: 农副指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_commodity_price_index = ak.macro_china_commodity_price_index()
        macro_china_commodity_price_index_df = sanitize_data_pandas(macro_china_commodity_price_index)
        return macro_china_commodity_price_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-费城半导体指数
@router.get("/macro_global_sox_index", operation_id="get_macro_global_sox_index")
async def get_macro_global_sox_index():
    """
    国民经济运行状况-行业指数-费城半导体指数

    接口: macro_global_sox_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00055562.html

    描述: 费城半导体指数数据, 数据区间从 19940504-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_global_sox_index = ak.macro_global_sox_index()
        macro_global_sox_index_df = sanitize_data_pandas(macro_global_sox_index)
        return macro_global_sox_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-义乌小商品指数-电子元器件
@router.get("/macro_china_yw_electronic_index", operation_id="get_macro_china_yw_electronic_index")
async def get_macro_china_yw_electronic_index():
    """
    国民经济运行状况-行业指数-义乌小商品指数-电子元器件

    接口: macro_china_yw_electronic_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00055551.html

    描述: 义乌小商品指数-电子元器件数据, 数据区间从 20060911-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_yw_electronic_index = ak.macro_china_yw_electronic_index()
        macro_china_yw_electronic_index_df = sanitize_data_pandas(macro_china_yw_electronic_index)
        return macro_china_yw_electronic_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-建材指数
@router.get("/macro_china_construction_index", operation_id="get_macro_china_construction_index")
async def get_macro_china_construction_index():
    """
    国民经济运行状况-行业指数-建材指数

    接口: macro_china_construction_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662541.html

    描述: 建材指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_construction_index = ak.macro_china_construction_index()
        macro_china_construction_index_df = sanitize_data_pandas(macro_china_construction_index)
        return macro_china_construction_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-建材价格指数
@router.get("/macro_china_construction_price_index",
            operation_id="get_macro_china_construction_price_index")
async def get_macro_china_construction_price_index():
    """
    国民经济运行状况-行业指数-建材价格指数

    接口: macro_china_construction_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662541.html

    描述: 建材指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_construction_price_index = ak.macro_china_construction_price_index()
        macro_china_construction_price_index_df = sanitize_data_pandas(macro_china_construction_price_index)
        return macro_china_construction_price_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-建材价格指数
@router.get("/macro_china_construction_price_index",
            operation_id="get_macro_china_construction_price_index")
async def get_macro_china_construction_price_index():
    """
    国民经济运行状况-行业指数-建材价格指数

    接口: macro_china_construction_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662541.html

    描述: 建材指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_construction_price_index = ak.macro_china_construction_price_index()
        macro_china_construction_price_index_df = sanitize_data_pandas(macro_china_construction_price_index)
        return macro_china_construction_price_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-建材价格指数
@router.get("/macro_china_construction_price_index",
            operation_id="get_macro_china_construction_price_index")
async def get_macro_china_construction_price_index():
    """
    国民经济运行状况-行业指数-建材价格指数

    接口: macro_china_construction_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662541.html

    描述: 建材指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_construction_price_index = ak.macro_china_construction_price_index()
        macro_china_construction_price_index_df = sanitize_data_pandas(macro_china_construction_price_index)
        return macro_china_construction_price_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-物流景气指数
@router.get("/macro_china_lpi_index",
            operation_id="get_macro_china_lpi_index")
async def get_macro_china_lpi_index():
    """
    国民经济运行状况-行业指数-物流景气指数

    接口: macro_china_construction_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00662541.html

    描述: 建材指数数据, 数据区间从 20111205-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_lpi_index = ak.macro_china_lpi_index()
        macro_china_lpi_index_df = sanitize_data_pandas(macro_china_lpi_index)
        return macro_china_lpi_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-商品零售价格指数
@router.get("/macro_china_retail_price_index",
            operation_id="get_macro_china_retail_price_index")
async def get_macro_china_retail_price_index():
    """
    国民经济运行状况-行业指数-商品零售价格指数

    接口: macro_china_retail_price_index

    目标地址: http://finance.sina.com.cn/mac/#price-12-0-31-1

    描述: 国家统计局-商品零售价格指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_retail_price_index = ak.macro_china_retail_price_index()
        macro_china_retail_price_index_df = sanitize_data_pandas(macro_china_retail_price_index)
        return macro_china_retail_price_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-国房景气指数
@router.get("/macro_china_real_estate",
            operation_id="get_macro_china_real_estate")
async def get_macro_china_real_estate():
    """
    国民经济运行状况-行业指数-国房景气指数

    接口: macro_china_real_estate

    目标地址: http://data.eastmoney.com/cjsj/hyzs_list_EMM00121987.html

    描述: 国家统计局-国房景气指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_real_estate = ak.macro_china_real_estate()
        macro_china_real_estate_df = sanitize_data_pandas(macro_china_real_estate)
        return macro_china_real_estate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
