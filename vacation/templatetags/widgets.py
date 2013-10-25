from django import template
import feedparser
import requests


register = template.Library()

@register.inclusion_tag('widget.html')
def render_widget(widget):
    if widget.type == 'TEXT':
        value = '<pre>%s</pre>' % widget.value
    elif widget.type == 'RSS':
        value = build_rss(widget.value)
    elif widget.type == 'STOCK':
        r = requests.get(widget.value)
        value = r.content
    else:
        raise Exception

    context = {
        'title': widget.title,
        'value': value,
    }
    
    return context


def build_rss(value):
    try: 
        r = requests.get(value)
        feed = feedparser.parse(r.content)
    except:
        return 'No RSS found at %s' % value

    link_list = []
    for entry in feed['entries']:
        link_list.extend(['<li><a href="">', entry['title'], '</a></li>'])

    if not link_list:
        return 'No RSS found at %s' % value
    return '<ul>' + ''.join(link_list) + '</ul>'


def format_stocks(value):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=snl1c1p2' % value
    try:
        r = requests.get(value)
    except:
        return 'Broken'

    csv = r.content
    return csv
