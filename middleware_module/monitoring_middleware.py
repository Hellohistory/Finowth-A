# monitoring_middleware.py

import time
from fastapi import Request
from collections import defaultdict

from middleware_module.monitoring_utils import get_time_range_key, notify_clients

# 统计数据
api_request_counts = defaultdict(int)
api_response_times = defaultdict(list)
api_status_codes = defaultdict(int)
api_success_counts = defaultdict(int)
api_failure_counts = defaultdict(int)

# 时间序列数据
time_series_data = defaultdict(lambda: {"time": "", "count": 0})

excluded_paths = ["/api_monitor"]


async def count_requests_middleware(request: Request, call_next):
    path = request.url.path

    if request.method == "OPTIONS" or path in excluded_paths:
        return await call_next(request)

    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    status_code = response.status_code

    # 更新统计数据
    api_request_counts[path] += 1
    api_response_times[path].append(duration)
    api_status_codes[status_code] += 1

    # 根据状态码更新成功或失败计数
    if 200 <= status_code < 300:
        api_success_counts[path] += 1
    else:
        api_failure_counts[path] += 1

    # 更新时间序列数据
    time_key = get_time_range_key("1h")
    time_series_data[time_key]["time"] = time_key
    time_series_data[time_key]["count"] += 1

    # 通知 WebSocket 客户端
    await notify_clients()
    return response
