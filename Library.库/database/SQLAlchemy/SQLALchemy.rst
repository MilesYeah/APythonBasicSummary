******************************************************************************************
SQLALchemy
******************************************************************************************



>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///:memory:', echo=True)

>>> from sqlalchemy.ext.declarative import declarative_base

>>> Base = declarative_base()


>>> from sqlalchemy import Column, Integer, String
>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     fullname = Column(String)
...     password = Column(String)
...
...     def __repr__(self):
...        return "<User(name='%s', fullname='%s', password='%s')>" % (
...                             self.name, self.fullname, self.password)


>>> Base.metadata.create_all(engine)
SELECT ...
PRAGMA table_info("users")
()
CREATE TABLE users (
    id INTEGER NOT NULL, name VARCHAR,
    fullname VARCHAR,
    password VARCHAR,
    PRIMARY KEY (id)
)
()
COMMIT


from sqlalchemy import Sequence
Column(Integer, Sequence('user_id_seq'), primary_key=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)


>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> ed_user.name
'ed'
>>> ed_user.password
'edspassword'
>>> str(ed_user.id)
'None'


>>> from sqlalchemy.orm import sessionmaker
>>> Session = sessionmaker(bind=engine)


>>> Session = sessionmaker()
>>> Session.configure(bind=engine)  # once engine is available
>>> session = Session()

>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> session.add(ed_user)

>>> our_user = session.query(User).filter_by(name='ed').first() 
>>> our_user
<User(name='ed', fullname='Ed Jones', password='edspassword')>


>>> ed_user is our_user
True



>>> session.add_all([
...     User(name='wendy', fullname='Wendy Williams', password='foobar'),
...     User(name='mary', fullname='Mary Contrary', password='xxg527'),
...     User(name='fred', fullname='Fred Flinstone', password='blah')])



>>> ed_user.password = 'f8s7ccs'



>>> session.dirty
IdentitySet([<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>])


>>> session.new  
IdentitySet([<User(name='wendy', fullname='Wendy Williams', password='foobar')>,
<User(name='mary', fullname='Mary Contrary', password='xxg527')>,
<User(name='fred', fullname='Fred Flinstone', password='blah')>])


>>> session.commit()



>>> ed_user.id 
1




>>> ed_user.name = 'Edwardo'


>>> fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
>>> session.add(fake_user)

>>> session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
[<User(name='Edwardo', fullname='Ed Jones', password='f8s7ccs')>, <User(name='fakeuser', fullname='Invalid', password='12345')>]



>>> session.rollback()
>>> ed_user.name
u'ed'
>>> fake_user in session
False


>>> session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]



>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone



>>> for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone



>>> for row in session.query(User, User.name).all():
...    print(row.User, row.name)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
<User(name='wendy', fullname='Wendy Williams', password='foobar')> wendy
<User(name='mary', fullname='Mary Contrary', password='xxg527')> mary
<User(name='fred', fullname='Fred Flinstone', password='blah')> fred




>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
ed
wendy
mary
fred


>>> from sqlalchemy.orm import aliased
>>> user_alias = aliased(User, name='user_alias')


>>> for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
<User(name='fred', fullname='Fred Flinstone', password='blah')>




>>> for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>



>>> for name, in session.query(User.name).\
...             filter_by(fullname='Ed Jones'):
...    print(name)
ed


>>> for name, in session.query(User.name).\
...             filter(User.fullname=='Ed Jones'):
...    print(name)
ed


>>> for user in session.query(User).\
...          filter(User.name=='ed').\
...          filter(User.fullname=='Ed Jones'):
...    print(user)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>



