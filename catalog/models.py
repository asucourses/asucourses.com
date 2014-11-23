from django.db import models

# Create your models here.

class Subject(models.Model):
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.abbreviation

class Course(models.Model):
    number = models.IntegerField()
    subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return "{} {}".format(unicode(self.subject), unicode(self.number))

class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

class DayOfWeek(models.Model):
    MONDAY = 'M'
    TUESDAY = 'T'
    WEDNESDAY = 'W'
    THURSDAY = 'Th'
    FRIDAY = 'F'
    SATURDAY = 'S'
    SUNDAY = 'Su'

    DAYS_OF_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )

    ABBREVIATIONS = tuple((abbreviation,abbreviation) for abbreviation, full_name in DAYS_OF_WEEK)
    LIST_OF_DAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

    day = models.CharField(max_length = 2,
                           choices = DAYS_OF_WEEK)

    def __unicode__(self):
        return unicode(self.day)

#   def __unicode__(self):
#       return self.get_day_display()

class GeneralStudies(models.Model):
    LITERACY             = 'L'  # Literacy and Critical Inquiry
    MATHEMATICS          = 'MA' # Mathematical Studies
    COMPUTER_SCIENCE     = 'CS' # Computer/statistics/quantitative applications
    HUMANITIES           = 'HU' # Humanities, Arts and Design
    SOCIAL_BEHAVIORAL    = 'SB' # Social-Behavioral Sciences
    SCIENCE_QUALITATIVE  = 'SQ' # Natural Science - Quantitative
    SCIENCE_GENERAL      = 'SG' # Natural Science - General 
    CULTURAL_DIVERSITY   = 'C'  # Cultural Diversity in the United States
    GLOBAL_AWARENESS     = 'G'  # Global Awareness
    HISTORICAL_AWARENESS = 'H'  # Historical Awareness

    GENERAL_STUDIES = (
        (LITERACY,            'Literacy and Critical Inquiry'),
        (MATHEMATICS,         'Mathematical Studies'),
        (COMPUTER_SCIENCE,    'Computer/statistics/quantitative applications'),
        (HUMANITIES,          'Humanities, Arts and Design'),
        (SOCIAL_BEHAVIORAL,   'Social-Behavioral Sciences'),
        (SCIENCE_QUALITATIVE, 'Natural Science - Quantitative'),
        (SCIENCE_GENERAL,     'Natural Science - General'),
        (CULTURAL_DIVERSITY,  'Cultural Diversity in the United States'),
        (GLOBAL_AWARENESS,    'Global Awareness'),
        (HISTORICAL_AWARENESS,'Historical Awareness'),
    )

    ABBREVIATIONS = tuple((abbreviation,abbreviation) for abbreviation, full_name in GENERAL_STUDIES)


    study_type = models.CharField(max_length =2,
                                  choices = GENERAL_STUDIES)

class Section(models.Model):
    number = models.IntegerField(primary_key = True)
    course = models.ForeignKey(Course)
    instructors = models.ManyToManyField(Instructor)
    general_studies = models.ManyToManyField(GeneralStudies)
    term_number = models.IntegerField()
    min_units = models.FloatField(null=True, db_index=True)
    max_units = models.FloatField(null=True, db_index=True)
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    seats_available = models.IntegerField()
    seats_total = models.IntegerField()

class SectionMeeting(models.Model):
    start_time = models.TimeField(db_index=True)
    end_time = models.TimeField(db_index=True)
    days_of_week = models.ManyToManyField(DayOfWeek)
    location = models.CharField(max_length=300)
    section = models.ForeignKey(Section,null=True)