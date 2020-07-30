from flask import Flask, request, redirect, jsonify
from kpopy import get_specific_artist, get_similar_artist

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#/equal?
@app.route("/equals", methods=['GET'])
def equal():
    data = request.args
    stage_name = data.get('stage_name') if data.get('stage_name') else ''
    full_name = data.get('full_name') if data.get('full_name') else ''
    korean_name = data.get('korean_name') if data.get('korean_name') else ''
    korean_stage_name = data.get('korean_stage_name') if data.get('korean_stage_name') else ''
    dob = data.get('date_of_birth') if data.get('date_of_birth') else ''
    group = data.get('group') if data.get('group') else ''
    country = data.get('country') if data.get('country') else ''
    second_country = data.get('second_country') if data.get('second_country') else ''
    height = data.get('height') if data.get('height') else ''
    weight = data.get('weight') if data.get('weight') else ''
    birthplace = data.get('birthplace') if data.get('birthplace') else ''
    other_group = data.get('other_group') if data.get('other_group') else ''
    former_group = data.get('former_group') if data.get('former_group') else ''
    gender = data.get('gender') if data.get('gender') else ''
    position = data.get('position') if data.get('position') else ''
    instagram = data.get('instagram') if data.get('instagram') else ''
    twitter = data.get('twitter') if data.get('twitter') else ''
    print("getting:", stage_name, full_name, korean_name, korean_stage_name)
    kpop_data = get_specific_artist(stage_name = stage_name, full_name = full_name, korean_name = korean_name,
                                korean_stage_name = korean_stage_name, dob = dob, group = group, country = country,
                                second_country = second_country, height = height, weight =weight, birthplace = birthplace,
                                other_group = other_group, former_group = former_group, gender = gender, position = position,
                                instagram = instagram, twitter = twitter)

    print("gathered:", kpop_data)
    return jsonify(kpop_data)

@app.route("/contains", methods=['GET'])
def contains():
    data = request.args
    stage_name = data.get('stage_name') if data.get('stage_name') else ''
    full_name = data.get('full_name') if data.get('full_name') else ''
    korean_name = data.get('korean_name') if data.get('korean_name') else ''
    korean_stage_name = data.get('korean_stage_name') if data.get('korean_stage_name') else ''
    dob = data.get('date_of_birth') if data.get('date_of_birth') else ''
    group = data.get('group') if data.get('group') else ''
    country = data.get('country') if data.get('country') else ''
    second_country = data.get('second_country') if data.get('second_country') else ''
    height = data.get('height') if data.get('height') else ''
    weight = data.get('weight') if data.get('weight') else ''
    birthplace = data.get('birthplace') if data.get('birthplace') else ''
    other_group = data.get('other_group') if data.get('other_group') else ''
    former_group = data.get('former_group') if data.get('former_group') else ''
    gender = data.get('gender') if data.get('gender') else ''
    position = data.get('position') if data.get('position') else ''
    instagram = data.get('instagram') if data.get('instagram') else ''
    twitter = data.get('twitter') if data.get('twitter') else ''
    print("getting:", stage_name, full_name, korean_name, korean_stage_name, dob, group, country, second_country, height, weight,
                     birthplace, other_group, former_group, gender, position, instagram, twitter)
    kpop_data = get_similar_artist(stage_name = stage_name, full_name = full_name, korean_name = korean_name,
                                korean_stage_name = korean_stage_name, dob = dob, group = group, country = country,
                                second_country = second_country, height = height, weight =weight, birthplace = birthplace,
                                other_group = other_group, former_group = former_group, gender = gender, position = position,
                                instagram = instagram, twitter = twitter)

    print("gathered:", kpop_data)
    return jsonify(kpop_data)

@app.route("/instructions")
def instructions():
    text = "<h1> instructions </h1><br>"
    text += "use /equals to get if you want parameters to be exact and /contains if looking less strict parameters (all case insensitive) <br>"
    text += "add ? after then add the parameters you want"
    text += "parameters: stage_name,  full_name,  korean_name, korean_stage_name, date_of_birth, group, country, second_country, height, weight, birthplace, other_group, former_group, gender, position, instagram, twitter <br>"
    text += "ex: https://kpop-api.herokuapp.com/equals?stage_name=Yeji&group=ITZY <br>"
    text += "data scraped from https://dbkpop.com/"
    return text

@app.route("/")
def index():
    return redirect("http://yoonpatrick3.github.io")

if __name__ == '__main__':
    app.run(debug=True)