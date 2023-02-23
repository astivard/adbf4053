from werkzeug.datastructures import ImmutableMultiDict

from .models import db, Data


def add_form_data_to_db(data: ImmutableMultiDict) -> None:
    data = Data(form_data=data)
    db.session.add(data)
    db.session.commit()


def is_form_valid(form: ImmutableMultiDict) -> bool:
    keys = [f'Name {i}' for i in range(len(form))]
    return any([not (form[key].isspace()) for key in keys])


def get_data_from_all_forms() -> list[dict]:
    data = db.session.query(Data.form_id,
                            Data.form_data,
                            Data.time_create).all()
    return [dict(form_id=item[0],
                 form_data=item[1],
                 time_create=item[2].strftime("%d.%m.%Y %H:%M")) for item in data]
