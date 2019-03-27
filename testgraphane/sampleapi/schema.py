import graphene
from graphene_django import DjangoObjectType

from .models import SampleObject


class SampleType(DjangoObjectType):
    class Meta:
        model = SampleObject


class Query(graphene.ObjectType):
    all_samples = graphene.List(SampleType)

    def resolve_all_samples(self, info, **kwargs):
        return SampleObject.objects.all()


class CreateSample(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    ok = graphene.Boolean()
    sample = graphene.Field(lambda: SampleType)

    @staticmethod
    def mutate(_root, _info, name, description):
        sample = SampleObject(name=name, description=description)
        sample.save()
        return CreateSample(sample=sample, ok=True)


class Mutation(graphene.ObjectType):
    create_sample = CreateSample.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
