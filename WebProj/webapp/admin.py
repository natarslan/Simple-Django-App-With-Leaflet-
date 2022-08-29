from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Modelclass
from django.contrib.gis.geos import Point
import pandas as pd

# # Observe: country and geom are the fields you created in models.py
# @admin.register(Modelclass)
# class WebAdmin(admin.OSMGeoAdmin):
#     list_display = ('country', 'magnitude', 'geom')

# Observe: country and geom are the fields you created in models.py
@admin.register(Modelclass)
class WebAdmin(LeafletGeoAdmin):
    list_display = ('geom', 'magnitude', 'country')


# file = '/Users/nat/Desktop/Mooncake/Courses/Coding/DjangoApp/WebProj/earthquake.xls'
# df_excelReader = pd.read_excel(file, sheet_name="earthquake")

# # Read file and add data to table

# for index, row in df_excelReader.iterrows():
#     lat = row['latitude']
#     lon = row['longitude']
#     magnitude = row['mag']
#     country = row['country']

#     # Be sure to add longiture before latitude! Id=Id,
#     Modelclass(geom=Point(lon, lat), magnitude=magnitude, country=country).save()