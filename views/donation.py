from flask import Blueprint

from utils import render_or_cache_template
from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1
from template_global_datas import global_variables


bp = Blueprint('donation', __name__)


@bp.route("/donation")
def index():
    return render_or_cache_template("pages/donation.html", caching_key='donation', context={
        'global': global_variables,
        # TODO : support multiple currencies
        'devise': '€'
    })
