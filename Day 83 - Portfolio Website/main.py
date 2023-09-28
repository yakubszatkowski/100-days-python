from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, fields, marshal

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
    technology_id = db.Column(db.String, db.ForeignKey('technologies.id'))
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


class GetContent(Resource):
    def get(self):
        args = request.args
        content_type = args['content']
        content_id = args['id']
        got_content = globals().get(content_type).query.filter_by(id=content_id).first()  # !

        return marshal_wo_null(got_content), 200


class PostContent(Resource):
    def post(self):
        content = request.form
        if content['content'] == 'technology':
            new_content = Technology(
                technology_name=content['technology_name']
            )
        elif content['content'] == 'subtechnology':
            new_content = SubTechnology(
                technology_name=content['technology_name'],
                subtechnology_name=content['subtechnology_name']
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
        db.session.delete(got_content)
        db.session.commit()

        return f'Content from {content_type} with id {content_id} has been deleted'


# CHECK IF EVERYTHING IS WORKING THEN COMMIT
api.add_resource(GetContent, '/get/')
api.add_resource(PostContent, '/post/')
api.add_resource(GetAllContent, '/getall/')
api.add_resource(DeleteContent, '/delete/')

if __name__ == '__main__':
    app.run(debug=True)
