from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kroketweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'kroket.views.index', name='home'),
    url(r'^assortiment$', 'kroket.views.assortiment', name='assortiment'),
    url(r'^afrekenen$', 'kroket.views.afrekenen', name='afrekenen'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
