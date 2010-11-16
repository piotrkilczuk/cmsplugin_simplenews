from django.contrib import admin
import forms
import models
from multilingual.admin import MultilingualModelAdmin


class SimpleNewsAdmin(MultilingualModelAdmin):
    form = forms.SimpleNewsForm
    list_display = ('published', 'title',)
    list_display_links = ('title',)
    list_filter = ('category', 'published',)
    ordering = ['-published']
    search_fields = ('title', 'subtitle',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        """Hack the widgets attribute"""
        from cms.plugins.text.widgets import wymeditor_widget
        if db_field.name == 'content':
            kwargs['widget'] = wymeditor_widget.WYMEditor()
        return super(admin.ModelAdmin, self).formfield_for_dbfield(db_field, **kwargs) 

    class Media:
        js = ('cms/js/lib/jquery.js',)


class SimpleNewsCategoryAdmin(MultilingualModelAdmin):
    pass


admin.site.register(models.SimpleNews, SimpleNewsAdmin)
admin.site.register(models.SimpleNewsCategory, SimpleNewsCategoryAdmin)