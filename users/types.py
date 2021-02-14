import graphene
from graphene_django import DjangoObjectType
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password", "isSuperuser", "last_login")


class RoomListResponse(graphene.ObjectType):
    arr = graphene.List(UserType)
    total = graphene.Int()
