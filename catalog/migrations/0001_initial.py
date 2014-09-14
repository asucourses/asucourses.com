# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'catalog_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'catalog', ['Subject'])

        # Adding model 'Course'
        db.create_table(u'catalog_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Subject'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'catalog', ['Course'])

        # Adding model 'Instructor'
        db.create_table(u'catalog_instructor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'catalog', ['Instructor'])

        # Adding model 'DayOfWeek'
        db.create_table(u'catalog_dayofweek', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'catalog', ['DayOfWeek'])

        # Adding model 'GeneralStudies'
        db.create_table(u'catalog_generalstudies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('study_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'catalog', ['GeneralStudies'])

        # Adding model 'Section'
        db.create_table(u'catalog_section', (
            ('number', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Course'])),
            ('term_number', self.gf('django.db.models.fields.IntegerField')()),
            ('min_units', self.gf('django.db.models.fields.FloatField')(null=True, db_index=True)),
            ('max_units', self.gf('django.db.models.fields.FloatField')(null=True, db_index=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('seats_available', self.gf('django.db.models.fields.IntegerField')()),
            ('seats_total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'catalog', ['Section'])

        # Adding M2M table for field instructors on 'Section'
        m2m_table_name = db.shorten_name(u'catalog_section_instructors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm[u'catalog.section'], null=False)),
            ('instructor', models.ForeignKey(orm[u'catalog.instructor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['section_id', 'instructor_id'])

        # Adding M2M table for field general_studies on 'Section'
        m2m_table_name = db.shorten_name(u'catalog_section_general_studies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm[u'catalog.section'], null=False)),
            ('generalstudies', models.ForeignKey(orm[u'catalog.generalstudies'], null=False))
        ))
        db.create_unique(m2m_table_name, ['section_id', 'generalstudies_id'])

        # Adding model 'SectionMeeting'
        db.create_table(u'catalog_sectionmeeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(db_index=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(db_index=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Section'], null=True)),
        ))
        db.send_create_signal(u'catalog', ['SectionMeeting'])

        # Adding M2M table for field days_of_week on 'SectionMeeting'
        m2m_table_name = db.shorten_name(u'catalog_sectionmeeting_days_of_week')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sectionmeeting', models.ForeignKey(orm[u'catalog.sectionmeeting'], null=False)),
            ('dayofweek', models.ForeignKey(orm[u'catalog.dayofweek'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sectionmeeting_id', 'dayofweek_id'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'catalog_subject')

        # Deleting model 'Course'
        db.delete_table(u'catalog_course')

        # Deleting model 'Instructor'
        db.delete_table(u'catalog_instructor')

        # Deleting model 'DayOfWeek'
        db.delete_table(u'catalog_dayofweek')

        # Deleting model 'GeneralStudies'
        db.delete_table(u'catalog_generalstudies')

        # Deleting model 'Section'
        db.delete_table(u'catalog_section')

        # Removing M2M table for field instructors on 'Section'
        db.delete_table(db.shorten_name(u'catalog_section_instructors'))

        # Removing M2M table for field general_studies on 'Section'
        db.delete_table(db.shorten_name(u'catalog_section_general_studies'))

        # Deleting model 'SectionMeeting'
        db.delete_table(u'catalog_sectionmeeting')

        # Removing M2M table for field days_of_week on 'SectionMeeting'
        db.delete_table(db.shorten_name(u'catalog_sectionmeeting_days_of_week'))


    models = {
        u'catalog.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Subject']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'catalog.dayofweek': {
            'Meta': {'object_name': 'DayOfWeek'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'catalog.generalstudies': {
            'Meta': {'object_name': 'GeneralStudies'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'catalog.instructor': {
            'Meta': {'object_name': 'Instructor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalog.section': {
            'Meta': {'object_name': 'Section'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Course']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'general_studies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.GeneralStudies']", 'symmetrical': 'False'}),
            'instructors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.Instructor']", 'symmetrical': 'False'}),
            'max_units': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_index': 'True'}),
            'min_units': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_index': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'seats_available': ('django.db.models.fields.IntegerField', [], {}),
            'seats_total': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'term_number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'catalog.sectionmeeting': {
            'Meta': {'object_name': 'SectionMeeting'},
            'days_of_week': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.DayOfWeek']", 'symmetrical': 'False'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Section']", 'null': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'db_index': 'True'})
        },
        u'catalog.subject': {
            'Meta': {'object_name': 'Subject'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['catalog']