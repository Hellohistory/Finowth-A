import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-其他指标-中国日度沿海六大电库存
@router.get("/macro_china_daily_energy",
            operation_id="get_macro_china_daily_energy")
async def get_macro_china_daily_energy():
    """
    国民经济运行状况-其他指标-中国日度沿海六大电库存

    接口: macro_china_daily_energy

    目标地址: https://datacenter.jin10.com/reportType/dc_qihuo_energy_report

    描述: 中国日度沿海六大电库存数据, 数据区间从20160101-至今, 不再更新, 只能获得历史数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_daily_energy = ak.macro_china_daily_energy()
        macro_china_daily_energy_df = sanitize_data_pandas(macro_china_daily_energy)
        return macro_china_daily_energy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



