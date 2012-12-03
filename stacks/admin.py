from cms.utils import get_language_from_request
from django.contrib import admin
from stacks.models import Stack
from cms.admin.placeholderadmin import PlaceholderAdmin
from django.conf import settings


class StackAdmin(PlaceholderAdmin):
    list_display = ('name', 'code',)
    search_fields = ('name', 'code',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = self.update_language_tab_context(request, obj, context)
        tab_language = request.GET.get("language", None)
        response = super(StackAdmin, self).change_view(request, object_id, extra_context=extra_context)

        if tab_language and response.status_code == 302 and response._headers['location'][1] == request.path :
            location = response._headers['location']
            response._headers['location'] = (location[0], "%s?language=%s" % (location[1], tab_language))
        return response

    def update_language_tab_context(self, request, obj, context=None):
        if not context:
            context = {}
        language = get_language_from_request(request, obj)
        languages = [lang for lang, __ in settings.LANGUAGES]
        context.update({
            'language': language,
            'language_tabs': languages,
            'show_language_tabs': len(languages) > 1,
            })
        return context

admin.site.register(Stack, StackAdmin)
