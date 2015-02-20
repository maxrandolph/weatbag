import sys
from . import words
from weatbag.items import combine
import random

def get_action():
    """Prompts for an action, splits it into words, and removes any prepositions.

    movement actions will be represented by the move token object in this module,
    followed by a one-letter direction.
    """
    action = []
    while len(action) == 0:
        action = input('\n> ').lower().split()
        action = [w for w in action if w not in words.prepositions]
    return action

move_directions = {'n','e','s','w','north','east','south','west'}
mother=["You ought to be ashamed!","Such language for such a bold adventurer!","What would your mother say?"]
def is_move(do):
    return len(do) == 1 and (do[0] in words.move)

def handle_action(tile, player, do):
    if len(do) == 1 and do[0] == 'quit':
        print("until next time, adventurer!")
        sys.exit()
    if len(do) == 1 and (do[0]in words.help):
        print("To move, use 'n,e,w,s'\nTo examine your surroundings, type:'look around'\nTo check your inventory, type:'bag' or 'i'\nOther commands will be intuitive to the situation.")        
    if len(do) == 1 and (do[0]in words.swear):
        print(random.choice(mother))
    elif len(do) == 1 and (do[0] in words.look):
        # Look around
        tile.describe()
    
    elif len(do) == 1 and (do[0] in words.inventory):
        # Look at bag
        for item, n in player.inventory.most_common():
            if n < 1:
                break
            print(item, '(%d)' % n)
    
    elif len(do) >= 3 and (do[0] in words.combine):
        for split in range(2, len(do)):
            item1 = ' '.join(do[1:split])
            item2 = ' '.join(do[split:])
            if player.has(item1):
                if player.has(item2):
                    results = combine(item1, item2)
                    if results is not None:
                        player.take(item1)
                        player.take(item2)
                        player.inventory.update(results)
                    else:
                        print("You can't combine {} with {}".format(item1, item2))
                
                else:
                    print("You don't have a {}".format(item2))
                
                return
            
            elif player.has(item2):
                print("You don't have a {}".format(item1))
                return
            
        else:
            print("You don't have those items.")
    
    else:
        tile.action(player, do)

move_coords = {
    'n': (0,  1),
    's': (0, -1),
    'w': (-1, 0),
    'e': (1,  0)
}
