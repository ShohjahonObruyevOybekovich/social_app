
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import HomePageView
schema_view = get_schema_view(
   openapi.Info(
      title="Social Media project API",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shohjahonobruyev3@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomePageView.as_view()),
    path('api/post/', include("PostAPP.API.urls",namespace="post"),name="url_post"),
    path('api/comment/', include("CommentAPP.API.urls", namespace="comment"), name="url_comment"),
    path('api/user/', include("UserAPP.API.urls", namespace="user"), name="url_user"),
    path('api/savedpost/', include("SavedPostAPP.API.urls", namespace="savedpost"), name="url_savedpost"),
    path('api/story/', include("StoryAPP.API.urls", namespace="stories"), name="url_stories"),
    path('api/like/', include("LikeAPP.API.urls", namespace="likes"), name="url_likes"),
    path('api/notification/', include("NotificationAPP.API.urls", namespace="notification"), name="url_notification"),
    path('api/follow/', include("FollowAPP.API.urls", namespace="follow"), name="url_follow"),
    path("api/test/",include("TestApp.api.urls",),name="url_test"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

