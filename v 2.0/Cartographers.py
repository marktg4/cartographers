# My attempt at recreating Cartographers

# Moved deck to it's own file, Card_Deck.py
# Created a Shapes.py file to store all shapes and how they fit on a 4x4 grid
# Created a Map_Sheet.py file to store the 2 starting maps. Note may need a new map variable for current map config, and reference base map for ruin spaces?

from Card_Deck import card_deck
from Shapes import shapes
from Map_Sheet import maps
import PySimpleGUI as sg
import random
import textwrap

# Initialize global vairables
MAP_SIZE = 500
BOX_SIZE = MAP_SIZE / 11
GRAPH_COLORS = {
    0: 'bisque',
    1: 'forest green',
    2: 'maroon',
    3: 'goldenrod',
    4: 'RoyalBlue1',
    5: 'blue violet',
    6: 'saddle brown',
    7: 'dim gray',
}
SEASONS = {
    0: 'spring',
    1: 'summer',
    2: 'fall',
    3: 'winter',
}
TERRAINS ={
    0: 'forest',
    1: 'village',
    2: 'farm',
    3: 'water',
    4: 'monster',
}

# Build card functions here

# Find a card index value from a provided key value
def card_lookup_index_from_value(key_value):
    index = -1
    for card in card_deck:
        index += 1
        for key, value in card.items():
            if str(value).lower() == key_value.lower():
                print(f"Match at key {key} value {value}. Returning {index}")
                # update_log(f"\nMatch at key {key} value {value}. Returning {index}")
                return index
    print(F'No result found for card lookup with {key_value} as the parameter')
    # update_log(F'\nNo result found for card lookup with {key_value} as the parameter')
    return 0

# Increment the season counter, as well as update each season variable
def advance_season(counter, season, card, edicts, thresh, time, ambush, explore, used):
    if time >= thresh:
        if counter < len(SEASONS)-1:
            counter += 1
            print(F"Season counter updated to: {counter}")
            # update_log(F"\nSeason counter updated to: {counter}")

            # Update season and get card values in return
            temp = update_season(counter, season, card, edicts, thresh, time)
            counter = temp[0]
            season = temp[1]
            card = temp[2]
            edicts = temp[3]
            thresh = temp[4]
            time = temp[5]

            # Update graphics here
            window['-CURRENT_SEASON-'].update(season.title())
            window['-CURRENT_EDICTS-'].update(f"Edicts: {edicts[0].title()} {edicts[1].title()}")
            window['-TIME_THRESHOLD-'].update(f"Time Threshhold: {thresh}")
            window['-CURRENT_TIME-'].update(f"Current Time: {time}")
            window['-CARD_NAME-'].update("Card Name: Click 'Draw Card' to begin!")
            window['-CARD_ROTATION-'].update("Card Rotation: ")
            window['-CARD_CORNER-'].update("Card Corner: ")
            window['-COIN_VALUE_ONE-'].update("Coin Value: 0")
            window['-COIN_VALUE_TWO-'].update("Coin Value: 0")

            # Set up decks for next season
            print('Removing used Ambush cards..')
            # update_log('\nRemoving used Ambush cards..')
            used = remove_used_ambush(used)
            print('Putting used cards back into the Explore Deck..')
            # update_log('\nPutting used cards back into the Explore Deck..')
            explore = explore + used
            print('Emptying Used Deck..')
            # update_log('\nEmptying Used Deck..')
            used = []
            print('Adding new Ambush card..')
            # update_log('\nAdding new Ambush card..')
            temp2 = add_ambush(ambush, explore)
            ambush = temp2[0]
            explore = temp2[1]
            print('Shuffling Explore Deck..')
            # update_log('\nShuffling Explore Deck..')
            explore = shuffle_deck(explore)

            # Clear terrain and shape grids
            clear_terrain_grid(ct)
            clear_shape_grids(cs1, cs2)

            return counter, season, card, edicts, thresh, time, ambush, explore, used
        else:
            print(F"Season already at max value: {counter}")
            # update_log(F"\nSeason already at max value: {counter}")
            print('Add up your score and update your total score!')
            # update_log('\nAdd up your score and update your total score!')
            return counter, season, card, edicts, thresh, time, ambush, explore, used
    else:
        print('Unable to advance season, time value has not reached time threshold')
        # update_log('\nUnable to advance season, time value has not reached time threshold')
        return counter, season, card, edicts, thresh, time, ambush, explore, used

