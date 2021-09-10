from flask import Blueprint
from utils import render_or_cache_template

from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1


bp = Blueprint('contact', __name__)

@bp.route("/contact")
def home():
    return render_or_cache_template("pages/contact.html", caching_key='contact', context={}
    )
