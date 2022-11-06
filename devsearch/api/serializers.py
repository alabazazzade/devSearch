from  rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import profile

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
      
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    owner = profileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
        
    def get_reviews(self, obj): #obj will be Project
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
  