from rest_framework import serializers
from ..models import Review,Photo
from .review_comment import ReviewCommentSerializer
from .photo import PhotoSerializer

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review 
        fields = '__all__'
        extra_kwargs = {'user':{'read_only':True}}
    
class ReviewRetrieveSerializer(ReviewSerializer):

    comments = ReviewCommentSerializer(many=True,read_only=True)
    photos = PhotoSerializer(many=True)

    class Meta(ReviewSerializer.Meta):

        pass

    def create(self,validated_data):

        photos = validated_data.pop('photos')        
        review = Review.objects.create(**validated_data)
        for photo in photos:
            Photo.objects.create(review=review,**photo)
        return review
