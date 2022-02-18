from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # Get sample data and prepare for graphing
    data = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("03-01-2020", 1908),
        ("04-01-2020", 896)
    ]

    # Separate data into labels and values for charting purposes
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("graph.html", labels=labels, values=values)


if __name__ == '__main__':
    app.run()