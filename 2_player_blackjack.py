import random

deck = ['2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'Jack' , 'Queen' , 'King' , 'Ace']

point_values = {'2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 , '10':10 ,'Jack':10 , 'Queen':10 , 'King':10 , 'Ace':11}

dealer = []
player1 = []
player1_stack = 100
player2 = []
player2_stack = 100


#draws a random card and appends that card to the list of a player's hand.
def draw_card(x):
    new_card = random.choice(deck)
    x.append(new_card)

#will deal cards at the beginning of the round
def deal_cards():
    i = 1
    while i < 3:
        draw_card(dealer)
        draw_card(player1)
        draw_card(player2)
        i = i + 1

#checks the point total of a player
def check_points(x):
    total_points = 0
    for i in x:
        total_points = total_points + point_values[i]
    if total_points > 21 and 'Ace' in x:
            for i in x:
                if i == 'Ace':
                    while total_points > 21:
                        total_points = total_points - 10
    point_values['Ace'] = 11
    return total_points

#checks whether a player has gone over 21
def check_bust(x):
    if check_points(x) > 21:
        return True
    else:
        return False

#checks for win
def check_win(x):
    if check_points(x) == 21:
        return True
    else:
        return False

#asks for the player's move
def player_move(x):
    move = input("Hit or stand? Enter 'hit' for hit and 'stand' for stand: ")
    if move == 'hit':
        draw_card(x)
        print ('You hit.')
        return False
    elif move == 'stand':
        print ('You stood.')
        return True
    else:
        move = input("Please enter either 'hit' or 'stand': ")
        if move == 'hit':
            print ('You hit.')
            draw_card(x)
            return False
        else:
            print ('You stood.')
            return True

#determines whether computer hits or stands
def computer_move():
    if check_points(dealer) < 17:
        draw_card(dealer)
        print ('Dealer hit.')
        return False
    elif check_points(dealer) > 21 and check_points(dealer) > 16 and 'Ace' in dealer:
        print('Dealer stood.')
        return True
    elif check_points(player1) > check_points(dealer) or check_points(player2) > check_points(dealer) or (check_points(player1) > check_points(dealer) and check_points(player2) > check_points(dealer)):
        draw_card(dealer)
        print ('Dealer hit.')
        return False
    else:
        print ('Dealer stood.')
        return True


#prints all hands
def print_board():
    print ("Dealer's hand:")
    for i in dealer:
        print (i)
    print ("Player 1's hand: ")
    for i in player1:
        print (i)
    print ("Player 2's hand: ")
    for i in player2:
        print (i)

#prints board with dealer's full hand
def print_board_up():
    print ("Dealer's hand: {0}".format(dealer))
    print ("Player 1's hand: {0}".format(player1))
    print ("Player 2's hand: {0}".format(player2))

#clears hands
def clear_board():
    global dealer
    global player1
    global player2
    dealer = []
    player1 = []
    player2 = []

#takes player's bet
def player_bets():
    global player1_stack
    global player2_stack
    global player1_bet
    global player2_bet
    player1_bet = int(input('Player 1 currently has {0} chips in their stack. How much will Player 1 bet? '.format(player1_stack)))
    while player1_bet > player1_stack or player1_bet < 1:
        player1_bet = int(input("Please bet a value less than {0} and more than 0. How much will Player 1 bet? ".format(player1_stack + 1)))
    player1_stack = player1_stack - player1_bet
    player2_bet = int(input('Player 2 currently has {0} chips in their stack. How much will Player 2 bet? '.format(player2_stack)))
    while player2_bet > player2_stack or player2_bet < 1:
        player2_bet = int(input("Please bet a value less than {0} and more than 0. How much will Player 2 bet? ".format(player2_stack + 1)))
    player2_stack = player2_stack - player2_bet


while True:
    game_on = True
    while game_on:
        print ("NEW ROUND:")
        clear_board()
        player_bets()
        deal_cards()
        print_board()
        player1_skip = False
        player2_skip = False
        player1_loss = False
        player2_loss = False
        player1_win = False
        player2_win = False
        if player1_skip == False:
            if check_win(player1) == True:
                if player1_bet % 2 == 0:
                    print("Player 1's hand is a natural, Player 1 wins {0} chips.".format(player1_bet * 1.5))
                    player1_stack = player1_stack + 1.5 * player1_bet
                    player1_win = True
                else:
                    print("Player 1's hand is a natural, Player 1 wins {0} chips.".format(player1_bet * 1.5 + 0.5))
                    player1_stack = player1_stack + 1.5 * player1_bet + 0.5
                    player1_win = True
            while player1_skip == False:
                print("----------PLAYER 1'S TURN----------")
                print_board()
                if check_bust(player1) == True:
                    print_board()
                    print ("Player 1's hand is a bust.")
                    player1_loss = True
                    player1_skip = True
                if check_win(player1) == True:
                    print_board()
                    print ('Player 1 has 21, Player 1 wins {0} chips. '.format(player1_bet * 2))
                    player1_stack = player1_stack + 2 * player1_bet
                    player1_win = True
                    player1_skip = True
                if player1_skip == False:
                    if player_move(player1) == True:
                        player1_skip = True
            while player2_skip == False:
                print("----------PLAYER 2'S TURN----------")
                print_board()
                if check_win(player2) == True:
                    if player2_bet % 2 == 0:
                        print("Player 2's hand is a natural, Player 2 wins {0} chips.".format(player2_bet * 1.5))
                        player2_stack = player2_stack + 1.5 * player2_bet
                        player2_win = True
                        player2_skip = True
                    else:
                        print("Player 2's hand is a natural, Player 2 wins {0} chips.".format(player2_bet * 1.5 + 0.5))
                        player2_stack = player2_stack + 1.5 * player2_bet + 0.5
                        player2_win = True
                        player2_skip = True
                while player2_skip == False:
                    print("----------PLAYER 2'S TURN----------")
                    print_board()
                    if check_bust(player2) == True:
                        print_board()
                        print ("Player 2's hand is a bust.")
                        player2_loss = True
                        player2_skip = True
                    if check_win(player2) == True:
                        print_board()
                        print ('Player 2 has 21, Player 2 wins {0} chips. '.format(player2_bet * 2))
                        player1_stack = player1_stack + 2 * player2_bet
                        player2_win = True
                        player2_skip = True
                    if player2_skip == False:
                        if player_move(player2) == True:
                            player2_skip = True
                if player2_skip == True:
                    computer_skip = False
                    while computer_skip == False:
                        print ("----------DEALER'S TURN----------")
                        if check_bust(dealer) == True and check_bust(player1) == False and check_bust(player2) == False:
                            print_board_up()
                            print ("Dealer's hand is a bust, Player 1 wins {0} chips and Player 2 wins {1} chips.".format(player1_bet * 2 , player2_bet * 2))
                            player1_stack = player1_stack + 2 * player1_bet
                            player2_stack = player2_stack + 2 * player2_bet
                            game_on = False
                            computer_skip = True
                        if check_bust(dealer) == True and check_bust(player1) == True and check_bust(player2) == False:
                            print_board_up()
                            print ("Dealer's hand is a bust, Player 2 wins {0} chips.".format(player2_bet * 2))
                            player2_stack = player2_stack + 2 * player2_bet
                            game_on = False
                            computer_skip = True
                        if check_bust(dealer) == True and check_bust(player1) == False and check_bust(player2) == True:
                            print_board_up()
                            print ("Dealer's hand is a bust, Player 1 wins {0} chips.".format(player1_bet * 2))
                            player1_stack = player1_stack + 2 * player1_bet
                            game_on = False
                            computer_skip = True
                        if check_bust(dealer) == True and check_bust(player1) == True and check_bust(player2) == True:
                            print_board_up()
                            print ("Dealer's hand is a bust.")
                            game_on = False
                            computer_skip = True
                        if check_win(dealer) == True:
                            print_board_up()
                            print ('Dealer has 21, you both lose.')
                            game_on = False
                            computer_skip = True
                        if computer_skip == False:
                            print_board()
                            if computer_move() == True:
                                computer_skip = True
                    if computer_skip == True:
                        if check_points(dealer) > check_points(player1) and check_points(dealer) > check_points(player2):
                            print_board_up()
                            print ("Dealer's hand is closer to 21, you both lose.")
                            game_on = False
                        elif check_points(dealer) == check_points(player1) and check_points(dealer) > check_points(player2):
                            print_board_up()
                            print ("Player 1 and dealer tie, it's a push. Player 2 loses.")
                            player1_stack = player1_stack + player1_bet
                            game_on = False
                        elif check_points(dealer) == check_points(player2) and check_points(dealer) > check_points(player1):
                            print_board_up()
                            print ("Player 2 and dealer tie, it's a push. Player 1 loses.")
                            player2_stack = player2_stack + player2_bet
                            game_on = False
                        elif check_points(dealer) == check_points(player1) and check_points(dealer) == check_points(player2):
                            print_board_up()
                            print ("Both Player 1 and Player 2 tie with dealer, it's a push.")
                            player1_stack = player1_stack + player1_bet
                            player2_stack = player2_stack + player2_bet
                            game_on = False
                        elif check_points(dealer) < check_points(player1) and check_points(dealer) < check_points(player2):
                            print_board_up()
                            print ("Dealer's hand is further from 21, Player 1 wins {0} chips and Player 2 wins {1} chips.".format(player1_bet * 2 , player2_bet * 2))
                            player1_stack = player1_stack + player1_bet * 2
                            player2_stack = player2_stack + player2_bet * 2
                            game_on = False
                        elif check_points(dealer) == check_points(player1) and check_points(dealer) < check_points(player2):
                            print_board_up()
                            print ("Player 1 and dealer tie, it's a push. Player 2 wins {0} chips.".format(player2_bet * 2))
                            player1_stack = player1_stack + player1_bet
                            player2_stack = player2_stack + player2_bet * 2
                            game_on = False
                        elif check_points(dealer) == check_points(player2) and check_points(dealer) < check_points(player1):
                            print_board_up()
                            print ("Player 2 and dealer tie, it's a push. Player 1 wins {0} chips.".format(player1_bet * 2))
                            player2_stack = player2_stack + player2_bet
                            player1_Stack = player1_stack + player1_bet * 2
                            game_on = False
