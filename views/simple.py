from flask import Blueprint

from utils import render_or_cache_template
from service.ApiService import ApiService
from api_request.RequestsApiV1 import RequestsApiV1
from template_global_datas import global_variables


bp = Blueprint('simple', __name__)


@bp.route("/about")
def about():
    return render_or_cache_template("pages/about.html", caching_key='about', context={
        'global': global_variables
    })


@bp.route("/rules")
def rules():
    return render_or_cache_template("pages/rules.html", caching_key='rules', context={
        'global': global_variables
    })


@bp.route("/contact")
def contact():
    return render_or_cache_template("pages/contact.html", caching_key='contact', context={
        'global': global_variables
    })


@bp.route("/vote")
def vote():
    return render_or_cache_template("pages/vote.html", caching_key='vote', context={
        'global': global_variables,
        'page': 'vote',
        'websites_list': [
            {
                'titre': 'Serveurs-minecraft.org',
                'explainations': 'Sur la page, descendez jusqu\'au bouton vert "Voter pour RedCraft". Cliquez simplement dessus.',
                'url': 'https://www.serveurs-minecraft.org/',
                'path_img': 'img/pages/vote/serveurs-minecraft-org.png'
            },
            {
                'titre': 'top-serveurs.net',
                'explainations': 'TODO Entrez ici une description de comment voter sur le site',
                'url': 'https://top-serveurs.net/',
                'path_img': 'img/pages/vote/top-serveurs.png'
            },
            {
                'titre': 'liste-serveur-minecraft.net',
                'explainations': 'TODO Entrez ici une description de comment voter sur le site',
                'url': 'http://www.liste-serveur-minecraft.net/',
                'path_img': 'img/pages/vote/liste-serveurs-minecraft.png'
            },
            {
                'titre': 'serveursminecraft.org',
                'explainations': 'TODO Entrez ici une description de comment voter sur le site',
                'url': 'https://www.serveursminecraft.org/',
                'path_img': 'img/pages/vote/serveursminecraft-org.png'
            },
        ]
    })


@bp.route("/stats")
def stats():
    return render_or_cache_template("pages/comingsoon.html", caching_key='stats', context={
        'global': global_variables
    })


@bp.route("/livemap")
def livemap():
    return render_or_cache_template("pages/comingsoon.html", caching_key='livemap', context={
        'global': global_variables
    })