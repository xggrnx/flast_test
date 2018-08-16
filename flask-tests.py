from flask import Flask
from controllers import TestView

app = Flask(__name__)
app.add_url_rule('/', view_func=TestView.as_view('test'))
if __name__ == '__main__':
    app.run()
