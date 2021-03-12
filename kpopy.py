import json

with open("kpop_data.json", "r", encoding='utf-8-sig') as read_file:
    all_artist = json.load(read_file)

'''
# removes unnecessary things
for artist in all_artist:
    if '_id'in artist:
        del artist['_id']
    if 'T00:00:00.000Z' in artist['Date of Birth']:
        artist['Date of Birth'] = artist['Date of Birth'].replace('T00:00:00.000Z', '')
'''

def get_specific_artist(stage_name='', full_name='', korean_name='', korean_stage_name='', dob='', 
                        group='', country='', second_country='', height='', weight='', birthplace='', 
                        other_group='', former_group='', gender='', position='', instagram='', twitter=''):
    attributes = [stage_name, full_name, korean_name, korean_stage_name, dob, group, country,
                    second_country, height, weight, birthplace, other_group, former_group, gender,
                    position, instagram, twitter]
    artists = []
    for artist in all_artist:
        artist_attributes = [artist['Stage Name'], artist['Full Name'], artist['Korean Name'],
                            artist['Korean Stage Name'], artist['Date of Birth'], artist['Group'],
                            artist['Country'], artist['Second Country'], artist['Height'],
                            artist['Weight'], artist['Birthplace'], artist['Other Group'], 
                            artist['Former Group'], artist['Gender'], artist['Position'], 
                            artist['Instagram'], artist['Twitter']]
        isIn = True

        for i in range(len(attributes)):
            if attributes[i] != '' and attributes[i].lower() != artist_attributes[i].lower():
                isIn = False
                break
        if isIn:
            artist['Stage_Name'] = artist.pop('Stage Name')
            artist['Full_Name'] = artist.pop('Full Name')
            artist['Korean_Name'] = artist.pop('Korean Name')
            artist['Korean_Stage_Name'] = artist.pop('Korean Stage Name')
            artist['Date_of_Birth'] = artist.pop('Date of Birth')
            artist['Second_Country'] = artist.pop('Second Country')
            artist['Other_Group'] = artist.pop('Other Group')
            artist['Former_Group'] = artist.pop('Former Group')
            artists.append(artist)
    return artists
        
def get_similar_artist(stage_name='', full_name='', korean_name='', korean_stage_name='', dob='', 
                        group='', country='', second_country='', height='', weight='', birthplace='', 
                        other_group='', former_group='', gender='', position='', instagram='', twitter=''):
    attributes = [stage_name, full_name, korean_name, korean_stage_name, dob, group, country,
                    second_country, height, weight, birthplace, other_group, former_group, gender,
                    position, instagram, twitter]
    artists = []
    for artist in all_artist:
        
        
        
        artist_attributes = [artist['Stage Name'], artist['Full Name'], artist['Korean Name'],
                            artist['Korean Stage Name'], artist['Date of Birth'], artist['Group'],
                            artist['Country'], artist['Second Country'], artist['Height'],
                            artist['Weight'], artist['Birthplace'], artist['Other Group'], 
                            artist['Former Group'], artist['Gender'], artist['Position'], 
                            artist['Instagram'], artist['Twitter']]
        isIn = True

        for i in range(len(attributes)):
            if attributes[i] != '' and attributes[i].lower() not in artist_attributes[i].lower():
                isIn = False
                break
        if isIn:
            artist['Stage_Name'] = artist.pop('Stage Name')
            artist['Full_Name'] = artist.pop('Full Name')
            artist['Korean_Name'] = artist.pop('Korean Name')
            artist['Korean_Stage_Name'] = artist.pop('Korean Stage Name')
            artist['Date_of_Birth'] = artist.pop('Date of Birth')
            artist['Second_Country'] = artist.pop('Second Country')
            artist['Other_Group'] = artist.pop('Other Group')
            artist['Former_Group'] = artist.pop('Former Group')
            artists.append(artist)
    return artists

print(get_similar_artist(country="usa"))