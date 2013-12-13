# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'KeyActivity.interval'
        db.add_column('kat_keyactivity', 'interval',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'KeyActivity.last_time'
        db.add_column('kat_keyactivity', 'last_time',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'KeyActivity.interval'
        db.delete_column('kat_keyactivity', 'interval')

        # Deleting field 'KeyActivity.last_time'
        db.delete_column('kat_keyactivity', 'last_time')


    models = {
        'kat.keyactivity': {
            'Meta': {'object_name': 'KeyActivity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'key_goal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kat.KeyGoal']"}),
            'last_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'kat.keygoal': {
            'Meta': {'object_name': 'KeyGoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['kat']