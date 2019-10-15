from indicoio.graphql import GraphClient
from .base import ObjectProxy


class ModelGroup(ObjectProxy):
    def predict(self, data):
        self.gql_query()

