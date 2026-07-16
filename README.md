# School-Digital-Library
A Flask-based School Digital Library AI Assistant that allows students to upload PDF textbooks, organize them by subject and chapter, and search for topics with an easy-to-use web interface. 
 
# Objective

The School Digital Library AI Assistant is a web application that helps students search and learn from digital textbooks. Users can upload PDF books, select a subject and chapter, and search for topics. The system extracts relevant information from the uploaded books and displays it in a simple and user-friendly interface.

# Features
Upload multiple PDF textbooks
Subject-wise book management
Chapter-wise organization
Search topics from uploaded books
Display relevant content from textbooks
Simple and user-friendly interface
Fast PDF text extraction
SQLite database for storing book details
# Technologies Used
Python
Flask
HTML
CSS
JavaScript
SQLite
PyPDF2
# Project Structure
School-Digital-Library/
│
├── app.py
├── database.py
├── pdf_reader.py
├── database.db
├── requirements.txt
├── README.md
│
├── uploads/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
    ├── Screenshot1_Home.png
    ├── Screenshot2_Upload.png
    └── Screenshot3_SearchResult.png
# Installation
1. Install the required packages
pip install -r requirements.txt
2. Create the database
python database.py
3. Run the application
python app.py
4. Open the application
http://127.0.0.1:5000
