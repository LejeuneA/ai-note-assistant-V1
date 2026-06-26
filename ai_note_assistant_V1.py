# Eğer note içinde "bug" veya "fix" varsa → "Development"
# Eğer note içinde "design" veya "ui" varsa → "Design"
# Eğer note içinde "meeting" veya "call" varsa → "Communication"
# Diğer durumlarda → "General"


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


print(get_category("Fix login bug before Friday"))
print(get_category("Create UI design for dashboard"))
print(get_category("Prepare meeting notes"))
print(get_category("Buy coffee"))


# Eğer note içinde "urgent" veya "today" varsa → "High"
# Eğer note içinde "this week" veya "soon" varsa → "Medium"
# Diğer durumlarda → "Low"


def get_priority(note):
    note = note.lower()

    if "urgent" in note or "today" in note:
        return "High"
    elif "this week" in note or "soon" in note:
        return "Medium"
    else:
        return "Low"


print(get_priority("Fix urgent login bug today"))
print(get_priority("Prepare report this week"))
print(get_priority("Review notes later"))


# Eğer priority "High" ise → "Do this first"
# Eğer category "Development" ise → "Plan the technical task"
# Eğer category "Design" ise → "Prepare the design work"
# Eğer category "Communication" ise → "Prepare the message or meeting"
# Diğer durumlarda → "Add it to your task list"


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


print(get_suggested_action("Development", "High"))
print(get_suggested_action("Development", "Medium"))
print(get_suggested_action("Design", "Low"))
print(get_suggested_action("Communication", "Low"))
print(get_suggested_action("General", "Low"))


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


print(analyze_note("Fix urgent login bug today"))
