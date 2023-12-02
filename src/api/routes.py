import logging
from flask import Blueprint, request

from ..service.recognition import verify

blueprint = Blueprint("routes", __name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@blueprint.route("/")
def home():
    logger.info("Calling home endpoint")
    return "<h1>Rest API for Face Recognition!</h1>"


@blueprint.route("/verify", methods=["POST"])
def verification_route():
    logger.info(f"Calling verify endpoint with request {request.get_json()}")
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty input set passed"}

    img1 = input_args.get("img1")
    img2 = input_args.get("img2")

    if img1 is None:
        return {"message": "you must pass img1 input"}

    if img2 is None:
        return {"message": "you must pass img2 input"}

    verification = verify(img1=img1, img2=img2)

    verification["verified"] = str(verification["verified"])

    return verification
