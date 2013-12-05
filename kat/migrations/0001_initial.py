# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KeyGoal'
        db.create_table('kat_keygoal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('kat', ['KeyGoal'])

        # Adding model 'KeyActivity'
        db.create_table('kat_keyactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('key_goal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kat.KeyGoal'])),
        ))
        db.send_create_signal('kat', ['KeyActivity'])


    def backwards(self, orm):
        # Deleting model 'KeyGoal'
        db.delete_table('kat_keygoal')

        # Deleting model 'KeyActivity'
        db.delete_table('kat_keyactivity')


    models = {
        'kat.keyactivity': {
            'Meta': {'object_name': 'KeyActivity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_goal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kat.KeyGoal']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'kat.keygoal': {
            'Meta': {'object_name': 'KeyGoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['kat']