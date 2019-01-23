import requests
import xml.etree.ElementTree as et
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator
from lxml import etree
import xml.etree.ElementTree as et
from .models import Pose
from .models import Sequence
from .serializers import SequenceSerializer
from .serializers import PoseSerializer
from rest_framework import generics


class SequenceView(generics.ListAPIView):

    # queryset = Sequence.objects.all()
    model = Sequence
    serializer_class = SequenceSerializer

    def get_queryset(self):
        queryset = Sequence.objects.all()
        target = self.request.query_params.get('target', None)
        if target is not None:
            queryset = queryset.filter(target=target)

        return queryset

class PoseView(generics.ListAPIView):

    # queryset = Sequence.objects.all()
    model = Pose
    serializer_class = PoseSerializer

    def get_queryset(self):
        queryset = Pose.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)


        return queryset
#


# def home(request):
#
#     target = "abdominals"
#     practice = "stretch"
#     level = "Intermediate"
#
#     response = requests.get(f'http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input=yoga%20poses%20to%20{practice}%20{target}&format=image')
#
#     tree = et.ElementTree(response.content.decode("utf-8"))
#     root = et.fromstring(response.content)
#
#     for elem in root.iterfind(f'pod/subpod[@title="{level}"]/img'):
#         raw_list = elem.attrib['alt']
#
#     raw_list = raw_list.split("|")
#
#     poses_list = [pose.strip() for pose in raw_list]
#     poses_list.pop()
#     poses_to_call = [pose.replace(" ", "%20") for pose in poses_list]
#
#     for pose in poses_to_call:
#         name = pose.replace("%20", " ")
#         check = Pose.objects.filter(name=name)
#         #CHANGE BACK TO NOT
#         if not check:
#             response = requests.get(f'http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input={pose}')
#             tree = et.ElementTree(response.content.decode("utf-8"))
#             root = et.fromstring(response.content)
#
#             for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
#                 image = elem.attrib['src']
#             for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
#                 height = elem.attrib['height']
#             for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
#                 width = elem.attrib['width']
#             for elem in root.iterfind('pod[@title="Instructions"]/subpod/img'):
#                 description = elem.attrib['alt']
#
#             new_pose = Pose.objects.create(name=name, image=image, description=description, target=target, level=level, height=height, width=width)
#             new_pose.save()
#
#             sequence = []
#             sequence.append(new_pose)
#
#             while description.startswith('From ') and new_pose.name != "Easy Pose" and new_pose.name != "Reclining Big Toe Pose A":
#                 temp = description.split("From ", 1)
#                 temp2 = temp[1].split(", ", 1)
#                 next_pose = temp2[0].replace(" ", "%20")
#                 check2 = Pose.objects.filter(name=temp2[0])
#
#                 if not check2:
#                     response = requests.get(f'http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input={next_pose}')
#                     tree = et.ElementTree(response.content.decode("utf-8"))
#                     print(tree)
#                     root = et.fromstring(response.content)
#                     for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
#                         image = elem.attrib['src']
#                     for elem in root.iterfind('pod[@title="Instructions"]/subpod/img'):
#                         description = elem.attrib['alt']
#                     for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
#                         height = elem.attrib['height']
#                     for elem in root.iterfind('pod[@title="Schematic"]/subpod/img'):
#                         width = elem.attrib['width']
#
#                     new_pose = Pose.objects.create(name=temp2[0], image=image, description=description, target=target, level=level, height=height, width=width)
#                     new_pose.save()
#
#                 else:
#                     new_pose = Pose.objects.get(name=temp2[0])
#                     description = new_pose.description
#
#                 sequence.insert(0, new_pose)
#                 print(sequence)
#
#             new_seq = Sequence.objects.create(name=sequence[-1].name, target=target)
#             new_seq.save()
#             new_seq.poses.set(sequence)
#
#
#     response_good = (response.status_code == 200)
#     if response_good:
#         message = "It worked!"
#     else:
#         message = "Oh no! Search API returned %d" % response.status_code
#
#     return render(request, 'core/home.html', {
#     'message': message,
#     'data': root
#     })\
