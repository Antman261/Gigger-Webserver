from django.shortcuts import render
from Gigger.utilities.ggr_config import *
from .models import Performer
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    context = {
        "OGTitle": "Gigger - The live music industry's search engine",
        "OGType": "website",
        "PageDescription": "Gigger is the fastest way to find bands for your next gig.",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }
    return render(request, 'search.html', context)

def faq(request):
    context = {
        "OGTitle": "Gigger - FAQ",
        "OGType": "website",
        "PageDescription": "Got a few questions about Gigger? Get all your answers and more...and find out how awesome our free online gig booking system is.",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }
    return render(request, 'faq.html', context)

def about(request):
    context = {
        "OGTitle": "Gigger - About",
        "OGType": "website",
        "PageDescription": "Why we do what we do at Gigger, what drives us, what keeps us madly striving to the great future we envision for the music industry",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }
    return render(request, 'about.html', context)

def blog(request):
    context = {
        "OGTitle": "Gigger - Blog",
        "OGType": "website",
        "PageDescription": "Want helpful tips, Gigger updates and insights from industry professionals? Read our blog!",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }
    return render(request, 'blog.html', context)

def contact(request):
    context = {
        "OGTitle": "Gigger - Contact",
        "OGType": "website",
        "PageDescription": "Gigger is the fastest way to find bands for your next gig.",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }
    return render(request, 'contact.html', context)

def privacy(request):
    import requests
    import json
    # $pp = file_get_contents('http://www.iubenda.com/api/privacy-policy/646296/only-legal');
    # $pp = json_decode($pp);
    # if ($pp->success == true) {
    #   $PrivacyView['IUB_Content'] =  $pp->content;
    # }
    context = {
        "OGTitle": "Gigger - Privacy",
        "OGType": "website",
        "PageDescription": "Learn more about Gigger's privacy policy and practices, including what types of info Gigger receives and how info is used and shared.",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }

    r = requests.get("http://www.iubenda.com/api/privacy-policy/646296/only-legal")
    if r.status_code == 200:
        r_json = json.loads(r.content.decode('utf-8'))
        if r_json['success']:
            context['IUB_Content'] = r_json['content']
    return render(request, 'privacy.html', context)

def tos(request):
    context = {
        "OGTitle": "Gigger - Terms and Conditions",
        "OGType": "website",
        "PageDescription": "Learn how use of Gigger.rocks is subject to the following terms and conditions.",
        "OGImage": "https://cdn.gigger.rocks/img/ggrlp2.png",
        "PageKeywords": "",
    }
    return render(request, 'tos.html', context)

def catchall(request):
    try:
        p = Performer.objects.get(username=request.path.strip('/'))

        if p and p.deleted == 0:
            import json
            events_json = []
            for event in p.events.all():
                events_json.append({
                    "title": event.name,
                    "date": event.start_time[:10]
                })

            context = {
                "OGTitle": p.name,
                "PageDescription": p.about,
                "OGImage": p.cover_source,
                "performer": p,
                "events_json": json.dumps(events_json)
            }
            return render(request, 'bandprofile.html', context)
        else:
            return render(request, '404.html')
    except ObjectDoesNotExist:
        return render(request, '404.html')
