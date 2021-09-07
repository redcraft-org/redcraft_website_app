from flask import Blueprint
from utils import render_or_cache_template

from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1


bp = Blueprint('home', __name__)

@bp.route("/")
def home():
    return render_or_cache_template("base.html", caching_key='home',
        context={
            'text': 'Hello Redvax !!'
        }
    )
