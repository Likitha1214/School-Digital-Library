from flask import Flask, render_template, request
import os
from pdf_reader import read_pdf
import sqlite3

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Upload PDF
@app.route("/upload", methods=["POST"])
def upload():

    subject = request.form["subject"]
    chapter = request.form["chapter"]

    pdf = request.files["pdf"]

    if pdf.filename == "":
        return "No PDF Selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
    pdf.save(filepath)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books(subject,chapter,filename) VALUES(?,?,?)",
        (subject, chapter, pdf.filename),
    )

    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        answer="✅ Book Uploaded Successfully!"
    )


# Search
@app.route("/search", methods=["POST"])
def search():

    question = request.form["question"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT filename FROM books")

    books = cursor.fetchall()

    conn.close()

    if len(books) == 0:
        return render_template(
            "index.html",
            answer="No Books Uploaded."
        )

    result = ""

    for book in books:

        path = os.path.join("uploads", book[0])

        try:
            text = read_pdf(path)

            if question.lower() in text.lower():

                start = text.lower().find(question.lower())

                result = text[start:start+600]

                break

        except:
            pass

    if result == "":
        result = "Topic not found in uploaded books."

    return render_template(
        "index.html",
        answer=result
    )


if __name__ == "__main__":
    app.run(debug=True)