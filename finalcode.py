#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

def create_kalaha_list(h,s): 
    
    """ Creates the Kalaha-list. """
    
    if h < 1 or s < 1:
        raise Exception("Unacceptable h or s has been given. Impossible Kalaha board.")
        
    else:
    
        kalaha_list = []
    
        kalaha_list.append(s)
    
        kalaha_list *= h
    
        kalaha_list.append(0)
    
        kalaha_list *= 2
    
        return kalaha_list


""" Codes that are used for modifying the Kalaha-board after a move."""


def first_round(kalaha_list, sowing_pits, chosen_house_index, distance):
    
    """ This algorithm adds seeds to the board in the first cycle of the board
    """
    
    last_pit_in_rotation_index = sowing_pits - 1
    
    if chosen_house_index == last_pit_in_rotation_index:
        
        return kalaha_list # ignore cases where additional seeds are not added
    
    if chosen_house_index < last_pit_in_rotation_index: 
        
        if distance >= last_pit_in_rotation_index: 
            
            for x in range((chosen_house_index + 1), sowing_pits):
                
                kalaha_list[x] += 1 # add seeds to all remaining pits
            
            return kalaha_list
        
        else: # if not all remaining pits will get another seed
            
            for x in range((chosen_house_index + 1), (distance + 1)): 
                
                kalaha_list[x] += 1 # add remaining seeds to pits
            
            return kalaha_list
    
    else: #to find cases where the chosen_pit happens to be the opponent's store
        raise ArithmeticError("The chosen pit is the opponent's store, cannot pick up from there.")
            

def inbetween_cycles(kalaha_list, cycles, sowing_pits):
    
    """ This algorithm adds seeds to the board for the cycles the player makes
    that are not the first or the last cycles.
    """
    
    if cycles > 1:
        
        inbetween_cycles = int(cycles - 1) 
        
        for x in range(sowing_pits):
            
            kalaha_list[x] += inbetween_cycles #1 seed per cycle added to pits
        
        return kalaha_list
    
    else: #ignoring cases where there is less than 1 cycle
        
        return kalaha_list

    
def last_round(kalaha_list, cycles, last_seed_index):
    
    """ This algorithm adds seeds to the board for the last round it makes. """
    
    if cycles >= 1:
        
        for x in range(last_seed_index+1): 
            
            kalaha_list[x] += 1 # add seeds to pits up until last seed
            
        return kalaha_list
    
    else:
        return kalaha_list
    

""" Codes for ???"""
    
    
def modifylistfornextplayer(kalaha_list):
    
    """ This algorithm flips the Kalaha board around so that it is from the
    perspective of the next player, by placing the last half of the list
    in front of the first half.
    """
    
    rotated_board = []
   
    l = len(kalaha_list)
   
    current_players_store_index = int(l / 2)
   
    for x in range(current_players_store_index,l): 
       
        rotated_board.append(kalaha_list[x])
   
    for x in range(current_players_store_index):
       
        rotated_board.append(kalaha_list[x])
   
    return rotated_board



""" Codes for determining who has won """

def findwinner(kalaha_list, player):
    
    """ This algorithm looks at a terminal position and determines the winner
    by how many points there are on each side of the board.
    """
    
    l = len(kalaha_list)
    
    current_players_store_index = int(l / 2) 
    
    p = player % 2  # 1 = player 1, 0 = player 2
    
    seeds_in_store_1 = 0 # seeds on current players side of board
    
    seeds_in_store_2 = 0 # seeds on opponent's current side of board
    
    for x in range(current_players_store_index): # collect current player's seeds
    
        seeds_in_pit_index_x = kalaha_list[x] 
        
        seeds_in_store_1 += seeds_in_pit_index_x
    
    for y in range(current_players_store_index,l): # collect opponent's seeds
    
        seeds_in_pit_index_x = kalaha_list[y]
        
        seeds_in_store_2 += seeds_in_pit_index_x
        
        
    if seeds_in_store_1 == seeds_in_store_2:
        return "draw"
    
    if p == 1: # if current player is p1
    
        if seeds_in_store_1 > seeds_in_store_2: 
            return "p1win"
        
        else: #
            return "p2win"
        
    if p == 0: # if current player is p2
        
        if seeds_in_store_1 > seeds_in_store_2: 
            return "p2win"
        
        else:
            return "p1win"
        
    

