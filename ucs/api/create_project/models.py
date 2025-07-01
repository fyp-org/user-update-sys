from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ucs.core.database import Base

class Project(Base):
    __tablename__ = "project"

    id_project = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    subtitle = Column(String(255))
    description = Column(Text)
    id_category = Column(Integer, ForeignKey("category.id_category"))
    id_stage = Column(Integer, ForeignKey("stage.id_stage"))
    invest_amount = Column(Integer)
    count_of_participant = Column(Integer, default=0)
    date_of_birth = Column(DateTime, default=datetime.utcnow)
    links_to_resources = Column(Text)

    # связи (документы, участники, ссылки)
    members = relationship("ProjectMember", back_populates="project", cascade="all, delete-orphan")
    links   = relationship("ProjectLink", back_populates="project", cascade="all, delete-orphan")
    documents = relationship("ProjectDocument", back_populates="project", cascade="all, delete-orphan")

class ProjectMember(Base):
    __tablename__ = "project_member"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id_project"))
    email = Column(String(255), nullable=False)
    function = Column(String(255))

    project = relationship("Project", back_populates="members")

class ProjectLink(Base):
    __tablename__ = "project_link"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id_project"))
    title = Column(String(255))
    url = Column(String(1024))

    project = relationship("Project", back_populates="links")

class ProjectDocument(Base):
    __tablename__ = "project_document"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id_project"))
    filename = Column(String(255))

    project = relationship("Project", back_populates="documents")