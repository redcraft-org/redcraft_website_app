from flask import Blueprint

from utils import render_or_cache_template
from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1
from template_global_datas import global_variables


bp = Blueprint('simple', __name__)

@bp.route("/about")
def about():
    return render_or_cache_template("pages/about.html", caching_key='about', context={
        'global' : global_variables
        }
    )

@bp.route("/rules")
def rules():
    return render_or_cache_template("pages/rules.html", caching_key='rules', context={
        'global' : global_variables
        }
    )

@bp.route("/contact")
def contact():
    return render_or_cache_template("pages/contact.html", caching_key='contact', context={
        'global' : global_variables
        }
    )
