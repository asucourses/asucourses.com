from django import forms
from catalog.models import Subject, DayOfWeek, GeneralStudies


class ClassSearchForm(forms.Form):
    class_number = forms.IntegerField(
        label='Class #:',
        help_text='Unique ASU Class #:',
        min_value=0,
        max_value=100000,
        required=False
    )
    subject = forms.ChoiceField(
        choices=[('','---')] + zip(Subject.objects.all(), Subject.objects.all()),
        label='Subject:',
        help_text='See <a href="https://webapp4.asu.edu/catalog/Subjects.html">ASU Subject List</a>',
        required=False,
    )
    course_number = forms.IntegerField(
        label='Course Number:',
        help_text='Example: 101',
        min_value=0,
        max_value=900,
        required=False
    )
    class_title = forms.CharField(
        label='Name of Course:',
        help_text='Example: Scientific Computing',
        required=False   
    )
    number_of_units = forms.IntegerField(
        label='Number of Units:',
        help_text='Example: 3 (credit hours)',
        min_value=0,
        max_value=12,
        required=False
    )
    meeting_days = forms.MultipleChoiceField(
        label='Meeting Days',
        help_text='Weekly schedule',
        choices=DayOfWeek.ABBREVIATIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    start_time = forms.TimeField(
        label='Start Time:',
        help_text="Example: 14:30",
        required=False
    )
    end_time = forms.TimeField(
        label='End Time:',
        help_text="Example: 15:30",
        required=False
    )
    general_studies = forms.MultipleChoiceField(
        label='General Studies',
        choices=GeneralStudies.ABBREVIATIONS,
        widget=forms.CheckboxSelectMultiple,
        help_text='See: <a href="https://catalog.asu.edu/ug_gsr">Requirements</a>',
        required=False
    )
    instructor = forms.CharField(
        label='Instructor Name',
        help_text='Example: John Jones',
        required=False
    )