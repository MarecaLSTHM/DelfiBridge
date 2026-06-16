from flask import Flask, request, render_template

app = Flask(__name__)

DELFI_URL = "https://southafrica.cad4tb.care/ahri/series/"

@app.route("/delfi")
def delfi():
    patient_id = request.args.get("patientid", "")
    return render_template("redirect.html", patient_id=patient_id, delfi_url=DELFI_URL)

if __name__ == "__main__":
    app.run()