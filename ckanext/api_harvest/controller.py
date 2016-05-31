from logging import getLogger
from ckan.lib.base import request, BaseController, abort, json, c
from ckan.plugins import toolkit

import ckan.plugins as p
import json
import pylons.config as config

import subprocess
import shlex
import os, sys

log = getLogger(__name__)

class Resource_api_harvestController(BaseController):

	def stop_job(self):
		
		if not request.method == 'GET':
			log.info("API harvest - error detected, incorrect method used in call")
			abort(405, 'Method not allowed')

		if not c.userobj:
			log.info("API harvest - error detected, need user login")
			abort(403, 'Forbidden, need user login')

		if not c.userobj.sysadmin:
			log.info("API harvest - error detected, need API-Key")
			abort(403, 'Forbidden, need API-Key')

		job_name = request.params.get('job_name','')

		if job_name == '':
			log.info("API harvest - error detected, need job_name param in get parameter")
			abort(400, 'Bad Request, need job_name param')

		config_file = config.get('ckan.api_basic.config_file','')
		
		if config_file == '':
			log.info("API harvest - error detected, config_file parameter not defined in configuration file")
			abort(403, 'Forbidden, config_file parameter not defined in configuration file')
		
		ve_route =  config.get('ckan.api_basic.virtual_evnvironment_route')

		if ve_route == '':
			log.info("API harvest - error detected, ve_route parameter not defined in configuration file")
			abort(403, 'Forbidden, ve_route parameter not defined in configuration file')

		if config.get('ckan.plugins').find(" harvest ") == -1:
			log.info("API harvest - error detected, harvest extension must be active in CKAN'")
			abort(403, 'Forbidden, harvest extension must be active in CKAN')

		log.info("API harvest - Validations ok, stop the job specified")
		subprocess.check_output(shlex.split(ve_route + '/bin/paster --plugin=ckanext-harvest harvester job_abort ' + job_name + ' --config=' + config_file), cwd=ve_route + '/src/ckan')
		
	def create_job(self):
		
		if not request.method == 'GET':
			log.info("API harvest - error detected, incorrect method used in call")
			abort(405, 'Method not allowed')

		if not c.userobj:
			log.info("API harvest - error detected, need user login")
			abort(403, 'Forbidden, need user login')

		if not c.userobj.sysadmin:
			log.info("API harvest - error detected, need API-Key")
			abort(403, 'Forbidden, need API-Key')

		job_name = request.params.get('job_name','')

		if job_name == '':
			log.info("API harvest - error detected, need job_name param in get parameter")
			abort(400, 'Bad Request, need job_name param')

		config_file = config.get('ckan.api_basic.config_file','')
		
		if config_file == '':
			log.info("API harvest - error detected, config_file parameter not defined in configuration file")
			abort(403, 'Forbidden, config_file parameter not defined in configuration file')
		
		ve_route =  config.get('ckan.api_basic.virtual_evnvironment_route')

		if ve_route == '':
			log.info("API harvest - error detected, ve_route parameter not defined in configuration file")
			abort(403, 'Forbidden, ve_route parameter not defined in configuration file')

		if config.get('ckan.plugins').find(" harvest ") == -1:
			abort(403, 'Forbidden, harvest extension must be active in CKAN')

		log.info("API harvest - Validations ok, create the job specified")
		subprocess.check_output(shlex.split(ve_route + '/bin/paster --plugin=ckanext-harvest harvester job ' + job_name + ' --config=' + config_file), cwd=ve_route + '/src/ckan')

	def create_job_all(self):
		
		if not request.method == 'GET':
			log.info("API harvest - error detected, incorrect method used in call")
			abort(405, 'Method not allowed')

		if not c.userobj:
			log.info("API harvest - error detected, need user login")
			abort(403, 'Forbidden, need user login')

		if not c.userobj.sysadmin:
			log.info("API harvest - error detected, need API-Key")
			abort(403, 'Forbidden, need API-Key')

		config_file = config.get('ckan.api_basic.config_file','')
		
		if config_file == '':
			log.info("API harvest - error detected, config_file parameter not defined in configuration file")
			abort(403, 'Forbidden, config_file parameter not defined in configuration file')
		
		ve_route =  config.get('ckan.api_basic.virtual_evnvironment_route')

		if ve_route == '':
			log.info("API harvest - error detected, ve_route parameter not defined in configuration file")
			abort(403, 'Forbidden, ve_route parameter not defined in configuration file')

		if config.get('ckan.plugins').find(" harvest ") == -1:
			log.info("API harvest - Validations ok, create the job specified")
			abort(403, 'Forbidden, harvest extension must be active in CKAN')

		subprocess.check_output(shlex.split(ve_route + '/bin/paster --plugin=ckanext-harvest harvester job-all --config=' + config_file), cwd=ve_route + '/src/ckan')
		
	def run_job(self):
		
		if not request.method == 'GET':
			log.info("API harvest - error detected, incorrect method used in call")
			abort(405, 'Method not allowed')

		if not c.userobj:
			log.info("API harvest - error detected, need user login")
			abort(403, 'Forbidden, need user login')

		if not c.userobj.sysadmin:
			log.info("API harvest - error detected, need API-Key")
			abort(403, 'Forbidden, need API-Key')

		config_file = config.get('ckan.api_basic.config_file','')
		
		if config_file == '':
			log.info("API harvest - error detected, config_file parameter not defined in configuration file")
			abort(403, 'Forbidden, config_file parameter not defined in configuration file')
	
		ve_route =  config.get('ckan.api_basic.virtual_evnvironment_route')

		if ve_route == '':
			log.info("API harvest - error detected, ve_route parameter not defined in configuration file")
			abort(403, 'Forbidden, ve_route parameter not defined in configuration file')

		if config.get('ckan.plugins').find(" harvest ") == -1:
			log.info("API harvest - error detected, harvest extension must be active in CKAN")
			abort(403, 'Forbidden, harvest extension must be active in CKAN')

		log.info("API harvest - Validations ok, execute command run")
		subprocess.check_output(shlex.split(ve_route + '/bin/paster --plugin=ckanext-harvest harvester run --config=' + config_file), cwd=ve_route + '/src/ckan')
