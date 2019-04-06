import graphene
from graphene_django import DjangoObjectType

from promise import Promise
from promise.dataloader import DataLoader

from .models import SampleObject, ObjectsChild


class SampleTypeChild(DjangoObjectType):
    class Meta:
        model = ObjectsChild


class ChildrenLoader(DataLoader):
    def batch_load_fn(self, keys):
        children_mapping = {}
        for child in ObjectsChild.objects.filter(parent_id__in=keys):
            if not children_mapping.get(child.parent_id):
                children_mapping[child.parent_id] = []
            children_mapping[child.parent_id].append(child)
        result = [children_mapping.get(child_id, []) for child_id in keys]
        return Promise.resolve(result)


children_loader = ChildrenLoader()


class SampleType(DjangoObjectType):
    class Meta:
        interfaces = (graphene.Node, )
        model = SampleObject

    def resolve_objectschild_set(self, info, **kwargs):
        return children_loader.load(self.id)


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
