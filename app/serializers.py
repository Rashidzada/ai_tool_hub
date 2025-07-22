
from rest_framework import serializers
from .models import (
    Category, PricingPlan, AITool, ToolImage, ToolVideo, Feature,
    Review, Comparison, Article, NewsletterSubscriber, ContactSubmission,
    ToolSubmission, SiteStat
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'

class ToolImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolImage
        fields = '__all__'

class ToolVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolVideo
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AIToolSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    images = ToolImageSerializer(many=True, read_only=True)
    videos = ToolVideoSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = AITool
        fields = '__all__'

class ComparisonSerializer(serializers.ModelSerializer):
    tools = AIToolSerializer(many=True, read_only=True)

    class Meta:
        model = Comparison
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = '__all__'

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'

class ToolSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolSubmission
        fields = '__all__'

class SiteStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteStat
        fields = '__all__'
