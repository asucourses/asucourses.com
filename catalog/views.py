from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from catalog.models import Subject, Course, Section

# Create your views here.

def subject_listing(request):
	template = loader.get_template('catalog/subject_listing.html')
	all_subjects = Subject.objects.all()

	context = RequestContext(request, {
			'subjects' : all_subjects
		})
	return HttpResponse(template.render(context))

def course_listing(request, subject='MAT'):
	template = loader.get_template('catalog/course_listing.html')
	subject = Subject.objects.get(abbreviation = subject)
	all_courses = Course.objects.filter(subject = subject).prefetch_related('subject')

	context = RequestContext(request, {
			'courses' : all_courses
		})
	return HttpResponse(template.render(context))

def section_listing(request, subject='MAT'):
	template = loader.get_template('catalog/section_listing.html')
	subject = Subject.objects.get(abbreviation = subject)
	all_sections = Section.objects.filter(course__subject = subject).prefetch_related('course__subject').prefetch_related('sectionmeeting_set__days_of_week')

	context = RequestContext(request, {
			'sections' : all_sections
		})
	return HttpResponse(template.render(context))