from weatbag import words
import random

class Tile:
    def __init__(self):
        self.contents = {'bag of gold': 1}
        self.blocked='w'

    
    def describe(self):
        if self.contents['bag of gold']:
            print("you've been teleported to a magical room. Mysterious patterns ebb and swirl on the walls.\nA bag of gold sits on the floor.\n There is a wormhole to the west.")
        else:
            print("you've been teleported to a magical room. Mysterious patterns ebb and swirl on the walls.\n There is a wormhole to the west.")
            
    def action(self, player, do):
        if do[0] == "explode" and not self.contents['bag of gold']: 
            try: 
                if do[1] == "self": 
                    print("You start feeling queasy and your stomach rumbles.")
                    print("All of the sudden, your entrails blow out of your body like "
                        "Old Faithful."
                        "The stench is horrible, and for a few seconds you marvel at"
                        "how much pressure must have been built up inside of you."
                        "I guess you should have laid off the beans last night at dinner?")
                    player.hit_points=0
                    player.give('biohazard waste')
                    return
            except: 
                print("barnacles. You just dodged death while traversing the universe.")
        if (do[0] in words.take) and ('gold' in do):
            player.give('bag of gold')
            self.contents['bag of gold'] -= 1
        else:
            print("Sorry, I don't understand.")
            
    def leave(self, player, direction):
        if direction == "w":
            if player.hit_points>0:
                print("'"+player.name,", You must explode yourself first.'\nA mysterious voice rings out.")
                return False
            else:
                print("The wormhole opens wide, and snatches and sucks you in like a starving sentient being.")
                return True
 