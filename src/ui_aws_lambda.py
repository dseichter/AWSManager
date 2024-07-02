# import the newly created GUI file
import wx

import aws_lambda
import settings
import iconsaws
import webbrowser
import json


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


def aws_lambda_load_details(self, event):
    # get the selected item
    item = self.treeLambda.GetSelection()
    if not item:
        return
    # get the text of the selected item
    text = self.treeLambda.GetItemText(item)
    # get the function name
    function_name = text.split(' ')[0]
    # get the function details
    lambdafunction = aws_lambda.get_lambda_function(settings.read_config()['region'], function_name)

    # add all information to the text control
    self.textCtrlLambda_FunctionName.SetValue(lambdafunction.get('Configuration', {}).get('FunctionName', ''))
    self.textCtrlLambda_FunctionArn.SetValue(lambdafunction.get('Configuration', {}).get('FunctionArn', ''))
    self.textCtrlLambda_Version.SetValue(lambdafunction.get('Configuration', {}).get('Version', ''))
    self.textCtrlLambda_MemorySize.SetValue(str(lambdafunction.get('Configuration', {}).get('MemorySize', '')))
    self.textCtrlLambda_Handler.SetValue(lambdafunction.get('Configuration', {}).get('Handler', ''))
    self.textCtrlLambda_Timeout.SetValue(str(lambdafunction.get('Configuration', {}).get('Timeout', '')))
    self.textCtrlLambda_Runtime.SetValue(lambdafunction.get('Configuration', {}).get('Runtime', ''))
    self.textCtrlLambda_LastModified.SetValue(str(lambdafunction.get('Configuration', {}).get('LastModified', '')))
    self.textCtrlLambda_Description.SetValue(lambdafunction.get('Configuration', {}).get('Description', ''))
    # load the environment variables
    self.propertyGridLambda_EnvVar.Clear()
    # add the environment variables to the property grid
    for key, value in lambdafunction.get('Configuration', {}).get('Environment', {}).get('Variables', {}).items():
        self.propertyGridLambda_EnvVar.Append(wx.propgrid.StringProperty(key, key, value))
    self.propertyGridLambda_EnvVar.Refresh()
    # get the tags
    self.propertyGridLambda_Tags.Clear()
    # add the tags to the property grid
    for key, value in lambdafunction.get('Tags', {}).items():
        self.propertyGridLambda_Tags.Append(wx.propgrid.StringProperty(key, key, value))
    self.propertyGridLambda_Tags.Refresh()


def aws_lambda_refresh_function(self, event):
    aws_lambda_load_details(self, event)


def aws_lambda_open_mgmt_console(self, event):
    webbrowser.open_new_tab('https://' + settings.read_config()['region'] + '.console.aws.amazon.com/lambda/home?region=' + settings.read_config()['region'] + '#/functions/' + self.textCtrlLambda_FunctionName.GetValue())


def aws_lambda_invoke(self, event):
    # get the function name
    function_name = self.textCtrlLambda_FunctionName.GetValue()

    # create a small dialog to ask the user for the payload
    dlg = wx.TextEntryDialog(self, 'Enter the payload for the function:', 'Invoke Lambda Function', '', style=wx.TextEntryDialogStyle | wx.TE_MULTILINE)
    dlg.SetSize((400, 300))
    dlg.SetMinSize((400, 300))
    # find the OK button
    ok_button = dlg.FindWindowById(wx.ID_OK)
    # change the text of the OK button
    ok_button.SetLabel('Invoke')
    if dlg.ShowModal() == wx.ID_OK:
        payload = json.dumps(dlg.GetValue())
        # invoke the function
        response = aws_lambda.invoke_lambda_function(settings.read_config()['region'], function_name, payload)
        # show the response in a new dialog
        dlg_response = wx.TextEntryDialog(self, 'Enter the payload for the function:', 'Response of Invocation', response, style=wx.TextEntryDialogStyle | wx.TE_MULTILINE | wx.TE_DONTWRAP)
        dlg_response.ShowModal()
        dlg_response.Destroy()
    dlg.Destroy()