def whowon(board_side,player):
    
    """ This algorithm looks at which side of the board that has won by
    collecting enough seeds in their store, and from which player's perspective
    we are looking at the board. The algorithm the winning player.
    """
    
    p = player % 2  # current player: 1 = player 1, 0 = player 2
    
    if board_side == 1: # if current player has won
        
        if p == 1:
            return "p1win"
        else:
            return "p2win"
    
    else: # if opponent has won
        
        if p == 1:
            return "p2win"
        else:
            return "p1win"
            
        

def isthegameover(kalaha_list, player):
    
    """ This algorithm looks at the board configuration and whether a player 
    has won by then. It also returns which player has won, through additional
    functions whowon and findwinner.
    """
    
    required_number_of_seeds_to_win = int(sum(kalaha_list) / 2) 
    
    l = len(kalaha_list) 
    
    current_players_store_index = int(l / 2) - 1 
    
    opponents_store_index = l - 1
    
    seeds_in_current_players_store = kalaha_list[current_players_store_index]
    
    seeds_in_opponents_store = kalaha_list[opponents_store_index]
    
    if seeds_in_current_players_store > required_number_of_seeds_to_win:
    
        winning_player = whowon(1,player) 
        return winning_player
    
    if seeds_in_opponents_store > required_number_of_seeds_to_win: #the pit at index -1 will be opponent's store
    
        winning_player = whowon(0,player) #status identifies whether p1 or p2 won
        return winning_player
    
    else: # determining if we are at a terminal position
    
        non_empty_houses_1 = 0
        
        non_empty_houses_2 = 0
        
        for x in range(current_players_store_index):
            if kalaha_list[x] != 0: # checking whether house is empty or not
                non_empty_houses_1 += 1
                break
            
        for x in range((current_players_store_index + 1), opponents_store_index):
            if kalaha_list[x] != 0: # checking whether house is empty or not
                non_empty_houses_2 += 1
                break
        
        if non_empty_houses_1 and non_empty_houses_2 !=  0:
            return False # game can not be over if no row of houses is empty
        
        else: #if one row is empty, game has been terminated
            winning_player = findwinner(kalaha_list,player) 
            return winning_player
    
                    


def highestnumber(kalaha_list):
    
    """ This algorithm looks at a list with the game positions the player can
    move to (that results in it being the next players turn, without any
    confirmed win), and returns an ordered list, ranked from most collected
    seeds for the current player, to the least collected seeds.
    """
    #print(kalaha_list)
    ordered_list = []
    
    seed_numbers_list = []
    
    for game_position_item in kalaha_list:
        
        #print(game_position_item)
        
        board_list = game_position_item[2]
        seeds_in_store_number = board_list[-1] 
        
        if seeds_in_store_number not in seed_numbers_list:
            seed_numbers_list.append(seeds_in_store_number)
            
    seed_numbers_list.sort(reverse = True) 
    
    for number in seed_numbers_list:
        for item in kalaha_list:
            if number == item[2][-1]:
                ordered_list.append(item)
    
    return ordered_list


def available_options(kalaha_list):
    
    """ This algorithm looks at a current player's side of the board, and at
    which index in the list they have a non-empty house they can pick up seeds
    from. The algorithm returns a list with these indexes.
    """
    
    available_options_list = []
    
    current_players_store_index = int((len(kalaha_list) - 2)/2)
    
    for house in range(current_players_store_index):
        
        if kalaha_list[house] != 0: 
            
            available_options_list.append(house)
            
    return available_options_list


def listcheck(game_positions_list):
    
    """ This algorithm reformats the list with game positions so that the
    functions in solvegameposition and newmove can be applied to every list.
    """
    
    acceptable_index_zero_values = ["draw","p1win","p2win","go"]
    
    if game_positions_list[0] not in acceptable_index_zero_values:
        return game_positions_list
    else:
        return [game_positions_list]


