from flask import jsonify, request, render_template
from flask.views import MethodView
from flask_security import roles_accepted

import json
from wtforms.form import Form
from wtforms.fields import TextField
from wtforms.fields.html5 import DateField

class TestForm(Form):
    text = TextField('Test')
    date = DateField('start_time', format='%m/%d/%Y')


class TestView(MethodView):

    def get(self):
        dataform = TestForm()
        return render_template('index.html', dataform=dataform)

    def post(self):
        dataform = TestForm(request.form)
        # import ipdb; ipdb.set_trace()
        return render_template('index.html', dataform=dataform)

