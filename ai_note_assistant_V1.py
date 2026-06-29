# AI Note Assistant v1
# A small rule-based Python app that analyzes short notes.
import json

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
    elif "this week" in note or "soon" in note or "tomorrow" in note:
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
    

def count_priorities(analyzed_notes):
    high_priority_count = 0
    medium_priority_count = 0
    low_priority_count = 0

    for analysis in analyzed_notes:
        if analysis['priority'] == 'High':
            high_priority_count += 1
        elif analysis['priority'] == 'Medium':
            medium_priority_count += 1
        elif analysis['priority'] == 'Low':
            low_priority_count += 1

    return {
        "High": high_priority_count,
        "Medium": medium_priority_count,
        "Low": low_priority_count,
    }

def count_categories(analyzed_notes):
    development_count = 0
    design_count = 0
    communication_count = 0
    general_count = 0
     
    for analysis in analyzed_notes:             
        if analysis['category'] == 'Development':
            development_count += 1
        elif analysis['category'] == 'Design':
            design_count += 1
        elif analysis['category'] == 'Communication':
            communication_count += 1
        else:
            general_count += 1
            
    return {
        'Development': development_count,
        'Design': design_count,
        'Communication': communication_count,
        'General': general_count,
    }


def display_session_table(analyzed_notes):
    if len(analyzed_notes) > 0:
        print("\nSession Summary")
        print("-----------------")
        print("No | Note | Category | Priority | Action")
        print("----------------------------------------")

        for index, analysis in enumerate(analyzed_notes, start=1):
            print(
                f"{index} | "
                f"{analysis['note']} | "
                f"{analysis['category']} | "
                f"{analysis['priority']} | "
                f"{analysis['action']}"
            )
    else:
        print("\nNo notes analyzed in this session.")
        

def display_summary_stats(total_notes, priority_counts, category_counts):
    print("\nSummary Stats")
    print("---------------")

    print(f"You analyzed {total_notes} note(s).")

    print("\nPriority")
    print(f"High priority notes: {priority_counts['High']}")
    print(f"Medium priority notes: {priority_counts['Medium']}")
    print(f"Low priority notes: {priority_counts['Low']}")

    print("\nCategory")
    print(f"Development category: {category_counts['Development']}")
    print(f"Design category: {category_counts['Design']}")
    print(f"Communication category: {category_counts['Communication']}")
    print(f"General category: {category_counts['General']}")
    
        
def display_summary(analyzed_notes):
    total_notes = len(analyzed_notes)
    priority_counts = count_priorities(analyzed_notes)
    category_counts = count_categories(analyzed_notes)
    
    display_summary_stats(total_notes, priority_counts, category_counts)
    display_session_table(analyzed_notes)
    
    
def display_welcome():
    print("----------------------------------------")
    print("AI Note Assistant v1")
    print("Type a short note and I will analyze it.")
    print("Type 'help' or 'h' to see commands.")
    print("Type 'rules' or 'r' to see category and priority rules.")
    print("Type 'summary' or 's' to see current session summary.")
    print("Type 'save' or 'sv' to save notes to a file.")
    print("Type 'quit' or 'q' to exit.")
    print("----------------------------------------")
    
    
def display_help():
    print("\nCommands:")
    print("----------")
    
    print("Write any note to analyze it.")
    print("Type 'help' or 'h' to see instructions.")
    print("Type 'rules' or 'r' to see category and priority rules.")
    print("Type 'summary' or 's' to see the current session summary.")
    print("Type 'save' or 'sv' to save notes to a file.")
    print("Type 'quit' or 'q' to exit.")
    
    print("\nExamples:")
    print("----------")
    
    print("Fix urgent login bug today")
    print("Create UI design this week")
    print("Prepare meeting notes soon")
    print("Call the customer tomorrow")



def display_rules():
    print("\nRules:")
    print("--------")
    
    print("\nCategory rules:")
    print("- bug / fix → Development")
    print("- design / ui → Design")
    print("- meeting / call → Communication")
    print("- otherwise → General")
    
    print("\nNote: The first matching category rule wins.")
    
    print("\nPriority rules:")
    print("- urgent / today → High")
    print("- this week / soon / tomorrow → Medium")
    print("- otherwise → Low")
        
        
def save_notes_to_file(analyzed_notes):
    if len(analyzed_notes) == 0:
        print('No notes to save.')
    else:
        with open("session_notes.txt", "w") as file:
            file.write("Saved notes:\n")
            file.write("--------------\n")

            for index, analysis in enumerate(analyzed_notes, start=1):
                file.write(
                    f"{index}. "
                    f"Note: {analysis['note']} | "
                    f"Category: {analysis['category']} | "
                    f"Priority: {analysis['priority']} | "
                    f"Action: {analysis['action']}\n"
                )

        print('\nNotes saved to session_notes.txt')
        
        
def save_notes_to_json(analyzed_notes):
    if len(analyzed_notes) == 0:
        print('No notes to save.')
    else:
        with open("session_notes.json", "w") as file:
            json.dump(analyzed_notes, file, indent=4)

        print('\nNotes saved to session_notes.json')
        
        
def main():
    analyzed_notes = []
    display_welcome()

    while True:
        user_note = input("\nWrite a note, or type 'help': ").strip()
        command = user_note.lower()

        if command == "quit" or command == "q":
            display_summary(analyzed_notes)
            print("Session ended. Goodbye.")
            break
        
        elif command == "help" or command == "h":
            display_help()
            
        elif command == "summary" or command == "s":
            display_summary(analyzed_notes)        
            
        elif command == "rules" or command == "r":
            display_rules()
            
        elif command == "save" or command == "sv":
            save_notes_to_json(analyzed_notes)
            
        elif user_note == "":
            print("Please write a note first.")

        else:
            analysis = analyze_note(user_note)
            display_analysis(analysis)

            analyzed_notes.append(analysis)
        

if __name__ == "__main__":
    main()