# Update season with provided counter value, update and return all season variables   
def update_season(counter, season, card, edicts, thresh, time):
    if season == SEASONS[counter]:
        print(F"Current season is same as provided counter value: {counter}")
        # update_log(F"\nCurrent season is same as provided counter value: {counter}")
        return counter, season, card, edicts, thresh, time
    else:
        season = SEASONS[counter]
        card = card_lookup_index_from_value(season)
        edicts = card_deck[card].get('season_edicts')
        thresh = card_deck[card].get('time_threshold')
        time = 0
        print(F"Season updated to {season}")
        # update_log(F"\nSeason updated to {season}")
        print(F"Season edicts updated to {edicts}")
        # update_log(F"\nSeason edicts updated to {edicts}")
        print(F"Season time threshold updated to {thresh}")
        # update_log(F"\nSeason time threshold updated to {thresh}")
        print(F"Season current time updated to {time}")
        # update_log(F"\nSeason current time updated to {time}")
        return counter, season, card, edicts, thresh, time

# Shuffle given deck
def shuffle_deck(deck):
    if len(deck) > 1:
        random.shuffle(deck)
        print(F"Deck shuffled!")
        # update_log(F"\nDeck shuffled!")
        return deck
    else:
        print('Deck contains only one item or is empty')
        # update_log('\nDeck contains only one item or is empty')
        return deck
    
# Add ambush card to explore deck
def add_ambush(ambush, explore):
    if len(ambush) > 0:
        temp = ambush.pop()
        print(F"Removed a card from the Ambush Deck")
        # update_log(F"\nRemoved a card from the Ambush Deck")
        explore.append(temp)
        print(F"Added the card to the Explore Deck")
        # update_log(F"\nAdded the card to the Explore Deck")
        return ambush, explore
    else:
        print('Ambush deck is empty')
        # update_log('\nAmbush deck is empty')
        return ambush, explore

# Removed used ambush cards, multiple or none
def remove_used_ambush(used):
    a = 0
    index = 0
    for card in used:
        if card_deck[card]['type'] == 'ambush':
            used.pop(index)
            a += 1
            print(F"Removed {card} from Used Deck")
            # update_log(F"\nRemoved {card} from Used Deck")
        index += 1
    if a == 0:
        print('No cards removed from Used Deck')
        # update_log('\nNo cards removed from Used Deck')
    return used

# Draw a card from the explore deck, update current card and used decks
def draw_card (explore, current, used):
    #Verify explore deck has content
    if len(explore) > 0:
        current = explore.pop()
        print(F"Drew card {current}")
        # update_log(F"\nDrew card {current}")
        used.append(current)
        print(F"Card {current} added to Used Deck")
        # update_log(F"\vCard {current} added to Used Deck")
        return explore, current, used
    else:
        print('Explore deck is empty')
        # update_log('\nExplore deck is empty')
        return explore, current, used

