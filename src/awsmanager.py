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
import icons
import iconsaws


class AWSManagerFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)

        # specify all the icons
        gui.MainFrame.SetIcon(self, icons.happy_cloud.GetIcon())
        self.menuitemFileClose.SetBitmap(icons.cancel.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemExtrasConfiguration.SetBitmap(icons.settings.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpSupport.SetBitmap(icons.get_help.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpUpdate.SetBitmap(icons.restart.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpAbout.SetBitmap(icons.info.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())

        # Add the AWS icons to all Notebook tabs
        self.m_auinotebook1.SetPageBitmap(self.m_auinotebook1.FindPage(self.panelEC2), iconsaws.arch_amazon_ec2_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.m_auinotebook1.SetPageBitmap(self.m_auinotebook1.FindPage(self.panelLambda), iconsaws.arch_aws_lambda_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.m_auinotebook1.SetPageBitmap(self.m_auinotebook1.FindPage(self.panelRDS), iconsaws.arch_amazon_rds_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.m_auinotebook1.SetPageBitmap(self.m_auinotebook1.FindPage(self.panelS3), iconsaws.arch_amazon_simple_storage_service_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.m_auinotebook1.SetPageBitmap(self.m_auinotebook1.FindPage(self.panelCloudfront), iconsaws.arch_amazon_cloudfront_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())

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
