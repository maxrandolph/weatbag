"""A thesaurus of words the player might use, so you can easily accept
synonyms of the word you want.

e.g. This will recognise take, pick, get or collect::

    if do[0] in weatbag.words.take:
        #...
"""
# Verbs
move = {'n','w','s','e'}
give = {'give', 'feed', 'present'}
use = {'eat', 'use', 'wear'}
fight = {'fight', 'kill', 'hit', 'attack'}
drop = {'drop'}
take = {'pick', 'take', 'get', 'collect'}
look = {'look', 'inspect', 'examine'}
attack = {'attack', 'swing', 'hit', 'punch', 'fight'}
combine = {'combine', 'join', 'mix'}
talk = {'talk', 'speak', 'converse'}
help = {'help', 'h'}
swear = {'fuck','shit','ass','damn','cock','tits','goddammit','asshole'}
# Nouns
inventory = {'inventory', 'possessions', 'belongings', 'bag','i'}
surroundings = {'surroundings', 'around', 'scenery'}

prepositions = {'up', 'down', 'on', 'under', 'in', 'at', 'to', 'with', 'and'}

# yes/no
yes = {'yes','y','yup','ye'}
no = {'no','n','nope'}
