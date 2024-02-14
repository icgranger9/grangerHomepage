from app.main import bp


@bp.route('/')
def index():
    return '<h1>Home</h1>'


@bp.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'
