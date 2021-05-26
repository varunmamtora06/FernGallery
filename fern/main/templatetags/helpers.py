from django import template
register = template.Library()

from ..models import Profile
from django.core.exceptions import ObjectDoesNotExist



@register.filter(name='profile_exists')
def profile_exists(user):
    print(user)
    try:
        print(Profile.objects.get(user=user))
        return True
    except ObjectDoesNotExist:
        return None