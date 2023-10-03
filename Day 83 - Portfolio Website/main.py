from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, fields, marshal, abort
from sqlalchemy.dialects.postgresql import ENUM

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Description(db.Model):
    __tablename__ = "descriptions"
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer, nullable=False)
    object_type = db.Column(ENUM('aboutme', 'technology', 'subtechnology',
        name='object_types'), nullable=False)
    language = db.Column(db.String)
    text = db.Column(db.String)


class AboutMe(db.Model):
    __tablename__ = 'aboutme'
    id = db.Column(db.Integer, primary_key=True)
    descriptions = db.relationship(
        'Description',
        primaryjoin="and_(Description.object_type == 'aboutme', foreign(Description.object_id) == AboutMe.id)",
        lazy='dynamic',
        overlaps="descriptions" # addresses SAWarning
    )


class MyProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, primary_key=True)
    subtechnologies = db.relationship('Subtechnology', backref='technology')
    technology_name = db.Column(db.String(50), nullable=False)
    descriptions = db.relationship(
        'Description',
        primaryjoin="and_(Description.object_type == 'technology', foreign(Description.object_id) == Technology.id)",
        lazy='dynamic',
        overlaps="descriptions"
    )


class Subtechnology(db.Model):
    __tablename__ = 'subtechnologies'
    id = db.Column(db.Integer, primary_key=True)
    technology_name = db.Column(db.String, db.ForeignKey(Technology.technology_name))
    subtechnology_name = db.Column(db.String(50), nullable=False)
    descriptions = db.relationship(
        'Description',
        primaryjoin="and_(Description.object_type == 'subtechnology', foreign(Description.object_id) == Subtechnology.id)",
        lazy='dynamic',
        overlaps="descriptions"
    )


class WorkExperience(db.Model):  # populate
    id = db.Column(db.Integer, primary_key=True)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class SoftSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Interests(db.Model):
    id = db.Column(db.Integer, primary_key=True)


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
    'descriptions': fields.List(
        fields.Nested(
            {
                'language': fields.String(attribute='language'),
                'text': fields.String(attribute='text')
            }
        )
    ),
    'object_type': fields.String,
    'object_id': fields.Integer,
    'language': fields.String,
    'text': fields.String
}

# fields.Nested({
#     'language': fields.String(attribute='language'),
#     'text': fields.String(attribute='text')
# })

def marshal_wo_null(content):
    content_marshal = marshal(content, resource_fields)
    content_marshal_wo_null = {k: v for (k, v) in content_marshal.items() if v is not None and v != 0 and v} # some empty lists or 0s appear
    return content_marshal_wo_null


def abort_if_exist(contents, args, checked_var):
    if any(content[checked_var] == args[checked_var] for content in contents):  # !
        abort(409, message=f'{args[checked_var]} already exist')


class GetContent(Resource):
    def get(self):
        args = request.args
        content_type = args['content'].title()
        content_id = args['id']
        got_content = globals().get(content_type).query.filter_by(id=content_id).first()
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
            abort_if_exist(table, args, 'technology_name')
            new_content = Technology(
                technology_name=args['technology_name']
            )
        elif content_type == 'subtechnology':
            table = all_content['Subtechnologies']
            abort_if_exist(table, args, 'subtechnology_name')
            new_content = Subtechnology(
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
        subtechnologies = [marshal_wo_null(subtechnology) for subtechnology in db.session.query(Subtechnology).all()]
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


class PostText(Resource):
    def post(self):
        args = request.form
        new_text = Description(
            object_id=args['object_id'],
            object_type=args['object_type'],
            language=args['language'],
            text=args['text']
        )
        db.session.add(new_text)
        db.session.commit()

        return marshal_wo_null(new_text)


api.add_resource(GetContent, '/get/')
api.add_resource(GetAllContent, '/get-all/')
api.add_resource(PostContent, '/post/')
api.add_resource(PostText, '/post-text/')
api.add_resource(DeleteContent, '/delete/')

if __name__ == '__main__':
    app.run(debug=True)
