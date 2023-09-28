from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, fields, marshal, abort

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, primary_key=True)
    technology_name = db.Column(db.String(50), nullable=False)
    subtechnologies = db.relationship('SubTechnology', backref='technology')


class SubTechnology(db.Model):
    __tablename__ = 'subtechnologies'
    id = db.Column(db.Integer, primary_key=True)
    # technology_id = db.Column(db.String, db.ForeignKey('technologies.id'))  # create a technology first if doesn't exist exception
    technology_name = db.Column(db.String, db.ForeignKey('technologies.technology_name'))
    subtechnology_name = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main_page():
    language = request.args.get('language')
    if language == 'english':
        return render_template('main.html')
    elif language == 'polish':
        return render_template('main.html')


resource_fields = {
    'id': fields.Integer,
    'technology_name': fields.String,
    'subtechnologies': fields.List(fields.String(attribute='subtechnology_name')),
    'subtechnology_name': fields.String,
}


def marshal_wo_null(content):
    content_marshal = marshal(content, resource_fields)
    content_marshal_wo_null = {k: v for (k, v) in content_marshal.items() if v is not None}  # !

    return content_marshal_wo_null

def abort_if_exist(content, checked_var):
    try:
        if checked_var in content[0].values(): # is there a possibility to do it differently? explore content[0].values()
            abort(409, message=f'{checked_var} is already in database')
    except IndexError:
        pass


class GetContent(Resource):
    def get(self):
        args = request.args
        content_type = args['content']
        content_id = args['id']
        got_content = globals().get(content_type).query.filter_by(id=content_id).first()  # !
        if not got_content:
            abort(404, message='Couldn\'t find requested content')
        else:
            return marshal_wo_null(got_content), 200


class PostContent(Resource):
    def post(self):
        args = request.form
        content_type = args['content']
        all_content = GetAllContent().get()

        if content_type == 'technology':
            table = all_content['Technologies']
            abort_if_exist(table, args['technology_name'])
            new_content = Technology(
                technology_name=args['technology_name']
            )
        elif content_type == 'subtechnology':
            table = all_content['Subtechnologies']
            abort_if_exist(table, args['subtechnology_name'])
            new_content = SubTechnology(
                technology_name=args['technology_name'],
                subtechnology_name=args['subtechnology_name']
            )
        else:
            return 'Wrong content key', 400
        db.session.add(new_content)
        db.session.commit()
        return marshal_wo_null(new_content), 200


class GetAllContent(Resource):
    def get(self):
        technologies = [marshal_wo_null(technology) for technology in db.session.query(Technology).all()]
        subtechnologies = [marshal_wo_null(subtechnology) for subtechnology in db.session.query(SubTechnology).all()]
        getall = {
            'Technologies': technologies,
            'Subtechnologies': subtechnologies
        }
        return getall


class DeleteContent(Resource):
    def delete(self):
        args = request.args
        content_type = args['content']
        content_id = args['id']
        got_content = globals().get(content_type).query.filter_by(id=content_id).first()
        if not got_content:
            abort(404, message='Couldn\'t find requested content')
        else:
            db.session.delete(got_content)
            db.session.commit()
            return {'message': f'Content from {content_type} with id {content_id} has been deleted'}, 200


# CHECK IF EVERYTHING IS WORKING THEN COMMIT
api.add_resource(GetContent, '/get/')
api.add_resource(PostContent, '/post/')
api.add_resource(GetAllContent, '/get-all/')
api.add_resource(DeleteContent, '/delete/')

if __name__ == '__main__':
    app.run(debug=True)
