from django.shortcuts import render
from django.views import View


class Index(View):
	@staticmethod
	def get(request, **webUrl):
		if not webUrl:
			context = {}
			template = ''

		else:
			context = {}
			template = ''

		return render(template, context)
