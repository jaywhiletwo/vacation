from django import template
import feedparser
import requests
import csv


register = template.Library()

@register.inclusion_tag('widget.html')
def render_widget(widget):
    if widget.type == 'TEXT':
        value = '<pre>%s</pre>' % widget.value
    elif widget.type == 'RSS':
        value = build_rss(widget.value)
    elif widget.type == 'STOCK':
        value = format_stocks(widget.value)
    elif widget.type == 'LINKS':
        value = build_links(widget.value)
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
    for entry in feed['entries'][:7]:
        link_list.extend(['<li><a target="blank" href="%s">' % entry['link'], entry['title'], '</a></li>'])

    if not link_list:
        return 'No RSS found at %s' % value
    return '<ul>' + ''.join(link_list) + '</ul>'


def format_stocks(value):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2' % value
    try:
        r = requests.get(url)
    except:
        return 'Broken'
    
    text = []
    for row in r.content.split('\n'):
        if row:
            line = row.split(',')
            s = line[0][1:-1]
            linked_symbol = '<tr><td><a target="blank" href="http://finance.yahoo.com/q?s=%s">%s</a>' % (s, s)
            text.extend([linked_symbol, color(line[2]), color(line[3].replace('"','(', 1).replace('"', ')')), '</td><td align="right">', line[1], '</td></tr>', ])
    return '<table>' + ' '.join(text) + '</table>'


def color(change):
    if '-' in change:
        color = 'red'
    elif '+' in change:
        color = 'green'
    else:
        color = ''

    return '<font size=2 color="%s">%s</font>' % (color, change)


def build_links(value):
    links_val = ['<ul>', ]
    for row in value.split('\n'):
        line = row.split(',')
        links_val.extend(['<li><a target="blank" href="', line[1], '">', line[0], '</a></li>',])  
    links_val.append('</ul>')
    return ''.join(links_val)
