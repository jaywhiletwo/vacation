from django import template


register = template.Library()

def randomtag(msg):
    return {'msg': msg}

register.inclusion_tag('bigtag.html', name='bigtag')(randomtag)
register.inclusion_tag('littletag.html', name='littletag')(randomtag)
