from .utilities.ggr_config import *

def globals(request):
    NoGA = False
    if 'Speed Insights' in request.META.get('HTTP_USER_AGENT', ''):
        NoGA = True
    return {
        "FB_APP_ID": CONFIG['FB_APP_ID'],
        "ENV": {
            "DEPLOYMENT": CONFIG['DEPLOYMENT'],
            "NoGA": NoGA
        }
    }
