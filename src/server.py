from flask import Flask, render_template, request, jsonify
import api

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/representatives")
def representatives():
    zipcode = request.args.get("zip")
    address = request.args.get("address")

    data = api.get_representatives(zipcode, address)

    # return jsonify(data)

    federal = list(filter(lambda k: "country" in k["office"]["levels"], data["representatives"]))
    state = list(filter(lambda k: "administrativeArea1" in k["office"]["levels"], data["representatives"]))
    local = list(filter(lambda k: not (k in federal or k in state), data["representatives"]))

    return render_template(
        "representatives.html",
        input=data["input"],
        federal=federal,
        state=state,
        local=local,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
