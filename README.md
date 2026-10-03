# \# CampusTask

# 

# CampusTask is a simple college task management web application built using Flask and SQLite.

# 

# It helps students organize assignments, practicals, projects, exams, deadlines, priorities, and completion status in one place.

# 

# \## 1. The Problem

# 

# College students often have assignments, practicals, projects, and exams with different deadlines. Managing these tasks in different places can make it easy to forget deadlines or lose track of completed work.

# 

# CampusTask provides one simple place to add, view, filter, complete, and delete college tasks.

# 

# \## 2. My Constraint

# 

# My PRN ends in 4, so my assigned constraint was "No Mouse".

# 

# I designed CampusTask so that the main features can be accessed using only a keyboard. The application uses semantic HTML, labels, keyboard focus indicators, and a skip-to-main-content link to improve keyboard accessibility.

# 

# \## 3. Features

# 

# \- Add college tasks

# \- Add task description and deadline

# \- Select task priority

# \- Select task category

# \- View all tasks

# \- Filter tasks by Pending and Completed status

# \- Mark tasks as completed

# \- Delete tasks

# \- Dashboard showing total, pending, and completed tasks

# \- Responsive design for laptop and mobile screens

# \- Keyboard-friendly navigation

# \- SQLite database for persistent task storage

# 

# \## 4. What I Am Most Proud Of

# 

# I am most proud of the dashboard because it gives a quick overview of total, pending, and completed tasks without requiring the user to open every task.

# 

# \## 5. Technology Used

# 

# \- Python

# \- Flask

# \- SQLite

# \- HTML

# \- CSS

# \- Jinja Templates

# 

# \## 6. Data Storage

# 

# CampusTask uses SQLite through the Flask backend.

# 

# Tasks are stored in the `campustask.db` database instead of only being stored in the browser.

# 

## 7. User Testing

I showed CampusTask to two people who had not seen the application before.

Both testers were asked to add a college task, find it in the task list, mark it as completed, and find the completed task.

- Tester 1 completed the task successfully without difficulty.
- Tester 2 completed the task successfully without difficulty.
- No major usability problems were found.
- No major changes were required after testing.
- Login required in future

## 8. AI Usage

AI assistance was used during development to understand implementation steps, debug code, improve the CSS design, and get suggestions for keyboard accessibility.

One issue with the AI-generated guidance was related to the CSS file structure/path. The CSS file was initially not being loaded correctly, so the website appeared without the intended styling. I checked the project folder structure, corrected the CSS file location/path, and verified that the styling worked correctly.

# \## 9. What I Did Not Build

# 

# I intentionally kept the project small and focused.

# 

# The following features were not included:

# 

# \- User authentication

# \- Email notifications

# \- Calendar integration

# \- Automatic reminders

# 

# \## 10. How to Run

# 

# 1\. Clone the repository.

# 

# 2\. Open the CampusTask folder in the terminal.

# 

# 3\. Install the required package:

# 

# ```bash

# pip install -r requirements.txt

