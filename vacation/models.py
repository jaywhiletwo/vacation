from django.db import models
from django.core.urlresolvers import reverse



class Widget(models.Model):
    WIDGET_TYPE_CHOICES = (
        ('RSS', 'RSS Feed'),
        ('TEXT', 'Simple Text'),
        ('STOCK', 'Stocks Widget'),
    )
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=WIDGET_TYPE_CHOICES, default='TEXT')
    value = models.TextField()

    def __unicode__(self):
        return '(%s) %s' % (self.type, self.title)


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
