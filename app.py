import asyncio
import importlib
import logging
import os
from typing import List, Dict, Any

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from middleware_module.monitoring_middleware import count_requests_middleware

# 配置日志记录
logging.basicConfig(level=logging.ERROR)


app = FastAPI()

# 配置CORS
origins = [
    "http://localhost:36924",
    "http://localhost:36925",
    "http://192.168.1.18:36929",
    "http://192.168.1.16:8083"
]

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 添加拆分后的中间件
app.middleware("http")(count_requests_middleware)

# WebSocket客户端集合
websocket_clients = []


@app.get("/api_monitor", operation_id="api_monitor")
async def get_api_monitor():
    """
    获取API的统计信息
    """
    from middleware_module.monitoring_middleware import api_request_counts, api_response_times, api_status_codes
    from middleware_module.monitoring_middleware import api_success_counts, api_failure_counts, time_series_data

    return {
        "api_details": dict(api_request_counts),
        "response_times": {k: sum(v) / len(v) for k, v in api_response_times.items()},
        "status_codes": dict(api_status_codes),
        "success_counts": dict(api_success_counts),
        "failure_counts": dict(api_failure_counts),
        "time_series": list(time_series_data.values())[-24:],  # 返回最近24小时的数据
        "total_success": sum(api_success_counts.values()),
        "total_failures": sum(api_failure_counts.values())
    }


@app.websocket("/ws/api_monitor")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket 端点，接收并发送监控数据
    """
    await websocket.accept()
    websocket_clients.append(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        websocket_clients.remove(websocket)


class APIInfo(BaseModel):
    api_name: str
    api_path: str
    method: str
    description: str
    parameters: List[Dict[str, Any]]


@app.get("/api_info", response_model=List[APIInfo], operation_id="api_info")
async def api_info():
    """
    获取 API 信息
    """
    from api_info_model import process_api_info
    return process_api_info()


@app.get("/openapi.json", operation_id="openapi.json")
async def open_api_endpoint():
    """
    获取 OpenAPI 文档
    """
    from fastapi.openapi.utils import get_openapi
    openapi_schema = get_openapi(
        title="FinDataAPI",
        version="0.0.1",
        routes=app.routes,
    )
    return openapi_schema


# 自动加载路由
def include_all_routers(app: FastAPI, router_dir: str):
    """
    动态加载给定目录中的所有FastAPI路由模块，并处理模块加载错误
    """
    for root, dirs, files in os.walk(router_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # 获取完整模块路径并正确处理模块名称
                module_name = os.path.splitext(file)[0]
                relative_path = os.path.relpath(root, os.getcwd())  # 相对路径
                module_path = f"{relative_path.replace(os.sep, '.')}.{module_name}"

                try:
                    module = importlib.import_module(module_path)
                    if hasattr(module, "router"):
                        app.include_router(module.router)
                        logging.info(f"成功加载路由模块: {module_path}")
                except ModuleNotFoundError as e:
                    logging.error(f"模块未找到: {module_path} - 错误: {str(e)}")
                except Exception as e:
                    logging.error(f"加载模块 {module_path} 时发生错误: {str(e)}")


# 加载所有路由模块
include_all_routers(app, "Akshare_Data")
include_all_routers(app, "Finowth")
include_all_routers(app, "Tools_API")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=36925)
