from rest_framework import serializers

from ...models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "id", "uuid"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("is_active",)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")

        rep["category"] = CategorySerializer(instance=instance.category).data
        return rep
