import tkinter as tk
import os

root = tk.Tk()
images = {}

for filename in os.listdir("cards"):
    if filename.endswith(".png"):
        images[filename] = tk.PhotoImage(file="cards/"+filename).subsample(6, 6)

def create_window():
    global root
    global dealer_label
    global player_label
    global score_label
    global money_label
    global message_label
    global hit_button
    global stand_button
    global gallery_frame1
    global gallery_frame2

    global bet_button

    root.title("Blackjack")
    root.geometry("820x650")
    root.configure(bg='green')
    root.iconbitmap("cards/ace_of_hearts.ico") # Set app icon

    button_config = { 
        'highlightbackground':'green',
        'width':10,
        'font':('Arial', 12)
    }

    label_config = {
        'text':"",
        'bg':'green',
        'fg':'white'
    }

    # Frames
    gallery_frame1 = tk.Frame(root, bg='green')
    gallery_frame2 = tk.Frame(root, bg='green')
    button_frame = tk.Frame(root, bg='green')

    # Labels
    dealer_label = tk.Label(root, font=('Arial', 14), **label_config)
    player_label = tk.Label(root, font=('Arial', 14), **label_config)
    score_label = tk.Label(root, font=('Arial', 12), **label_config)
    money_label = tk.Label(root, font=('Arial', 12), **label_config)
    message_label = tk.Label(root, font=('Arial', 14, 'bold'), **label_config)
    
    # Buttons
    hit_button = tk.Button(button_frame, text="Hit", **button_config)
    stand_button = tk.Button(button_frame, text="Stand", **button_config)
    new_button = tk.Button(button_frame, text="New game", **button_config)
    bet_button = tk.Button(button_frame, text="Double bet", **button_config)

    # Packing
    dealer_label.pack(pady=20)
    gallery_frame1.pack(pady=20)
    player_label.pack(pady=20)
    gallery_frame2.pack(pady=20)
    score_label.pack()
    money_label.pack()
    message_label.pack(pady=20)
    button_frame.pack(pady=20)
    bet_button.pack(side='left', padx=5)
    hit_button.pack(side='left', padx=5)
    stand_button.pack(side='left', padx=5)
    new_button.pack(side='left', padx=5)
    
    return hit_button, stand_button, new_button, bet_button


def hand_to_string(hand):
    result_string = ""
    for card in hand:
        last_card_string = " of ".join(str(item) for item in card)
        result_string += last_card_string + ", "

    return result_string.rstrip(", ")

def update_gallery(gallery,hand,hidden):  
    for label in gallery.winfo_children():
        label.destroy()

    for card in hand:
        card_image = tk.Label(gallery, image=images["_of_".join(card).lower()+".png"], bg='green')

        if hidden and hidden == True:
            card_image = tk.Label(gallery, image=images["card_back.png"], bg='green')

        card_image.pack(side='left', padx=5)

def show_game(dealer_hand, player_hand, hidden=False):
    # Show dealer cards

    if hidden:
        dealer_label.config(text="Dealer: ???")
    else:
        dealer_label.config(text=f"Dealer: {hand_to_string(dealer_hand)}")

    update_gallery(gallery_frame1,dealer_hand,hidden)

    # Show player cards
    player_label.config(text=f"You: {hand_to_string(player_hand)}")
    update_gallery(gallery_frame2,player_hand,hidden=False)

def show_score(score):
    score_label.config(text=f"Your score: {score}")

def show_money(money):
    money_label.config(text=f"Your money: ${money}")

def show_message(text):
    message_label.config(text=text)

def enable_buttons():
    hit_button['state'] = 'normal'
    stand_button['state'] = 'normal'
    bet_button['state'] = 'normal'

def disable_buttons():
    hit_button['state'] = 'disabled'
    stand_button['state'] = 'disabled'

def disable_bet_button():
    bet_button['state'] = 'disabled'

def run():
    root.mainloop()
