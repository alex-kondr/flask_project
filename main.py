from flask import Flask, render_template


app = Flask(__name__, template_folder="temp", static_folder="data/static")


@app.get("/")
def index():
    return render_template("index.html")


# @app.get("/menu/")
# def menu():
#     return render_template("menu.html", pizza_1="Пепероні", pizza_2="Класична", pizza_3="Моцарела")


@app.get("/menu/")
def menu():
    context = {
        "pizza_1": "Пепероні",
        "pizza_2": "Класична",
        "pizza_3": "Моцарела"
    }
    return render_template("menu.html", **context)


@app.get("/menu_2/")
def menu_2():
    pizzas = [
        "Пепероні",
        "Класична",
        "Моцарела"
    ]
    return render_template("menu_2.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True)
