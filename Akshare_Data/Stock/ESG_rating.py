import akshare as ak
from fastapi import HTTPException, APIRouter

router = APIRouter()


# ESG 评级数据
@router.get("/stock_esg_rate_sina", operation_id="get_stock_esg_rate_sina")
def get_stock_esg_rate_sina():
    """
    接口: stock_esg_rate_sina
    目标地址: https://finance.sina.com.cn/esg/grade.shtml
    描述: 新浪财经-ESG评级中心-ESG评级-ESG评级数据
    限量: 单次返回所有数据
    """
    try:
        stock_esg_rate_sina_df = ak.stock_esg_rate_sina()
        return stock_esg_rate_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# MSCI
@router.get("/stock_esg_msci_sina", operation_id="get_stock_esg_msci_sina")
def get_stock_esg_msci_sina():
    """
    接口: stock_esg_msci_sina
    目标地址: https://finance.sina.com.cn/esg/grade.shtml
    描述: 新浪财经-ESG评级中心-ESG评级-MSCI
    限量: 单次返回所有数据
    """
    try:
        stock_esg_msci_sina_df = ak.stock_esg_msci_sina()
        return stock_esg_msci_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 路孚特
@router.get("/stock_esg_rft_sina", operation_id="get_stock_esg_rft_sina")
def get_stock_esg_rft_sina():
    """
    接口: stock_esg_rft_sina
    目标地址: https://finance.sina.com.cn/esg/grade.shtml
    描述: 新浪财经-ESG评级中心-ESG评级-路孚特
    限量: 单次返回所有数据
    """
    try:
        stock_esg_rft_sina_df = ak.stock_esg_rft_sina()
        return stock_esg_rft_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 秩鼎
@router.get("/stock_esg_zd_sina", operation_id="get_stock_esg_zd_sina")
def get_stock_esg_zd_sina():
    """
    接口: stock_esg_zd_sina
    目标地址: https://finance.sina.com.cn/esg/grade.shtml
    描述: 新浪财经-ESG评级中心-ESG评级-秩鼎
    限量: 单次返回所有数据
    """
    try:
        stock_esg_zd_sina_df = ak.stock_esg_zd_sina()
        return stock_esg_zd_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 华证指数
@router.get("/stock_esg_hz_sina", operation_id="get_stock_esg_hz_sina")
def get_stock_esg_hz_sina():
    """
    接口: stock_esg_hz_sina
    目标地址: https://finance.sina.com.cn/esg/grade.shtml
    描述: 新浪财经-ESG评级中心-ESG评级-华证指数
    限量: 单次返回所有数据
    """
    try:
        stock_esg_hz_sina_df = ak.stock_esg_hz_sina()
        return stock_esg_hz_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
