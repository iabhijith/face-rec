import argparse
import logging

from waitress import serve

from src.api import app


logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    deepface_app = app.create_app()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", type=int, default=9009, help="Port of serving api"
    )
    args = parser.parse_args()
    serve(deepface_app, host="0.0.0.0", port=args.port)