def investigatenextnodes(game_positions_list,player):
    
    """ This function looks at the list with possible subpositions the player
    can move to, whose game-theoretic value has not been determined yet. It
    sends the position through different functions and ultimately determines
    its value. """
    
    #print(game_positions_list)
    
    draw_value_count = 0 # cases of subpositions with value "draw"
    
    p = player % 2 # current player: 1 = player 1, 0 = player 2
    
    ordered_opts_list = highestnumber(game_positions_list)
    
    game_positions_with_values = []
    
    for game_position_item in ordered_opts_list:
        
        current_player = game_position_item[1]
        kalaha_list = game_position_item[2]
        starting_house_index = game_position_item[3] # index of house ?
        
        result = solvegameposition(current_player,kalaha_list)
        result.append(starting_house_index)
        
        game_theoretic_value = result[0]
        
        if game_theoretic_value == "p1win" and p == 1: 
            return result 
        
        if game_theoretic_value == "p2win" and p == 0:
            return result
        
        if draw_value_count > 0: # ignore counting additional draw cases
            continue
        
        else:
            if game_theoretic_value == "draw":
                draw_value_count += 1
                game_positions_with_values.append(result)
            else:
                game_positions_with_values.append(result)
                    
    
    if draw_value_count > 0:
        for game_position_item in game_positions_with_values:
            if game_position_item[0] == "draw": # game_position_item[0] = value
                return game_position_item
    
    else:
        return game_positions_with_values[0] # return loss-valued position
    

def newmove(player, kalaha_board):
    
    """ This algorithm looks at the possible subpositions a player can move to
    from a given game position (gamestate). It collects all of the subpositions,
    and returns them. If a winning strategy is found, the win is returned.
    """

    houses_to_choose_from = available_options(kalaha_board) 
    
    next_opts = [] # list of subpositions positions the player can move to
    
    p = int(player % 2) # current player: 1 = player 1, 0 = player 2
    
    for house in houses_to_choose_from:
        
        kalaha_list = kalaha_board.copy()
        
        options = update_board(player, house,kalaha_list) 
        
        game_positions = listcheck(options) #reformats list for ease
        
        for item in game_positions:
            game_theoretic_value = item[0] 
            if game_theoretic_value  == "p1win" and p == 1:
                return item
            if game_theoretic_value == "p2win" and p == 0:
                return item
            else:
                next_opts.append(item)
                
    return next_opts

 

def newaction(kalaha_list,last_seed_index, player):
    
    """ This algorithm determines whose turn it is next, and whether the game
    has ended at this point.
    """
    
    game_status = isthegameover(kalaha_list,player) 
    
    if game_status == False: # game has not been terminated / won
        
        current_players_store_index = (len(kalaha_list) - 2) / 2 
        
        if last_seed_index == current_players_store_index: 
            
            next_move = newmove(player,kalaha_list)
            
            return next_move
        
        else:
            
            player += 1 # indicates that it is a new players turn
            
            next_players_kalaha_list = modifylistfornextplayer(kalaha_list) 
            
            return ["go", player, next_players_kalaha_list]
            
    else: # if the game has been terminated or won 
        
        return [game_status, player, kalaha_list]

  


def update_board(player, chosen_house, kalaha_list):
    
    """ This algorithm represents the action of picking up seeds and sowing
    them counter-clockwise around the board. It receives which house the
    current player has chosen to pick up seeds from, and the board's current
    configuration.

    The algorithm returns an updated board configuration, and determines
    whether another pick-up must be made.
    
    If the move is deemed completed, it sends the list with the index of the
    pit the last seed was placed in to another function to determine what shall
    be done next with the game.
    """
        
    l = len(kalaha_list)
    
    sowing_pits = l - 1 # number of pits players can sow into
    
    store_1 = (l - 2) / 2
    
    house_contents = kalaha_list[chosen_house] # seeds in chosen house
    
    d = house_contents + chosen_house  # distance_traveled
    
    last_seed_index = int(d % sowing_pits )
    
    rounds = int((d - last_seed_index) / sowing_pits)
    
    kalaha_list[chosen_house] = 0 # empties chosen house
    
    kalaha_list_new = first_round(kalaha_list, sowing_pits, chosen_house, d)
    
    kalaha_list_new = last_round(kalaha_list_new, rounds, last_seed_index)
    
    kalaha_list_new = inbetween_cycles(kalaha_list_new, rounds, sowing_pits)
    
    
    if kalaha_list_new[last_seed_index] != 1 and last_seed_index != store_1:
        
        return update_board(player,last_seed_index,kalaha_list_new)

    else: 
        
        return newaction(kalaha_list_new,last_seed_index,player)
        

