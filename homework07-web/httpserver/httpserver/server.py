import concurrent
import socket
import threading
import typing as tp
from concurrent.futures import ThreadPoolExecutor

from .handlers import BaseRequestHandler


class TCPServer:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 5000,
        backlog_size: int = 1,
        max_workers: int = 1,
        timeout: tp.Optional[float] = 4,
        request_handler_cls: tp.Type[BaseRequestHandler] = BaseRequestHandler,
    ) -> None:
        self.host = host
        self.port = port
        self.server_address = (host, port)
        # @see: https://stackoverflow.com/questions/36594400/what-is-backlog-in-tcp-connections
        self.backlog_size = backlog_size
        self.request_handler_cls = request_handler_cls
        self.max_workers = max_workers
        self.timeout = timeout
        self._threads: tp.List[threading.Thread] = []

    def serve_forever(self) -> None:
        # @see: http://veithen.io/2014/01/01/how-tcp-backlog-works-in-linux.html
        # @see: https://en.wikipedia.org/wiki/Thundering_herd_problem
        # @see: https://stackoverflow.com/questions/17630416/calling-accept-from-multiple-threads

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        address = (self.host, self.port)
        server_socket.bind(address)
        server_socket.listen(self.backlog_size)

        print(f"Server working on {self.host}:{self.port}")

        threads = []
        try:
            while True:
                client_socket, address = server_socket.accept()
                client_socket.settimeout(self.timeout)
                threads.append(
                    ThreadPoolExecutor(max_workers=self.max_workers).submit(
                        self.handle_accept, client_socket
                    )
                )
        except KeyboardInterrupt:
            for thread in threads:
                thread.cancel()
            concurrent.futures.wait(threads, timeout=self.timeout)
            print("\nSTOP!")

        server_socket.close()

    def handle_accept(self, server_socket: socket.socket) -> None:
        self.request_handler_cls(server_socket, self.server_address, self).handle()


class HTTPServer(TCPServer):
    pass
