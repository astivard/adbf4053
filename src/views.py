from flask import (
    Blueprint, request, render_template, flash, redirect, url_for
)
from flask_restful import Api, Resource

from src.utils import add_form_data_to_db, is_form_valid, get_data_from_all_forms

bp = Blueprint('form', __name__)
api = Api(bp)


@bp.route('/form/', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        if is_form_valid(request.form):
            add_form_data_to_db(data=request.form)
            flash("Форма успешно отправлена")
        else:
            flash("Заполните все поля")

    return render_template('form.html')


class FormDataList(Resource):
    @staticmethod
    def get():
        return get_data_from_all_forms()


def page_not_found(e):
    return redirect(url_for('form.form')), 404


api.add_resource(FormDataList, '/data/')
