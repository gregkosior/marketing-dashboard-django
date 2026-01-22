from django.shortcuts import render

def home(request):
	return render(request, "index.html")

from django.shortcuts import render
from django.http import JsonResponse
from .models import ShopData
from django.db.models import Sum


def api_summary(request):
	agg = ShopData.objects.aggregate(
		total_cost=Sum("cost"),
		total_revenue=Sum("revenue"),
		total_pandl=Sum("pandl")
	)
	return JsonResponse(agg)

def api_group(request):
	groups = (
		ShopData.objects.values("ad_group")
		.annotate(total_pandl=Sum("pandl"))
		.order_by("-total_pandl")
	)
	return JsonResponse(list(groups), safe=False)
