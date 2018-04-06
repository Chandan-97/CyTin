"""CyTin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CyTin_View.views import *
from accounts.views import (login_view,
                            register_view, 
                            logout_view, requestnew_view)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^software/(?P<id>\d+)$', details),
    url(r'^categories$', categories),
    url(r'^newlyadded$', newlyadded),
    url(r'^majoros$', majoros),
    url(r'^news$', news),
    url(r'^news/(?P<id>\d+)$', news_details),
    url(r'^requested$', requested),
    url(r'^categories/(?P<category>[a-zA-Z]+)$', bycategories),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'^requestnew/', requestnew_view, name="requestnew"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
