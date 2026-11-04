# Learning Assistant 5.0 - Study Activity Organiser
# Uses only Sessions 1-5: variables, conditions, loops, basic collections.

# list       -> ordered study durations (minutes), one per recorded activity
# tuple      -> fixed weekly goal that must never change: (minutes, label)
# set        -> unique topics (duplicates are ignored automatically)
# dictionary -> accumulated minutes per topic (topic -> total minutes)
durations = []
WEEKLY_GOAL = (300, "minutes per week")
topics = set()
time_by_topic = {}

print("=== Learning Assistant 5.0 ===")
print("Weekly goal:", WEEKLY_GOAL[0], WEEKLY_GOAL[1])

while True:
    print("\nMenu:")
    print("1. Record study activity")
    print("2. Show summary")
    print("3. Compare with weekly goal")
    print("4. Look up a topic")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        topic = input("Topic: ").strip().lower()
        if topic == "":
            print("Topic cannot be empty.")
            continue

        # Validate without exception handling: digits only (one dot allowed)
        text = input("Duration in minutes: ").strip()
        if text.replace(".", "", 1).isdigit() == False:
            print("Please enter a positive number, e.g. 45 or 30.5.")
            continue
        minutes = float(text)
        if minutes <= 0 or minutes > 1440:
            print("Duration must be above 0 and at most 1440 minutes.")
            continue

        durations.append(minutes)
        topics.add(topic)
        # .get() gives 0 for a new topic, so no KeyError can occur
        time_by_topic[topic] = time_by_topic.get(topic, 0) + minutes
        print("Recorded", minutes, "minutes of", topic)

    elif choice == "2":
        if len(durations) == 0:
            print("No activities recorded yet.")
            continue
        total = 0
        for d in durations:
            total += d
        print("\n--- Summary ---")
        print("Activities:", len(durations))
        print("Total minutes:", total)
        print("Average minutes:", round(total / len(durations), 1))
        print("Longest:", max(durations), "| Shortest:", min(durations))
        print("Unique topics:", len(topics))
        for t in sorted(topics):
            print(" -", t, ":", time_by_topic[t], "minutes")

    elif choice == "3":
        total = 0
        for d in durations:
            total += d
        goal = WEEKLY_GOAL[0]
        percent = total / goal * 100
        print("Studied", total, "of", goal, "minutes (", round(percent, 1), "%)")
        if total >= goal:
            print("Goal reached! Great job.")
        else:
            print("Remaining:", goal - total, "minutes")

    elif choice == "4":
        name = input("Topic to look up: ").strip().lower()
        # Membership test on the set / dict avoids missing-key errors
        if name in topics:
            print(name, "->", time_by_topic[name], "minutes studied")
        else:
            print("Topic not found. Known topics:", sorted(topics))

    elif choice == "5":
        print("Goodbye, keep learning!")
        break

    else:
        print("Invalid option. Enter a number from 1 to 5.")