def solvegameposition(player, kalaha_board):
    
    """ This algorithm looks at all the possible subpositions that can be
    moved to from the initial game position given (kalaha_board). It sends the
    list through algorithms that stop once it reaches a terminal position
    or a position in which it is the next player's turn. 
    
    It collects all the established game-theoretic values and then places the
    positions for the next player in a seperate list (next_opts). If the
    current player cannot force a win during their turn, the game-theoretic
    values of the game positions in next_opts are then analyzed.
    """
    
    p = int(player % 2) # current player: 1 = player 1, 0 = player 2
    
    subpositions_with_established_values = [] 
    
    unexplored_nodes = [] # subpositions with undetermined game values
    
    nodes_to_study = 0 # counter for nodes that can be further analyzed
    
    draw_subpositions_count = 0 # counter for subpositions with "draw" value
    
    houses_to_choose_from = available_options(kalaha_board) 
    
    for house_index in houses_to_choose_from:
        
        kalaha_list = kalaha_board.copy()
        
        options = update_board(player, house_index, kalaha_list) 
        
        subpositions = listcheck(options) # reformatting items for ease
        
        for subposition in subpositions:
            
            subposition.append(house_index)
            
            status = subposition[0]
            
            if status  == "p1win" and p == 1:
                return subposition
            
            if status == "p2win" and p == 0:
                return subposition
            
            if status == "go":
                unexplored_nodes.append(subposition)
                nodes_to_study += 1
                
            else:
                if draw_subpositions_count != 0:
                    continue
                
                if status == "draw":
                    draw_subpositions_count += 1
                    subpositions_with_established_values.append(subposition)
                    
                else:
                    subpositions_with_established_values.append(subposition)
                
    if nodes_to_study == 0: 
        
        if draw_subpositions_count != 0:
        
            for item in subpositions_with_established_values:

                if item[0] == "draw": # item[0] is the GTC value of the item
  
                    return item
                
        else:
            return subpositions_with_established_values[0]
    
    else:

        subposition_item = investigatenextnodes(unexplored_nodes, player)
        
        game_theoretic_value = subposition_item[0]
        
        if game_theoretic_value == "p1win" and p == 1:
            return subposition_item
        
        if game_theoretic_value == "p2win" and p == 0:
            return subposition_item
        
        if game_theoretic_value == "draw":
            return subposition_item
        
        else: # game_theoretic_value must be a loss for the current player
            if draw_subpositions_count != 0:
                
                for item in subpositions_with_established_values:
                    
                    if item[0] == "draw":
                        
                        return subposition_item
        
            else:
                
                return subposition_item
            
    
    
def startsolving():
    
    """ This algorithm sends the list to find its game-theoretic value,
    and then returns the value and says what house the player must choose
    to reach the game-theoretic value.
    """
    
    print("Which Kalaha(h,s) would you like to solve?")
    print("h = Number of houses on each side of the board.")
    print("s = Number of seeds on in each house at the start of the game.")
    print("")
    h_string = input("Type your desired h-value here: ")
    s_string = input("Type your desired s-value here: ")
    print(" ")
    
    h = int(h_string)
    s = int(s_string)
    
    kalaha_list = create_kalaha_list(h,s)
    
    game_theoretic_value = solvegameposition(1, kalaha_list) 

    if game_theoretic_value[0] == "p1win":
        
        chosen_house_index = game_theoretic_value[-1]
        chi = str(chosen_house_index)
        print(game_theoretic_value)
        return("Player 1 must pick seeds from house "+chi+" in order to win.")
    if game_theoretic_value[0] == "draw":
        chosen_house_index = game_theoretic_value[-1]
        chi = str(chosen_house_index)
        print("Player 1 can at the most force a draw.")
        return("Player 1 must pick seeds from house "+chi+" in order to draw.")
    if game_theoretic_value[0] == "p2win":
        return("Under perfect play, Player 1 cannot win.")
        
        
        
                
            
            
print(startsolving())


    
