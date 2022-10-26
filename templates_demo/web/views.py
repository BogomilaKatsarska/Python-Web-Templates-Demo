import datetime
import random

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name:{self.name}; Age:{self.age}'


def index(request):
    context = {
        'title': 'softUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia',
        },
        'student': Student('Bogomila', 27),
        'now': datetime.datetime.now(),
        'students': ['Pesho', 'Gosho', 'Maria', 'Stamat'],
        'values': list(range(20)),
    }

    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')

