all_items = ['the horse and the hound and the horn', 
             'the farmer sowing his corn', 
             'the rooster that crowed in the morn', 
             'the priest all shaven and shorn', 
             'the man all tattered and torn', 
             'the maiden all forlorn', 
             'the cow with the crumpled horn', 
             'the dog', 
             'the cat', 
             'the rat', 
             'the malt', 
             'the house']

all_actions = ['belonged to', 
               'kept', 
               'woke', 
               'married', 
               'kissed', 
               'milked', 
               'tossed', 
               'worried', 
               'killed', 
               'ate', 
               'lay in', 
               'Jack built.']


def rhyme():

    # Add line breaks after each item, except for the last one
    formatted_items = [item + '\n' for item in all_items[:-1]]
    formatted_items.append(all_items[-1] + ' ')

    output = ''

    # Create a verse for each progressively longer list of items and actions
    for i in range(len(formatted_items)-1, -1, -1):
        output += verse(formatted_items[i:], all_actions[i:])
        if i != 0:
            output += '\n\n'

    return output


def verse(items, actions):
    output =  'This is'
    for item, action in zip(items, actions):
        output += ' ' + item + 'that ' + action
    return output
