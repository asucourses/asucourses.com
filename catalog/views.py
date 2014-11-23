import copy

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from catalog.forms import ClassSearchForm

from catalog.models import Subject, Course, Section, DayOfWeek

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

def search_results(request):
    template = loader.get_template('catalog/search.html')
    form = ClassSearchForm(request.GET)
    # check whether it's valid:
    filters = dict()
    excludes = dict()
    all_sections = list()
    if form.is_valid():
        if form.cleaned_data['class_number']:
            filters['number'] = form.cleaned_data['class_number']
        else:
            if form.cleaned_data['subject']:
                filters['course__subject'] = Subject.objects.get(abbreviation = form.cleaned_data['subject'])
            if form.cleaned_data['course_number']:
                filters['course__number'] = form.cleaned_data['course_number']
            if form.cleaned_data['class_title']:
                filters['course__title__contains'] = form.cleaned_data['class_title']
            if form.cleaned_data['number_of_units']:
                filters['min_units__lte'] = form.cleaned_data['number_of_units']
                filters['max_units__gte'] = form.cleaned_data['number_of_units']
            if form.cleaned_data['meeting_days']:
                print form.cleaned_data['meeting_days']
                days_of_week = copy.deepcopy(DayOfWeek.LIST_OF_DAYS)
                for day in form.cleaned_data['meeting_days']:
                    days_of_week.remove(day)
                excludes['sectionmeeting__days_of_week__day__in'] = days_of_week
            if form.cleaned_data['start_time']:
                filters['sectionmeeting__start_time__gte'] = form.cleaned_data['start_time']
            if form.cleaned_data['end_time']:
                filters['sectionmeeting__end_time__lte'] = form.cleaned_data['end_time']

    all_sections = Section.objects.filter(**filters).exclude(**excludes).prefetch_related('course__subject').prefetch_related('sectionmeeting_set__days_of_week')
    #general_studies
    #instructor 

    context = RequestContext(request, {
            'sections' : all_sections
    })
    return HttpResponse(template.render(context))

def home_page(request):
    template = loader.get_template('catalog/home.html')
    form = ClassSearchForm()

    context = RequestContext(request, {
            'form' : form
        })

    return HttpResponse(template.render(context))
