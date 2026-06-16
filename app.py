from flask import Flask, request, jsonify
from playwright_script import run_delfi_search

app = Flask(__name__)

@app.route("/")
def home():
    return "DELFI Playwright Service Running"

@app.route("/search", methods=["GET"])
def search():
    patient_id = request.args.get("patientid")

    if not patient_id:
        return jsonify({"error": "missing patientid"}), 400

    result = run_delfi_search(patient_id)

    return jsonify({
        "status": "completed",
        "patient_id": patient_id,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
