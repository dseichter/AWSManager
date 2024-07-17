# import the newly created GUI file
import wx

import aws_rds
import settings
import iconsaws
import webbrowser


def aws_rds_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    rds_database = image_list.Add(
        iconsaws.arch_amazon_rds_48.GetBitmap()
        .ConvertToImage()
        .Rescale(16, 16)
        .ConvertToBitmap()
    )
    self.treeRDS.AssignImageList(image_list)
    # now, start loading the data
    databases = aws_rds.get_rds_databases(settings.read_config()["region"])
    self.treeRDS.DeleteAllItems()
    root = self.treeRDS.AddRoot("Databases")
    for database in databases:
        database_name = database["DBInstanceIdentifier"]
        database_engine = database["Engine"]
        database_status = database["DBInstanceStatus"]
        item = self.treeRDS.AppendItem(
            root, database_name + " (" + database_engine + ") - " + database_status
        )
        self.treeRDS.SetItemImage(item, rds_database, wx.TreeItemIcon_Normal)
    self.treeRDS.ExpandAll()


def aws_rds_load_details(self, event):
    # get the selected item
    item = self.treeRDS.GetSelection()

    if item:
        rds_database = aws_rds.get_rds_database(
            settings.read_config()["region"],
            self.treeRDS.GetItemText(item).split(" ")[0],
        )
        # add all information to the text control
        self.textCtrlRDS_DBInstanceIdentifier.SetValue(
            rds_database.get("DBInstanceIdentifier", "")
        )
        self.textCtrlRDS_Engine.SetValue(rds_database.get("Engine", ""))
        self.textCtrlRDS_EngineVersion.SetValue(rds_database.get("EngineVersion", ""))
        self.textCtrlRDS_DBInstanceStatus.SetValue(
            rds_database.get("DBInstanceStatus", "")
        )
        self.textCtrlRDS_DBName.SetValue(rds_database.get("DBName", ""))
        self.textCtrlRDS_Endpoint.SetValue(
            rds_database.get("Endpoint", {}).get("Address", "")+':' + str(rds_database.get("Endpoint", {}).get("Port", ""))
        )
        self.textCtrlRDS_AllocatedStorage.SetValue(
            str(rds_database.get("AllocatedStorage", ""))
        )
        self.textCtrlRDS_MultiAZ.SetValue(str(rds_database.get("MultiAZ", "")))
        self.textCtrlRDS_PubliclyAccessible.SetValue(
            str(rds_database.get("PubliclyAccessible", ""))
        )

        # get the tags
        self.propertyGridRDS_Tags.Clear()
        # add the tags to the property grid
        for tag in rds_database["TagList"]:
            self.propertyGridRDS_Tags.Append(
                wx.propgrid.StringProperty(tag["Key"], tag["Key"], tag["Value"])
            )
        self.propertyGridRDS_Tags.Refresh()


def aws_rds_refresh_dbinstance(self, event):
    aws_rds_load_details(self, event)


def aws_rds_open_mgmt_console(self, event):
    # get the selected item
    item = self.treeRDS.GetSelection()
    if item:
        rds_database = aws_rds.get_rds_database(
            settings.read_config()["region"],
            self.treeRDS.GetItemText(item).split(" ")[0],
        )
        url = f"https://console.aws.amazon.com/rds/home?region={settings.read_config()['region']}#database:id={rds_database['DBInstanceIdentifier']}"
        webbrowser.open_new_tab(url)


def aws_rds_change_state(self, event):
    # create a small dialog to ask the user for the new state using a combobox
    states = ["start", "stop", "reboot", "delete"]

    if self.textCtrlRDS_DBInstanceStatus.GetValue() == "available":
        states.remove("start")

    if self.textCtrlRDS_DBInstanceStatus.GetValue() == "stopped":
        states.remove("stop")

    if self.textCtrlRDS_DBInstanceStatus.GetValue() == "deleting":
        states.remove("delete")

    dlg = wx.SingleChoiceDialog(
        self, "Select the new state for the database", "Change State", states
    )
    if dlg.ShowModal() == wx.ID_OK:
        selected_state = dlg.GetStringSelection()
        # perform the necessary actions based on the selected state
        if selected_state == "start":
            aws_rds.start_rds_database(
                settings.read_config()["region"],
                self.textCtrlRDS_DBInstanceIdentifier.GetValue(),
            )
        elif selected_state == "stop":
            aws_rds.stop_rds_database(
                settings.read_config()["region"],
                self.textCtrlRDS_DBInstanceIdentifier.GetValue(),
            )
        elif selected_state == "reboot":
            aws_rds.reboot_rds_database(
                settings.read_config()["region"],
                self.textCtrlRDS_DBInstanceIdentifier.GetValue(),
            )
        elif selected_state == "delete":
            aws_rds.delete_rds_database(
                settings.read_config()["region"],
                self.textCtrlRDS_DBInstanceIdentifier.GetValue(),
            )
    dlg.Destroy()
