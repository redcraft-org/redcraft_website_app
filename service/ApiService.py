import requests
from string import Formatter

from dynaconf import settings


class RequestApi:
    def __init__(self, method, slug, request_params=[], version=1):
        base_url = settings[f'url_api_v{version}']
        self.url = f'{base_url}/{slug}'

        self.url_params = [fn for _, fn, _, _ in Formatter().parse(self.url) if fn is not None]
        self.request_params = request_params
        self.method = method


class ApiService:
    @staticmethod
    def request(request_api, params):
        url_params = {key: params.get(key) for key in request_api.url_params}
        request_params = {key: params.get(key) for key in request_api.request_params}

        url = request_api.url.format(**url_params)

        response = requests.request(request_api.method, url, params=request_params)
        response.raise_for_status()
        return response.json()
