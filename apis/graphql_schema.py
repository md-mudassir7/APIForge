import graphene
from graphene_django.types import DjangoObjectType
from django.apps import apps
from core.models import DynamicModel


class DynamicModelType(DjangoObjectType):
    class Meta:
        model = DynamicModel


class Query(graphene.ObjectType):
    dynamic_model = graphene.Field(DynamicModelType, model_name=graphene.String())

    def resolve_dynamic_model(self, info, model_name):
        try:
            model = apps.get_model("core", model_name)
            return model
        except LookupError:
            return None


schema = graphene.Schema(query=Query)
