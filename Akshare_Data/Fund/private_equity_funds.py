import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 会员机构综合查询
@router.get("/fund_amac_member_info", operation_id="get_fund_amac_member_info")
async def get_fund_amac_member_info():
    """
    会员机构综合查询

    接口: fund_amac_member_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html

    描述: 中国证券投资基金业协会-信息公示-会员信息-会员机构综合查询

    限量: 单次返回当前时刻所有历史数据
    """
    fund_amac_member_info = ak.amac_member_info()
    fund_amac_member_info_df = sanitize_data_pandas(fund_amac_member_info)

    return fund_amac_member_info_df.to_dict(orient="records")


class InterestSymbolRequest(BaseModel):
    symbol: str = Field(..., title="信息类型",
                        description="可选择：公募基金管理公司, 公募基金管理公司资管子公司, 商业银行, "
                                    "证券公司, 证券公司子公司, 私募基金管理人, 保险公司子公司, 保险公司, "
                                    "外包服务机构, 期货公司, 期货公司资管子公司, 媒体机构, 证券投资咨询机构, "
                                    "评价机构, 外资私募证券基金管理人, 支付结算, 独立服务机构, 地方自律组织, "
                                    "境外机构, 律师事务所, 会计师事务所, 交易所, 独立第三方销售机构, 证券公司资管子公司, 证券公司私募基金子公司, 其他")


# 基金从业人员资格注册信息
@router.post("/fund_amac_person_fund_org_list", operation_id="post_fund_amac_person_fund_org_list")
def post_fund_amac_person_fund_org_list(request: InterestSymbolRequest):
    """
    基金从业人员资格注册信息

    接口: fund_amac_person_fund_org_list

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/person/personOrgList.html

    描述: 中国证券投资基金业协会-信息公示-从业人员信息-基金从业人员资格注册信息

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_person_fund_org_list = ak.amac_person_fund_org_list(symbol=request.symbol)
        fund_amac_person_fund_org_list_df = sanitize_data_pandas(fund_amac_person_fund_org_list)

        return fund_amac_person_fund_org_list_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 私募基金-从业人员信息-债券投资交易相关人员公示
@router.get("/fund_amac_person_fund_org_list", operation_id="get_fund_amac_person_bond_org_list")
async def get_fund_amac_person_bond_org_list():
    """
    私募基金-从业人员信息-债券投资交易相关人员公示

    接口: fund_amac_person_fund_org_list

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/person/personOrgList.html

    描述: 中国证券投资基金业协会-信息公示-从业人员信息-债券投资交易相关人员公示

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_person_bond_org_list = ak.amac_person_bond_org_list()
        fund_amac_person_bond_org_list_df = sanitize_data_pandas(fund_amac_person_bond_org_list)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_person_bond_org_list_df.to_dict(orient="records")


