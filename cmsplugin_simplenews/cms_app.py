from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SimpleNewsApphook(CMSApp):
    name = _("Simple news")
    urls = ["cmsplugin_simplenews.urls"]


def calculate_hook():
    """Return url where current page is hooked"""
    import models
    from cms import models as cms_models
    from django.utils import translation
    language = translation.get_language()
    hook = cms_models.Title.objects.filter(
        language=language, 
        application_urls='SimpleNewsApphook',
    )[0]
    return hook.path


apphook_pool.register(SimpleNewsApphook)