import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    userID = Column(Integer, primary_key=True)
    username = Column(String(50), index=True, nullable=False)    # >-< DirectMessage.SenderID
    email = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    profilePicture = Column(String(50), nullable=False)
    createdAt = Column(DateTime)
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    postID = Column(Integer, ForeignKey(User.userID), primary_key=True)
    userID = Column(Integer, ForeignKey(User.userID))
    image = Column(String(100), nullable=False)
    caption = Column(String(250))
    createdAt = Column(DateTime)

class Comment(Base):
    __tablename__ = 'comment'
    commentID = Column(Integer, ForeignKey(User.userID), primary_key=True)
    postID = Column(Integer, ForeignKey(Post.postID))
    userID = Column(Integer, ForeignKey(User.userID))
    commentTest = Column(Integer, ForeignKey(Post.postID))
    createdAt = Column(DateTime)

class Like (Base):
    __tablename__ = 'like'
    likeID = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey(Post.postID))
    userID = Column(Integer, ForeignKey(User.userID))
    createdAt = Column(DateTime)

class Follower(Base):
    __tablename__ = 'follower'
    followerID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey(User.userID))
    followerUserID = Column(Integer, ForeignKey(User.userID))
    followedAT = Column(DateTime)

class DirectMessage(Base):
    __tablename__ = 'directMessage'
    messageID = Column(Integer, primary_key=True)
    senderID = Column(Integer, ForeignKey(User.userID))
    receiver = Column(Integer, ForeignKey(User.userID))
    messageText = Column(String(250))
    createdAt = Column(DateTime)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
