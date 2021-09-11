from flask import Blueprint

from utils import render_or_cache_template
from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1
from template_global_datas import global_variables


bp = Blueprint('about', __name__)

@bp.route("/about")
def index():
    return render_or_cache_template("pages/about.html", caching_key='about', context={
        'global' : global_variables
        }
    )
