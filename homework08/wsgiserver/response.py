import dataclasses
import typing as tp

from httpserver import HTTPResponse


@dataclasses.dataclass
class WSGIResponse(HTTPResponse):
    status: int = 200

    def start_response(
        self, status: str, response_headers: tp.List[tp.Tuple[str, str]], exc_info=None
    ) -> None:
        self.status = int(status.split(" ")[0])
        self.headers = dict(response_headers)
