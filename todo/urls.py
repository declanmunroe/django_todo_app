"""todo URL Configuration

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
from todoitem.views import get_index, add_item, edit_item, toggle_item

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", get_index),
    url(r"add$", add_item), #add$ means the url must end with add
    url(r"^edit/(\d+)$", edit_item), #^means the url must begin with edit. $ means it must end with the last character before the doller sign. \d+ means one or more digit after the edit. We use this to access the many different id numbers.
                                            #(?P<id>\d+) the brackets creates a group for the numbers \d+    ?P<id> puts the number ie \d+ into a variable called id. Can also be written like this (\d+)
    url(r"^toggle/(\d+)$", toggle_item), # r"^toggle/(\d+)$ toggle is one argument and (\d+) is the second argument
]
