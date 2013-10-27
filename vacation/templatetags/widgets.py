from django import template
from django.template.loader import render_to_string
import feedparser
import requests
import csv


register = template.Library()

@register.simple_tag
def render_widget(widget, head_color='black', body_color='white'):
    context = {
        'title': widget.title,
        'title_link': widget.title_link or '',
        'edit_link': '/admin/vacation/widget/%s/' % widget.id,
        'head_color': head_color,
        'body_color': body_color,
        'cols': widget.columns,
    }
    
    if widget.type == 'TEXT':
        context['value'] = build_text(widget.value)
    elif widget.type == 'RSS':
        context['value'] = build_rss(widget.value)
    elif widget.type == 'STOCK':
        context['quotes'] = format_stocks(widget.value)
        return render_to_string('widget_%s.html' % widget.type, context)
    elif widget.type == 'LINKS':
        context['value'] = build_links(widget.value)
    elif widget.type == 'RAW':
        context['value'] = widget.value
    else:
        raise Exception('not a valid widget')

    return render_to_string('widget.html', context)


def build_text(value):
    contents = value.split('\n')
    if contents[0].startswith('style='):
        style = contents[0]
        text = ''.join(contents[1:])
    else:
        style = ''
        text = value
    
    return '<pre %s>%s</pre>' % (style, text)


def build_rss(value):
    try: 
        r = requests.get(value)
        feed = feedparser.parse(r.content)
    except:
        return 'No RSS found at %s' % value

    link_list = []
    for entry in feed['entries'][:7]:
        link_list.extend(['<li><a target="_blank" href="%s">' % entry['link'], entry['title'], '</a></li>'])

    if not link_list:
        return 'No RSS found at %s' % value
    return '<ul>' + ''.join(link_list) + '</ul>'


def format_stocks(value):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2r' % value
    try:
        r = requests.get(url)
    except:
        return 'Broken'
    
    quotes = []
    for row in r.content.split('\n'):
        if row:
            line = row.split(',')
            quote = {
                'symbol': line[0][1:-1],
                'change_price': color(line[3].replace('"','(', 1).replace('"', ')')),
                'change_percent': color(line[2]), 
                'pe': color(line[4], given_color='#888888'),
                'price': line[1],
            }
            quotes.append(quote)
    return quotes


def color(change, given_color=None):
    if given_color:
        color = given_color
    elif '-' in change:
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
        links_val.extend(['<li><a target="_blank" href="', line[1], '">', line[0], '</a></li>',])  
    links_val.append('</ul>')
    return ''.join(links_val)
