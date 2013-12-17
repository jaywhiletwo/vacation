# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'KeyGoal.last_activity'
        db.add_column('kat_keygoal', 'last_activity',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kat.KeyActivity'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'KeyGoal.interval'
        db.add_column('kat_keygoal', 'interval',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)

        # Deleting field 'KeyActivity.interval'
        db.delete_column('kat_keyactivity', 'interval')

        # Deleting field 'KeyActivity.last_time'
        db.delete_column('kat_keyactivity', 'last_time')

        # Adding field 'KeyActivity.completed'
        db.add_column('kat_keyactivity', 'completed',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'KeyGoal.last_activity'
        db.delete_column('kat_keygoal', 'last_activity_id')

        # Deleting field 'KeyGoal.interval'
        db.delete_column('kat_keygoal', 'interval')

        # Adding field 'KeyActivity.interval'
        db.add_column('kat_keyactivity', 'interval',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'KeyActivity.last_time'
        db.add_column('kat_keyactivity', 'last_time',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'KeyActivity.completed'
        db.delete_column('kat_keyactivity', 'completed')


    models = {
        'kat.keyactivity': {
            'Meta': {'object_name': 'KeyActivity'},
            'completed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_goal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kat.KeyGoal']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'kat.keygoal': {
            'Meta': {'object_name': 'KeyGoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'last_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kat.KeyActivity']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['kat']