from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippetz import views

# v3
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# # v1
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
# v 2
urlpatterns = format_suffix_patterns(urlpatterns)