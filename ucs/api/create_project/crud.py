from sqlalchemy.orm import Session
from . import models, schemas

def create_project(db: Session, data: schemas.ProjectCreate) -> models.Project:
    project = models.Project(
        title=data.title,
        subtitle=data.subtitle,
        description=data.description,
        id_category=data.category_id,
        id_stage=data.stage_id,
        invest_amount=data.invest_amount,
        count_of_participant=len(data.members),
    )
    db.add(project)
    db.flush()  # получаем id_project

    # дочерние записи
    for m in data.members:
        db.add(models.ProjectMember(project_id=project.id_project, email=m.email, function=m.function))
    for l in data.links:
        db.add(models.ProjectLink(project_id=project.id_project, title=l.title, url=l.url))
    for d in data.documents:
        db.add(models.ProjectDocument(project_id=project.id_project, filename=d.filename))

    return project