from logging import getLogger

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from pylons import config

log = getLogger(__name__)

class Api_HarvestPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'api_harvest')

    def before_map(self, map):
	map.connect('/api_harvest/stop_job',
		controller='ckanext.api_harvest.controller:Resource_api_harvestController',
		action='stop_job')
	map.connect('/api_harvest/create_job',
		controller='ckanext.api_harvest.controller:Resource_api_harvestController',
		action='create_job')
	map.connect('/api_harvest/run_job',
		controller='ckanext.api_harvest.controller:Resource_api_harvestController',
		action='run_job')
	return map

