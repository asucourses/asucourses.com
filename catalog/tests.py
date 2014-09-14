from django.test import TestCase
from datetime import time, date

# Create your tests here.
from catalog.models import Subject, Course, Section, Instructor, DayOfWeek, GeneralStudies


class SubjectTests(TestCase):

	def setUp(self):
		Subject.objects.create(abbreviation = 'MAT',
										 name = 'Mathematics')

	def test_that_subject_has_abbreviation(self):
		subject = Subject.objects.get(abbreviation = 'MAT')
		self.assertEqual(subject.abbreviation, 'MAT')

	def test_that_subject_has_a_name(self):
		subject = Subject.objects.get(name = 'Mathematics')
		self.assertEqual(subject.name, 'Mathematics')

	def test_that_subject_string_is_abbreviation(self):
		subject = Subject.objects.get(abbreviation = 'MAT')
		self.assertEqual(unicode(subject), 'MAT')

class CourseTests(TestCase):

	def setUp(self):
		self.subject = Subject.objects.create(abbreviation = 'MAT',
											  name = 'Mathematics')

		Course.objects.create(subject = self.subject,
							  number = 110)

	def test_that_course_has_a_number(self):
		course = Course.objects.get(number = 110)
		self.assertEqual(course.number, 110)

	def test_that_course_has_a_subject(self):
		course = Course.objects.get(number = 110)
		self.assertEqual(course.subject, self.subject)

	def test_that_subject_has_courses(self):
		course = Course.objects.get(number = 110)
		courses = self.subject.course_set.all()
		self.assertTrue(course in courses)

	def test_that_course_string_is_abbreviated_subject_number(self):
		course = Course.objects.get(number = 110)
		self.assertEqual(unicode(course), 'MAT 110')

class InstructorTests(TestCase):
	def setUp(self):
		Instructor.objects.create(name = 'John Jones')
		self.subject = Subject.objects.create(name = 'Mathematics',
											  abbreviation = 'MAT')
		self.course = Course.objects.create(subject = self.subject,
											number = 110)
		self.section = Section.objects.create(course = self.course,
											  number = 123456,
							   				  start_time = time(13,2,0),
											  end_time = time(14,2,0),
											  seats_total = 100,
											  seats_available = 5,
											  term_number = 1,
											  min_units = 1,
											  max_units = 5,
											  start_date = date(2014, 2, 20),
											  end_date = date(2014, 4, 20),
											  location = 'Arizona, How do you do!')

	def test_that_instructor_has_a_name(self):
		instructor = Instructor.objects.get(name = 'John Jones')
		self.assertEqual(instructor.name, 'John Jones')

	def test_that_instructor_can_have_multiple_sections(self):
		instructor = Instructor.objects.get(name = 'John Jones')
		self.section.instructors.add(instructor)
		self.section.save()
		self.assertTrue(self.section in instructor.section_set.all())

	def test_that_instructor_string_is_name(self):
		instructor = Instructor.objects.get(name = 'John Jones')
		self.assertEqual(unicode(instructor), 'John Jones')

class SectionTests(TestCase):

	def setUp(self):
		self.subject = Subject.objects.create(abbreviation = 'MAT',
											  name = 'Mathematics')

		self.course = Course.objects.create(subject = self.subject,
											number = 110)

		self.instructor = Instructor.objects.create(name = 'John Jones')

		Section.objects.create(course = self.course,
							   number = 123456,
							   start_time = time(13,2,0),
							   end_time = time(14,2,0),
							   seats_total = 100,
							   seats_available = 5,
							   term_number = 1,
							   min_units = 1,
							   max_units = 5,
							   start_date = date(2014, 2, 20),
							   end_date = date(2014, 4, 20),
							   location = 'Arizona, How do you do!')

	def test_that_section_has_a_number(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.number, 123456)

	def test_that_section_has_a_course(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.course, self.course)

	def test_that_section_has_instructors(self):
		section = Section.objects.get(number = 123456)
		section.instructors.add(self.instructor)
		self.assertTrue(self.instructor in section.instructors.all())

	def test_that_section_knows_days_met(self):
		section = Section.objects.get(number = 123456)
		day1 = DayOfWeek.objects.create(day = DayOfWeek.MONDAY)
		day2 = DayOfWeek.objects.create(day = DayOfWeek.TUESDAY)
		section.days_met.add(day1)
		section.days_met.add(day2)
		self.assertTrue(day1 in section.days_met.all())
		self.assertTrue(day2 in section.days_met.all())

	def test_that_section_knows_time_starts(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.start_time.strftime("%I:%M %p"), "01:02 PM")

	def test_that_section_knows_time_ends(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.end_time.strftime("%I:%M %p"), "02:02 PM")

	def test_that_section_knows_seats_total(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.seats_total, 100)

	def test_that_section_knows_seats_available(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.seats_available, 5)

	def test_that_section_knows_term_number(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.term_number, 1)

	def test_that_section_knows_min_units(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.min_units, 1)

	def test_that_section_knows_max_units(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.max_units, 5)

	def test_that_section_knows_start_date(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.start_date.strftime('%m/%d/%Y'), '02/20/2014')

	def test_that_section_knows_end_date(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.end_date.strftime('%m/%d/%Y'), '04/20/2014')

	def test_that_section_knows_location(self):
		section = Section.objects.get(number = 123456)
		self.assertEqual(section.location, 'Arizona, How do you do!')

class DayOfWeekTests(TestCase):
	def test_that_valid_weekdays_can_exist(self):
		day = DayOfWeek.objects.create(day = DayOfWeek.MONDAY)
		self.assertEqual(day.day, 'M')

	def test_that_string_is_short_form(self):
		day = DayOfWeek.objects.create(day = DayOfWeek.MONDAY)
		self.assertEqual(unicode(day), 'M')