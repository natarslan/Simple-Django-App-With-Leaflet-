from django.contrib import admin
from django.urls import  path, re_path, include
from djgeojson.views import GeoJSONLayerView # Use this to visualise the markers

from .models import Modelclass
from .views import * # This imports the MapView the all_earthquake function from views.py
#from .views import all_earthquake # This imports the all_earthquake function from views.py


# Observe name='data' --> You define data here and use it in the index.html
# Notice: The map will be displayed at: http://localhost:8000/map/
# Notice: the geojson data will be displayed at: http://localhost:8000/data/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', MapView.as_view()),

    # You need to define the properties in order to use them in index.html For example in your popups.
    path('data/', GeoJSONLayerView.as_view(model=Modelclass, properties=('geom', 'magnitude', 'country')), name='data'),

    # Below path is connected to a serializer function. Defined in view.py.
    path('mydata/', all_earthquake, name='mydata'),
    
]

