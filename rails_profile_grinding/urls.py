from django.urls import path, include

# from .V1 import urls import routerV1, urlpatterns

urlpatterns = [
    # path("v1/", include(routerV1.urls)),
    path("v1/", include("rails_profile_grinding.V1.urls"))
]
