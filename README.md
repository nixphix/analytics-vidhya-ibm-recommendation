![Banner](https://datahack.analyticsvidhya.com/media/__sized__/contest_cover/AV_Banner_1920x480_Nv3-thumbnail-1200x1200-90.jpg)
# [IBM Recommendation Engine Hackathon](https://datahack.analyticsvidhya.com/contest/build-a-recommendation-engine-powered-by-ibm-cloud/)

[Private Leaderboard](https://datahack.analyticsvidhya.com/contest/build-a-recommendation-engine-powered-by-ibm-cloud/pvt_lb):

- Score: 0.326319211973979


Public Leaderboard:

- Score: 0.321784658100713

# Challenge:

The challenge is to build a recommendation engine for a retailer based on users purchase history and expose the ML model as a rest service.
The train and test dataset comprised of disjoint set of users and their past purchases, country and time of purchase.


# Solution:

## Recommendation Engine

- The final recommendation engine is build with [Apple's Turi Create](https://github.com/apple/turicreate) using Item Similarity Recommender.

- A Django Rest API to expose the ML model as service, hosted on Heroku.


## REST API

The Django app has two API end points 

 - User based recommendation, given a `user_id` and an optional `k` for number of item recommendations required, estimator will predict k number of items. 

- Basket based recommendation, given list of `items` in user basket and an optional `k` number of item recommendation required, estimator will predict k number of items 

  

- Default value for k is 10 

   

***NOTE: The endpoints have a browsable django rest framework document, can also be accessed via Postman.
The api are hosted in Heroku, the apps may have been put to sleep by Heroku if there is no web traffic, so please give it a few minuit on first request to spin up the containers.***


User Based Recommendation
---  


**End Point**: https://**<YOUR_APP_NAME_HERE>**.herokuapp.com/recommend/user 

**HTTP Method**: POST 

**Payload**: 

 - user: required parameter it can be any user from the given dataset. 

 - k: number of required items recommendation, default is 10. 

**Sample Json Payload**: 
```javascript
      { 

        "user": 27270,   

        "k": 3  

      }   
```

**Sample Json Output**: 

```javascript
     { 
        "top_recommendation": [
            "21212D",
            "22178V",
            "22720A"
        ],
        "score": {
            "21212D": 0.1528126357532129,
            "22178V" 0.1359131576084509,
            "22720A": 0.13515295197324054
        },
        "estimator": "ItemSimilarityRecommender"
    } 

```


Items Based Recommendation
---


**End Point**: https://**<YOUR_APP_NAME_HERE>**.herokuapp.com/recommend/items 

**HTTP Method**: POST 

**Payload**: 

 - items: required parameter it can be any item from the given dataset. 

 - k: number of required items recommendation, default is 10. 

**Sample Json Payload**: 
```javascript
    {    
    "items": ["21212D", "22720A"],    
    "k": 5 
    } 
```
**Sample Json Output**: 

```javascript
    {     
        "top_recommendation": [
            "47566Y",
            "85099BJ",
            "85123AY",
            "22423U",
            "22666I"
        ],
        "score": { 
            "47566Y": 0.47120603919029236,
            "85099BJ": 0.470460444688797,
            "85123AY": 0.4658285975456238, 
            "22423U": 0.4650574326515198, 
            "22666I": 0.4602021276950836 
        }, 
        "estimator": "ItemSimilarityRecommender" 
    }
```

---


# API Deployment Instruction

Read below instruction to deploy the api in your own free Heroku account.

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
