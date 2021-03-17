
```py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://learn:Aa123456@localhost/lsqlalchemy"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'weibo_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, default=0)


class UserAddress(db.Model):
    __tablename__ = 'weibo_user_addr'
    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('weibo_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('address', lazy=True))


@app.route('/user/<int:page>/')
def list_user(page):
    q_user = User.query
    user_page_data = q_user.paginate(int(page), per_page=10)
    return render_template("list_user.html", user_page_data=user_page_data)


@app.route('/')
def list_user_2():
    q_user = User.query
    user_page_data = q_user.paginate(2, per_page=10)
    return render_template("list_user.html", user_page_data=user_page_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
```

templates/list_user.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Show users</title>
</head>
<body>
    <h2>User list: total {{ user_page_data.pages }} pages, current at {{ user_page_data.page }} page.</h2>
    <ul>
        {% for user in user_page_data.items %}
        <li>{{ user.username }} - {{ user.password }}</li>
        {% endfor %}
    </ul>

    {% if user_page_data.has_prev %}
        <a href="{{ url_for('list_user', page=user_page_data.prev_num) }}">上一页</a>
    {% endif %}

    {% if user_page_data.has_next %}
        <a href="{{ url_for('list_user', page=user_page_data.next_num) }}">下一页</a>
    {% endif %}

</body>
</html>
```

