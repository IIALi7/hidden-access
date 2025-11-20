from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "CSC{H0m0glYph_Acc3ss}"

# هذا الحرف І هو سيرِيليّة وليس I لاتينية
HOMOGLYPH_ADMIN = "admіn"  # انتبه للحرف i هنا (U+0456)
PASSWORD = "shadow123"


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == HOMOGLYPH_ADMIN and password == PASSWORD:
            return render_template("panel.html", flag=FLAG)
        else:
            error = "Invalid credentials."

    return render_template("index.html", error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
