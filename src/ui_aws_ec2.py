# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# import the newly created GUI file
import wx
import wx.propgrid
import wx.grid

import aws_ec2
import settings
import iconsaws
import webbrowser


def aws_ec2_refresh_instance(self, event):
    aws_ec2_load_details(self, event)


def aws_ec2_open_mgmt_console(self, event):
    item = self.treeEC2.GetSelection()
    if item:
        ec2_instance = aws_ec2.get_ec2_instance(settings.read_config()['region'], self.treeEC2.GetItemText(item).split(' ')[0])
        url = f"https://eu-central-1.console.aws.amazon.com/ec2/home?region={settings.read_config()['region']}#InstanceDetails:instanceId={ec2_instance['InstanceId']}"
        webbrowser.open_new_tab(url)


def aws_ec2_change_state(self, event):
    # create a small dialog to ask the user for the new state using a combobox
    states = ['start', 'stop', 'terminate', 'reboot']

    # remove the 'terminate' option if the instance is already in the 'terminated' state
    if self.textCtrlEC2_State.GetValue() == 'terminated':
        states.remove('terminate')

    # remove the 'start' option if the instance is already in the 'running' state
    if self.textCtrlEC2_State.GetValue() == 'running':
        states.remove('start')

    # remove the 'stop' option if the instance is already in the 'stopped' state
    if self.textCtrlEC2_State.GetValue() == 'stopped':
        states.remove('stop')

    dlg = wx.SingleChoiceDialog(self, 'Select the new state:', 'Change EC2 Instance State', states)
    if dlg.ShowModal() == wx.ID_OK:
        selected_state = dlg.GetStringSelection()
        # perform the necessary actions based on the selected state
        if selected_state == 'start':
            aws_ec2.start_ec2_instance(settings.read_config()['region'], self.textCtrlEC2_InstanceId.GetValue())
        elif selected_state == 'stop':
            aws_ec2.stop_ec2_instance(settings.read_config()['region'], self.textCtrlEC2_InstanceId.GetValue())
        elif selected_state == 'terminate':
            # code to terminate the EC2 instance
            aws_ec2.terminate_ec2_instance(settings.read_config()['region'], self.textCtrlEC2_InstanceId.GetValue())
        elif selected_state == 'reboot':
            # code to reboot the EC2 instance
            aws_ec2.reboot_ec2_instance(settings.read_config()['region'], self.textCtrlEC2_InstanceId.GetValue())
    dlg.Destroy()


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
        self.propertyGridEC2_Tags.Clear()
        # add the tags to the property grid
        for tag in ec2_instance['Tags']:
            self.propertyGridEC2_Tags.Append(wx.propgrid.StringProperty(tag['Key'], tag['Key'], tag['Value']))
        self.propertyGridEC2_Tags.Refresh()
        # get volume information and add it to the grid
        self.gridEC2_Volumes.ClearGrid()
        volumes = ec2_instance['BlockDeviceMappings']
        self.gridEC2_Volumes.DeleteRows(0, self.gridEC2_Volumes.GetNumberRows())
        self.gridEC2_Volumes.AppendRows(len(volumes))
        for i, volume in enumerate(volumes):
            volume_information = aws_ec2.get_ec2_volume(settings.read_config()['region'], volume['Ebs'].get('VolumeId', ''))
            self.gridEC2_Volumes.SetCellValue(i, 0, volume_information.get('VolumeId', ''))
            self.gridEC2_Volumes.SetCellValue(i, 1, volume_information['Attachments'][0].get('Device', ''))
            self.gridEC2_Volumes.SetCellValue(i, 2, volume_information.get('VolumeType', ''))
            self.gridEC2_Volumes.SetCellValue(i, 3, str(volume_information.get('Size', '0')))
            self.gridEC2_Volumes.SetCellValue(i, 4, str(volume_information.get('Iops', '0')))
            self.gridEC2_Volumes.SetCellValue(i, 5, str(volume_information.get('Throughput', '0')))
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
