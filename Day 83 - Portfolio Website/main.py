from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, fields, marshal, abort
from sqlalchemy.dialects.postgresql import ENUM
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Translation(db.Model):
    __tablename__ = "Translations"
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer, nullable=False)
    object_type = db.Column(ENUM('softskill', 'myproject', 'technology', 'subtechnology', 'experience',
        name='object_types'), nullable=False)
    language = db.Column(db.String)
    title = db.Column(db.String)
    text = db.Column(db.String)


class SoftSkill(db.Model):
    __tablename__ = 'Softskills'
    id = db.Column(db.Integer, primary_key=True)
    type_soft = db.Column(db.String)  # either aboutme, language, soft skill, interest
    translations = db.relationship(  # this contains both title and text and translations for them
        'Translation',
        primaryjoin="and_(Translation.object_type == 'softskill', foreign(Translation.object_id) == SoftSkill.id)",
        lazy='dynamic',
        overlaps="translations" # addresses SAWarning
    )


class MyProject(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key=True)
    subtechnologies_used = db.Column(db.String) # doesn't require translation
    image_path = db.Column(db.String)
    link = db.Column(db.String)
    translations = db.relationship(
        'Translation',
        primaryjoin="and_(Translation.object_type == 'myproject', foreign(Translation.object_id) == MyProject.id)",
        lazy='dynamic',
        overlaps="translations"
    )


class Technology(db.Model):
    __tablename__ = 'Technologies'
    id = db.Column(db.Integer, primary_key=True)
    subtechnologies = db.relationship('Subtechnology', backref='technology')
    technology_name = db.Column(db.String(50), nullable=False) # doesn't require translation
    translations = db.relationship(
        'Translation',
        primaryjoin="and_(Translation.object_type == 'technology', foreign(Translation.object_id) == Technology.id)",
        lazy='dynamic',
        overlaps="translations"
    )


class Subtechnology(db.Model):
    __tablename__ = 'Subtechnologies'
    id = db.Column(db.Integer, primary_key=True)
    technology_name = db.Column(db.String, db.ForeignKey(Technology.technology_name))
    subtechnology_name = db.Column(db.String(50), nullable=False) # doesn't require translation
    translations = db.relationship(
        'Translation',
        primaryjoin="and_(Translation.object_type == 'subtechnology', foreign(Translation.object_id) == Subtechnology.id)",
        lazy='dynamic',
        overlaps="translations"
    )


class Experience(db.Model):
    __tablename__ = 'Experiences'
    id = db.Column(db.Integer, primary_key=True)
    type_exp = db.Column(db.String)  # either work or education (similar model)
    location = db.Column(db.String)
    time_range = db.Column(db.String)
    translations = db.relationship(
        'Translation',
        primaryjoin="and_(Translation.object_type == 'experience', foreign(Translation.object_id) == Experience.id)",
        lazy='dynamic',
        overlaps="translations"
    )


with app.app_context():
    db.create_all()


resource_fields = {
    'id': fields.Integer,
    'technology_name': fields.String,
    'subtechnologies': fields.List(fields.String(attribute='subtechnology_name')),
    'subtechnology_name': fields.String,
    'translations': fields.List(
        fields.Nested(
            {
                'language': fields.String(attribute='language'),
                'title': fields.String(attribute='title'),
                'text': fields.String(attribute='text')
            }
        )
    ),
    'object_type': fields.String,
    'object_id': fields.Integer,
    'language': fields.String,
    'title': fields.String(attribute='title'),
    'text': fields.String
}

def date_output(beginning_date, ending_date=None):
    format_beg_day = datetime.strptime(beginning_date, '%m-%Y')
    if ending_date:
        format_end_day = datetime.strptime(ending_date, '%m-%Y')
        works_here = False
    else:
        format_end_day = datetime.today()
        works_here = True

    years = format_end_day.year - format_beg_day.year
    months = format_end_day.month - format_beg_day.month
    output = f'{beginning_date} - {"Now" if works_here else ending_date}{", " if months or years != 0 else ", just started!"}'

    if years > 0:
        output += f'{years} year{"s" if years > 1 else ""} '
    if months > 0:
        output += f'{months} month{"s" if months > 1 else ""}'
    return output


def marshal_wo_null(content):  # !
    content_marshal = marshal(content, resource_fields)
    content_marshal_wo_null = {k: v for (k, v) in content_marshal.items() if v is not None and v != 0 and v}
    return content_marshal_wo_null


def if_already_exist(contents, args, checked_var):
    if any(content[checked_var] == args[checked_var] for content in contents):  # !
        abort(409, message=f'{args[checked_var]} already exist')
        # return f'{args[checked_var]} has been changed'


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

        if content_type == 'SoftSkill':
            new_content = SoftSkill(
                type_soft=args['type_soft']
            )
        elif content_type == 'MyProject':
            new_content = SoftSkill(
                subtechnologies_used=args['subtechnologies_used'],
                image_path=args['image_path'],  #
                link=args['github_link']

            )
        elif content_type == 'Technology':
            table = all_content['Technologies']
            if_already_exist(table, args, 'technology_name')

            new_content = Technology(
                technology_name=args['technology_name']
            )
        elif content_type == 'Subtechnology':
            table = all_content['Subtechnologies']
            if_already_exist(table, args, 'subtechnology_name')

            new_content = Subtechnology(
                technology_name=args['technology_name'],
                subtechnology_name=args['subtechnology_name']
            )
        elif content_type == 'Experience':
            new_content = SoftSkill(
                type_soft=args['type_soft'],
                location=args['location'],
                time_range=date_output(args['starting_date'], args['ending_date'])
            )
        else:
            return 'Wrong content key', 400

        db.session.add(new_content)
        db.session.commit()

        return marshal_wo_null(new_content), 200


class GetAllContent(Resource):
    def get(self):  # populate
        technologies = [marshal_wo_null(technology) for technology in db.session.query(Technology).all()]
        subtechnologies = [marshal_wo_null(subtechnology) for subtechnology in db.session.query(Subtechnology).all()]
        getall = {
            'Technologies': technologies,
            'Subtechnologies': subtechnologies,
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
        new_text = Translation(
            object_id=args['object_id'],
            object_type=args['object_type'],
            language=args['language'],
            text=args['text'],
            title=args['title']
        )
        db.session.add(new_text)
        db.session.commit()

        return marshal_wo_null(new_text)


api.add_resource(GetContent, '/get/')
api.add_resource(GetAllContent, '/get-all/')
api.add_resource(PostContent, '/post/')
api.add_resource(PostText, '/post-text/')
api.add_resource(DeleteContent, '/delete/')

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main_page():  # start returning content to the website
    language = request.args.get('language')
    if language == 'english':
        return render_template('main.html')
    elif language == 'polish':
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
