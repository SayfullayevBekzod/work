from django.db.models import (
    Model,
    DateTimeField,
    CharField,
    IntegerField,
    ForeignKey,
    CASCADE,
    DateField,
    FloatField,
    ManyToManyField,
)


class AbstractModel(Model):
    created_at = DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Color(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Edge(Model):
    name = CharField(max_length=128)
    price = IntegerField()

    def __str__(self):
        return self.name


class Client(AbstractModel):
    name = CharField(max_length=128)
    metr = FloatField(default=0)
    color_id = ForeignKey(Color, on_delete=CASCADE, related_name="clients")
    edge_id = ForeignKey(Edge, on_delete=CASCADE, related_name="clients")


class LaminateColor(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Laminate(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class LaminatePrice(Model):
    price = IntegerField(default=0)

    def __str__(self):
        return str(self.price)


class Saw(AbstractModel):
    name = CharField(max_length=128)
    list_list = CharField(max_length=128, default=0)
    color_id = ForeignKey(LaminateColor, on_delete=CASCADE, related_name="clients")
    laminate = ForeignKey(Laminate, on_delete=CASCADE, related_name="clients")
    price = ForeignKey(LaminatePrice, on_delete=CASCADE, related_name="clients")

    def __str__(self):
        return self.name


class AddEdge(Model):
    name = CharField(max_length=128)
    number = IntegerField()
    edge_id = ForeignKey(Edge, on_delete=CASCADE, related_name="edges")

    def __str__(self):
        return self.name
