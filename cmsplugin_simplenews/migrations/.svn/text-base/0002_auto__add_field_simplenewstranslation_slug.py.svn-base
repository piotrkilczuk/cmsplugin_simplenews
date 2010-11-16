# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SimpleNewsTranslation.slug'
        db.add_column('cmsplugin_simplenews_simplenews_translation', 'slug', self.gf('django.db.models.fields.SlugField')(db_index=True, default='', max_length=100, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SimpleNewsTranslation.slug'
        db.delete_column('cmsplugin_simplenews_simplenews_translation', 'slug')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_simplenews.simplenews': {
            'Meta': {'object_name': 'SimpleNews'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_simplenews.SimpleNewsCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {})
        },
        'cmsplugin_simplenews.simplenewscategory': {
            'Meta': {'object_name': 'SimpleNewsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cmsplugin_simplenews.simplenewscategorytranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'SimpleNewsCategoryTranslation', 'db_table': "'cmsplugin_simplenews_simplenewscategory_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['cmsplugin_simplenews.SimpleNewsCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'})
        },
        'cmsplugin_simplenews.simplenewsexcerptplugin': {
            'Meta': {'object_name': 'SimpleNewsExcerptPlugin', 'db_table': "'cmsplugin_simplenewsexcerptplugin'", '_ormbases': ['cms.CMSPlugin']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_simplenews.SimpleNewsCategory']", 'symmetrical': 'False'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'limit': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'cmsplugin_simplenews.simplenewstranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'SimpleNewsTranslation', 'db_table': "'cmsplugin_simplenews_simplenews_translation'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'lead': ('django.db.models.fields.TextField', [], {}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['cmsplugin_simplenews.SimpleNews']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_simplenews']
