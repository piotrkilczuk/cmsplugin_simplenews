from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.template import Context, Template
from django.utils.translation import ugettext as _
from models import *
from settings import *


class CMSSimpleNewsPlugin(CMSPluginBase):
    model = SimpleNewsExcerptPlugin
    name = _("Simple news excerpt")
    render_template = "cmsplugin_simplenews/simple_news.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'news': instance.get_news_set(),
        })
        return context


plugin_pool.register_plugin(CMSSimpleNewsPlugin)