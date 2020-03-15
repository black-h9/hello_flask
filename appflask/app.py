from flask import Flask,request,session,redirect
from flask_sqlalchemy import  SQLAlchemy
from  flask import  render_template
import  pymysql

app = Flask(__name__)

# 数据库
pymysql.install_as_MySQLdb()

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:hello123@localhost/flask_app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)

# 创建模型类 - Models
class Users(db.Model):
    # 创建Users类，映射到数据库中叫Users表
    __tablename__ = "users"
    # 创建字段： id， 主键和自增涨
    id = db.Column(db.Integer, primary_key=True)
    # 创建字段：username， 长度为80的字符串，不允许为空，值必须唯一
    username = db.Column(db.String(80), unique=True, nullable=False)
    # 创建字段：password ，长度为80 的字符串，不允许为空
    password = db.Column(db.String(80), nullable=True)

db.create_all()


# session
app.config["SECRET_KEY"] = "asdfghjkl"


@app.route('/')
def hello_world():
    name = session.get('name')

    return '%s'% name


@app.route('/register',methods = ['POST', 'GET'])
def hello_register():

    if request.method=='POST':
        name = request.form.get('name')
        password = request.form.get('password')
        db.session.add(Users(username=name, password=password))
        db.session.commit()

    return render_template('register.html')

@app.route('/login',methods = ['POST', 'GET'])
def hello_login():

    if request.method=='POST':
        session['name'] = request.form.get('name')
        session['password'] = request.form.get('password')
        user = Users.query.filter(Users.username == session['name']).first()
        password = Users.query.filter(Users.password == session['password']).first()

        if session.get('name') ==user.username and session.get('password')==password.password:
            return render_template('base.html')
        else:

            return render_template('register.html')

    return render_template('login.html',)

# 退出登陆
@app.route('/logout')
def hello_logout():
    if not session['name']:
        return render_template('login.html')
    
    return render_template('base.html')

@app.route('/base')
def hello_base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
