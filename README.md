# An-eCommerce-Recommender-System

## Overview

To run this program, run *recommend.py*. This will recommend 3 classes for a target user. Detailed instructions are included below to
allow for generation of recommendations for a new user.

This program was built in order to create a recommender system for a **LIFT gym mock website** which can be viewed [here (*work in progress*)](https://github.com/feiIin/django-ecommerce/tree/jymbud_recommend).
This program allows new users to sign up and express their interest in different workout plans or categories, and this data can be used to 
recommend specific classes to them.

This is a recommender system built to work for data from lift gyms in Edinburgh [(lift-gyms.co.uk)](lift-gyms.co.uk). LIFT gyms provide many classes (both
paid and free) to it's members. A recommender system would be very helpful here, as this is a classic recommender system problem (a
user-item matrix with many unfilled cells). Members of LIFT gyms can view their history of classes attended on the LIFT gym phone app.

## Design & Implementation

A nearest neighbour collaborative filtering method using taxonomies of items was used to achieve recommendations, which was a direct
implementation of the methodology outlined in (Ziegler, 2004, DOI: 10.1145/1031171.1031252). Like that paper, the data here has a native
classification hierarchy. LIFT gyms has categorised all of their classes into different categories (each category can have many classes).
Above that, they have categorised all their categories into different plans (each plan can have many categories). 

Points were assigned to categories and plans for each user by propagating points through the tree for each class they have taken (and the
amount of times the hava taken that class). So, if the users takes the *Absolute Abs* class, the user will score some points in the 
*Core* category of classes, and a smaller number of points again in the *Build Muscle* plan of categories.

The users were then matched based on their distance from othet users based on the *cosine* similarity metric. The nearest neighbours
then influenced which class would be recommended to the target user.

Data was created in the same format it would be gathered from the LIFT gyms official app, and it was saved to a csv file. This data was
pre-processed and normalised until a user-item matrix was created with processed and normalised data. Nearest Neighbour methods were then
performed, and the most popular classes amongst nearest neighbours were identified and recommended to the target user (excluding classes
the user has already attended). For detailed information, read below.


## Requirements
- pandas
- numpy
- sklearn


## Role of each Python file

**A Priori**

*constants.py*

Constants used throughout the project.

**Scripts in order of Use**

*load_usage_data.py*

Load in csv files of the users information, the class information, and the history of classes attended by users. Merge them into 1 table.

*load_user_item_matrix.py*

Initialise an empty user-item matrix, rows = users, columns = classes,categories,plans

*populate_user_item_matrix.py*

Fill the user-item matrix with raw data scores from user attendance.

*normalise_user_item_matrix.py*

Create a user-item matrix with normalised data.

*recommend.py*

For a target user, find the nearest neighbours of that user and recommend this target user unseen classes depending on neighbour ratings.
