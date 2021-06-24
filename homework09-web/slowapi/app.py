import http
import typing as tp
from urllib.parse import parse_qsl

from slowapi.middlewares import Middleware
from slowapi.request import Request
from slowapi.router import Route, Router


class SlowAPI:
    def __init__(self):
        self.router = Router()
        self.middlewares: tp.List[tp.Type[Middleware]] = []

    def __call__(self, environ, start_response):
        headers = {}
        for k in environ:
            if k.startswith("HTTP_"):
                headers[k[5:].lower()] = environ[k]
        query: tp.Dict[str, any] = {}

        for query_var, query_val in parse_qsl(environ.get("QUERY_STRING", "")):
            query[query_var] = query_val

        request = Request(
            path=environ.get("PATH_INFO").rstrip("/") or "/",
            method=environ.get("REQUEST_METHOD"),
            query=query,
            headers=headers,
            body=environ.get("wsgi.input"),
        )
        answer = self.router.resolve(request)
        status = http.HTTPStatus(answer.status)
        start_response(" ".join([str(status.value), status.phrase]), answer.headers)
        if answer.body is not None:
            return answer.body.encode()
        else:
            return b""

    def route(self, path=None, method=None, **options):
        def decorator(func: tp.Callable):
            route = Route(path.rstrip("/"), method, func)
            self.router.add_route(route)
            return func

        return decorator

    def get(self, path=None, **options):
        return self.route(path, method="GET", **options)

    def post(self, path=None, **options):
        return self.route(path, method="POST", **options)

    def patch(self, path=None, **options):
        return self.route(path, method="PATCH", **options)

    def put(self, path=None, **options):
        return self.route(path, method="PUT", **options)

    def delete(self, path=None, **options):
        return self.route(path, method="DELETE", **options)

    def add_middleware(self, middleware: tp.Type[Middleware]) -> None:
        self.middlewares.append(middleware)
