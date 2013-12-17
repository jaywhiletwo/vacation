# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'KeyActivity.completed'
        db.alter_column('kat_keyactivity', 'completed', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 16, 0, 0)))

    def backwards(self, orm):

        # Changing field 'KeyActivity.completed'
        db.alter_column('kat_keyactivity', 'completed', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

    models = {
        'kat.keyactivity': {
            'Meta': {'object_name': 'KeyActivity'},
            'completed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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