import requests
import xml.etree.ElementTree as et
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator
from lxml import etree
import xml.etree.ElementTree as et
from .models import Pose


def home(request):
    # response = requests.get('http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input=yoga%20poses%20to%20stretch%20calves')
    # tree = et.ElementTree(response.content.decode("utf-8"))
    #
    # root = et.fromstring(response.content)
    # for elem in root.iterfind('pod/subpod[@title="Beginner"]/img'):
    #     poses = elem.attrib['alt']
    #
    # poses = poses.split("|")
    #
    # stripped = [pose.strip() for pose in poses]
    # stripped.pop()
    # stripped = [pose.replace(" ", "%20") for pose in stripped]
    #
    # # for pose in stripped:

    response = requests.get('http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input=Dolphin%20Pose')
    tree = et.ElementTree(response.content.decode("utf-8"))

    root = et.fromstring(response.content)

    # name = [pose.replace("%20", " ")]
    name = "Dolphin Pose"

    for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
        image = elem.attrib['src']

    for elem in root.iterfind('pod[@title="Instructions"]/subpod/img'):
        description = elem.attrib['alt']

    target = "calves"
    # print(name, image, description, target)
    # dummy = Pose.objects.create(name=name, image=image, description=description, target=target)
    # dummy.save()
    dummy = Pose.objects.all()
    print(dummy)

    response_good = (response.status_code == 200)
    if response_good:
        message = "It worked!"
    else:
        message = "Oh no! Search API returned %d" % response.status_code

    return render(request, 'core/home.html', {
        'message': message,
        'data': root
    })\
