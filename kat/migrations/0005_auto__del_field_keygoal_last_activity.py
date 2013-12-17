# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'KeyGoal.last_activity'
        db.delete_column('kat_keygoal', 'last_activity_id')


    def backwards(self, orm):
        # Adding field 'KeyGoal.last_activity'
        db.add_column('kat_keygoal', 'last_activity',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kat.KeyActivity'], null=True, blank=True),
                      keep_default=False)


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['kat']