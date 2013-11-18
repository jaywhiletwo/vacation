from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class MenuItem(models.Model):
    posted = models.DateTimeField(auto_now_add=True)

    @property
    def menu_name(self):
        menu_name = self.name if hasattr(self, 'name') else self.filename
        return menu_name

    @property
    def menu_path(self):
        return 'show_home'
    
    class Meta:
        abstract = True


class Gallery(MenuItem, models.Model):
    name = models.CharField(max_length=255)
    dir_name = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name

    @property
    def menu_path(self):
        return 'list_images'

    class Meta:
        verbose_name_plural = 'galleries'
        ordering = ['order']


class Image(models.Model):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=10)
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return '%s/%s.%s' % (self.gallery.dir_name, self.filename, self.extension)
    

class WidgetPage(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=200, null=True)
    header_color = models.CharField(max_length=10, default='black')
    banner_image = models.ForeignKey(Image, null=True, blank=True)
    
    def __unicode__(self):
        return '(%s) %s' % (self.user, self.name)


class Widget(models.Model):
    WIDGET_TYPE_CHOICES = (
        ('RSS', 'RSS Feed'),
        ('TEXT', 'Simple Text'),
        ('STOCK', 'Stocks Widget'),
        ('IMAGE', 'Image Widget'),
        ('LINKS', 'Links and Bookmarks'),
        ('CAL', 'Calendar Iframe'),
        ('RAW', 'Raw HTML and JS'),
        ('NOTES', 'Shared Notes'),
    )
    title = models.CharField(max_length=50)
    title_link = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=20, choices=WIDGET_TYPE_CHOICES, default='TEXT')
    value = models.TextField()
    page = models.ForeignKey(WidgetPage, null=True, related_name='old_page')
    pages = models.ManyToManyField(WidgetPage)
    columns = models.PositiveSmallIntegerField(default=4)
    order = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return '(%s) %s' % (self.type, self.title)


class Video(MenuItem, models.Model):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=10)
    dir_name = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s/%s.%s' % (self.dir_name, self.filename, self.extension)

    @property
    def menu_path(self):
        return 'show_video'


class Message(MenuItem, models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=2048)
    image = models.ForeignKey(Image, blank=True, null=True)
    video = models.ForeignKey(Video, blank=True, null=True)
    
    def __unicode__(self):
        return self.name

    @property
    def menu_path(self):
        return 'show_message'

    class Meta:
        ordering = ['-posted']
