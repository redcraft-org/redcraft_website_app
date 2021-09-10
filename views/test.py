from flask import Blueprint
from utils import render_or_cache_template

from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1


bp = Blueprint('test', __name__)

@bp.route("/test")
def test():

    data = ApiService.request(RequestsApiV1.ARTICLE_LAST, {"language" : "fr"})

    print(data)

    return render_or_cache_template("test.html", caching_key='test',
        context={
            'text': 'Welcome on the test page!'
        }
    )
