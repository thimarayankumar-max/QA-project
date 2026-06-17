from flask import Flask, render_template, request
from file_processor import extract_text_from_file
from question_generator import generate_all_questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    text = ""
    error = ""
    question_type = "all"

    if request.method == "POST":
        text = request.form.get("text", "")
        question_type = request.form.get("question_type", "all")
        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename != "":
            text = extract_text_from_file(uploaded_file)

        if text.strip() and not text.startswith("Error") and not text.startswith("Unsupported"):
            all_result = generate_all_questions(text)

            if question_type == "2":
                result = {"two_mark": all_result["two_mark"]}
            elif question_type == "8":
                result = {"eight_mark": all_result["eight_mark"]}
            elif question_type == "13":
                result = {"thirteen_mark": all_result["thirteen_mark"]}
            elif question_type == "16":
                result = {"sixteen_mark": all_result["sixteen_mark"]}
            else:
                result = all_result
        else:
            error = "Please enter text or upload PDF, DOCX, PPTX, or TXT file."

    return render_template(
        "index.html",
        result=result,
        text=text,
        error=error,
        question_type=question_type
    )

if __name__ == "__main__":
    app.run(debug=True)