from flask import render_template


def render_or_cache_template(template, caching_key, context, duration_caching=None):
    # TODO: Implement caching with redis
    return render_template(template, **context)
