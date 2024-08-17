from starlette.websockets import WebSocketDisconnect
from datetime import datetime, timedelta


# 时间区间划分函数
def get_time_range_key(duration="1h"):
    now = datetime.now()
    if duration == "1h":
        return now.strftime('%Y-%m-%d %H:00:00')
    elif duration == "6h":
        return (now - timedelta(hours=now.hour % 6)).strftime('%Y-%m-%d %H:00:00')
    elif duration == "12h":
        return (now - timedelta(hours=now.hour % 12)).strftime('%Y-%m-%d %H:00:00')
    elif duration == "24h":
        return now.strftime('%Y-%m-%d 00:00:00')
    elif duration == "7d":
        return now.strftime('%Y-%m-%d')


async def notify_clients():
    disconnected_clients = []
    from app import websocket_clients
    for websocket in websocket_clients:
        try:
            from middleware_module.monitoring_middleware import api_request_counts, api_response_times, \
                api_status_codes, \
                api_success_counts, api_failure_counts, time_series_data
            await websocket.send_json({
                "api_details": dict(api_request_counts),
                "response_times": {k: sum(v) / len(v) for k, v in api_response_times.items()},
                "status_codes": dict(api_status_codes),
                "success_counts": dict(api_success_counts),
                "failure_counts": dict(api_failure_counts),
                "time_series": list(time_series_data.values())[-24:],  # 发送最后24小时的数据
                "total_success": sum(api_success_counts.values()),
                "total_failures": sum(api_failure_counts.values())
            })
        except WebSocketDisconnect:
            disconnected_clients.append(websocket)

    for websocket in disconnected_clients:
        websocket_clients.remove(websocket)
