# Ads data analysis


## Context and objectives 

Within the framework of proficiency test, I carried out an analysis based on user profiles and advertisement data to help developp business and product ideas. 


## Import data into a database

From data contained in several csv files, I set up in postgresql database to conduct my analysis and sqlite database to ilustrate the better choice in terms of relational database management system. 

I have chosen to use PostgreSQL for analysis because overall I prefer postgresql syntax that I find smarter (filter clause, with queries etc.)
Moreover, PostgreSQL is for high volume processing in a business application, more suitable for production.

However, it would have been easier to use SQLite (zero-configuration, self_contained, serverless) for quick analysis. SQLite is more suitable to make it production-ready because it represents a response to portability and reliability issues. That's why I also made a script that imports the '.csv' files into a SQLite database.

Scripts can be run on the current working directory with the other files. For the SQLite import, the database_name will be specified when launching the script. I didn’t specify the absolute path. If the database not exist, then python will create the databse in the current working directory.

In the same directory from script, we could create a Dockerfile to indicate the configuration statements needed to create the Docker Image such as:

On Mac OS environment:

- FROM python:3.8 **(Python 3.8 base image from the Docker)**
- COPY ./ requirements.txt ./ **(file with python packages required to run the script, for example pandas==1.1.4, located in the root directory of my project, I did not have time to create it)**
- RUN pip3 install -r requirements.txt **(running installation for packages required)**
- COPY import_sqlite.py Users/Documents/gdf **(working directoy : for me)**
- CMD [ "python 3.8", "./import_sqlite.py" ] **(running the import_sqlite.py script when the container is started)**

After creating the script and the Dockerfile, it can build Docker Image with the Docker build command:

- docker build -t test_gdf .  (test_gdf is the Docker image name)
 
Finally, it can run the docker container on local machine:

- docker run -p 80:80 -t test_gdf (port 8080)


## Analytical approach :

After a first exchange information with the Talent Acquisition Manager, I noted two important issues beyond the growth in the number of users:

- the increase in the activity of these users
- the development of new verticals

In terms of products and features, the website already seems to purpose a referrers recommendation engine and an ad suggestion engine.

From the data available, I focused the analysis on three prisms:

- mapping of users
- difference between the starting price and the sold price
- user traffic and connection informations

The analysis was carried out in a jupyter notebook and presented in a google slides document (current repository)
