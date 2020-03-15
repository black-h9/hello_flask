#encoding:utf-8

from  flask import Blueprint,views,render_template,request,session,redirect,url_for,g
from  .forms import LoginForm
from .models import CMSUser
from .decorators import login_reguired
import config

bp = Blueprint("cms",__name__,url_prefix='/cms')

@bp.route('/')
@login_reguired
def index():
    return render_template('cms/index.html')


@bp.route('/logout')
@login_reguired
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

class Loginviews(views.MethodView):


    def get(self,message=None):
        return render_template('cms/login.html',message=message)

    def post(self):

        form = LoginForm(request.form)
        if form.validate():

            emaill = form.emaill.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(emaill=emaill).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent=True
                return redirect(url_for('cms.index'))
            else:
                # return '邮箱或者密码错误'
                return self.get(message='邮箱或者密码错误')

        else:

            # print(form.errors)
            message = form.errors.popitem()[1][0]
            # return '表单验证错误'
            return self.get(message=message)

@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user

bp.add_url_rule('/login/',view_func=Loginviews.as_view('login'))
