from django.shortcuts import render
from django.views import View


class Index(View):
	@staticmethod
	def get(request, **webUrl):
		if not webUrl:
			context = {}
			template = 'index.html'

		else:
			context = {}
			print(webUrl['webUrl'])
			template = 'index.html'

		return render(request, template, context)
