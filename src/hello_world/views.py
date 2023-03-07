import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import speedtest
import json

def speed_test():
    servers = [5243, 7575, 3783, 6883, 5354, 3402]
    threads = None
    s = speedtest.Speedtest()

    try:
        s.get_servers(servers)

    except Exception as e:
        return json.dumps({'status': 'error', 'message': 'An error occured. Please, try later'}, separators=(',', ':'))

    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()

    result = json.dumps({
        'status': 'success',
        'download': f"{results_dict['download'] / 1024 / 1024:.2f}",
        'upload': f"{results_dict['upload'] / 1024 / 1024:.2f}",
        'ping': f"{results_dict['ping']:.2f}"
    }, separators=(',', ':'))

    return result


def hello_world(request):
    result = random.randint(1, 100)
    return HttpResponse(f"{speed_test()}")
