import re
import random

STOP_WORDS = {"the", "is", "are", "was", "were", "and", "or", "in", "on", "at", "to", "for", "of", "a", "an", "with", "by", "this", "that", "it", "as", "from", "be", "can", "will", "which", "using", "used"}

def get_sentences(text):
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in sentences if len(s.split()) >= 5]

def get_topic(sentence):
    words = re.findall(r"\b[A-Za-z]{4,}\b", sentence)
    keywords = [w for w in words if w.lower() not in STOP_WORDS]
    return " ".join(keywords[:2]) if keywords else "given topic"

def generate_two_mark(sentences):
    return [{"question": f"What is {get_topic(s)}?", "answer": s + " It is an important concept in computer science."} for s in sentences[:8]]

def generate_eight_mark(sentences):
    items = []
    for s in sentences[:5]:
        topic = get_topic(s)
        answer = f"""
Introduction:
{s}

Explanation:
{topic} is an important concept used in engineering and computer science.

Working:
1. Input is received.
2. Processing is performed.
3. Output is produced.

Advantages:
1. Improves efficiency.
2. Reduces manual work.
3. Gives better performance.

Applications:
1. Education
2. Industry
3. Research

Conclusion:
Thus, {topic} plays an important role in modern technology.
"""
        items.append({"question": f"Explain {topic} in detail.", "answer": answer})
    return items

def generate_thirteen_mark(sentences):
    items = []
    for s in sentences[:3]:
        topic = get_topic(s)
        answer = f"""
Introduction:
{s}

Definition:
{topic} is a key concept in engineering applications.

Architecture:
The system consists of input, processing, storage, and output modules.

Working:
1. Data is collected from the user.
2. The data is processed using suitable methods.
3. Important information is identified.
4. Output is generated based on the processed data.

Features:
1. Easy to use
2. Fast processing
3. Accurate output
4. Scalable design

Advantages:
1. Saves time
2. Improves accuracy
3. Reduces human effort
4. Useful for automation

Applications:
1. Web applications
2. Education systems
3. Business systems
4. Research projects

Conclusion:
Therefore, {topic} is useful for solving real-world engineering problems.
"""
        items.append({"question": f"Discuss {topic} with architecture and applications.", "answer": answer})
    return items

def generate_sixteen_mark(sentences):
    items = []
    for s in sentences[:2]:
        topic = get_topic(s)
        answer = f"""
Introduction:
{s}

Definition:
{topic} is an important topic in computer science and engineering.

Need:
It is needed to improve automation, accuracy, and efficiency in real-time applications.

Architecture:
1. Input Layer
2. Processing Layer
3. Storage Layer
4. Output Layer

Working Principle:
1. User gives input.
2. System reads and processes the input.
3. Important keywords and concepts are extracted.
4. Questions and answers are generated.
5. Output is displayed to the user.

Advantages:
1. Reduces manual work
2. Saves time
3. Improves productivity
4. Supports automation
5. Easy to access

Disadvantages:
1. Accuracy depends on input quality
2. Large files may take more time
3. Requires proper preprocessing

Applications:
1. Education
2. Online examination
3. Question paper preparation
4. E-learning platforms
5. Research support systems

Example:
A question generation system can read study material and automatically produce 2 mark, 8 mark, 13 mark, and 16 mark questions.

Conclusion:
Thus, {topic} is an effective concept for developing intelligent and useful engineering applications.
"""
        items.append({"question": f"Explain {topic} in detail with working, advantages, disadvantages and applications.", "answer": answer})
    return items

def generate_mcq(sentences):
    mcqs = []
    words = list(set(re.findall(r"\b[A-Za-z]{4,}\b", " ".join(sentences))))
    for s in sentences[:5]:
        topic = get_topic(s).split()[0]
        options = random.sample(words, min(3, len(words))) if len(words) >= 3 else ["System", "Data", "Process"]
        if topic not in options:
            options.append(topic)
        random.shuffle(options)
        mcqs.append({"question": f"Which term is related to: {s}", "options": options[:4], "answer": topic})
    return mcqs

def generate_engineering_maths():
    return [
        {"question": "Find determinant of matrix [[2,3],[1,4]]", "answer": "Determinant = (2×4) - (3×1) = 5"},
        {"question": "Find Eigen Values of matrix [[2,1],[1,2]]", "answer": "Eigen Values are 3 and 1"},
        {"question": "Evaluate ∫(x²+3x+2)dx", "answer": "x³/3 + 3x²/2 + 2x + C"},
        {"question": "Solve dy/dx + y = eˣ", "answer": "This can be solved using integrating factor method."}
    ]

def generate_all_questions(text):
    sentences = get_sentences(text)
    return {
        "two_mark": generate_two_mark(sentences),
        "eight_mark": generate_eight_mark(sentences),
        "thirteen_mark": generate_thirteen_mark(sentences),
        "sixteen_mark": generate_sixteen_mark(sentences),
        "mcq": generate_mcq(sentences),
        "maths": generate_engineering_maths()
    }