# import the newly created GUI file
import wx

import aws_s3
import settings
import iconsaws
import webbrowser


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


def aws_s3_load_details(self, event):
    # get the selected item
    item = self.treeS3.GetSelection()
    if not item:
        return
    # get the text of the selected item
    text = self.treeS3.GetItemText(item)
    # get the bucket name
    bucket_name = text.split(' ')[0]
    # load the objects of the bucket
    objects = aws_s3.get_s3_bucket_objects(settings.read_config()['region'], bucket_name)
    # clear the tree control
    self.treeCtrlS3_Objects.DeleteAllItems()
    root = self.treeCtrlS3_Objects.AddRoot('Objects')
    for obj in objects:
        object_name = obj['Key']
        object_size = obj['Size']
        object_last_modified = obj['LastModified']
        self.treeCtrlS3_Objects.AppendItem(root, object_name + ' (' + str(object_size) + ' bytes) - ' + object_last_modified.strftime('%Y-%m-%d %H:%M:%S'))

    self.treeCtrlS3_Objects.ExpandAll()


def aws_s3_refresh_bucket(self, event):
    aws_s3_load_details(self, event)


def aws_s3_open_mgmt_console(self, event):
    # get the selected item
    item = self.treeS3.GetSelection()
    if item:
        # get the text of the selected item
        text = self.treeS3.GetItemText(item)
        # get the bucket name
        bucket_name = text.split(' ')[0]
        # open the management console
        webbrowser.open('https://s3.console.aws.amazon.com/s3/buckets/' + bucket_name + '?region=' + settings.read_config()['region'])
