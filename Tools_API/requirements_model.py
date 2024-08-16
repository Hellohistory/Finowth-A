import importlib.metadata

from fastapi import APIRouter

router = APIRouter()


@router.get("/dependencies")
async def get_dependencies():
    # 获取所有已安装的依赖库及其版本
    installed_packages = importlib.metadata.distributions()

    # 创建一个包含库名和版本号的列表
    dependencies = [{"名称": package.metadata["Name"], "版本号": package.version} for package in installed_packages]

    return dependencies


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)

