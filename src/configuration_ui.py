# importing wx files
import wx
# import the newly created GUI file
import gui

# import workdir specific libraries
import settings
import icons


class DialogConfiguration(gui.dialogConfiguration):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogConfiguration.__init__(self, parent)

        # specify all the icons
        gui.dialogAbout.SetIcon(self, icons.settings.GetIcon())

    def showConfig(self, event):
        # get the config
        config = settings.read_config()
        # set the values
        self.textAwsAccessKeyId.SetValue(config['aws_access_key_id'])
        self.textAwsSecretAccessKey.SetValue(config['aws_secret_access_key'])
        self.textAwsSessionToken.SetValue(config['aws_session_token'])
        self.comboBoxAwsProfile.SetValue(config['aws_profile'])
        self.comboBoxAwsRegion.SetValue(config['region'])

        self.Layout()
        self.Fit()

    def saveConfig(self, event):
        # save the config
        settings.save_config('aws_access_key_id', self.textAwsAccessKeyId.GetValue())
        settings.save_config('aws_secret_access_key', self.textAwsSecretAccessKey.GetValue())
        settings.save_config('aws_session_token', self.textAwsSessionToken.GetValue())
        settings.save_config('aws_profile', self.comboBoxAwsProfile.GetValue())
        settings.save_config('region', self.comboBoxAwsRegion.GetValue())
        # close the dialog
        self.Close()

    def closeConfig(self, event):
        self.Close()
