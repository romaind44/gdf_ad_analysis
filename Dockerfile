FROM python:3.8
COPY import_sqlite.py Users/Documents/gdf
CMD [ "python 3.8", "./import_sqlite.py" ]