# import the newly created GUI file
import wx

import aws_s3
import settings
import iconsaws


def aws_s3_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    s3_buckets = image_list.Add(iconsaws.arch_amazon_simple_storage_service_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    self.treeS3.AssignImageList(image_list)
    # now, start loading the data
    buckets = aws_s3.get_s3_buckets(settings.read_config()['region'])
    self.treeS3.DeleteAllItems()
    root = self.treeS3.AddRoot('Buckets')
    for bucket in buckets:
        bucket_name = bucket['Name']
        bucket_creation_date = bucket['CreationDate']
        item = self.treeS3.AppendItem(root, bucket_name + ' (' + bucket_creation_date.strftime('%Y-%m-%d %H:%M:%S') + ')')
        self.treeS3.SetItemImage(item, s3_buckets, wx.TreeItemIcon_Normal)
    self.treeS3.ExpandAll()
