# app/models.py

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    password = fields.CharField(max_length=255)

    seeds = fields.ReverseRelation["Seed"]


class Seed(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    user = fields.ForeignKeyField("models.User", related_name="seeds")

    comments = fields.ReverseRelation["Comment"]


class Comment(Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    user = fields.ForeignKeyField("models.User", related_name="comments")
    seed = fields.ForeignKeyField("models.Seed", related_name="comments")
