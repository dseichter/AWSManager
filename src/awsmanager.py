# importing wx files
import wx
# import the newly created GUI file
import gui
# import common libraries
import webbrowser

# import workdir specific libraries
import about_ui
import configuration_ui
import settings
import helper


class AWSManagerFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)

    def miFileClose(self, event):
        self.Close()

    def miExtrasConfiguration(self, event):
        # open the configuration dialog
        dlg = configuration_ui.DialogConfiguration(self)
        dlg.ShowModal()
        dlg.Destroy()

    def miHelpSupport(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/AWSManager')  # Add the URL of the GitHub repository

    def miHelpUpdate(self, event):
        if helper.check_for_new_release():
            result = wx.MessageBox('A new release is available.\nWould you like to open the download page?', 'Update available', wx.YES_NO | wx.ICON_INFORMATION)
            if result == wx.YES:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            wx.MessageBox('No new release available.', 'No update', wx.OK | wx.ICON_INFORMATION)

    def miHelpAbout(self, event):
        # open the about dialog
        dlg = about_ui.DialogAbout(self)
        dlg.ShowModal()
        dlg.Destroy()



# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = AWSManagerFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()
