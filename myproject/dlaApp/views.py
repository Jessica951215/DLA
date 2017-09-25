# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def visual(request):
	return render(request, "dlaApp/visual.html")

