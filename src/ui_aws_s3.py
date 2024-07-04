# import the newly created GUI file
import wx

import aws_s3
import settings
import iconsaws
import webbrowser

NEWKEY_DEFAULT = 'Select an object or key to upload a new file.'
NEWFILE_DEFAULT = 'Drag and drop a file here to upload it to the selected key.'


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
        item = self.treeS3.AppendItem(root, bucket_name)
        self.treeS3.SetItemImage(item, s3_buckets, wx.TreeItemIcon_Normal)
    self.treeS3.ExpandAll()


# Load all details
def aws_s3_load_details(self, event):
    def add_paths_to_tree_ctrl(treectrl, paths):
        root = treectrl.GetRootItem()
        if not root:  # If there's no root item, create one.
            root = treectrl.AddRoot("Root")

        for path in paths:
            components = path.split('/')
            parent = root
            for component in components:
                parent = find_or_create_node(treectrl, parent, component)

    def find_or_create_node(treectrl, parent, component):
        child, cookie = treectrl.GetFirstChild(parent)
        while child.IsOk():
            if treectrl.GetItemText(child) == component:
                return child
            child, cookie = treectrl.GetNextChild(parent, cookie)

        # If the component does not exist, create it.
        return treectrl.AppendItem(parent, component)

    # get the selected item
    item = self.treeS3.GetSelection()
    if not item:
        return
    # get the text of the selected item
    bucket_name = self.treeS3.GetItemText(item)
    # get the bucket name
    self.textCtrlS3_Details_BucketName.SetValue(bucket_name)

    # load the objects of the bucket
    objects = aws_s3.get_s3_bucket_objects(settings.read_config()['region'], bucket_name)
    # clear the tree control
    self.treeCtrlS3_Objects.DeleteAllItems()
    self.treeCtrlS3_Objects.AddRoot('/')
    for obj in objects:
        object_name = obj['Key']
        add_paths_to_tree_ctrl(self.treeCtrlS3_Objects, [object_name])

    self.treeCtrlS3_Objects.ExpandAll()


def aws_s3_selected_key(self, event):
    # get the selected item
    item = self.treeCtrlS3_Objects.GetSelection()
    if not item:
        return
    # read the full path of the selected item
    path = []
    while item:
        path.insert(0, self.treeCtrlS3_Objects.GetItemText(item))
        item = self.treeCtrlS3_Objects.GetItemParent(item)
    text = '/'.join(path)
    # remove all leading slashes
    text = text.lstrip('/')

    # if the item has a child node, add a / at the end, because this is a folder
    if self.treeCtrlS3_Objects.ItemHasChildren(self.treeCtrlS3_Objects.GetSelection()):
        text += '/'

    self.textCtrlS3_SelectedKey.SetLabel(text)


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


def aws_s3_upload_file(self, event):
    # check first, if default text is still in the text control. If so, show a message box and return
    if self.staticTextS3_Upload_DragZone.GetLabel() == NEWFILE_DEFAULT or self.textCtrlS3_SelectedKey.GetValue() == NEWKEY_DEFAULT:
        wx.MessageBox("Please drop a file and select/enter a key before uploading.", "Warning", wx.OK | wx.ICON_WARNING)
        return

    # if both are set, upload the file
    aws_s3.upload_file(settings.read_config()['region'], self.textCtrlS3_Details_BucketName.GetValue(), self.staticTextS3_Upload_DragZone.GetLabel(), self.textCtrlS3_SelectedKey.GetValue())
    # show a message box that the file was uploaded
    wx.MessageBox("File uploaded successfully.", "Success", wx.OK | wx.ICON_INFORMATION)
    # clear the text control
    self.staticTextS3_Upload_DragZone.SetLabel(NEWFILE_DEFAULT)
    self.textCtrlS3_SelectedKey.SetValue(NEWKEY_DEFAULT)
    # refresh the bucket
    aws_s3_load_details(self, event)


def aws_s3_drop_file(self, event):
    # read the dropped file
    file_path = event.GetFiles()[0]
    # show the file in the static text
    self.staticTextS3_Upload_DragZone.SetLabel(file_path)
