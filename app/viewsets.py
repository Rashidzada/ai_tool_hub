# ai_tools/viewsets.py
from rest_framework import viewsets
from .models import (
    Category, PricingPlan, AITool, ToolImage, ToolVideo, Feature,
    Review, Comparison, Article, NewsletterSubscriber, ContactSubmission,
    ToolSubmission, SiteStat
)
from .serializers import (
    CategorySerializer, PricingPlanSerializer, AIToolSerializer, ToolImageSerializer,
    ToolVideoSerializer, FeatureSerializer, ReviewSerializer, ComparisonSerializer,
    ArticleSerializer, NewsletterSubscriberSerializer, ContactSubmissionSerializer,
    ToolSubmissionSerializer, SiteStatSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PricingPlanViewSet(viewsets.ModelViewSet):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer

class AIToolViewSet(viewsets.ModelViewSet):
    queryset = AITool.objects.all()
    serializer_class = AIToolSerializer

class ToolImageViewSet(viewsets.ModelViewSet):
    queryset = ToolImage.objects.all()
    serializer_class = ToolImageSerializer

class ToolVideoViewSet(viewsets.ModelViewSet):
    queryset = ToolVideo.objects.all()
    serializer_class = ToolVideoSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ComparisonViewSet(viewsets.ModelViewSet):
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

class ToolSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ToolSubmission.objects.all()
    serializer_class = ToolSubmissionSerializer

class SiteStatViewSet(viewsets.ModelViewSet):
    queryset = SiteStat.objects.all()
    serializer_class = SiteStatSerializer
