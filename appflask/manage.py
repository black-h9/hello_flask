from  flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zlbbs import create_app
from  exts import db
from apps.cms import models as cms_modles

CMSUser = cms_modles.CMSUser
app = create_app()
manager = Manager(app)
Migrate(app,db)
db.init_app(app)
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--emaill',dest='emaill')

def create_cms_user(username,password,emaill):
    user = CMSUser(username=username,password=password,emaill=emaill)
    db.session.add(user)
    db.session.commit()
    print('用户添加成功')








if __name__ =='__main__':
    manager.run()