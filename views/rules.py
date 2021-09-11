from flask import Blueprint

from utils import render_or_cache_template
from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1
from template_global_datas import global_variables


bp = Blueprint('rules', __name__)

@bp.route("/rules")
def index():
    return render_or_cache_template("pages/rules.html", caching_key='rules', context={
        'global' : global_variables
        }
    )
