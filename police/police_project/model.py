# -*- coding: utf-8 -*- 
import datetime
from datetime import timedelta
from openerp import models, fields, api

class PoliceDetail(models.Model): 
	_name = 'police.detail' 
	_rec_name = 'number'

	number  = fields.Char(string="Report Number")
	date    = fields.Date()
	day     = fields.Char()
	time    = fields.Char()
	road_name = fields.Many2one('road.name', string="Road Name")
	center_name = fields.Many2one('center.name', string="Center Name")
	location_name = fields.Many2one('location.name', string="Location Name")
	digital_tag = fields.Many2one('digital.tag', string="Digital Tag")
	direction_name = fields.Many2one('direction.name', string="Direction Name")
	Violation    = fields.Char(string='Time of Violation')
	Code    = fields.Char(string='Code of Police CAR')
	police_officer = fields.Char(string='Name of Police  Officer 1')
	rank_officer    = fields.Char(string='Rank Of Police Officer 1')
	name_officer_2    = fields.Char(string='Name of Police officer 2')
	rank_officer_2    = fields.Char(string='Rank of police officer 2')
	receiving_party = fields.Many2one('receiving.party', string="Receiving Party")
	receiving_party_rank = fields.Many2one('receiving.party.rank', string="Receiving Party Rank")
	type_case = fields.Many2one('type.case', string="Case Type")
	case_detail   = fields.Text(string='Case details ')
	party_link = fields.One2many('party.detail',"main_class",string="Party Detail")

	def confirm():
		pass

	@api.model
	def create(self, vals):
		vals['number'] = self.env['ir.sequence'].next_by_code('rec.number')
		new_record = super(PoliceDetail, self).create(vals)
		return new_record

	@api.onchange('date')
	def _change_daytime(self):
		if self.date:
			self.day  = datetime.date.today().strftime("%A")
			self.time = ( datetime.datetime.now() + timedelta(hours=5) ).strftime("%I:%M:%S %p")




class PartyDetail(models.Model): 
	_name = 'party.detail' 

	name  = fields.Char("Driver Name")
	party = fields.Text("Party")
	car_name = fields.Char("Name of Car")
	car_color = fields.Char("Color of Car")
	car_model = fields.Char("Model of Car")
	car_plate = fields.Char("Plate Number")
	driver_country = fields.Many2one('res.country',"Nationality")
	id_num = fields.Char("ID number")
	id_type =fields.Many2one('id.type',"ID Type")
	what_found =fields.Many2one('what.found',"What we found")
	qty =fields.Char("Qty")
	accident_reason =fields.Char("Reason of accident ")
	result =fields.Char("Results")
	mean_trans =fields.Many2one('mean.trans',"Means of Transportation")
	hospital_name =fields.Many2one('hospital.name',"Name of Hospital")
	main_class = fields.Many2one('police.detail',"Party Detail")
	additional = fields.Text("Additional Details")

	previous_record  = fields.Boolean("Previous records")
	complaint_detail = fields.Boolean("Complaints Details")

	previous_record_link = fields.One2many('previous.record',"main_class",string="Rrevious Record")
	complaint_detail_link = fields.One2many('complaint.detail',"main_class",string="Complaint Detail")


class ComplaintDetail(models.Model): 
	_name = 'complaint.detail' 

	name  = fields.Char("Name")
	country = fields.Many2one('res.country',"Nationality")
	id_num = fields.Char("ID number")
	id_type =fields.Many2one('id.type',"ID Type")
	relation =fields.Char("Relation")
	what_found =fields.Char("What we found")
	qty =fields.Char("Qty")
	accident_reason =fields.Char("Reason of accident ")
	result =fields.Char("Results")
	mean_trans =fields.Many2one('mean.trans',"Means of Transportation")
	hospital_name =fields.Many2one('hospital.name',"Name of Hospital")
	
	main_class = fields.Many2one('party.detail')


class PreviousRecord(models.Model): 
	_name = 'previous.record' 
	
	ministry_name =fields.Many2one('ministry.name',"Name of Ministry")
	no_complaint = fields.Char("Number Of Complaint")
	no_complaint = fields.Char("Time of Complaint")
	date    = fields.Date()
	day     = fields.Char()

	main_class = fields.Many2one('party.detail')

	@api.onchange('date')
	def _change_daytime(self):
		if self.date:
			self.day  = datetime.date.today().strftime("%A")


class MinistryName(models.Model): 
	_name = 'ministry.name'

	name  = fields.Char(string="Name of Ministry")


class HospitalName(models.Model): 
	_name = 'hospital.name'

	name  = fields.Char(string="Name of Hospital")

class MaenTrans(models.Model): 
	_name = 'mean.trans'

	name  = fields.Char(string="Means of Transportation")

class WhatFound(models.Model): 
	_name = 'waht.found'

	name  = fields.Char(string="What we found")

class IDType(models.Model): 
	_name = 'id.type'

	name  = fields.Char(string="ID Type")

class RoadName(models.Model): 
	_name = 'road.name'

	name  = fields.Char(string="Road Name")

class CenterName(models.Model): 
	_name = 'center.name'

	name  = fields.Char(string="Center Name")

class Location(models.Model): 
	_name = 'location.name'

	name  = fields.Char(string="Location Name")


class DigitalTag(models.Model): 
	_name = 'digital.tag'

	name  = fields.Char(string="Name")

class Direction(models.Model): 
	_name = 'direction.name'

	name  = fields.Char(string="Direction")

class ReceivingParty(models.Model): 
	_name = 'receiving.party'

	name  = fields.Char(string="Receiving Party")

class ReceivingPartyRank(models.Model): 
	_name = 'receiving.party.rank'

	name  = fields.Char(string="Receiving Party Rank")

class TypeOfCase(models.Model): 
	_name = 'type.case'

	name  = fields.Char(string="Type of Case")