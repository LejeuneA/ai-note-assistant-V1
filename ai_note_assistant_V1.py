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
    
    


def display_summary(analyzed_notes):
    # Priority
    high_priority_count = 0
    medium_priority_count = 0
    low_priority_count = 0
    # Category
    development_count = 0
    design_count = 0
    communication_count = 0
    general_count = 0
     
    for analysis in analyzed_notes:
        if analysis['priority'] == 'High':
            high_priority_count += 1
        elif analysis['priority'] == 'Medium':
            medium_priority_count += 1
        elif analysis['priority'] == 'Low':
            low_priority_count += 1
             
        if analysis['category'] == 'Development':
            development_count += 1
        elif analysis['category'] == 'Design':
            design_count += 1
        elif analysis['category'] == 'Communication':
            communication_count += 1
        else:
            general_count += 1
            
    print("\nSummary Stats")
    print("---------------") 
        
    print(f"You analyzed {len(analyzed_notes)} note(s).")
    
    print("\nPriority")
    print(f"High priority notes: {high_priority_count}")
    print(f"Medium priority notes: {medium_priority_count}")
    print(f"Low priority notes: {low_priority_count}")
    
    print("\nCategory")
    print(f"Development category: {development_count}")
    print(f"Design category: {design_count}")
    print(f"Communication category: {communication_count}")
    print(f"General category: {general_count}")
    

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
        
def display_welcome():
    print("----------------------------------------")
    print("AI Note Assistant v1")
    print("Type a short note and I will analyze it.")
    print("Type 'help' or 'h' to see commands.")
    print("Type 'rules' or 'r' to see category and priority rules.")
    print("Type 'summary' or 's' to see current session summary.")
    print("Type 'quit' or 'q' to exit.")
    print("----------------------------------------")
    
    
def display_help():
    print("\nCommands:")
    print("----------")
    
    print("Write any note to analyze it.")
    print("Type 'help' or 'h' to see instructions.")
    print("Type 'rules' or 'r' to see category and priority rules.")
    print("Type 'summary' or 's' to see the current session summary.")
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
            
        elif user_note == "":
            print("Please write a note first.")

        else:
            analysis = analyze_note(user_note)
            display_analysis(analysis)

            analyzed_notes.append(analysis)


if __name__ == "__main__":
    main()
