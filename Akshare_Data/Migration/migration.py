import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class MigrationAreaBaidu(BaseModel):
    area: str = Field(..., title="需查询的省份或者城市",
                      description="输入需要查询的省份或者城市, 都需要用全称, 比如: 浙江省, 乌鲁木齐市")
    indicator: str = Field(..., title="迁入地/迁出地",
                           description="可选择 move_in: 返回迁入地详情, move_out: 返回迁出地详情")
    date: str = Field(..., title="指定日期", description="例：20240724, 需要滞后一天")


# 迁入与迁出地详情
@router.post("/migration_area_baidu", operation_id="migration_area_baidu")
async def migration_area_baidu(request: MigrationAreaBaidu):
    """
    迁入与迁出地详情

    接口: migration_area_baidu

    目标地址: https://qianxi.baidu.com/?from=shoubai#city=0

    描述: 百度-百度地图慧眼-百度迁徙-迁入/迁出地数据接口

    限量: 单次返回前 100 个城市的数据
    """
    try:
        migration_area_baidu = ak.migration_area_baidu(
            area=request.area,
            indicator=request.indicator,
            date=request.date,
        )
        migration_area_baidu.rename(columns={
            "city_name": "城市名称",
            "province_name": "所属省份",
            "value": "按比例迁徙规模",
        }, inplace=True)
        return migration_area_baidu.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class MigrationScaleBaidu(BaseModel):
    area: str = Field(..., title="需查询的省份或者城市",
                      description="输入需要查询的省份或者城市, 都需要用全称, 比如: 浙江省, 乌鲁木齐市")
    indicator: str = Field(..., title="迁入地/迁出地",
                           description="可选择 move_in: 返回迁入地详情, move_out: 返回迁出地详情")


# 迁入与迁出地详情
@router.post("/migration_scale_baidu", operation_id="migration_scale_baidu")
async def migration_scale_baidu(request: MigrationScaleBaidu):
    """
    迁徙规模

    接口: migration_scale_baidu

    目标地址: https://qianxi.baidu.com/?from=shoubai#city=0

    描述: 百度-百度地图慧眼-百度迁徙-迁徙规模

    (1)迁徙规模指数：反映迁入或迁出人口规模，城市间可横向对比

    (2)城市迁徙边界采用该城市行政区划，包含该城市管辖的区、县、乡、村

    限量: 单次返回所有迁徙规模数据
    """
    try:
        migration_scale_baidu = ak.migration_scale_baidu(
            area=request.area,
            indicator=request.indicator
        )
        return migration_scale_baidu.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
