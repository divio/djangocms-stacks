from classytags.arguments import Argument, KeywordArgument
from classytags.core import Tag, Options
from django import template
from django.utils import translation
from django.utils.safestring import mark_safe
from stacks import models as stack_models

register = template.Library()

class StackNode(Tag):
    name = 'stack'
    options = Options(
        Argument('code', required=True),
        KeywordArgument('language', required=False, default=None, ),
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, code, language, varname):
        if not code:
            # an empty string was passed in or the variable is not available in the context
            return ''
        current_language = translation.get_language()
        language = language or current_language
        if not language == current_language:
            translation.activate(language)

        # TODO: caching?
        stack, created = stack_models.Stack.objects.get_or_create(code=code, defaults={'name': code})
        placeholder = stack.content
        rendered_placeholder = mark_safe(placeholder.render(context, None))
        if varname:
            context[varname] = rendered_placeholder
            rendered_placeholder = u''

        if not language == current_language:
            translation.activate(current_language)
        return rendered_placeholder

register.tag(StackNode)