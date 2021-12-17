Title of the project: Craig ad list retrieval

PROJECT-DESCRIPTION:
	craigslist.org is an online platform where users can post any gigs about various services like tutoring, marketing, ads etc. For this 
    project we will be scraping all the gig data or the ad data from craigslist.org and will be using it for building a search engine 
    (IR-system) on top of it to retrieve ad data when a user enters a query.


INSTRUCTIONS FOR RUNNING THE PROJECT:

STEP-1: INSTALLING THE REQUIRED PACKAGES

    pip install requirements.txt
    This will install all the required packages for the project to run.

STEP - 2 : GETTING THE REQUIRED DATASET

For the dataset,
	You can get the dataset by 2 ways

    Choice - 1 : By scraping the web:
	    This can be done by running the command,
            python script.py

    Choice - 2 : Downloading dataset from github/drive

STEP-3 : INDEXING THE DATASET:

    After getting the dataset, Run 
        python positionalindex.py
    This will generate a positional index for the dataset

STEP-3: RUNNING THE PROJECT FOR QUERYING

    Then run ranking.py,
        python ranking.py
    With this command the user will be able to run the program where the user will be prompted to enter a query.	

Description of the functions:
    