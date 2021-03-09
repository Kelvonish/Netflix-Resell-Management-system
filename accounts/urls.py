from django.urls import path
from . import views
from django.conf.urls.static import static
from netflix import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('',views.index, name='dashboard'),
path('netflix',views.netflix, name="accounts"),
path('cards',views.card, name="cards"),
path('customer',views.customer,name="customers"),
path('accounts/login',views.view_login,name="login"),
path('logout',views.logout_view,name="logout"),
path('edit-customer/<int:pk>/super-edit/', views.editCustomer, name="editCustomer"),
path('edit-netflix-account/<int:pk>/super-edit/', views.editNetflix, name="editNetflix"),
path('edit-card/<int:pk>/super-edit/', views.editCard, name="editCard"),
path('delete-customer/<int:pk>/sad-to-delete',views.deleteCustomer, name="deleteCustomer"),
path('delete-netflix-account/<int:pk>/sad-to-delete',views.deleteNetflix, name="deleteNetflix"),
path('delete-card/<int:pk>/sad-to-delete',views.deleteCard, name="deleteCard"),
path('renew-customer-suscription/<int:pk>/great-news',views.renewCustomer,name="renewCustomer"),
path('renew-netflix-suscription/<int:pk>/great-news',views.renewNetflix,name="renewNetflix")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()