# Draw the available terrain types for given card
def draw_card_terrain_grid(card, ct):
    clear_terrain_grid(ct)
    card_terrains = []
    for num in range(5):
        try:
            card_terrains.append(card_deck[card].get('terrain', ['', '', '', '', ''])[num])
        except:
            card_terrains.append('')
    for terrain in card_terrains:
        if terrain != '':
            print(F"Enabling terrain {terrain} on terrain grid")
            # update_log(F"\nEnabling terrain {terrain} on terrain grid")
            for num2 in range(5):
                if TERRAINS[num2] == terrain:
                    ct.draw_rectangle((num2*BOX_SIZE, 0), ((num2+1)*BOX_SIZE, BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[num2+1])
    
# Clear terrain grid before next card terrain is displayed
def clear_terrain_grid(ct):
    print("Clearing terrain grid")
    # update_log("\nClearing terrain grid")
    for row in range(5):
        ct.draw_rectangle((row*BOX_SIZE, 0), ((row+1)*BOX_SIZE, BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[7])

# Clear shape grids before next card shapes are displayed
def clear_shape_grids(cs1, cs2):
    print("Clearing shape grids")
    # update_log("\nClearing shape grids")
    for row in range(4):
        for col in range(4):
            cs1.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[7])
            cs2.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[7])

# Draw the available shapes for the given card
def draw_card_shapes(card, cs1, cs2):
    clear_shape_grids(cs1, cs2)
    card_shapes = []
    for num in range(2):
        try:
            card_shapes.append(card_deck[card].get('shape', ['', ''])[num])
        except:
            card_shapes.append('')
    if card_shapes[0] != '':
        print(F"Drawing {card_shapes[0]} on first shape grid")
        # update_log(F"\nDrawing {card_shapes[0]} on first shape grid")
        box_number = 0
        for row in range(4):
            for col in range(4):
                if shapes[card_shapes[0]][box_number] == 1:
                    cs1.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[0])
                else:
                    cs1.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[7])
                box_number += 1
    # Being a little redundant since only 2 shape grids.. Could update this later to a function possibly
    if card_shapes[1] != '':
        print(F"Drawing {card_shapes[1]} on second shape grid")
        # update_log(F"\nDrawing {card_shapes[1]} on second shape grid")
        box_number = 0
        for row in range(4):
            for col in range(4):
                if shapes[card_shapes[1]][box_number] == 1:
                    cs2.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[0])
                else:
                    cs2.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[7])
                box_number += 1

