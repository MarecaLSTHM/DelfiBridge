from flask import Flask, request, render_template

app = Flask(__name__)

DELFI_URL = "https://cloud.cad4tb.care/winny-solutions/thi-ctb-1196/series/"

@app.route("/delfi")
def delfi():
    patient_id = request.args.get("patientid", "")
    return render_template("redirect.html", patient_id=patient_id, delfi_url=DELFI_URL)

if __name__ == "__main__":
    app.run()