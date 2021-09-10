from flask import Blueprint
from utils import render_or_cache_template

from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1


bp = Blueprint('home', __name__)


@bp.route("/")
def home():

    #TODO: Use our own API for the player heads
    
    return render_or_cache_template("pages/home.html", caching_key='home', context={
        'discord': {
            'count_players_online': 15  # TODO: API call
        },
        'minecraft_server': {
            'count_players_online': 27,  # TODO: API call
            'ip_address': 'play.redcraft.org',
        },
        'articles': ApiService.request(RequestsApiV1.ARTICLE_LAST, {'language': 'fr'}),

        'network_presentations': None,
        'servers_list': None,
        'staff_list': [
            {
                'name': 'lululombard',
                        'path_img': 'https://crafatar.com/avatars/15f7b6b0-d787-48e2-b54b-0336e17f6316',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url': 'https://twitter.com/lululombard',
                                'logo_fa': 'twitter'
                            },
                            {
                                'name': 'YouTube',
                                'url': 'https://www.youtube.com/lululombard',
                                'logo_fa': 'youtube'
                            },
                            {
                                'name': 'Reddit',
                                'url': 'https://www.reddit.com/user/lululombard/',
                                'logo_fa': 'reddit-alien'
                            },
                        ],
            },
            {
                'name': 'Likyaz',
                        'path_img': 'https://crafatar.com/avatars/3d4213de-68fc-4494-b043-82a27e7ab56a',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url': 'https://twitter.com/LikyazRS',
                                'logo_fa': 'twitter'
                            },
                        ],
            },
            {
                'name': 'Codelta',
                        'path_img': 'https://crafatar.com/avatars/9430befb-3238-455c-be89-1ff0cd5907f2',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url': 'https://twitter.com/_Codelta_',
                                'logo_fa': 'twitter'
                            },
                        ],
            },
            {
                'name': 'Omeganx',
                        'path_img': 'https://crafatar.com/avatars/742f8aa4-7ec7-4caf-aad9-244813484450',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url': 'https://twitter.com/Omeganx',
                                'logo_fa': 'twitter'
                            },
                        ],
            },
            {
                'name': 'Nano_',
                        'path_img': 'https://crafatar.com/avatars/45418653-fadb-4e6d-8dcc-8c79b90ec527',
                        'socials': [
                            {
                                'name': 'Twitter',
                                'url': 'https://twitter.com/Nano1010010110',
                                'logo_fa': 'twitter'
                            },
                        ],
            },
        ]
    })
