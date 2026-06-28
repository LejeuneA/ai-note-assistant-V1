# AI Note Assistant v1
# A small rule-based Python app that analyzes short notes.


def get_category(note):
    note = note.lower()

    if "bug" in note or "fix" in note:
        return "Development"
    elif "design" in note or "ui" in note:
        return "Design"
    elif "meeting" in note or "call" in note:
        return "Communication"
    else:
        return "General"


def get_priority(note):
    note = note.lower()

    if "urgent" in note or "today" in note:
        return "High"
    elif "this week" in note or "soon" in note:
        return "Medium"
    else:
        return "Low"


def get_suggested_action(category, priority):
    if priority == "High":
        return "Do this first"
    elif category == "Development":
        return "Plan the technical task"
    elif category == "Design":
        return "Prepare the design work"
    elif category == "Communication":
        return "Prepare the message or meeting"
    else:
        return "Add it to your task list"


def analyze_note(note):
    category = get_category(note)
    priority = get_priority(note)
    action = get_suggested_action(category, priority)

    return {
        "note": note,
        "category": category,
        "priority": priority,
        "action": action,
    }


def display_analysis(analysis):
    print("\nAI Note Analysis")
    print("----------------")
    print(f"Note: {analysis['note']}")
    print(f"Category: {analysis['category']}")
    print(f"Priority: {analysis['priority']}")
    print(f"Action: {analysis['action']}")


def display_summary(analyzed_notes):
    print(f"\nYou analyzed {len(analyzed_notes)} note(s).")

    if len(analyzed_notes) > 0:
        print("\nSession Summary")
        print("---------------")

        for analysis in analyzed_notes:
            print(
                f"{analysis['note']} | "
                f"{analysis['category']} | "
                f"{analysis['priority']} | "
                f"{analysis['action']}"
            )


def main():
    analyzed_notes = []

    while True:
        user_note = input("\nWrite your note or type 'quit': ").strip()

        if user_note.lower() == "quit":
            display_summary(analyzed_notes)
            print("Goodbye")
            break

        elif user_note == "":
            print("Please write a note first.")

        else:
            analysis = analyze_note(user_note)
            display_analysis(analysis)

            analyzed_notes.append(analysis)


if __name__ == "__main__":
    main()
