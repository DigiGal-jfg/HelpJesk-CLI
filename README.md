# HelpJesk
A lightweight command-line helpdesk ticketing system written in Python.  
HelpJesk simulates a simplified IT service desk workflow, allowing tickets to be created, assigned, viewed, and managed through a structured CLI interface.

This is an ongoing portfolio project focused on clean code structure, incremental refactoring, and good programming practice rather than feature complexity.

---

## Purpose

The aim of HelpJesk is not to build an enterprise ticketing platform, but to:

- Practise structured Python scripting in an IT-operations context
- Develop clean, modular code that can grow without becoming messy
- Build habits around versioning, refactoring, and separation of responsibilities
- Apply and reinforce core programming fundamentals from Programmering 1

Each version introduces deliberate improvements. Structure comes before complexity.

---

## Current Version – v0.1 (Foundation)

- Ticket creation with title, description, and priority selection
- Post-creation submenu for operator assignment (notes option was a placeholder only)
- Basic input validation inline within functions
- Ticket listing with compact overview
- Ticket detail view with notes display
- Error messages printed directly in plain text
- Data stored in memory using a list of dictionaries
- Main menu and program flow as loose code at the bottom of the file

v0.1 establishes the core workflow and basic functionality. Code structure was functional but dense — functions handled multiple responsibilities and the foundation for refactoring was identified early.

---

## Development Roadmap

### v0.2 – Refactor *(in progress)*
- Separation of responsibilities across smaller, focused functions
- Reusable input validation pattern via `ask_until_valid()`
- Colour-coded CLI output
- Operator assignment and notes moved into ticket creation flow
- Cleaner main menu structure via `main()` function

### v0.3 – Persistent Storage
- Store tickets in JSON or SQLite
- Tickets persist between sessions

### v0.4 – Ticket Editing
- Status updates (New → In Progress → Resolved → Closed)
- Operator reassignment
- Adding additional notes to existing tickets

### Future Iterations
- Timestamped notes
- Dynamic operator management (add/remove operators at runtime)
- Ticket filtering and search
- Possible migration to class-based structure

---

## Data Structure

Tickets are stored in memory as a list of dictionaries:

```python
{
    "id": 1,
    "title": "Shared drive not visible",
    "description": "User cannot see network drive",
    "status": "New",
    "priority": "Medium",
    "assigned_to": "Mario",
    "notes": ["Initial report from user"]
}
```

### Future Iterations
- Persistent storage via JSON or SQLite
- Timestamped notes
- Dynamic operator management (add/remove operators at runtime)
- Ticket filtering and search
- Possible migration to class-based structure

---

## Requirements

- Python 3

---

## Running the Program

Open a terminal in the project directory and run:

    python helpjesk.py

---

## Background

HelpJesk started as a self-chosen project (eget val) during the Programmering 1 course within the Drifttekniker (IT-drift) programme.  
It was built and refactored incrementally as a way to practise Python fundamentals, learn clean code structure, and produce a portfolio piece that reflects real development habits rather than a one-shot submission.

The refactoring approach applied in v0.2 was directly influenced by lessons learned building a [Python CLI Calculator](https://github.com/DigiGal-jfg/python-cli-calculator) — a separate assignment used to deliberately practise clean code structure, separation of responsibilities, and incremental versioning.

PowerShell and infrastructure work lives separately in [WatchTower-PS](https://github.com/DigiGal-jfg/WatchTower-PS).
