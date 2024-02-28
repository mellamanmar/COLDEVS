from flask import Blueprint

tours = Blueprint('tours', __name__)

@tours.route("/tour")
def tourHome ():
    return 'Listado de tours'

@tours.route("/tour/1")
def tourList ():
    return 'Tour detalle'

@tours.route("tour/new")
def tourNew ():
    return 'Crear tour'

@tours.route("tour/update")
def tourUpdate ():
    return 'Actualizar tour'

@tours.route("tour/delete")
def tourDelete ():
    return 'Eliminar tour'