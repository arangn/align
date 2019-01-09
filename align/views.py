from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


def home(request):
    # routine = []
    # intensity = request["intensity"]
    # targets = request["targets"]
    # duration = request["duration"]/10
    # for target in targets:
    typeHeader = {'Content-Type': 'application/json'}
    response = requests.get('http://api.wolframalpha.com/v2/query?appid=R95QUT-242XGA8U6T&input=yoga%20poses%20to%20stretch%20calves', headers = typeHeader)
    # print (response)

    # return render(request, 'core/home.html', {
    #     print (response)
    # })

# def home(request):
#     response = requests.get('http://freegeoip.net/json/')
#     geodata = response.json()
#     return render(request, 'core/home.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
#     })
