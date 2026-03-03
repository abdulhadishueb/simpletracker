SimpleTracker CLI

SimpleTracker CLI is a Python-based Command-Line Interface (CLI) application that allows administrators to manage users and their tasks.

This project demonstrates Object-Oriented Programming (OOP), JSON file persistence, modular code structure, and CLI command handling using argparse.

📌 Features

Create users (name + email)

Assign tasks to users

View tasks for a specific user

Persistent data storage using JSON

Clean CLI output using the rich library

🏗 Project Structure
simpletracker/
│
├── main.py        # CLI entry point
├── models.py      # User and Task classes
├── storage.py     # JSON load/save logic
├── requirements.txt
└── data.json      # Auto-generated storage file
🧠 Object-Oriented Design
Classes

User

id

name

email

Task

id

title

user_id

Relationship

One-to-Many:

A single User can have multiple Tasks.

💾 Data Persistence

Data is stored locally in a data.json file using Python’s built-in json module.

The system automatically:

Creates the file if it does not exist

Loads data on startup

Saves changes after every modification

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd simpletracker
2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🚀 How to Use
Add a User
python3 main.py add-user --name "Alex" --email "alex@mail.com"
Add a Task to a User
python3 main.py add-task --user "Alex" --title "Finish summative lab"
List Tasks for a User
python3 main.py list-tasks --user "Alex"
🛠 Technologies Used

Python 3.10+

argparse (CLI handling)

json (file persistence)

rich (formatted terminal output)

Git & GitHub (version control)

🎯 Learning Outcomes Demonstrated

Object-Oriented Programming (OOP)

One-to-many data relationships

Modular code organization

CLI subcommand structure

File I/O persistence

External package management

👨‍💻 Author

Abdulhadi Mohamed

📄 License

This project is for academic purposes.