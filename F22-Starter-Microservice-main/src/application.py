from flask import Flask, Response, request, render_template, redirect, url_for
from datetime import datetime
import json
from columbia_student_resource import ColumbiaStudentResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            template_folder='template')

CORS(app)


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result

@app.route("/api/students/", methods=["GET", "POST"])
def input_uni():
    if request.method == "POST":
        UNI = request.form.get("fname")
        re_url = url_for('input_uni') + UNI
        return redirect(re_url, code = 302)
    
    return render_template("search.html")

@app.route("/api/students/<uni>", methods=["GET"])
def get_student_by_uni(uni):

    result = ColumbiaStudentResource.get_by_key(uni)

    if result:
        return render_template("displayinfo.html", GUID=result["guid"], LASTNAME=result["last_name"], FIRSTNAME=result["first_name"], MIDNAME=str(result["middle_name"]), EMAIL=result["email"], SCHOOL=result["school_code"])
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

