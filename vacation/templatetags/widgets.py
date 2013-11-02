from django import template
from django.template.loader import render_to_string
from random import choice
import feedparser
import requests
import csv
from vacation.models import Image


register = template.Library()

@register.simple_tag
def render_widget(widget, head_color='black', body_color='white'):
    head_color = widget.page.header_color
    context = {
        'id': widget.id,
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
        context['entries'] = get_rss_entries(widget.value)
        return render_to_string('widget_%s.html' % widget.type, context)
    elif widget.type == 'STOCK':
        context['quotes'] = format_stocks(widget.value)
        return render_to_string('widget_%s.html' % widget.type, context)
    elif widget.type == 'IMAGE':
        images = Image.objects.filter(id__in=widget.value.split(','))
        i = choice(images)
        context['image_title'] = i.filename
        context['image_path'] = '/static/%s/%s.%s' % (i.gallery.dir_name, i.filename, i.extension)
        return render_to_string('widget_%s.html' % widget.type, context)
    elif widget.type == 'LINKS':
        context['links'] = build_links(widget.value)
        return render_to_string('widget_%s.html' % widget.type, context)
    elif widget.type == 'CAL':
        context['value'] = widget.value
        return render_to_string('widget_%s.html' % widget.type, context)
    elif widget.type == 'RAW':
        context['value'] = widget.value
    else:
        print '%s is not a valid widget' % widget.type

    return render_to_string('widget.html', context)


def build_text(value):
    contents = value.split('\n')
    try:
        if contents[0].startswith('style='):
            style = contents[0]
            text = ''.join(contents[1:])
            return '<pre %s>%s</pre>' % (style, text)
    except IndexError:
        print 'failed to display text widget: %s' % value

    return '<pre %s>%s</pre>' % (style, value)


def get_rss_entries(value):
    try: 
        r = requests.get(value)
        feed = feedparser.parse(r.content)
    except:
        return 'No RSS found at %s' % value

    link_list = feed['entries']

    if not link_list:
        return 'No RSS found at %s' % value

    return link_list


def format_stocks(value):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2r' % value
    try:
        r = requests.get(url)
    except:
        return 'Broken'
    
    quotes = []
    for row in r.content.split('\n'):
        try:
            line = row.split(',')
            quote = {
                'symbol': line[0][1:-1],
                'change_price': color(line[3].replace('"','(', 1).replace('"', ')')),
                'change_percent': color(line[2]), 
                'pe': color(line[4], given_color='#888888'),
                'price': line[1],
            }
            quotes.append(quote)
        except IndexError:
            print 'stocks failed on row: %s' % row

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
    links = []
    for row in value.split('\n'):
        title, href = row.split(',')
        links.append({'href': href, 'title': title, })

    return links

