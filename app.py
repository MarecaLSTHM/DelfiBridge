from flask import Flask, render_template, request

app = Flask(__name__)

DELFI_URL = "https://cloud.cad4tb.care/winny-solutions/thi-ctb-1196/series/"  # replace with real URL

@app.route("/")
def home():
    return "DELFI Bridge Running"

@app.route("/delfi")
def delfi():
    patient_id = request.args.get("patientid", "")

    return render_template(
        "index.html",
        patient_id=patient_id,
        delfi_url=DELFI_URL
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)