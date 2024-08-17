import importlib.metadata

from fastapi import APIRouter

router = APIRouter()


@router.get("/dependencies")
async def get_dependencies():
    """
    工具API-获取依赖库名称及版本
    """
    installed_packages = importlib.metadata.distributions()

    dependencies = [{"名称": package.metadata["Name"], "版本号": package.version} for package in installed_packages]

    return dependencies


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)

