# 1 Since we're using models we'll need to create a session to query our database. We can create a session by using the
# sessionmaker.  sessionmakers, so initializing the object and then we're going to bind the my SQL engine to this
# sessionmaker, from there we'll create a new session. To configure the sessionmaker we write sessionmaker.configure
# and we're going to bind the engine that we set up here with my SQL.

#  a transaction is a set of all or nothing queries. We either want all of them to run or none of them to run at all.

#  commit this project edition with session.commit.

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# engine = create_engine("mysql+mysqlconnector://root:19865421@localhost:3306/house", echo=True)
#
# Base = declarative_base()
#
#
# class Project(Base):
#     __tablename__ = 'project'
#     __table_args__ = {'schema': 'house'}
#
#     project_id = Column(Integer, primary_key=True)
#     title = Column(String(length=50))
#     description = Column(String(length=50))
#
#     def __repr__(self):
#         return "<Project: title{0}, description{1} >".format(self.title, self.description)
#
#
# class Task(Base):
#     __tablename__ = 'task'
#     __table_args__ = {'schema': 'house'}
#
#     task_id = Column(Integer, primary_key=True)
#     project_id = Column(Integer, ForeignKey('house.project.project_id'))
#     description = Column(String(length=50))
#
#     project = relationship('Project')
#
#     def __repr__(self):
#         return "<Project: description{0} >".format(self.description)
#
#
# Base.metadata.create_all(engine)
#
# session_maker = sessionmaker()
# session_maker.configure(bind=engine)
# session = session_maker()
#
#