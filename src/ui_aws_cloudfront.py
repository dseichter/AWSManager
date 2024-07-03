# import the newly created GUI file
import wx
import wx.propgrid

import aws_cloudfront
import settings
import iconsaws
import webbrowser


def aws_cloudfront_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    cloudfront_distribution = image_list.Add(iconsaws.arch_amazon_cloudfront_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    self.treeCloudfront.AssignImageList(image_list)
    # now, start loading the data
    distributions = aws_cloudfront.get_cloudfront_distributions()
    self.treeCloudfront.DeleteAllItems()
    root = self.treeCloudfront.AddRoot('Distributions')
    for distribution in distributions:
        distribution_id = distribution['Id']
        distribution_status = distribution['Status']
        distribution_domain_name = distribution['DomainName']
        item = self.treeCloudfront.AppendItem(root, distribution_id + ' (' + distribution_status + ') - ' + distribution_domain_name)
        self.treeCloudfront.SetItemImage(item, cloudfront_distribution, wx.TreeItemIcon_Normal)
    self.treeCloudfront.ExpandAll()


def aws_cloudfront_load_details(self, event):
    # get the selected item
    item = self.treeCloudfront.GetSelection()
    if item:
        # get the text of the selected item
        text = self.treeCloudfront.GetItemText(item)
        # get the distribution id
        distribution_id = text.split(' ')[0]
        # get the distribution details
        distribution = aws_cloudfront.get_cloudfront_distribution(distribution_id)
        # set the details in the text control
        self.textCtrlCloudfront_Id.SetValue(distribution_id)
        self.textCtrlCloudfront_Status.SetValue(distribution['Distribution']['Status'])
        self.textCtrlCloudfront_Description.SetValue(distribution['Distribution']['DistributionConfig']['Comment'])
        self.textCtrlCloudfront_DomainName.SetValue(distribution['Distribution']['DomainName'])
        self.textCtrlCloudfront_AltDomainName.SetValue(', '.join(distribution['Distribution']['DistributionConfig']['Aliases']['Items']))
        self.textCtrlCloudfront_Origins.SetValue(', '.join([origin['DomainName'] for origin in distribution['Distribution']['DistributionConfig']['Origins']['Items']]))
        # get the tags
        self.propertyGridCloudfront_Tags.Clear()
        tags = aws_cloudfront.get_cloudfront_distribution_tags(distribution['Distribution']['ARN'])
        # add the tags to the property grid
        for tag in tags['Tags']['Items']:
            self.propertyGridCloudfront_Tags.Append(wx.propgrid.StringProperty(tag['Key'], tag['Key'], tag['Value']))
        self.propertyGridCloudfront_Tags.Refresh()


def aws_cloudfront_refresh_distribution(self, event):
    aws_cloudfront_load_details(self, event)


def aws_cloudfront_open_mgmt_console(self, event):
    # get the selected item
    item = self.treeCloudfront.GetSelection()
    if item:
        # get the text of the selected item
        text = self.treeCloudfront.GetItemText(item)
        # get the distribution id
        distribution_id = text.split(' ')[0]
        # open the management console
        webbrowser.open_new_tab(f"https://us-east-1.console.aws.amazon.com/cloudfront/v4/home?region=us-east-1#/distributions/{distribution_id}")


def aws_cloudfront_invalidate(self, event):
    # create a small dialog to ask the user for the paths to invalidate
    dlg = wx.TextEntryDialog(self, 'Enter the paths to invalidate separated by a comma:', 'Invalidate paths', '/*', style=wx.TextEntryDialogStyle | wx.TE_MULTILINE)
    if dlg.ShowModal() == wx.ID_OK:
        paths = dlg.GetValue().split(',')
        # get the selected item
        item = self.treeCloudfront.GetSelection()
        if item:
            # get the text of the selected item
            text = self.treeCloudfront.GetItemText(item)
            # get the distribution id
            distribution_id = text.split(' ')[0]
            # invalidate the distribution
            response = aws_cloudfront.invalidate_cloudfront_distribution(distribution_id, paths)
            # show the response in a new dialog
            dlg_response = wx.TextEntryDialog(self, 'Invalidation response:', 'Response of Invalidation', response, style=wx.TextEntryDialogStyle | wx.TE_MULTILINE | wx.TE_DONTWRAP)
            dlg_response.ShowModal()
            dlg_response.Destroy()
    dlg.Destroy()
