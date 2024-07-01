# import the newly created GUI file
import wx
import wx.propgrid
import wx.grid

import aws_ec2
import settings
import iconsaws


# def aws_ec2_load_details( self, event ):
#     ui_aws_ec2.aws_ec2_load_details(self, event)

# def aws_ec2_reload(self, event):
#     ui_aws_ec2.aws_ec2_reload(self, event)

# def aws_ec2_refresh_instance( self, event ):
#     ui_aws_ec2.aws_ec2_refresh_instance(self, event)

# def aws_ec2_open_mgmt_console( self, event ):
#     ui_aws_ec2.aws_ec2_open_mgmt_console(self, event)

# def aws_ec2_change_state( self, event ):
#     ui_aws_ec2.aws_ec2_change_state(self, event)

def aws_ec2_load_details(self, event):
    # get the selected item
    item = self.treeEC2.GetSelection()
    if item:
        ec2_instance = aws_ec2.get_ec2_instance(settings.read_config()['region'], self.treeEC2.GetItemText(item).split(' ')[0])
        # add all information to the text control
        self.textCtrlEC2_InstanceId.SetValue(ec2_instance.get('InstanceId', ''))
        self.textCtrlEC2_ImageId.SetValue(ec2_instance.get('ImageId', ''))
        self.textCtrlEC2_InstanceType.SetValue(ec2_instance.get('InstanceType', ''))
        self.textCtrlEC2_State.SetValue(ec2_instance['State']['Name'])
        self.textCtrlEC2_LaunchTime.SetValue(str(ec2_instance.get('LaunchTime', '')))
        self.textCtrlEC2_PrivateIpAddress.SetValue(ec2_instance.get('PrivateIpAddress', ''))
        self.textCtrlEC2_PublicIpAddress.SetValue(ec2_instance.get('PublicIpAddress', ''))
        self.textCtrlEC2_Architecture.SetValue(ec2_instance.get('Architecture', ''))
        # get the tags
        self.propertyGridEC2_tags.Clear()
        # add the tags to the property grid
        for tag in ec2_instance['Tags']:
            self.propertyGridEC2_tags.Append(wx.propgrid.StringProperty(tag['Key'], tag['Value']))
        self.propertyGridEC2_tags.Refresh()
        # get volume information and add it to the grid
        self.gridEC2_Volumes.ClearGrid()
        volumes = ec2_instance['BlockDeviceMappings']
        self.gridEC2_Volumes.AppendRows(len(volumes))
        self.gridEC2_Volumes.SetColLabelValue(0, 'Volume ID')
        self.gridEC2_Volumes.SetColLabelValue(1, 'Device')
        self.gridEC2_Volumes.SetColLabelValue(2, 'Type')
        self.gridEC2_Volumes.SetColLabelValue(3, 'Size')
        self.gridEC2_Volumes.SetColLabelValue(4, 'IOPS')
        self.gridEC2_Volumes.SetColLabelValue(5, 'Throughput')
        for i, volume in enumerate(volumes):
            volume_information = aws_ec2.get_ec2_volume(settings.read_config()['region'], volume['Ebs'].get('VolumeId', ''))
            self.gridEC2_Volumes.SetCellValue(i, 0, volume_information.get('VolumeId', ''))
            self.gridEC2_Volumes.SetCellValue(i, 1, volume_information.get('Device', ''))
            self.gridEC2_Volumes.SetCellValue(i, 2, volume_information.get('VolumeType', ''))
            self.gridEC2_Volumes.SetCellValue(i, 3, volume_information.get('Size', ''))
            self.gridEC2_Volumes.SetCellValue(i, 4, volume_information.get('Iops', ''))
            self.gridEC2_Volumes.SetCellValue(i, 5, volume_information.get('Throughput', '0'))
        self.gridEC2_Volumes.AutoSizeColumns()


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
