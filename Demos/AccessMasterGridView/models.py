from django.db import models

# Create your models here.

class AccessMaster(models.Model):
	access_id = models.AutoField(primary_key=True)
	access_name = models.CharField(max_length=45, blank=True, null=True)
	alias_name = models.CharField(max_length=45, blank=True, null=True)
	access_password = models.CharField(max_length=100, blank=True, null=True)
	access_email = models.CharField(max_length=100, blank=True, null=True)
	usa_phone = models.CharField(max_length=45, blank=True, null=True)
	access_permission = models.CharField(max_length=1, blank=True, null=True)
	department_id = models.IntegerField(blank=True, null=True)
	sub_department_id = models.IntegerField(blank=True, null=True)
	designation_id = models.IntegerField(blank=True, null=True)
	suspension_count = models.IntegerField(blank=True, null=True)
	manager_id = models.IntegerField(blank=True, null=True)
	holding_capacity = models.IntegerField(blank=True, null=True)
	holding_adjustment = models.IntegerField(blank=True, null=True)
	pwd_modified_on = models.DateTimeField(blank=True, null=True)
	pwd_modified_by = models.IntegerField(blank=True, null=True)
	is_internal = models.CharField(max_length=1, blank=True, null=True)
	access_state = models.CharField(max_length=1, blank=True, null=True)
	calling_enabled = models.IntegerField(blank=True, null=True)
	rtc_access = models.CharField(max_length=1)
	fs_newsystem_access = models.IntegerField(blank=True, null=True)
	fin_newsystem_access = models.IntegerField(blank=True, null=True)
	fin_role_id = models.IntegerField(blank=True, null=True)
	is_home = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'access_master'

	def __str__(self):
		return '%s' % self.access_name