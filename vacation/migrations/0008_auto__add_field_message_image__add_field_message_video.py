# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.image'
        db.add_column('vacation_message', 'image',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vacation.Image'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Message.video'
        db.add_column('vacation_message', 'video',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vacation.Video'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.image'
        db.delete_column('vacation_message', 'image_id')

        # Deleting field 'Message.video'
        db.delete_column('vacation_message', 'video_id')


    models = {
        'vacation.gallery': {
            'Meta': {'ordering': "['order']", 'object_name': 'Gallery'},
            'dir_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'vacation.image': {
            'Meta': {'object_name': 'Image'},
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vacation.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'vacation.message': {
            'Meta': {'ordering': "['-posted']", 'object_name': 'Message'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vacation.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '2048'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vacation.Video']", 'null': 'True', 'blank': 'True'})
        },
        'vacation.video': {
            'Meta': {'object_name': 'Video'},
            'dir_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['vacation']