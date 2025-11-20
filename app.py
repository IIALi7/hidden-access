from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "CSC{H0m0glYph_Unl0ck3d}"

# الحرف "і" هنا سيريلية وليس i الإنجليزية
CORRECT_USERNAME = "admіn"  # انتبه: هذا هو الحرف І (U+0456)


@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # المطلوب فقط username مطابق بالكامل
        if username == CORRECT_USERNAME:
            return render_template("panel.html", flag=FLAG)
        else:
            error = "Invalid username."

    return render_template("index.html", error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
