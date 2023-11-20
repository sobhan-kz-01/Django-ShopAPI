from rest_framework import serializers

from ...models import Product, Category, ProductInventory, Varient, VarientTitle


class VarientTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VarientTitle
        fields = ['title','varient_type']

class VarientSerializer(serializers.ModelSerializer):
    title = VarientTitleSerializer()
    value = serializers.SerializerMethodField("get_varient_value")

    
    class Meta:
        model = Varient
        fields = ['title','value']

    def get_varient_value(self,obj: Varient):
        """
        function will return value or color separate 
        """

        if obj.value:
            return obj.value
        
        return {"color":obj.color, "color_name":obj.color_name}


class ProductInventorySerializer(serializers.ModelSerializer):
    varients = VarientSerializer(many=True)
    
    class Meta:
        model = ProductInventory
        fields = ['varients','price','quantity']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "id", "uuid"]

class ShortProductSerializer(serializers.ModelSerializer):
    price_with_discount = serializers.ReadOnlyField(source="discount_price")
    inventory = serializers.SerializerMethodField("get_inventory")

    def get_inventory(self,obj: Product):
        query_inventory = ProductInventory.objects.filter(product=obj)
        return ProductInventorySerializer(instance=query_inventory, many=True).data
    
    class Meta:
        model = Product
        fields = ['title','unit_price','discount','price_with_discount','image','inventory']

class ProductSerializer(serializers.ModelSerializer):
    inventory = serializers.SerializerMethodField("get_inventory")
    price_with_discount = serializers.ReadOnlyField(source="discount_price")
    class Meta:
        model = Product
        exclude = ("is_active","uuid")


    def get_inventory(self,obj: Product):
        query_inventory = ProductInventory.objects.filter(product=obj)
        return ProductInventorySerializer(instance=query_inventory, many=True).data

    def to_representation(self, instance: Product):
        rep = super().to_representation(instance)
        

        rep["categories"] = CategorySerializer(instance=instance.categories.all(),many=True).data
        
        return rep
