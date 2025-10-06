from flask import Blueprint, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

main = Blueprint("main", __name__)

UPLOAD_FOLDER = "dataset"
REPORT_FOLDER = "reports"

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            df = pd.read_csv(filepath)
            summary = df.describe().to_html()

            report_path = os.path.join(REPORT_FOLDER, "summary.html")
            with open(report_path, "w") as f:
                f.write(summary)

            return f"Report generated: {report_path}"
    return render_template("index.html")
