# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# importing wx files
import wx

# import the newly created GUI file
import gui

# import workdir specific libraries
import settings
import icons

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


class DialogConfiguration(gui.dialogConfiguration):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogConfiguration.__init__(self, parent)

        # specify all the icons
        gui.dialogAbout.SetIcon(self, icons.settings.GetIcon())

    def showConfig(self, event):
        # read all available profiles
        profiles = settings.get_profiles()
        # set the values
        self.comboBoxAwsProfile.Clear()
        self.comboBoxAwsProfile.Append(profiles)
        # read all available regions
        regions = settings.get_regions()
        # set the values
        self.comboBoxAwsDefaultRegion.Clear()
        self.comboBoxAwsDefaultRegion.Append(regions)

        # get the config
        config = settings.read_config()
        # set the values
        self.textAwsAccessKeyId.SetValue(config["aws_access_key_id"])
        self.textAwsSecretAccessKey.SetValue(config["aws_secret_access_key"])
        self.textAwsSessionToken.SetValue(config["aws_session_token"])
        self.comboBoxAwsProfile.SetValue(config["aws_profile"])
        self.comboBoxAwsDefaultRegion.SetValue(config["region"])
        self.checkBoxLoadOnStartup.SetValue(config["load_on_startup"])
        self.checkBoxCheckForUpdates.SetValue(config["check_for_updates"])
        self.textCtrlConfigLogfile.SetValue(config["logfilename"])
        self.comboBoxConfigLoglevel.SetValue(config["loglevel"])

        self.Layout()
        self.Fit()

    def saveConfig(self, event):
        # save the config
        settings.save_config("aws_access_key_id", self.textAwsAccessKeyId.GetValue())
        settings.save_config(
            "aws_secret_access_key", self.textAwsSecretAccessKey.GetValue()
        )
        settings.save_config("aws_session_token", self.textAwsSessionToken.GetValue())
        settings.save_config("aws_profile", self.comboBoxAwsProfile.GetValue())
        settings.save_config("region", self.comboBoxAwsDefaultRegion.GetValue())
        settings.save_config("load_on_startup", self.checkBoxLoadOnStartup.GetValue())
        settings.save_config("check_for_updates", self.checkBoxCheckForUpdates.GetValue())
        settings.save_config("logfilename", self.textCtrlConfigLogfile.GetValue())
        settings.save_config("loglevel", self.comboBoxConfigLoglevel.GetValue())
        # close the dialog
        self.Close()

    def closeConfig(self, event):
        self.Close()

    def reloadAwsProfiles(self, event):
        # read all available profiles
        profiles = settings.get_profiles()
        # set the values
        self.comboBoxAwsProfile.Clear()
        self.comboBoxAwsProfile.Append(profiles)
