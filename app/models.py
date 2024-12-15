from tortoise import fields
from tortoise.models import Model
from enum import Enum, unique
from typing import Optional

class Item(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    
    def __str__(self):
        return f"Item(id={self.id}, name={self.name})"
    
class Person(Model):
    id = fields.IntField(primary_key=True)
    first_name = fields.CharField(max_length=100)  
    last_name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True) 
    address = fields.TextField(null=True)  
    created_at = fields.DatetimeField(auto_now_add=True)  
    updated_at = fields.DatetimeField(auto_now=True)  

    
    def __str__(self):
        return f"Item(id={self.id}, name={self.name})"

# -------------------------------------------
# Reporting Structure
@unique
class SkillTypeEnum(Enum):
    TECHNICAL = 'Technical'
    STYLE = 'Style'
    PERFORMANCE = 'PERFORMANCE'

@unique
class ScoreEnum(Enum):
    COMPLETE = 'Complete'
    INCOMPLETE = 'Incomplete'
    NOT_ATTEMPTED = 'Not Attempted'

class Path(Item):
    pass

class Level(Item):
    path = fields.OneToOneField(model_name='models.Path', related_name='level')

class Skill(Item):
    type = fields.CharEnumField(SkillTypeEnum, default=SkillTypeEnum.TECHNICAL)
    levels : fields.ManyToManyRelation[Level]

class Score(Model):
    score = fields.CharEnumField(ScoreEnum, default=ScoreEnum.NOT_ATTEMPTED)
    comment = fields. TextField()
    skill = fields.OneToOneField(model_name='models.Skill', related_name='score')
    
# --------------------------------------------
# Student Reporting

class Student(Person):
    birthday = fields.DatetimeField()
    
class StudentPath(Model):
    student = fields.ManyToManyRelation[Student]
    path : fields.ManyToManyRelation[Path]
    level : fields.ManyToManyRelation[Level]

class Teacher(Person):
    paths : fields.ManyToManyRelation[Path]

class StudentReport(Item):
    path : fields.ManyToManyRelation[StudentPath]
    scores : fields.ManyToManyRelation[Score]
    
