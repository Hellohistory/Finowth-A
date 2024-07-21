import json

import requests
from requests.exceptions import RequestException

# 请求OpenAPI文档
url = 'http://0.0.0.0:36925/openapi.json'
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    openapi_json = response.json()
except RequestException as e:
    print(f"请求失败: {e}")
    exit(1)
except ValueError as e:
    print(f"解析JSON失败: {e}")
    exit(1)

# 保存OpenAPI文档到本地文件（可选）
with open('openapi.json', 'w') as file:
    json.dump(openapi_json, file, indent=2)


# 解析并提取信息
def resolve_ref(ref, spec):
    """解析$ref引用"""
    parts = ref.lstrip('#/').split('/')
    result = spec
    for part in parts:
        result = result.get(part, {})
    return result


for path, path_item in openapi_json.get('paths', {}).items():
    print(f"处理路径: {path}")  # 调试信息
    for method, operation in path_item.items():
        api_name = operation.get('operationId', '无操作ID')
        api_summary = operation.get('summary', '无描述信息')
        api_description = operation.get('description', '无详细描述')

        print(f"API名称: {api_name}")
        print(f"API地址: {path}")
        print(f"描述信息: {api_summary} - {api_description}")

        if method == 'post':
            print("POST请求参数:")
            request_body = operation.get('requestBody', {})
            content = request_body.get('content', {})
            for media_type, media_type_object in content.items():
                schema = media_type_object.get('schema', {})
                if '$ref' in schema:
                    schema = resolve_ref(schema['$ref'], openapi_json)
                properties = schema.get('properties', {})
                required = schema.get('required', [])
                for param_name, param_info in properties.items():
                    param_type = param_info.get('type', '未知类型')
                    param_description = param_info.get('description', '无描述')
                    is_required = param_name in required
                    print(f"  参数名称: {param_name}")
                    print(f"  类型: {param_type}")
                    print(f"  必需: {is_required}")
                    print(f"  描述: {param_description}")
        print()
