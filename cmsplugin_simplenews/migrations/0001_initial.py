# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SimpleNewsCategoryTranslation'
        db.create_table('cmsplugin_simplenews_simplenewscategory_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=100, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['cmsplugin_simplenews.SimpleNewsCategory'])),
        ))
        db.send_create_signal('cmsplugin_simplenews', ['SimpleNewsCategoryTranslation'])

        # Adding unique constraint on 'SimpleNewsCategoryTranslation', fields ['language_code', 'master']
        db.create_unique('cmsplugin_simplenews_simplenewscategory_translation', ['language_code', 'master_id'])

        # Adding model 'SimpleNewsCategory'
        db.create_table('cmsplugin_simplenews_simplenewscategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('cmsplugin_simplenews', ['SimpleNewsCategory'])

        # Adding model 'SimpleNewsTranslation'
        db.create_table('cmsplugin_simplenews_simplenews_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('lead', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['cmsplugin_simplenews.SimpleNews'])),
        ))
        db.send_create_signal('cmsplugin_simplenews', ['SimpleNewsTranslation'])

        # Adding unique constraint on 'SimpleNewsTranslation', fields ['language_code', 'master']
        db.create_unique('cmsplugin_simplenews_simplenews_translation', ['language_code', 'master_id'])

        # Adding model 'SimpleNews'
        db.create_table('cmsplugin_simplenews_simplenews', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_simplenews.SimpleNewsCategory'])),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('cmsplugin_simplenews', ['SimpleNews'])

        # Adding model 'SimpleNewsExcerptPlugin'
        db.create_table('cmsplugin_simplenewsexcerptplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('limit', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('cmsplugin_simplenews', ['SimpleNewsExcerptPlugin'])

        # Adding M2M table for field categories on 'SimpleNewsExcerptPlugin'
        db.create_table('cmsplugin_simplenews_simplenewsexcerptplugin_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('simplenewsexcerptplugin', models.ForeignKey(orm['cmsplugin_simplenews.simplenewsexcerptplugin'], null=False)),
            ('simplenewscategory', models.ForeignKey(orm['cmsplugin_simplenews.simplenewscategory'], null=False))
        ))
        db.create_unique('cmsplugin_simplenews_simplenewsexcerptplugin_categories', ['simplenewsexcerptplugin_id', 'simplenewscategory_id'])


    def backwards(self, orm):
        
        # Deleting model 'SimpleNewsCategoryTranslation'
        db.delete_table('cmsplugin_simplenews_simplenewscategory_translation')

        # Removing unique constraint on 'SimpleNewsCategoryTranslation', fields ['language_code', 'master']
        db.delete_unique('cmsplugin_simplenews_simplenewscategory_translation', ['language_code', 'master_id'])

        # Deleting model 'SimpleNewsCategory'
        db.delete_table('cmsplugin_simplenews_simplenewscategory')

        # Deleting model 'SimpleNewsTranslation'
        db.delete_table('cmsplugin_simplenews_simplenews_translation')

        # Removing unique constraint on 'SimpleNewsTranslation', fields ['language_code', 'master']
        db.delete_unique('cmsplugin_simplenews_simplenews_translation', ['language_code', 'master_id'])

        # Deleting model 'SimpleNews'
        db.delete_table('cmsplugin_simplenews_simplenews')

        # Deleting model 'SimpleNewsExcerptPlugin'
        db.delete_table('cmsplugin_simplenewsexcerptplugin')

        # Removing M2M table for field categories on 'SimpleNewsExcerptPlugin'
        db.delete_table('cmsplugin_simplenews_simplenewsexcerptplugin_categories')


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
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_simplenews']