# Function to draw map grid
def draw_map_grid(g):
    box_number = 0
    for row in range(11):
        for col in range(11):
            if current_map[box_number] != 8:
                g.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[current_map[box_number]])
            else:
                g.draw_rectangle((col * BOX_SIZE, row * BOX_SIZE), (col * BOX_SIZE + BOX_SIZE, row * BOX_SIZE + BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[0])
                g.draw_text('R'.format(text_color=GRAPH_COLORS[7]), (col * BOX_SIZE + BOX_SIZE/2, row * BOX_SIZE + BOX_SIZE/2), font='Helvetica 20')
            box_number += 1

# Update log string and display it in the window
def update_log(text):
    global log_string, window
    log_string += text
    window['-LOG-'].update(log_string)


# Move all initilization to a function, so it can be called again
def initiliaze_values():
    # Initialize global variables
    global coins, total_score,  season_counter, current_season, current_season_card, current_season_edicts, time_threshold, current_time, shape1_coin, shape2_coin
    global ambush_deck, explore_deck, season_deck, edict_letter_deck, edicta_deck, edictb_deck, edictc_deck, edictd_deck, used_deck
    global current_card, current_card_name, current_card_rotation, current_card_corner, current_card_coin1, current_card_coin2
    global edicta, edictb, edictc, edictd, current_map, temp_map, log_string
    
    # Initialize log string
    log_string = 'Welcome to my digital recreation of the Cartographers board game! This is a delightful game, all credit to Jordy Adan and Thunderworks Games. To begin, click Draw Card'


    # Initialize which map to use
    temp_map = random.randint(0,1)
    current_map = maps[temp_map]
    print(F"Map selected for this game: {temp_map}")
    # update_log(F"\nMap selected for this game: {temp_map}")
    
    # Initialize coin value
    coins = 0

    # Initialize player score
    total_score = 0

    # Initialize current season
    season_counter = 0
    current_season = 'spring'
    current_season_card = 18
    current_season_edicts = ['a', 'b']

    # Initialize current time and time threshold
    time_threshold = card_deck[current_season_card].get('time_threshold')
    current_time = 0

    # Initialize shape coin values
    shape1_coin = 0
    shape2_coin = 0

    # Initialize the card decks (oh boy) - want to go back later and make these more robust
    # Such as searching the card list for the setup rather than hard coded values
    ambush_deck = [0, 1, 2, 3]
    print('Shuffling Ambush Deck..')
    # update_log('\nShuffling Ambush Deck..')
    shuffle_deck(ambush_deck)
    explore_deck = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print('Adding ambush to Explorer Deck..')
    # update_log('\nAdding ambush to Explorer Deck..')
    add = add_ambush(ambush_deck, explore_deck)
    ambush_deck = add[0]
    explore_deck = add[1]
    print('Shuffling Explore Deck..')
    # update_log('\nShuffling Explore Deck..')
    shuffle_deck(explore_deck)
    season_deck = [17, 18, 19, 20]
    edict_letter_deck = [21, 22, 23, 24]
    edicta_deck = [25, 26, 27, 28]
    print('Shuffling Edict A Deck..')
    # update_log('\nShuffling Edict A Deck..')
    shuffle_deck(edicta_deck)
    edictb_deck = [29, 30, 31, 32]
    print('Shuffling Edict B Deck..')
    # update_log('\nShuffling Edict B Deck..')
    shuffle_deck(edictb_deck)
    edictc_deck = [33, 34, 35, 36]
    print('Shuffling Edict C Deck..')
    # update_log('\nShuffling Edict C Deck..')
    shuffle_deck(edictc_deck)
    edictd_deck = [37, 38, 39, 40]
    print('Shuffling Edict D Deck..')
    # update_log('\nShuffling Edict D Deck..')
    shuffle_deck(edictd_deck)
    used_deck = []
    print('Used deck is empty')
    # update_log('\nUsed deck is empty')

    # Initialize current card values
    current_card = 0
    current_card_name = 'Goblin Attack'
    current_card_rotation = 'cc'
    current_card_corner = 'br'
    current_card_coin1 = 0
    current_card_coin2 = 0
    # current_card_shape1 = 0
    # current_card_shape2 = -1

    # Initialize edict cards
    edicta = edicta_deck[0]
    edictb = edictb_deck[0]
    edictc = edictc_deck[0]
    edictd = edictd_deck[0]


initiliaze_values()

# Create a layout
# Want a frame for each section of the layout, not sure if they need to be within columns or not

# Make a frame layout for the frames that have multiple things going on
layout_scoring = [[sg.Frame('Spring', [[sg.Input(s=5, key='-SCORE_SPRING-')]]),
                   sg.Frame('Summer', [[sg.Input(s=5, key='-SCORE_SUMMER-')]]),
                   sg.Frame('Fall', [[sg.Input(s=5, key='-SCORE_FALL-')]]),
                   sg.Frame('Winter', [[sg.Input(s=5, key='-SCORE_WINTER-')]]),
                   sg.Frame('Total', [[sg.Text(total_score, key='-SCORE_TOTAL-')]]),
                   sg.Button('Update', key='-SCORE_UPDATE-'),
                   ]]

layout_coins = [[sg.Text(coins, key='-COIN_VALUE-'), sg.Button('-', key='-COIN_DEC-'), sg.Button('+', key='-COIN_INC-')]]

layout_season = [[sg.Text(current_season.title(), key='-CURRENT_SEASON-'),],
                 [sg.Text(f"Edicts: {current_season_edicts[0].title()} {current_season_edicts[1].title()}", key='-CURRENT_EDICTS-')],
                 [sg.Text(f"Time Threshhold: {time_threshold}", key='-TIME_THRESHOLD-')],
                 [sg.Text(f"Current Time: {current_time}", key='-CURRENT_TIME-')],
                 [sg.Button('Advance To Next Season', key='-ADVANCE_SEASON-')]
                ]

layout_card_shapes = [[sg.Graph((4*BOX_SIZE+1, 4*BOX_SIZE+1), (0, 4*BOX_SIZE+1), (4*BOX_SIZE+1, 0),key='-SHAPES_ONE-', enable_events=True, drag_submits=False),
                       sg.VSep(),
                       sg.Graph((4*BOX_SIZE+1, 4*BOX_SIZE+1), (0, 4*BOX_SIZE+1), (4*BOX_SIZE+1, 0),key='-SHAPES_TWO-', enable_events=True, drag_submits=False)],
                      [sg.Text(F'Coin Value: {shape1_coin}', key='-COIN_VALUE_ONE-'),
                    #    sg.VSep(),
                       sg.Push(), sg.Text(F'Coin Value: {shape2_coin}', key='-COIN_VALUE_TWO-'),]
                     ]

layout_explore_deck = [[sg.Text("Card Name: Click 'Draw Card' to begin!", key='-CARD_NAME-'),
                        sg.Text("Card Rotation: ", key='-CARD_ROTATION-'),
                        sg.Text("Card Corner: ", key='-CARD_CORNER-')],
                       [sg.Frame('Card Terrain Types', [[sg.Graph((BOX_SIZE*5+1, BOX_SIZE+1), (0, BOX_SIZE+1), (BOX_SIZE*5+1, 0),
                                                     key='-CARD_TERRAIN-', enable_events=True, drag_submits=False)]])],
                       [sg.Frame("Card Shape(s)", layout_card_shapes)],
                       [sg.Button('Draw Card', key='-DRAW_CARD-')]
                       ]


# Make each frame with given layout
frame_map = sg.Frame('Map', [[sg.Push(), sg.Graph((MAP_SIZE+1, MAP_SIZE+1), (0, MAP_SIZE+1), (MAP_SIZE+1, 0),
                                                  key='-GRAPH-', enable_events=True, drag_submits=False)]],)
frame_scoring = sg.Frame('Scoring', layout_scoring)
frame_explore_deck = sg.Frame('Explore Deck', layout_explore_deck)
frame_coins = sg.Frame('Coins', layout_coins)
frame_edicta = sg.Column([[sg.Frame('Edict A', [[sg.Text(card_deck[edicta]['name'].title(), key='-EDICTA_NAME-')],
                                                [sg.Text(card_deck[edicta]['edict_description'], key='-EDICTA_DESC-')]])]])
frame_edictb = sg.Column([[sg.Frame('Edict B', [[sg.Text(card_deck[edictb]['name'].title(), key='-EDICTB_NAME-')],
                                                [sg.Text(card_deck[edictb]['edict_description'], key='-EDICTB_DESC-')]])]])
frame_edictc = sg.Column([[sg.Frame('Edict C', [[sg.Text(card_deck[edictc]['name'].title(), key='-EDICTC_NAME-')],
                                                [sg.Text(card_deck[edictc]['edict_description'], key='-EDICTC_DESC-')]])]])
frame_edictd = sg.Column([[sg.Frame('Edict D', [[sg.Text(card_deck[edictd]['name'].title(), key='-EDICTD_NAME-')],
                                                [sg.Text(card_deck[edictd]['edict_description'], key='-EDICTD_DESC-')]])]])
frame_season = sg.Frame('Current Season', layout_season)
frame_log = sg.Frame('Game Log', [[sg.Multiline(key='-LOG-', size=(35, 35), disabled=True, autoscroll=True)]])
frame_terrain = sg.Frame('Terrain Types', [[sg.Graph((BOX_SIZE*8+1, BOX_SIZE+1), (0, BOX_SIZE+1), (BOX_SIZE*8+1, 0),
                                                     key='-TERRAIN-', enable_events=True, drag_submits=False)]])
frame_current_terrain = sg.Frame('Current Terrain', [[sg.Graph((BOX_SIZE+1, BOX_SIZE+1), (0, BOX_SIZE+1), (BOX_SIZE+1, 0),
                                                               key='-CURRENT-', enable_events=True, drag_submits=False)]])

# Make the columns for the gui organization. Each column holds a vertical section of the gui.
# elements in the same array separated by commas are next to each other horizontally.
# col1 = sg.Column([[frame_log]]) <---- since logs are not yet fully functional, and since window is too large, remove for now
col2 = sg.Column([[frame_terrain, frame_current_terrain], [frame_map], [frame_coins, frame_scoring]])
col3 = sg.Column(
    [
        [frame_explore_deck, frame_season],
        [sg.HSep()],
        [frame_edicta],
        [frame_edictb],
        [frame_edictc],
        [frame_edictd],
    ]
)

layout = [
    [sg.Menu([['File', ['Restart', 'Exit']]],  key='-MENUBAR-', p=0)],
    # [col1, sg.VSep(), col2, sg.VSep(), col3]
    [col2, sg.VSep(), col3] # <--- Remove this when logs begin to work and can resize window
    ]

# Create a window
window = sg.Window('Cartographers', layout, resizable=True, finalize=True)

# Draw initial map grid
g = window['-GRAPH-']
draw_map_grid(g)


# Draw terrain grid
t = window['-TERRAIN-']
for row in range(8):
    t.draw_rectangle((row*BOX_SIZE, 0), ((row+1)*BOX_SIZE, BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[row])

# Draw card terrain grid
ct = window['-CARD_TERRAIN-']
clear_terrain_grid(ct)

# Draw current terrain tile
c = window['-CURRENT-']
c.draw_rectangle((0, 0), (BOX_SIZE, BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[0])

# Draw card shape grids
cs1 = window['-SHAPES_ONE-']
cs2 = window['-SHAPES_TWO-']
clear_shape_grids(cs1, cs2)

# Initialize the selected color variable
selected_color = 0

# Update logs
# window['-LOG-'].update(log_string)



# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    # Reset game when user selects Restart from File menu
    if event == 'Restart':
        print('Restarting game. Resetting initial values and clearing grids..')
        # update_log('\nRestarting game. Resetting initial values and clearing grids..')
        initiliaze_values()
        window['-COIN_VALUE-'].update(coins)
        window['-SCORE_TOTAL-'].update(total_score)
        window['-CURRENT_TIME-'].update(f"Current Time: {current_time}")
        window['-CARD_NAME-'].update(F"Card Name: Click 'Draw Card' to begin!")
        window['-CARD_ROTATION-'].update(F"Card Rotation: ")
        window['-CARD_CORNER-'].update(F"Card Corner: ")
        window['-COIN_VALUE_ONE-'].update(F"Coin Value: 0")
        window['-COIN_VALUE_TWO-'].update(F"Coin Value: 0")
        window['-CURRENT_SEASON-'].update(current_season.title())
        window['-CURRENT_EDICTS-'].update(f"Edicts: {current_season_edicts[0].title()} {current_season_edicts[1].title()}")
        window['-TIME_THRESHOLD-'].update(f"Time Threshhold: {time_threshold}")
        window['-CURRENT_TIME-'].update(f"Current Time: {current_time}")
        window['-SCORE_SPRING-'].update('')
        window['-SCORE_SUMMER-'].update('')
        window['-SCORE_FALL-'].update('')
        window['-SCORE_WINTER-'].update('')
        window['-EDICTA_NAME-'].update(F"{card_deck[edicta]['name'].title()}")
        window['-EDICTA_DESC-'].update(F"{card_deck[edicta]['edict_description']}")
        window['-EDICTB_NAME-'].update(F"{card_deck[edictb]['name'].title()}")
        window['-EDICTB_DESC-'].update(F"{card_deck[edictb]['edict_description']}")
        window['-EDICTC_NAME-'].update(F"{card_deck[edictc]['name'].title()}")
        window['-EDICTC_DESC-'].update(F"{card_deck[edictc]['edict_description']}")
        window['-EDICTD_NAME-'].update(F"{card_deck[edictd]['name'].title()}")
        window['-EDICTD_DESC-'].update(F"{card_deck[edictd]['edict_description']}")
        # Need to clear game log here as well whenever that gets working
        clear_terrain_grid(ct)
        clear_shape_grids(cs1, cs2)
        draw_map_grid(g)

# frame_edicta = sg.Column([[sg.Frame('Edict A', [[sg.Text(card_deck[edicta]['name'].title())], [sg.Text(card_deck[edicta]['edict_description'])]])]])
# frame_edictb = sg.Column([[sg.Frame('Edict B', [[sg.Text(card_deck[edictb]['name'].title())], [sg.Text(card_deck[edictb]['edict_description'])]])]])
# frame_edictc = sg.Column([[sg.Frame('Edict C', [[sg.Text(card_deck[edictc]['name'].title())], [sg.Text(card_deck[edictc]['edict_description'])]])]])
# frame_edictd = sg.Column([[sg.Frame('Edict D', [[sg.Text(card_deck[edictd]['name'].title())], [sg.Text(card_deck[edictd]['edict_description'])]])]])


    mouse = values['-GRAPH-']
    # If user clicks on the map graph, update box to selected color, check if ruin space, then re-add the ruin text
    if event == '-GRAPH-':
        if mouse == (None, None):
            continue
        box_x = int(mouse[0]//BOX_SIZE)
        box_y = int(mouse[1]//BOX_SIZE)
        print(F"Map updated. Square ({box_x+1}, {box_y+1}) updated to terrain value: {selected_color}")
        # update_log(F"\nMap updated. Square ({box_x+1}, {box_y+1}) updated to terrain value: {selected_color}")
        g.draw_rectangle((box_x * BOX_SIZE, box_y * BOX_SIZE), (box_x * BOX_SIZE + BOX_SIZE, box_y * BOX_SIZE + BOX_SIZE),
                         line_color='black', fill_color=GRAPH_COLORS[selected_color])
        array_convert = 11*box_y + box_x
        if current_map[array_convert] == 8:
            print('Redrawing ruin R on suare')
            # update_log('\nRedrawing ruin R on suare')
            g.draw_text('R'.format(text_color=GRAPH_COLORS[7]), (box_x * BOX_SIZE + BOX_SIZE/2, box_y * BOX_SIZE + BOX_SIZE/2), font='Helvetica 20')

    mouse = values['-TERRAIN-']
    # If user clicks on the terrain graph, update selected color to what was chosen
    if event == '-TERRAIN-':
        if mouse == (None, None):
            continue
        selected_color = int(mouse[0]//BOX_SIZE)
        print(F"Selected terrain value changed. Current terrain value: {selected_color}")
        # update_log(F"\nSelected terrain value changed. Current terrain value: {selected_color}")
        c.draw_rectangle((0, 0), (BOX_SIZE, BOX_SIZE), line_color='black', fill_color=GRAPH_COLORS[selected_color])

    # If user clicks on the - button, decrement their coin counter
    if event == '-COIN_DEC-':
        coins -= 1
        window['-COIN_VALUE-'].update(coins)
        print(F"Decrementing coin counter. New value: {coins}")
        # update_log(F"\nDecrementing coin counter. New value: {coins}")
    
    # Is user clicks on the + button, increment their coin counter
    if event == '-COIN_INC-':
        coins += 1
        window['-COIN_VALUE-'].update(coins)
        print(F"Incrementing coin counter. New value: {coins}")
        # update_log(F"\nIncrementing coin counter. New value: {coins}")

    # If user clicks the score Update button, sum their season scores and display it under Total
    if event == '-SCORE_UPDATE-':
        try:
            spring_score = int(values['-SCORE_SPRING-'])
        except:
            spring_score = 0
        try:
            summer_score = int(values['-SCORE_SUMMER-'])
        except:
            summer_score = 0
        try:
            fall_score = int(values['-SCORE_FALL-'])
        except:
            fall_score = 0
        try:
            winter_score = int(values['-SCORE_WINTER-'])
        except:
            winter_score = 0
        total_score = spring_score + summer_score + fall_score + winter_score
        print(f"Score updated. New total: {total_score}")
        # update_log(F"\nScore updated. New total: {total_score}")
        window['-SCORE_TOTAL-'].update(total_score)
    
    # If user clicks Advance To Next Season, reset some display values and prepare decks for next season
    if event == '-ADVANCE_SEASON-':
        # Advance the season, reinitiate the graphics for current season cards, add an ambush card, and shuffle the explore deck
        temp = advance_season(season_counter, current_season, current_season_card, current_season_edicts,
                              time_threshold, current_time, ambush_deck, explore_deck, used_deck)
        season_counter = temp[0]
        current_season = temp[1]
        current_season_card = temp[2]
        current_season_edicts = temp[3]
        time_threshold = temp[4]
        current_time = temp[5]
        ambush_deck = temp[6]
        explore_deck = temp[7]
        used_deck = temp[8]

        # Moved the graphic update to the function itself
        # window['-CURRENT_SEASON-'].update(current_season.title())
        # window['-CURRENT_EDICTS-'].update(f"Edicts: {current_season_edicts[0].title()} {current_season_edicts[1].title()}")
        # window['-TIME_THRESHOLD-'].update(f"Time Threshhold: {time_threshold}")
        # window['-CURRENT_TIME-'].update(f"Current Time: {current_time}")

    # If the user clicks Draw Card, pop a card from the explore deck and update screen and respective decks
    if event == '-DRAW_CARD-':
        # Check if season is still active
        if current_time < time_threshold:
            # Draw a card from the deck, set current card, and add to used deck
            print('Drawing from the Explore Deck..')
            # update_log('\nDrawing from the Explore Deck..')
            draw = draw_card(explore_deck, current_card, used_deck)
            explore_deck = draw[0]
            current_card = draw[1]
            used_deck = draw[2]

            # Update values from current card
            current_time += card_deck[current_card].get('time_value', 0)
            current_card_name = card_deck[current_card]['name']
            current_card_rotation = card_deck[current_card].get('rotation', '')
            current_card_corner = card_deck[current_card].get('corner', '')
            current_card_coin1 = card_deck[current_card].get('coin', [0, 0])[0]
            current_card_coin2 = card_deck[current_card].get('coin', [0, 0])[1]
            # current_card_coin1 = card_deck[current_card].get('coin_one', 0)
            # current_card_coin2 = card_deck[current_card].get('coin_two', 0)

            # Update values on screen
            window['-CURRENT_TIME-'].update(f"Current Time: {current_time}")
            window['-CARD_NAME-'].update(F"Card Name: {current_card_name.title()}")
            window['-CARD_ROTATION-'].update(F"Card Rotation: {current_card_rotation.upper()}")
            window['-CARD_CORNER-'].update(F"Card Corner: {current_card_corner.upper()}")
            window['-COIN_VALUE_ONE-'].update(F"Coin Value: {current_card_coin1}")
            window['-COIN_VALUE_TWO-'].update(F"Coin Value: {current_card_coin2}")

            # Update current card graphs on screen
            print('Attempting to update terrain grid..')
            # update_log('\nAttempting to update terrain grid..')
            draw_card_terrain_grid(current_card, ct)
            print('Attempting to update shape grids..')
            # update_log('\nAttempting to update shape grids..')
            draw_card_shapes(current_card, cs1, cs2)
        else:
            # Season is over, do not draw a new card
            print('Season has reached the time threshold. Please add up your score and advance to the next season.')
            # update_log('\nSeason has reached the time threshold. Please add up your score and advance to the next season.')

window.close()
