from django import template

register = template.Library()


@register.filter
def can_download_profiles(user):
    return user.has_perm('myapp.download_profiles')
