attendee_names = []

attendee_count = int(input("Attendee count: "))
for attendee in range(attendee_count):
    # TODO: For every attendee expected:
    attendee_name = input("Attendee name: ")

    # TODO: Add attendee_name to attendee_names
    attendee_names.append(attendee_name)

# TODO: Remove your name in attendees (if it’s there)


# TODO: print the late attendee (last attendee)
last_attendee = attendee_names[-1]
print(last_attendee)

# TODO: Remove the late attendee
attendee_names.pop(-1)
print(attendee_names)
