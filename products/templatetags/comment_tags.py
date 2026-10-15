from webbrowser import register

from django import template


register = template.Library()

@register.filter
def only_active_comments(cmmnts):
	return cmmnts.filter(status_cmmnt = True) # or cmmnts.exclude(status_cmmnt = False)
