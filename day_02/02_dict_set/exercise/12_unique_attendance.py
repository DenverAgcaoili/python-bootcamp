attendee_names = set()

attendee_count = int(input("Attendee count: "))
for attendee in range(attendee_count):
    # TODO: For every attendee expected:
    attendee_name = input("Attendee name: ")

    # TODO: Add attendee_name to attendee_names
    attendee_names.add(attendee_name)

print(attendee_names)
