import requests
import xml.etree.ElementTree as et
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator


def home(request):
    # routine = []
    # intensity = request["intensity"]
    # targets = request["targets"]
    # duration = request["duration"]/10
    # for target in targets:
    response = requests.get('http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input=yoga%20poses%20to%20stretch%20calves')
    tree = et.ElementTree(response.content.decode("utf-8"))
    root = tree.getroot()

    response_good = (response.status_code == 200)
    if response_good:
        message = "It worked!"
    else:
        message = "Oh no! Search API returned %d" % response.status_code

    return render(request, 'core/home.html', {
        'message': message,
        'data': root
    })
