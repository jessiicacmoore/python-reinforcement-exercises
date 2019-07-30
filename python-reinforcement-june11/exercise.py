project = {
    "committee": ["Stella", "Salma", "Kai"],
    "title": "Very Important Project",
    "due_date": "December 14, 2019",
    "id": "3284",
    "steps": [
        {"description": "conduct interviews", "due_date": "August 1, 2018"},
        {"description": "code of conduct", "due_date": "January 1, 2018"},
        {"description": "compile results", "due_date": "November 10, 2018"},
        {"description": "version 1", "due_date": "January 15, 2019"},
        {"description": "revisions", "due_date": "March 30, 2019"},
        {"description": "version 2", "due_date": "July 12, 2019"},
        {"description": "final edit", "due_date": "October 1, 2019"},
        {"description": "final version", "due_date": "November 20, 2019"},
        {"description": "Wrap up", "due_date": "December 1, 2019"},
    ],
}

project_steps = project["steps"]
steps_assigned = 0

while steps_assigned < len(project_steps):
    for committee_member in project["committee"]:
        project_steps[steps_assigned]["committee_member"] = committee_member
        steps_assigned += 1

for step in project_steps:
    print(step)

# {'description': 'conduct interviews', 'due_date': 'August 1, 2018', 'committee_member': 'Stella'}
# {'description': 'code of conduct', 'due_date': 'January 1, 2018', 'committee_member': 'Salma'}
# {'description': 'compile results', 'due_date': 'November 10, 2018', 'committee_member': 'Kai'}
# {'description': 'version 1', 'due_date': 'January 15, 2019', 'committee_member': 'Stella'}
# {'description': 'revisions', 'due_date': 'March 30, 2019', 'committee_member': 'Salma'}
# {'description': 'version 2', 'due_date': 'July 12, 2019', 'committee_member': 'Kai'}
# {'description': 'final edit', 'due_date': 'October 1, 2019', 'committee_member': 'Stella'}
# {'description': 'final version', 'due_date': 'November 20, 2019', 'committee_member': 'Salma'}
# {'description': 'Wrap up', 'due_date': 'December 1, 2019', 'committee_member': 'Kai'}
