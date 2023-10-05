def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(speakers):
    room_assignments = []
    for i, speaker in enumerate(speakers, start=1):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {i}!")
    return room_assignments

def printer(speakers):
    badges = batch_badge_creator(speakers)
    for badge in badges:
        print(badge)
    assignments = assign_rooms(speakers)
    for assignment in assignments:
        print(assignment)

