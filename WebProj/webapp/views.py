from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
import json
from .models import Modelclass

# Create view and get all the markers without filtering them
# class MapView(GeoJSONLayerView): # Thid turned the http://localhost:8000/map/ into a geojson data
class MapView(TemplateView):
   
    queryset = Modelclass.objects.all()
    template_name = 'index.html'

# Convert all the markers to geojson (Working)
# Serializer is one method of displaying all data. Check your DjangoApp.ipynb for more
# Reference: https://docs.djangoproject.com/en/3.1/ref/contrib/gis/serializers/
# Reference: https://dev.to/pauloxnet/maps-with-django-part-1-geodjango-spatialite-and-leaflet-2bn2
def all_earthquake(request):
    markers = serialize('geojson', Modelclass.objects.all(), geometry_field='geom')
    return HttpResponse(markers ,content_type='json')

    
    # serialize('geojson', Modelclass.objects.all(),
    #       geometry_field='geom')


