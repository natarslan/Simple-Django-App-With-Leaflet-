
from csv import DictReader
from django.core.management import BaseCommand
from django.contrib.gis.geos import Point
import pandas as pd


# Import the model 
from webapp.models import Modelclass


#Code to load the data into database

class Command(BaseCommand):

    def handle(self, *args, **options):

        # Read excel file with pandas // sheet_name="earthquake", index_col=0

        if Modelclass.objects.exists():
            print('child data already loaded...exiting.')
            return

        # # Im still abit unsure on how to load data to djamgo server
        # # You dont need this because you loaded our data from earthquake_data.py 
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


