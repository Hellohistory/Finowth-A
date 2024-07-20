import requests
import json

# 定义 OpenAPI 文档的 URL
url = "http://0.0.0.0:36925/openapi.json"

# 获取 OpenAPI 文档
response = requests.get(url)
openapi_doc = response.json()

# 提取并打印 API 地址、函数名称、请求类型、API 描述以及参数信息
print("API 文档：")

def resolve_ref(ref, components):
    ref_path = ref.split('/')
    schema = components
    for part in ref_path[1:]:
        if schema is None:
            return None
        schema = schema.get(part)
    return schema

components = openapi_doc.get('components', {})

for path, path_item in openapi_doc['paths'].items():
    for method, operation in path_item.items():
        print(f"API 地址: {path}")
        print(f"函数名称: {operation.get('operationId')}")
        print(f"请求类型: {method.upper()}")
        print(f"API 描述: {operation.get('description', '')}")

        # 如果是 POST 请求，则打印请求参数
        if method == 'post':
            request_body = operation.get('requestBody')
            if request_body:
                content = request_body.get('content')
                for media_type, media_schema in content.items():
                    schema = media_schema.get('schema')
                    if schema:
                        if '$ref' in schema:
                            resolved_schema = resolve_ref(schema['$ref'], components)
                            if resolved_schema:
                                print(f"请求参数示例:")
                                print(json.dumps(resolved_schema, indent=2, ensure_ascii=False))
                            else:
                                print(f"未找到引用的组件：{schema['$ref']}")
                        else:
                            print(f"请求参数示例:")
                            print(json.dumps(schema, indent=2, ensure_ascii=False))

        print("\n" + "="*50 + "\n")
