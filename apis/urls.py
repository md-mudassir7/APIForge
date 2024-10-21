from django.urls import path
from .views import DynamicApiView
from graphene_django.views import GraphQLView

urlpatterns = [
    path("api/<str:model_name>/", DynamicApiView.as_view(), name="dynamic_api"),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
