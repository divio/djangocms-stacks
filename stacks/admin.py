from cms.utils import get_language_from_request
from django.contrib import admin
from stacks.models import Stack
from cms.admin.placeholderadmin import PlaceholderAdmin
from django.conf import settings


class StackAdmin(PlaceholderAdmin):
    list_display = ('name', 'code',)
    search_fields = ('name', 'code',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self.language_tab_context(request))
        tab_language = request.GET.get("language", None)
        response = super(StackAdmin, self).change_view(request, object_id, extra_context=extra_context)

        if tab_language and response.status_code == 302 and response._headers['location'][1] == request.path:
            location = response._headers['location']
            response._headers['location'] = (location[0], "%s?language=%s" % (location[1], tab_language))
        return response

    def language_tab_context(self, request):
        language = get_language_from_request(request)
        languages = [(lang, lang_name) for lang, lang_name in settings.LANGUAGES]
        context = {
            'language': language,
            'language_tabs': languages,
            'show_language_tabs': len(languages) > 1,
        }
        return context

    def placeholder_plugin_filter(self, request, queryset):
        language = get_language_from_request(request)
        return queryset.filter(language=language)

admin.site.register(Stack, StackAdmin)
