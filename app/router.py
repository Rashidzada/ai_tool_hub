# ai_tools/router.py
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet, PricingPlanViewSet, AIToolViewSet, ToolImageViewSet,
    ToolVideoViewSet, FeatureViewSet, ReviewViewSet, ComparisonViewSet,
    ArticleViewSet, NewsletterSubscriberViewSet, ContactSubmissionViewSet,
    ToolSubmissionViewSet, SiteStatViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'pricing-plans', PricingPlanViewSet)
router.register(r'ai-tools', AIToolViewSet)
router.register(r'tool-images', ToolImageViewSet)
router.register(r'tool-videos', ToolVideoViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comparisons', ComparisonViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'newsletter-subscribers', NewsletterSubscriberViewSet)
router.register(r'contact-submissions', ContactSubmissionViewSet)
router.register(r'tool-submissions', ToolSubmissionViewSet)
router.register(r'site-stats', SiteStatViewSet)

urlpatterns = router.urls
