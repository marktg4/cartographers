# Build the deck of cards as a dictionary, storing an index value, card type, set, shapes, coins, rotation, name, terrains, corner, ruin, time value, time threshold
#  season edicts, edict letter, edict description, edict score value

# Template

# card_one = {
#     'index': 1,
#     'type': 'ambush',
#     'set': 'base',
#     'shape': [1],
#     'coin': [False],
#     'rotation': 'cc',
#     'name': 'goblin attack',
#     'terrain': ['monster'],
#     'corner': 'br',
#     'ruin': False,
#     'time_value': 0,
#     'time_threshold': '',
#     'season_edicts': [''],
#     'edict_letter': '',
#     'edict_description': '',
#     'edict_score_value': ''
# }
import textwrap

card_one = {
    'index': 1,
    'type': 'ambush',
    'set': 'base',
    'shape': [0],
    # 'coin': [False],
    'rotation': 'cc',
    'name': 'goblin attack',
    'terrain': ['monster'],
    'corner': 'br',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_two = {
    'index': 2,
    'type': 'ambush',
    'set': 'base',
    'shape': [1],
    # 'coin': [False],
    'rotation': 'cw',
    'name': 'bugbear assault',
    'terrain': ['monster'],
    'corner': 'tr',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_three = {
    'index': 3,
    'type': 'ambush',
    'set': 'base',
    'shape': [2],
    # 'coin': [False],
    'rotation': 'cw',
    'name': 'kobold onsluaght',
    'terrain': ['monster'],
    'corner': 'bl',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_four = {
    'index': 4,
    'type': 'ambush',
    'set': 'base',
    'shape': [3],
    # 'coin': [False],
    'rotation': 'cc',
    'name': 'gnoll raid',
    'terrain': ['monster'],
    'corner': 'tl',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_five = {
    'index': 5,
    'type': 'explore',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'temple ruins',
    # 'terrain': [''],
    # 'corner': '',
    'ruin': True,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_six = {
    'index': 6,
    'type': 'explore',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'outpost ruins',
    # 'terrain': [''],
    # 'corner': '',
    'ruin': True,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}
card_seven = {
    'index': 7,
    'type': 'explore',
    'set': 'base',
    'shape': [4, 5],
    'coin': [1, 0],
    # 'rotation': '',
    'name': 'great river',
    'terrain': ['water'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 1,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_eight = {
    'index': 8,
    'type': 'explore',
    'set': 'base',
    'shape': [6, 7],
    'coin': [1, 0],
    # 'rotation': '',
    'name': 'farmland',
    'terrain': ['farm'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 1,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_nine = {
    'index': 9,
    'type': 'explore',
    'set': 'base',
    'shape': [8, 9],
    'coin': [1, 0],
    # 'rotation': '',
    'name': 'hamlet',
    'terrain': ['village'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 1,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_ten = {
    'index': 10,
    'type': 'explore',
    'set': 'base',
    'shape': [10, 11],
    'coin': [1, 0],
    # 'rotation': '',
    'name': 'forgotten forest',
    'terrain': ['forest'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 1,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_eleven = {
    'index': 11,
    'type': 'explore',
    'set': 'base',
    'shape': [12],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'hinterland stream',
    'terrain': ['farm', 'water'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 2,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twelve = {
    'index': 12,
    'type': 'explore',
    'set': 'base',
    'shape': [2],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'homestead',
    'terrain': ['village', 'farm'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 2,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_thirteen = {
    'index': 13,
    'type': 'explore',
    'set': 'base',
    'shape': [13],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'orchard',
    'terrain': ['forest', 'farm'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 2,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_fourteen = {
    'index': 14,
    'type': 'explore',
    'set': 'base',
    'shape': [14],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'treetop village',
    'terrain': ['forest', 'village'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 2,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_fifteen = {
    'index': 15,
    'type': 'explore',
    'set': 'base',
    'shape': [15],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'marshlands',
    'terrain': ['forest', 'water'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 2,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_sixteen = {
    'index': 16,
    'type': 'explore',
    'set': 'base',
    'shape': [16],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'fishing village',
    'terrain': ['village', 'water'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 2,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_seventeen = {
    'index': 17,
    'type': 'explore',
    'set': 'base',
    'shape': [17],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'riftlands',
    'terrain': ['forest', 'village', 'farm', 'water', 'monster'],
    # 'corner': '',
    # 'ruin': False,
    'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_eighteen = {
    'index': 18,
    'type': 'season',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'spring',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    'time_threshold': 8,
    'season_edicts': ['a', 'b'],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_nineteen = {
    'index': 19,
    'type': 'season',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'summer',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    'time_threshold': 8,
    'season_edicts': ['b', 'c'],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty = {
    'index': 20,
    'type': 'season',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'fall',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    'time_threshold': 7,
    'season_edicts': ['c', 'd'],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty_one = {
    'index': 21,
    'type': 'season',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'winter',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    'time_threshold': 6,
    'season_edicts': ['d', 'a'],
    # 'edict_letter': '',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty_two = {
    'index': 22,
    'type': 'edict',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'edict a',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'a',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty_three = {
    'index': 23,
    'type': 'edict',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'edict b',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'b',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty_four = {
    'index': 24,
    'type': 'edict',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'edict c',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'c',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty_five = {
    'index': 25,
    'type': 'edict',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'edict d',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'd',
    # 'edict_description': '',
    # 'edict_score_value': ''
}

card_twenty_six = {
    'index': 26,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'sentinel wood',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'a',
    'edict_description': 'Earn one reputation star for each forest space adjacent to the edge of the map.',
    'edict_score_value': 25
}

card_twenty_seven = {
    'index': 27,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'greenbough',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'a',
    'edict_description': 'Earn one reputation star for each row and column with at least one forest space. The same forest space may be scored in a row and a column.',
    'edict_score_value': 22
}

card_twenty_eight = {
    'index': 28,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'treetower',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'a',
    'edict_description': 'Earn one reputation star for each forest space surrounded on all four sides by filled spaces or the edge of the map.',
    'edict_score_value': 17
}

card_twenty_nine = {
    'index': 29,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'stoneside forest',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'a',
    'edict_description': 'Earn three reputation stars for each mountain space connected to another mountain space by a cluster of forest spaces.',
    'edict_score_value': 18
}

card_thirty = {
    'index': 30,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'canal lake',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'b',
    'edict_description': 'Earn one reputation star for each water space adjacent to at least one farm space. Earn one reputation star for each farm space adjacent to at least one water space.',
    'edict_score_value': 24
}

card_thirty_one = {
    'index': 31,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'mages valley',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'b',
    'edict_description': 'Earn two reputation stars for each water space adjacent to a mountain space. Earn one reputation star for each farm space adjacent to a mountain space.',
    'edict_score_value': 22
}

card_thirty_two = {
    'index': 32,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'the golden granary',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'b',
    'edict_description': 'Earn two reputation stars for each water space adjacent to a ruins space. Earn three reputation stars for each farm space on a ruins space.',
    'edict_score_value': 20
}

card_thirty_three = {
    'index': 33,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'shoreside expanse',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'b',
    'edict_description': 'Earn three reputation stars for each cluster of farm spaces not adjacent to a water space or the edge of the map. Earn three reputation stars for each cluster of water spaces not adjacent to a farm space or the edge of the map.',
    'edict_score_value': 27
}

card_thirty_four = {
    'index': 34,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'wildholds',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'c',
    'edict_description': 'Earn eight reputation stars for each cluster of six or more village spaces.',
    'edict_score_value': 16
}

card_thirty_five = {
    'index': 35,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'great city',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'c',
    'edict_description': 'Earn one reputation star for each village space in the largest cluster of village spaces that is not adjacent to a mountain space.',
    'edict_score_value': 16
}

card_thirty_six = {
    'index': 36,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'greengold plains',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'c',
    'edict_description': 'Earn three reputation stars for each cluster of village spaces that is adjacent to three or more different terrain types.',
    'edict_score_value': 21
}

card_thirty_seven = {
    'index': 37,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'shieldgate',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'c',
    'edict_description': 'Earn two reputation stars for each village space in the second largest cluster of village spaces.',
    'edict_score_value': 20
}

card_thirty_eight = {
    'index': 38,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'borderlands',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'd',
    'edict_description': 'Earn six reputation stars for each complete row or complete column of filled spaces.',
    'edict_score_value': 24
}

card_thirty_nine = {
    'index': 39,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'lost barony',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'd',
    'edict_description': 'Earn three reputation stars for each space along one edge of the largest square of filled spaces.',
    'edict_score_value': 24
}

card_forty = {
    'index': 40,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'the broken road',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'd',
    'edict_description': 'Earn three reputation stars for each complete diagonal line of filled spaces that touches the left and bottom edges of the map.',
    'edict_score_value': 24
}

card_forty_one = {
    'index': 41,
    'type': 'scoring',
    'set': 'base',
    # 'shape': [''],
    # 'coin': [False],
    # 'rotation': '',
    'name': 'the cauldrons',
    # 'terrain': [''],
    # 'corner': '',
    # 'ruin': False,
    # 'time_value': 0,
    # 'time_threshold': '',
    # 'season_edicts': [''],
    'edict_letter': 'd',
    'edict_description': 'Earn one reputation star for each empty space surrounded on all four sdies by filled spaces or the edge of the map.',
    'edict_score_value': 20
}


card_deck = [
    card_one,
    card_two,
    card_three,
    card_four,
    card_five,
    card_six,
    card_seven,
    card_eight,
    card_nine,
    card_ten,
    card_eleven,
    card_twelve,
    card_thirteen,
    card_fourteen,
    card_fifteen,
    card_sixteen,
    card_seventeen,
    card_eighteen,
    card_nineteen,
    card_twenty,
    card_twenty_one,
    card_twenty_two,
    card_twenty_three,
    card_twenty_four,
    card_twenty_five,
    card_twenty_six,
    card_twenty_seven,
    card_twenty_eight,
    card_twenty_nine,
    card_thirty,
    card_thirty_one,
    card_thirty_two,
    card_thirty_three,
    card_thirty_four,
    card_thirty_five,
    card_thirty_six,
    card_thirty_seven,
    card_thirty_eight,
    card_thirty_nine,
    card_forty,
    card_forty_one
]

# print(deck[1].get('time_threshold', 'empty'))
# print(deck[0].get('shape', 0)[0])

# temp = (card_deck[1].get('shape', 0)[0])
# temp2 = temp + 1

# print(temp)
# print(temp2)

print(textwrap.wrap(card_thirty_one.get('edict_description')))