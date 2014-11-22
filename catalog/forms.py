from django import forms
from catalog.models import Subject, DayOfWeek, GeneralStudies


class ClassSearchForm(forms.Form):
    class_number = forms.IntegerField(
        label='Class #:',
        help_text='Specific ASU Class # (overrides the rest)',
        min_value=0,
        max_value=10000,
        required=False
    )
    subject = forms.ChoiceField(
        choices=zip(Subject.objects.all(), Subject.objects.all()),
        label='Subject:',
        help_text='See <a href="https://webapp4.asu.edu/catalog/Subjects.html">ASU Subject List</a>',
        required=False
    )
    course_number = forms.IntegerField(
        label='Course Number:',
        help_text=' Name of Course eg: "101"',
        min_value=0,
        max_value=900,
        required=False
    )
    class_title = forms.CharField(
        label='Name of Course:',
        help_text='Example: "Statistics"',
        required=False   
    )
    number_of_units = forms.IntegerField(
        label='Number of Units:',
        help_text='# of Credit Hours eg: "3"',
        min_value=0,
        max_value=12,
        required=False
    )
    meeting_days = forms.MultipleChoiceField(
        label='Meeting Days',
        help_text='Days that class will meet.',
        choices=DayOfWeek.DAYS_OF_WEEK,
        required=False
    )
    start_time = forms.TimeField(
        label='Start Time:',
        required=False
    )
    end_time = forms.TimeField(
        label='End Time:',
        required=False
    )
    general_studies = forms.MultipleChoiceField(
        label='General Studies',
        choices=GeneralStudies.GENERAL_STUDIES,
        help_text='See: <a href="https://catalog.asu.edu/ug_gsr">Requirements</a>',
        required=False
    )
    instructor = forms.CharField(
        label='Instructor Name',
        help_text='Name of Instructor eg: "John Jones"',
        required=False
    )