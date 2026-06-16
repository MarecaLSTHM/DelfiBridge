from flask import Flask, redirect, request

app = Flask(__name__)

DELFI_URL = "https://cloud.cad4tb.care/winny-solutions/thi-ctb-1196/series/"

@app.route("/delfi")
def delfi():
    patient_id = request.args.get("patientid", "")
    return redirect(f"{DELFI_URL}?inject_patient={patient_id}")

if __name__ == "__main__":
    app.run()
