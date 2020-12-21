# kpop-api-web
use /equals to get if you want parameters to be exact and /contains if looking less strict parameters (all case insensitive)

add ? after then add the parameters you wantparameters: stage_name, full_name, korean_name, korean_stage_name, date_of_birth, group, country, second_country, height, weight, birthplace, other_group, former_group, gender, position, instagram, twitter

ex: 

GET https://kpop-api.herokuapp.com/equals?stage_name=Yeji&group=ITZY

curl -X GET https://kpop-api.herokuapp.com/contains?country=Korea

data scraped from https://dbkpop.com/
