invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# TODO: Who are all the involved members?
print(f"Involved Members: {(invited.union(attended))}" )

# TODO: Who was absent?
print(f"Absent: {invited.difference(attended)}")

# TODO: Who gatecrashed?
print(f"Not enrolled but attended: {attended.difference(invited)}")

# TODO: Who was invited and attended
print(f"Attended properly: {invited.intersection(attended)}")
