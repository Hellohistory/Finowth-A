import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-财新指数-综合 PMI
@router.get("/index_pmi_com_cx", operation_id="get_index_pmi_com_cx")
def get_index_pmi_com_cx():
    """
    指数数据-财新指数-综合 PMI

    接口: index_pmi_com_cx

    目标地址: https://yun.ccxe.com.cn/indices/pmi

    描述: 财新数据-指数报告-财新中国 PMI-综合 PMI

    限量: 该接口返回所有历史数据
    """
    try:
        index_pmi_com_cx = ak.index_pmi_com_cx()
        data = index_pmi_com_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-制造业 PMI
@router.get("/index_pmi_man_cx", operation_id="get_index_pmi_man_cx")
def get_index_pmi_man_cx():
    """
    指数数据-财新指数-制造业 PMI

    接口: index_pmi_man_cx

    目标地址: https://yun.ccxe.com.cn/indices/pmi

    描述: 财新数据-指数报告-财新中国 PMI-制造业 PMI

    限量: 该接口返回所有历史数据
    """
    try:
        index_pmi_man_cx = ak.index_pmi_man_cx()
        data = index_pmi_man_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-服务业 PMI
@router.get("/index_pmi_ser_cx", operation_id="get_index_pmi_ser_cx")
def get_index_pmi_ser_cx():
    """
    指数数据-财新指数-服务业 PMI

    接口: index_pmi_ser_cx

    目标地址: https://yun.ccxe.com.cn/indices/pmi

    描述: 财新数据-指数报告-财新中国 PMI-服务业 PMI

    限量: 该接口返回所有历史数据
    """
    try:
        index_pmi_man_cx = ak.index_pmi_man_cx()
        data = index_pmi_man_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-数字经济指数
@router.get("/index_dei_cx", operation_id="get_index_dei_cx")
def get_index_dei_cx():
    """
    指数数据-财新指数-数字经济指数

    接口: index_dei_cx

    目标地址: https://yun.ccxe.com.cn/indices/dei

    描述: 财新指数-数字经济指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_dei_cx = ak.index_dei_cx()
        data = index_dei_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-产业指数
@router.get("/index_ii_cx", operation_id="get_index_ii_cx")
def get_index_ii_cx():
    """
    指数数据-财新指数-产业指数

    接口: index_ii_cx

    目标地址: https://yun.ccxe.com.cn/indices/dei

    描述: 财新指数-产业指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_ii_cx = ak.index_ii_cx()
        data = index_ii_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-溢出指数
@router.get("/index_si_cx", operation_id="get_index_si_cx")
def get_index_si_cx():
    """
    指数数据-财新指数-溢出指数

    接口: index_si_cx

    目标地址: https://yun.ccxe.com.cn/indices/dei

    描述: 财新指数-溢出指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_si_cx = ak.index_si_cx()
        data = index_si_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-融合指数
@router.get("/index_fi_cx", operation_id="get_index_fi_cx")
def get_index_fi_cx():
    """
    指数数据-财新指数-融合指数

    接口: index_fi_cx

    目标地址: https://yun.ccxe.com.cn/indices/dei

    描述: 财新指数-融合指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_fi_cx = ak.index_fi_cx()
        data = index_fi_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-基础指数
@router.get("/index_bi_cx", operation_id="get_index_bi_cx")
def get_index_bi_cx():
    """
    指数数据-财新指数-融合指数

    接口: index_bi_cx

    目标地址: https://yun.ccxe.com.cn/indices/dei

    描述: 财新指数-基础指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_bi_cx = ak.index_bi_cx()
        data = index_bi_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-中国新经济指数
@router.get("/index_nei_cx", operation_id="get_index_nei_cx")
def get_index_nei_cx():
    """
    指数数据-财新指数-中国新经济指数

    接口: index_nei_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-中国新经济指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_nei_cx = ak.index_nei_cx()
        data = index_nei_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-劳动力投入指数
@router.get("/index_li_cx", operation_id="get_index_li_cx")
def get_index_li_cx():
    """
    指数数据-财新指数-劳动力投入指数

    接口: index_li_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-劳动力投入指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_li_cx = ak.index_li_cx()
        data = index_li_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-资本投入指数
@router.get("/index_ci_cx", operation_id="get_index_ci_cx")
def get_index_ci_cx():
    """
    指数数据-财新指数-资本投入指数

    接口: index_ci_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-资本投入指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_ci_cx = ak.index_ci_cx()
        data = index_ci_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-科技投入指数
@router.get("/index_ti_cx", operation_id="get_index_ti_cx")
def get_index_ti_cx():
    """
    指数数据-财新指数-科技投入指数

    接口: index_ti_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-科技投入指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_ti_cx = ak.index_ti_cx()
        data = index_ti_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-新经济行业入职平均工资水平
@router.get("/index_neaw_cx", operation_id="get_index_neaw_cx")
def get_index_neaw_cx():
    """
    指数数据-财新指数-新经济行业入职平均工资水平

    接口: index_neaw_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-新经济行业入职平均工资水平

    限量: 该接口返回所有历史数据
    """
    try:
        index_neaw_cx = ak.index_neaw_cx()
        data = index_neaw_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-新经济入职工资溢价水平
@router.get("/index_awpr_cx", operation_id="get_index_awpr_cx")
def get_index_awpr_cx():
    """
    指数数据-财新指数-新经济入职工资溢价水平

    接口: index_awpr_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-新经济入职工资溢价水平

    限量: 该接口返回所有历史数据
    """
    try:
        index_awpr_cx = ak.index_awpr_cx()
        data = index_awpr_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-大宗商品指数
@router.get("/index_cci_cx", operation_id="get_index_cci_cx")
def get_index_cci_cx():
    """
    指数数据-财新指数-大宗商品指数

    接口: index_cci_cx

    目标地址: https://yun.ccxe.com.cn/indices/nei

    描述: 财新指数-大宗商品指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_cci_cx = ak.index_cci_cx()
        data = index_cci_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-高质量因子
@router.get("/index_qli_cx", operation_id="get_index_qli_cx")
def get_index_qli_cx():
    """
    指数数据-财新指数-高质量因子

    接口: index_qli_cx

    目标地址: https://yun.ccxe.com.cn/indices/qli

    描述: 财新指数-高质量因子

    限量: 该接口返回所有历史数据
    """
    try:
        index_qli_cx = ak.index_qli_cx()
        data = index_qli_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-AI策略指数
@router.get("/index_ai_cx", operation_id="get_index_ai_cx")
def get_index_ai_cx():
    """
    指数数据-财新指数-AI策略指数

    接口: index_ai_cx

    目标地址: https://yun.ccxe.com.cn/indices/ai

    描述: 财新指数-AI策略指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_ai_cx = ak.index_ai_cx()
        data = index_ai_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-基石经济指数
@router.get("/index_bei_cx", operation_id="get_index_bei_cx")
def get_index_bei_cx():
    """
    指数数据-财新指数-基石经济指数

    接口: index_bei_cx

    目标地址: https://yun.ccxe.com.cn/indices/bei

    描述: 财新指数-基石经济指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_bei_cx = ak.index_bei_cx()
        data = index_bei_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-财新指数-新动能指数
@router.get("/index_neei_cx", operation_id="get_index_neei_cx")
def get_index_neei_cx():
    """
    指数数据-财新指数-新动能指数

    接口: index_neei_cx

    目标地址: https://yun.ccxe.com.cn/indices/neei

    描述: 财新指数-新动能指数

    限量: 该接口返回所有历史数据
    """
    try:
        index_neei_cx = ak.index_neei_cx()
        data = index_neei_cx.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
