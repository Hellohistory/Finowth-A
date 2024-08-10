from typing import List

from fastapi.openapi.utils import get_openapi

from app import APIInfo, app


def process_api_info() -> List[APIInfo]:
    openapi_json = get_openapi(
        title="FinDataAPI",
        version="0.0.1",
        routes=app.routes,
    )

    def resolve_ref(ref, spec):
        """解析$ref引用"""
        parts = ref.lstrip('#/').split('/')
        result = spec
        for part in parts:
            result = result.get(part, {})
        return result

    api_info_list = []

    for path, path_item in openapi_json.get('paths', {}).items():
        for method, operation in path_item.items():
            api_name = operation.get('operationId', '无操作ID')
            operation.get('summary', '无描述信息')
            api_description = operation.get('description', '无详细描述')

            parameters = []

            if method == 'post':
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
                        param_title = param_info.get('title', '无标题')
                        is_required = param_name in required
                        parameters.append({
                            "name": param_name,
                            "type": param_type,
                            "required": is_required,
                            "description": param_description,
                            "title": param_title
                        })

            api_info = APIInfo(
                api_name=api_name,
                api_path=path,
                method=method,
                description=api_description,
                parameters=parameters
            )
            api_info_list.append(api_info)

    return api_info_list
