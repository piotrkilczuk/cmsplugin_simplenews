from multilingual.admin import MultilingualModelAdminForm
import models

class SimpleNewsForm(MultilingualModelAdminForm):
    
    class Meta: 
        from cms.plugins.text.widgets import wymeditor_widget 
        model = models.SimpleNews
        fields = ('category', 'title', 'image', 'subtitle', 'lead', 'content', 'published',)
        widgets = {
            'content': wymeditor_widget.WYMEditor(),
        }