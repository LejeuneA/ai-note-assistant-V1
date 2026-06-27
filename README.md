# AI Note Assistant v1

AI Note Assistant v1 is a small Python learning project that analyzes short notes and returns a simple structured result.

This is my first step toward building AI-powered applications with Python.
At this stage, the project does not use a real AI API yet. It works with rule-based logic so I can practice Python fundamentals first.

## What the app does

The app takes a note from the user and analyzes it based on simple rules.

It returns:

* the original note
* a category
* a priority level
* a suggested action

Example:

```text
Write your note: Fix urgent UI bug today

Note: Fix urgent UI bug today
Category: Development
Priority: High
Action: Do this first
```

## Current features

* Takes user input from the terminal
* Categorizes notes based on keywords
* Detects priority based on urgency words
* Suggests a basic action
* Returns the result as a structured Python dictionary
* Displays the analysis in the terminal

## Categories

The app currently detects these categories:

* Development
* Design
* Communication
* General

## Priority levels

The app currently uses these priority levels:

* High
* Medium
* Low

## Why I built this

I built this project as part of my Python learning journey.

My goal is to understand the basics step by step:

* functions
* parameters
* return values
* dictionaries
* conditional logic
* user input
* structured output
* simple application flow

This project is also a small proof of progress: I started from the basics and gradually built a working mini application.

## How to run

Clone the repository:

```bash
git clone https://github.com/LejeuneA/ai-note-assistant-v1.git
```

Go into the project folder:

```bash
cd ai-note-assistant-v1
```

Run the Python file:

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
py main.py
```

or:

```bash
python3 main.py
```

## Example notes to test

```text
Fix urgent login bug today
Create UI design for dashboard this week
Prepare meeting notes soon
Buy coffee later
```

## Future improvements

Planned next steps:

* improve the terminal output
* allow the user to analyze multiple notes
* save analyzed notes into a JSON file
* organize the project into multiple Python files
* add a simple Flask API
* connect the app to a real AI API later

## Status

This is a beginner learning project and will improve step by step.
