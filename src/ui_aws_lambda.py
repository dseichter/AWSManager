# import the newly created GUI file
import wx

import aws_lambda
import settings
import iconsaws


def aws_lambda_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    lambda_function = image_list.Add(iconsaws.arch_aws_lambda_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    self.treeLambda.AssignImageList(image_list)
    # now, start loading the data
    instances = aws_lambda.get_lambda_functions(settings.read_config()['region'])
    self.treeLambda.DeleteAllItems()
    root = self.treeLambda.AddRoot('Functions')
    for instance in instances:
        function_name = instance['FunctionName']
        function_runtime = instance['Runtime']
        function_handler = instance['Handler']
        function_description = instance['Description']
        item = self.treeLambda.AppendItem(root, function_name + ' (' + function_runtime + ') - ' + function_handler + ' - ' + function_description)
        self.treeLambda.SetItemImage(item, lambda_function, wx.TreeItemIcon_Normal)
    self.treeLambda.ExpandAll()
