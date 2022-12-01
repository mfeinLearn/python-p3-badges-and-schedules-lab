def badge_maker(name):
    badge = f'Hello, my name is {name}.'
    return badge
    #return None

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    message = []
    for index, name in enumerate(names):
        message.append(f'Hello, {name}! You\'ll be assigned to room {index+1}!')
    return message

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for yur_room in assign_rooms(names):
        print(yur_room)

