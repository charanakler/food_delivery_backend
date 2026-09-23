from rest_framework import serializers
from .models import Cart, CartItem, Order, OrderItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "created_at", "updated_at"]


class CartItemSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(
        source="food_item.name",
        read_only=True
    )

    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "food_item",
            "food_name",
            "quantity",
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(
        source="food_item.name",
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "food_item",
            "food_name",
            "quantity",
            "price",
        ]