from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("", search_views.index, name='home'),
    path("index1/", search_views.index1, name='home1'),
    path("membership/", search_views.membership, name='membership'),
    path("membership1/", search_views.membership1, name='membership1'),
    path("registration01/", search_views.registration01, name='registration01'),
    path("registration02/", search_views.registration02, name='registration02'),#new
    path("registration11/", search_views.registration11, name='registration11'),
    path("registration12/", search_views.registration12, name='registration12'),
    path("awards/", search_views.awards, name='awards'),
    path("awards1/", search_views.awards1, name='awards1'),
    path("downloads/", search_views.downloads, name='downloads'),
    path("downloads1/", search_views.downloads1, name='downloads1'),
    path("conferences/", search_views.conferences, name='conferences'),
    path("conferences1/", search_views.conferences1, name='conferences1'),
    # path("django-admin/", admin.site.urls),
    # path("admin/", include(wagtailadmin_urls)),
    # path("documents/", include(wagtaildocs_urls)),
    # path("/search/", search_views.search, name="search"),
    path('welcome/', search_views.welcome, name="index"),
    path('insert/', search_views.InsertValue, name='insert'),
    path('login/', search_views.login, name='login'),
    path('register/', search_views.register, name='register'),
    path('result/', search_views.ShowValues, name='result'),
    path('index/', search_views.index, name='index'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
