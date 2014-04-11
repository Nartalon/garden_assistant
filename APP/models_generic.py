# -*- coding: utf-8 -*-
# auto generated from an XMI file
import Image
from django.db import models

from django.utils.encoding import force_unicode

def getUnicode(object):
	if (object == None):
		return u""
	else:
		return force_unicode(object)
		

#
class z_garden(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=True, )
	c_info = models.TextField(null=False, default="", blank=True, )
	z_ground_type = models.ForeignKey('z_ground_type', blank=True, null=True, )
 	z_light_type = models.ForeignKey('z_light_type', blank=True, null=True, )
 	z_water_level = models.ForeignKey('z_water_level', blank=True, null=True, )
 
	class Meta:
		verbose_name = 'z_garden'
		verbose_name_plural = 'z_gardens'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_ground_type(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_info = models.TextField(null=False, default="", blank=True, )
	c_koef = models.FloatField(null=True, blank=True, )

	class Meta:
		verbose_name = 'z_ground_type'
		verbose_name_plural = 'z_ground_types'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_light_type(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_info = models.TextField(null=False, default="", blank=True, )
	c_koef = models.FloatField(null=True, blank=True, )

	class Meta:
		verbose_name = 'z_light_type'
		verbose_name_plural = 'z_light_types'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_water_level(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_info = models.TextField(null=False, default="", blank=True, )
	c_koef = models.FloatField(null=True, blank=True, )

	class Meta:
		verbose_name = 'z_water_level'
		verbose_name_plural = 'z_water_levels'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_plant(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=True, )
	c_count = models.IntegerField(null=True, blank=True, )
	z_plant_sort = models.ForeignKey('z_plant_sort', blank=False, null=False, default=1, )
 	z_garden_year = models.ForeignKey('z_garden_year', blank=False, null=False, default=1, )
 
	class Meta:
		verbose_name = 'z_plant'
		verbose_name_plural = 'z_plants'
		

	table_group = ''


#
class z_plant_type(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_info = models.TextField(null=False, default="", blank=True, )
	c_image = models.ImageField(upload_to = 'plant_types/', default = 'plant_types/None/no-img.jpg')
	class Meta:
		verbose_name = 'z_plant_type'
		verbose_name_plural = 'z_plant_types'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)
	def image_tag(self):
		return u'<img src="%s" />' % self.c_image.url
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	table_group = ''


#
class z_plant_sort(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_info = models.TextField(null=False, default="", blank=True, )
	c_ripe_min = models.IntegerField(null=True, blank=True, )
	c_ripe_max = models.IntegerField(null=True, blank=True, )
	z_plant_ripe = models.ForeignKey('z_plant_ripe', blank=False, null=False, default=1, )
 	z_plant_water = models.ForeignKey('z_plant_water', blank=False, null=False, default=1, )
 	z_plant_type = models.ForeignKey('z_plant_type', blank=False, null=False, default=1, )
 
	class Meta:
		verbose_name = 'z_plant_sort'
		verbose_name_plural = 'z_plant_sorts'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_plant_ripe(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_koef = models.FloatField(null=True, blank=True, )

	class Meta:
		verbose_name = 'z_plant_ripe'
		verbose_name_plural = 'z_plant_ripes'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_plant_water(models.Model):
	c_name = models.CharField(max_length=255, null=False, default="", blank=False, )
	c_koef = models.FloatField(null=True, blank=True, )

	class Meta:
		verbose_name = 'z_plant_water'
		verbose_name_plural = 'z_plant_waters'
		unique_together = (( 'c_name', ),)
	
	def __unicode__(self):
		return getUnicode(self.c_name)

	table_group = ''


#
class z_garden_year(models.Model):
	c_year = models.DateField(null=True, blank=True, )
	z_garden = models.ForeignKey('z_garden', blank=False, null=False, default=1, )
 
	class Meta:
		verbose_name = 'z_garden_year'
		verbose_name_plural = 'z_garden_years'
		

	table_group = ''


# Many To Many Tables 
