import game
import ui

def new_game():
    game.start_new_game()
    ui.show_message("")
    ui.show_game(game.dealer_hand, game.player_hand)
    ui.show_score(game.calculate_hand_value(game.player_hand))
    ui.enable_buttons()

def result():
    status = game.check_winner()

    ui.show_message(status)
    ui.disable_buttons()
    ui.show_money(game.money_count(game.check_winner()))

def hit():
    score = game.player_hit()
    ui.show_game(game.dealer_hand, game.player_hand)
    ui.show_score(score)
    
    if score > 21: result()

def stand():
    game.dealer_play()
    ui.show_game(game.dealer_hand, game.player_hand)
    result()

# Create the window
hit_btn, stand_btn, new_btn = ui.create_window()

# Connect buttons to functions
hit_btn.config(command=hit)
stand_btn.config(command=stand)
new_btn.config(command=new_game)

# Start first game
new_game()
ui.run()