# 私募基金管理人综合查询
@router.get("/fund_amac_manager_info", operation_id="get_fund_amac_manager_info")
async def get_fund_amac_manager_info():
    """
    私募基金管理人综合查询

    接口: amac_manager_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html

    描述: 中国证券投资基金业协会-信息公示-私募基金管理人公示-私募基金管理人综合查询

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_manager_info = ak.amac_manager_info()
        fund_amac_manager_info_df = sanitize_data_pandas(fund_amac_manager_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_manager_info_df.to_dict(orient="records")


# 私募基金管理人分类公示
@router.get("/fund_amac_manager_classify_info", operation_id="get_fund_amac_manager_classify_info")
async def get_fund_amac_manager_classify_info():
    """
    私募基金管理人分类公示

    接口: fund_amac_manager_classify_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/manager/managerList.html

    描述: 中国证券投资基金业协会-信息公示-私募基金管理人公示-私募基金管理人分类公示

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_manager_classify_info = ak.amac_manager_classify_info()
        fund_amac_manager_classify_info_df = sanitize_data_pandas(fund_amac_manager_classify_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_manager_classify_info_df.to_dict(orient="records")


# 证券公司私募基金子公司管理人信息公示
@router.get("/fund_amac_member_sub_info", operation_id="get_fund_amac_member_sub_info")
async def get_fund_amac_member_sub_info():
    """
    证券公司私募基金子公司管理人信息公示

    接口: fund_amac_member_sub_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/member/index.html?primaryInvestType=private

    描述: 中国证券投资基金业协会-信息公示-私募基金管理人公示-证券公司私募基金子公司管理人信息公示

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_member_sub_info = ak.amac_member_sub_info()
        fund_amac_member_sub_info_df = sanitize_data_pandas(fund_amac_member_sub_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_member_sub_info_df.to_dict(orient="records")


class StartEndRequest(BaseModel):
    start_page: str = Field(..., title="起始页码", description="例：1")
    end_page: str = Field(..., title="结束页码", description="例：100")


# 基金从业人员资格注册信息
@router.post("/fund_amac_fund_info", operation_id="post_fund_amac_fund_info")
def post_fund_amac_fund_info(request: StartEndRequest):
    """
    私募基金管理人基金产品

    接口: fund_amac_fund_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/fund/index.html

    描述: 中国证券投资基金业协会-信息公示-基金产品公示-私募基金管理人基金产品

    限量: 单次返回指定页码之间的所有历史数据, 其中与每页 100 条的目标网站对应; 默认返回所有数据
    """
    try:
        fund_amac_fund_info = ak.amac_fund_info(
            start_page=request.start_page,
            end_page=request.end_page
        )
        fund_amac_fund_info_df = sanitize_data_pandas(fund_amac_fund_info)

        return fund_amac_fund_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 证券公司集合资管产品公示
@router.get("/fund_amac_securities_info", operation_id="get_fund_amac_securities_info")
async def get_fund_amac_securities_info():
    """
    证券公司集合资管产品公示

    接口: fund_amac_securities_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/securities/index.html

    描述: 中国证券投资基金业协会-信息公示-基金产品公示-证券公司集合资管产品公示

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_securities_info = ak.amac_securities_info()
        fund_amac_securities_info_df = sanitize_data_pandas(fund_amac_securities_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_securities_info_df.to_dict(orient="records")


# 证券公司直投基金
@router.get("/fund_amac_aoin_info", operation_id="get_fund_amac_aoin_info")
async def get_fund_amac_aoin_info():
    """
    证券公司直投基金

    接口: fund_amac_aoin_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/aoin/product/index.html

    描述: 中国证券投资基金业协会-信息公示-基金产品公示-证券公司直投基金

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_aoin_info = ak.amac_aoin_info()
        fund_amac_aoin_info_df = sanitize_data_pandas(fund_amac_aoin_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_aoin_info_df.to_dict(orient="records")


# 证券公司私募投资基金
@router.get("/fund_amac_fund_sub_info", operation_id="get_fund_amac_fund_sub_info")
async def get_fund_amac_fund_sub_info():
    """
    证券公司私募投资基金

    接口: fund_amac_fund_sub_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/subfund/index.html

    描述: 中国证券投资基金业协会-信息公示-基金产品公示-证券公司私募投资基金

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_fund_sub_info = ak.amac_fund_sub_info()
        fund_amac_fund_sub_info_df = sanitize_data_pandas(fund_amac_fund_sub_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_fund_sub_info_df.to_dict(orient="records")


# 基金公司及子公司集合资管产品公示
@router.get("/fund_amac_fund_account_info", operation_id="get_fund_amac_fund_account_info")
async def get_fund_amac_fund_account_info():
    """
    基金公司及子公司集合资管产品公示

    接口: fund_amac_fund_account_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/fund/account/index.html

    描述: 中国证券投资基金业协会-信息公示-基金产品公示-基金公司及子公司集合资管产品公示

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_fund_account_info = ak.amac_fund_account_info()
        fund_amac_fund_account_info_df = sanitize_data_pandas(fund_amac_fund_account_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_fund_account_info_df.to_dict(orient="records")


# 资产支持专项计划
@router.get("/fund_amac_fund_abs", operation_id="get_fund_amac_fund_abs")
async def get_fund_amac_fund_abs():
    """
    资产支持专项计划

    接口: fund_amac_fund_abs

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/fund/abs/index.html

    描述: 中国证券投资基金业协会-信息公示-产品公示-资产支持专项计划

    限量: 单次返回当前时刻所有历史数据，数据量较大，获取时间较长，请耐心等待
    """
    try:
        fund_amac_fund_abs = ak.amac_fund_abs()
        fund_amac_fund_abs_df = sanitize_data_pandas(fund_amac_fund_abs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_fund_abs_df.to_dict(orient="records")


# 期货公司集合资管产品公示
@router.get("/fund_amac_futures_info", operation_id="get_fund_amac_futures_info")
async def get_fund_amac_futures_info():
    """
    期货公司集合资管产品公示

    接口: fund_amac_futures_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/pof/futures/index.html

    描述: 中国证券投资基金业协会-信息公示-基金产品公示-期货公司集合资管产品公示

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_futures_info = ak.amac_futures_info()
        fund_amac_futures_info_df = sanitize_data_pandas(fund_amac_futures_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_amac_futures_info_df.to_dict(orient="records")


# 已注销私募基金管理人名单
@router.get("/fund_amac_manager_cancelled_info", operation_id="get_fund_amac_manager_cancelled_info")
async def get_fund_amac_manager_cancelled_info():
    """
    已注销私募基金管理人名单

    接口: fund_amac_manager_cancelled_info

    目标地址: https://gs.amac.org.cn/amac-infodisc/res/cancelled/manager/index.html

    描述: 中国证券投资基金业协会-信息公示-诚信信息-已注销私募基金管理人名单

    限量: 单次返回当前时刻所有历史数据
    """
    try:
        fund_amac_manager_cancelled_info = ak.amac_manager_cancelled_info()
        fund_amac_manager_cancelled_info_df = sanitize_data_pandas(fund_amac_manager_cancelled_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")
