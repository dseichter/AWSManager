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

import ui_aws_ec2
import ui_aws_lambda
import ui_aws_s3
import ui_aws_rds
import ui_aws_cloudfront


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

        # add the icons to the menu items of S3
        self.menuItemS3_DownloadObject.SetBitmap(icons.download_from_the_cloud.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuItemS3_DeleteObject.SetBitmap(icons.delete.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())

    def awsmanagerClose(self, event):
        self.Close()

    def awsmanagerShow(self, event):
        # check if config.json exists, if not create it, if available, update it
        settings.create_config()

        # add the version to the label
        self.SetTitle(helper.NAME + ' ' + helper.VERSION)

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

    def aws_ec2_load_details(self, event):
        ui_aws_ec2.aws_ec2_load_details(self, event)

    def aws_ec2_reload(self, event):
        ui_aws_ec2.aws_ec2_reload(self, event)

    def aws_ec2_refresh_instance(self, event):
        ui_aws_ec2.aws_ec2_refresh_instance(self, event)

    def aws_ec2_open_mgmt_console(self, event):
        ui_aws_ec2.aws_ec2_open_mgmt_console(self, event)

    def aws_ec2_change_state(self, event):
        ui_aws_ec2.aws_ec2_change_state(self, event)

    def aws_lambda_load_details(self, event):
        ui_aws_lambda.aws_lambda_load_details(self, event)

    def aws_lambda_reload(self, event):
        ui_aws_lambda.aws_lambda_reload(self, event)

    def aws_lambda_refresh_function(self, event):
        ui_aws_lambda.aws_lambda_refresh_function(self, event)

    def aws_lambda_invoke(self, event):
        ui_aws_lambda.aws_lambda_invoke(self, event)

    def aws_lambda_open_mgmt_console(self, event):
        ui_aws_lambda.aws_lambda_open_mgmt_console(self, event)

    def aws_s3_load_details(self, event):
        ui_aws_s3.aws_s3_load_details(self, event)

    def aws_s3_reload(self, event):
        ui_aws_s3.aws_s3_reload(self, event)

    def aws_s3_refresh_bucket(self, event):
        ui_aws_s3.aws_s3_refresh_bucket(self, event)

    def aws_s3_open_mgmt_console(self, event):
        ui_aws_s3.aws_s3_open_mgmt_console(self, event)

    def aws_s3_selected_key(self, event):
        ui_aws_s3.aws_s3_selected_key(self, event)

    def aws_s3_upload_file(self, event):
        ui_aws_s3.aws_s3_upload_file(self, event)

    def aws_s3_drop_file(self, event):
        ui_aws_s3.aws_s3_drop_file(self, event)

    def aws_s3_menu_download_object(self, event):
        ui_aws_s3.aws_s3_menu_download_object(self, event)

    def aws_s3_menu_delete_object(self, event):
        ui_aws_s3.aws_s3_menu_delete_object(self, event)

    def aws_rds_reload(self, event):
        ui_aws_rds.aws_rds_reload(self, event)

    def aws_cloudfront_load_details(self, event):
        ui_aws_cloudfront.aws_cloudfront_load_details(self, event)

    def aws_cloudfront_reload(self, event):
        ui_aws_cloudfront.aws_cloudfront_reload(self, event)

    def aws_cloudfront_refresh_distribution(self, event):
        ui_aws_cloudfront.aws_cloudfront_refresh_distribution(self, event)

    def aws_cloudfront_open_mgmt_console(self, event):
        ui_aws_cloudfront.aws_cloudfront_open_mgmt_console(self, event)

    def aws_cloudfront_invalidate(self, event):
        ui_aws_cloudfront.aws_cloudfront_invalidate(self, event)


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = AWSManagerFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()
