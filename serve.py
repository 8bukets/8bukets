import http.server
import socketserver
import logging

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info(f"Incoming request: {self.client_address[0]} - {args[0]}")
        super().log_message(format, *args)

def run_server():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logging.info(f"Serving at http://localhost:{PORT}")
        logging.info(f"Test robots.txt at http://localhost:{PORT}/robots.txt")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()
            logging.info("Server stopped.")

if __name__ == "__main__":
    run_server()
