from rest_framework import serializers
from .models import StoreImg


class StoreImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreImg
        fields = ("id", "img")
        read_only_fields = ["id"]
        extra_kwargs = {
            "id": {"read_only": False, "required": False},
            "img": {"read_only": False, "required": True},
        }

    # def validate(self, attrs):
    #     request = self.context.get("request")
    #     user = request.user
    #     get_object_or_404(StoreProfile, owner=Seller.objects.get(user=user))

    #     return super().validate(attrs)

    # def validate_img(self, attrs):
    #     request = self.context.get("request")
    #     user = request.user
    #     profile_obj = get_object_or_404(
    #         StoreProfile, owner=Seller.objects.get(user=user))

    #     if request.method == "POST" and profile_obj.premium_content.store_imgs.count() >= settings.IMAGE_LIMIT:
    #         logger.error(
    #             f"{user} Cannot have more than {settings.IMAGE_LIMIT} images.")
    #         raise serializers.ValidationError(
    #             f"Cannot have more than {settings.IMAGE_LIMIT} images.")

    #     return super().validate(attrs)

    def create(self, validated_data):
        request = self.context.get("request")
        try:
            new_img = StoreImg.objects.create(img=validated_data.get("img"))
            return new_img
        except OSError as e:
            raise APIException("OS error: {0}".format(e))
