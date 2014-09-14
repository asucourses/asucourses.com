from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from catalog import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asucourses.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^faq$', TemplateView.as_view(template_name="faq.html")),
    url(r'^trivia$', TemplateView.as_view(template_name="trivia.html")),
    url(r'^about$', TemplateView.as_view(template_name="about.html")),
    url(r'^subjects/$', views.subject_listing),
    url(r'^subjects/(?P<subject>[A-Z]{3})/courses/$', views.course_listing),
    url(r'^subjects/(?P<subject>[A-Z]{3})/sections/$', views.section_listing)
)
