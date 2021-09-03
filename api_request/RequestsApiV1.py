from service.ApiService import ApiService, RequestApi


class RequestsApiV1:
    # Group Article
    ARTICLE_LIST = RequestApi('GET', '{language}/article', ['page', 'per_page', 'category'])
    ARTICLE_DETAIL = RequestApi('GET', '{language}/article/{id}')
    ARTICLE_LAST = RequestApi('GET', '{language}/article/last', ['count'])

    # Group Post
    POST_LIST = RequestApi('GET', '{language}/post', ['page', 'per_page', 'category'])
    POST_DETAIL = RequestApi('GET', '{language}/post/{id}')
    POST_LAST = RequestApi('GET', '{language}/post/last', ['count'])

    # Group Donation
    DONATION_LIST = RequestApi('GET', 'donation', ['per_page', 'page'])
    DONATION_DETAIL = RequestApi('GET', 'donation/{id}')
    DONATION_LAST = RequestApi('GET', 'donation/last', ['count'])
    DONATION_GRAPH = RequestApi('GET', 'donation/graph/{delta_time}', ['delta_time', 'start_date', 'stop_start', 'donation_count', 'refunded_count', 'donation_amount', 'refunded_amount'])
    DONATION_GRAPH = RequestApi('GET', 'donation/stats/{delta_time}', ['donation_count', 'refunded_count', 'donation_amount', 'refunded_amount'])

    # Group Player
    PLAYER_LIST = RequestApi('GET', 'player', ['per_page', 'page'])
    PLAYER_DETAIL = RequestApi('GET', 'player/{id}')

    # Group Language
    LANGUAGE_LIST = RequestApi('GET', 'network/language/supported')

    # Group Networks
    NETWORK_MC_STATUS = RequestApi('GET', 'network/minecraft/status')
    NETWORK_MC_VERSION = RequestApi('GET', 'network/minecraft/version')
    NETWORK_MC_PLAYER = RequestApi('GET', 'network/minecraft/player')
    NETWORK_MC_PLAYER_COUNT = RequestApi('GET', 'network/minecraft/player/count')
    NETWORK_DISCORD = RequestApi('GET', 'network/discord/player/count')