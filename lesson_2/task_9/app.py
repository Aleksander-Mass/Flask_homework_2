from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        context = {"name": request.form.get('name'), "email": request.form.get('email')}
        response = make_response(render_template('welcome.html', **context))
        response.set_cookie('username', context['name'])
        response.set_cookie('email', context['email'])
        return response
    return render_template('login.html')


@app.post("/logout")
def logout():
    response = make_response(redirect(url_for("index")))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == "__main__":
    app.run(debug=True)