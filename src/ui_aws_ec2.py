# import the newly created GUI file
import wx

import aws_ec2
import settings
import iconsaws


def aws_ec2_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    ec2_instance = image_list.Add(iconsaws.arch_amazon_ec2_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    self.treeEC2.AssignImageList(image_list)
    # now, start loading the data
    instances = aws_ec2.get_ec2_instances(settings.read_config()['region'])
    self.treeEC2.DeleteAllItems()
    root = self.treeEC2.AddRoot('Instances')
    for instance in instances:
        instance_id = instance['InstanceId']
        instance_state = instance['State']['Name']
        instance_type = instance['InstanceType']
        instance_name = ''
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
        item = self.treeEC2.AppendItem(root, instance_id + ' (' + instance_state + ') - ' + instance_type + ' - ' + instance_name)
        self.treeEC2.SetItemImage(item, ec2_instance, wx.TreeItemIcon_Normal)
    self.treeEC2.ExpandAll()
