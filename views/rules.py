from flask import Blueprint
from utils import render_or_cache_template

from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1


bp = Blueprint('rules', __name__)

@bp.route("/rules")
def home():
    return render_or_cache_template("pages/rules.html", caching_key='home', context={
            "test": "This is a test message"
        }
    )
