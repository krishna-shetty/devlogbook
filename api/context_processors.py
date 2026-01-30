from django.conf import settings


def google_analytics(request):
    """Expose GA_MEASUREMENT_ID and DEBUG to templates."""
    return {
        'GA_MEASUREMENT_ID': getattr(settings, 'GA_MEASUREMENT_ID', None),
        'DEBUG': settings.DEBUG,
    }
