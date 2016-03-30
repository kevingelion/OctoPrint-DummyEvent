# coding=utf-8
from __future__ import absolute_import

__author__ = "Kevin Murphy <kevin@voxel8.co>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2015 Kevin Murphy - Released under terms of the AGPLv3 License"

import octoprint.plugin
import flask
import os
from subprocess import Popen, call
import signal
import linecache
import psutil
import time
from octoprint.events import eventManager, Events

Events.DUMMY_EVENT = "ScheduledReboot"

class DummyEventPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.SimpleApiPlugin):

    def get_assets(self):
        return {
            "js": ["js/dummyevent.js"]
        }

    def get_api_commands(self):
        return dict(
            fire_event=[]
        )

    def on_api_command(self, command, data):
    	if command == "fire_event":
            eventManager().fire(Events.DUMMY_EVENT)
    	else:
    	    self._logger.info("Uknown command.")

    def on_api_get(self, request):
        return flask.make_response("Not found", 404)

    def get_template_configs(self):
        return [
            dict(type="settings", name="DummyEvent", data_bind="visible: true"),
	    ]

    def get_update_information(self):
        return dict(
            dummyevent_plugin=dict(
                displayName="DummyEvent Plugin",
                displayVersion=self._plugin_version,
                type="github_commit",
                user="kevingelion",
                repo="OctoPrint-DummyEvent",
                current=self._plugin_version,
                pip="https://github.com/kevingelion/OctoPrint-DummyEvent/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Dummy Event Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = DummyEventPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
