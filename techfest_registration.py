import sys

print("Welcome to SMIT TechFest!")
print("Event organized by Dirk Sebastian A. Buño of APPDAET BTCS2")

participants_num = int(input("\nHow many participants will register?: "))

if participants_num <= 0:
    print("Invalid number of participants.")
    sys.exit()
else:
    participants = []

    for i in range(participants_num):
        name = input("\nEnter participant name: ")
        track = input("Enter chosen track: ")


        participant = {"name": name, "track": track}
        participants.append(participant)


    print("\nRegistered Participants:")
    for index, p in enumerate(participants, start=1):
        print(f"{index}. {p['name']} - {p['track']}")

    unique_tracks = set(p['track'] for p in participants)

    if len(unique_tracks) < 2:
        print("\nNot enough variety in tracks.")
    else:
        print("\nTracks offered in this event:", ", ".join(unique_tracks))

    seen_names = set()
    duplicates = set()

    for p in participants:
        name = p['name']
        if name in seen_names:
            duplicates.add(name)
        else:
            seen_names.add(name)

    if duplicates:
        for name in duplicates:
            print(f"Duplicate name found: {name}")
    else:
        print("No duplicate names.")

    track_summary = {}

    for p in participants:
        track = p['track']
        if track in track_summary:
            track_summary[track] += 1
        else:
            track_summary[track] = 1

    print("\nParticipants per track:")
    for track, count in track_summary.items():
        print(f"{track}: {count}")

