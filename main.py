from flask import Flask, render_template, request
import wikipedia
from webbrowser import open_new_tab

app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search')
def search():
    prompt = request.args.get('prompt')
    if prompt:

        try:

            result = wikipedia.summary(prompt, sentences=5)

            return render_template('result.html', prompt=prompt, result=result)

        except Exception as e:

            result = None
            return render_template('result.html', prompt=prompt, result=result)

    else:
        return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)