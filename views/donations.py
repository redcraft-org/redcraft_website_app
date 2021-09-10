from flask import Blueprint
from utils import render_or_cache_template

from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1


bp = Blueprint('donations', __name__)

@bp.route("/donations")
def home():
    return render_or_cache_template("pages/donations.html", caching_key='donations', context={}
    )
