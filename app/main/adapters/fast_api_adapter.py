from traceback import format_exc
from typing import Any

from app.domain.usecases import Usecase
from app.services.helpers.http import HttpRequest, HttpResponse, HttpStatus


def fast_api_adapter(request: Any, usecase: Usecase) -> HttpResponse:

    try:
        http_request = HttpRequest(
            header=request['headers'], body=request['body'], query=request['query'])
        response = usecase.execute(http_request.body)

    except Exception:
        return HttpStatus.internal_server_error_500()

    return response