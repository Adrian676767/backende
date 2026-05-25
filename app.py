from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

students = [
    {"id": 1, "name": "Samuel Oravec", "age": 18, "vyska": 175},
    {"id": 2, "name": "Richard Benko", "age": 22, "vyska": 182},
    {"id": 3, "name": "Natália Hudáková", "age": 19, "vyska": 168},
    {"id": 4, "name": "Barbora Mikulová", "age": 25, "vyska": 170},
    {"id": 5, "name": "Michal Fedor", "age": 30, "vyska": 185},
    {"id": 6, "name": "Patrik Konečný", "age": 17, "vyska": 178},
    {"id": 7, "name": "Juraj Lipták", "age": 28, "vyska": 190},
    {"id": 8, "name": "Kristína Vaňová", "age": 21, "vyska": 165},
    {"id": 9, "name": "Erik Černý", "age": 26, "vyska": 180},
    {"id": 10, "name": "Veronika Poláková", "age": 16, "vyska": 172}
]

def bubble_sort(data, field):
    n = len(data)

    for _ in range(n):
        for i in range(n - 1):

            a = data[i][field]
            b = data[i + 1][field]

            # fix pre string (meno)
            if isinstance(a, str):
                a = a.lower()
                b = b.lower()

            if a > b:
                data[i], data[i + 1] = data[i + 1], data[i]

    return data


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/students", methods=["GET"])
def get_students():

    sort_by = request.args.get("sort") or "age"

    if sort_by not in ["age", "name", "vyska"]:
        return jsonify({"error": "Invalid sort field"}), 400

    sorted_list = bubble_sort(students.copy(), sort_by)
    return jsonify(sorted_list)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
