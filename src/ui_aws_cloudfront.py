# import the newly created GUI file
import wx

import aws_cloudfront
import settings
import iconsaws


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
