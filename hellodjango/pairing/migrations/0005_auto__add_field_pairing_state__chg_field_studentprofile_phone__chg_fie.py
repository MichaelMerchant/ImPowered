# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Pairing.state'
        db.add_column('pairing_pairing', 'state', self.gf('django.db.models.fields.CharField')(default='P', max_length=20), keep_default=False)

        # Adding M2M table for field student1 on 'Pairing'
        db.create_table('pairing_pairing_student1', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pairing', models.ForeignKey(orm['pairing.pairing'], null=False)),
            ('studentprofile', models.ForeignKey(orm['pairing.studentprofile'], null=False))
        ))
        db.create_unique('pairing_pairing_student1', ['pairing_id', 'studentprofile_id'])

        # Adding M2M table for field student2 on 'Pairing'
        db.create_table('pairing_pairing_student2', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pairing', models.ForeignKey(orm['pairing.pairing'], null=False)),
            ('studentprofile', models.ForeignKey(orm['pairing.studentprofile'], null=False))
        ))
        db.create_unique('pairing_pairing_student2', ['pairing_id', 'studentprofile_id'])

        # Changing field 'StudentProfile.phone'
        db.alter_column('pairing_studentprofile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'StudentProfile.facebook_url'
        db.alter_column('pairing_studentprofile', 'facebook_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'StudentProfile.email'
        db.alter_column('pairing_studentprofile', 'email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Pairing.state'
        db.delete_column('pairing_pairing', 'state')

        # Removing M2M table for field student1 on 'Pairing'
        db.delete_table('pairing_pairing_student1')

        # Removing M2M table for field student2 on 'Pairing'
        db.delete_table('pairing_pairing_student2')

        # Changing field 'StudentProfile.phone'
        db.alter_column('pairing_studentprofile', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'StudentProfile.facebook_url'
        db.alter_column('pairing_studentprofile', 'facebook_url', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'StudentProfile.email'
        db.alter_column('pairing_studentprofile', 'email', self.gf('django.db.models.fields.CharField')(default='', max_length=50))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pairing.pairing': {
            'Meta': {'object_name': 'Pairing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pairings'", 'to': "orm['pairing.Project']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '20'}),
            'student1': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'initiated_pairings'", 'symmetrical': 'False', 'to': "orm['pairing.StudentProfile']"}),
            'student2': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'invited_pairings'", 'symmetrical': 'False', 'to': "orm['pairing.StudentProfile']"})
        },
        'pairing.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'null': 'True', 'to': "orm['pairing.StudentProfile']"})
        },
        'pairing.studentprofile': {
            'Meta': {'object_name': 'StudentProfile'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'student_profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['pairing']
