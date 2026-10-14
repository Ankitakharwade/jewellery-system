from flask import Flask, render_template, request
from jewellery_system import get_jewellery

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/jewellery", methods=["GET", "POST"])
def jewellery():
    if request.method == "POST":
        name = request.form.get("name")
        choice = request.form.get("choice")

        item = get_jewellery(choice)

        if item is None:
            return render_template(
                "jewellery.html",
                error="Please select a valid jewellery item."
            )

        return render_template(
            "jewellery.html",
            name=name,
            item=item,
            price=item.get_price()
        )

    return render_template("jewellery.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)




    

