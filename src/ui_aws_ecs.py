# import the newly created GUI file
import wx
import wx.propgrid
import wx.grid

import aws_ecs
import settings
import iconsaws
import webbrowser


def aws_ecs_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    ecs_cluster = image_list.Add(
        iconsaws.arch_amazon_elastic_container_service_48.GetBitmap()
        .ConvertToImage()
        .Rescale(16, 16)
        .ConvertToBitmap()
    )
    ecs_service = image_list.Add(
        iconsaws.res_amazon_elastic_container_service_service_48.GetBitmap()
        .ConvertToImage()
        .Rescale(16, 16)
        .ConvertToBitmap()
    )
    self.treeECS.AssignImageList(image_list)
    # now, start loading the data
    clusters = aws_ecs.get_ecs_clusters(settings.read_config()["region"])
    self.treeECS.DeleteAllItems()
    root = self.treeECS.AddRoot("Clusters")
    for cluster in clusters:
        cluster_name = cluster.split("/")[1]
        item = self.treeECS.AppendItem(root, cluster_name)
        self.treeECS.SetItemImage(item, ecs_cluster, wx.TreeItemIcon_Normal)
        services = aws_ecs.get_ecs_services(
            settings.read_config()["region"], cluster_name
        )
        for service in services:
            service_name = service.split("/")[2]
            service_details = aws_ecs.get_ecs_service_details(
                settings.read_config()["region"], cluster_name, service_name
            )

            item = self.treeECS.AppendItem(
                item,
                service_name
                + " ("
                + str(service_details["services"][0]["desiredCount"])
                + "/"
                + str(service_details["services"][0]["runningCount"])
                + ")"
                + " - "
                + service_details["services"][0]["status"],
            )
            self.treeECS.SetItemImage(item, ecs_service, wx.TreeItemIcon_Normal)
    self.treeECS.ExpandAll()


def aws_ecs_load_details(self, event):
    item = self.treeECS.GetSelection()
    if not item:
        return

    # check, if the selected item is a cluster (has children)
    if self.treeECS.ItemHasChildren(self.treeECS.GetSelection()):
        return

    # now we know, that the selected item is a service
    service = self.treeECS.GetItemText(self.treeECS.GetSelection()).split(" ")[0]
    cluster = self.treeECS.GetItemText(
        self.treeECS.GetItemParent(self.treeECS.GetSelection())
    )

    service_details = aws_ecs.get_ecs_service_details(
        settings.read_config()["region"], cluster, service
    )
    self.textCtrlECS_ServiceName.SetValue(service_details["services"][0]["serviceName"])
    self.textCtrlECS_Status.SetValue(service_details["services"][0]["status"])
    self.textCtrlECS_DesiredCount.SetValue(
        str(service_details["services"][0]["desiredCount"])
    )
    self.textCtrlECS_RunningCount.SetValue(
        str(service_details["services"][0]["runningCount"])
    )
    self.textCtrlECS_PendingCount.SetValue(
        str(service_details["services"][0]["pendingCount"])
    )
    self.textCtrlECS_TaskDefinition.SetValue(
        service_details["services"][0]["taskDefinition"]
    )

    # get the tags
    self.propertyGridECS_Tags.Clear()
    # add the tags to the property grid
    if "tags" in service_details["services"][0]:
        for key, value in service_details["services"][0]["tags"].items():
            self.propertyGridECS_Tags.Append(
                wx.propgrid.StringProperty(key, key, value)
            )
        self.propertyGridECS_Tags.Refresh()

    serviceevents = service_details["services"][0]["events"]
    # load the events of the service
    self.gridECS_Events.ClearGrid()
    self.gridECS_Events.DeleteRows(0, self.gridECS_Events.GetNumberRows())
    self.gridECS_Events.AppendRows(len(serviceevents))
    for i, serviceevent in enumerate(serviceevents):
        self.gridECS_Events.SetCellValue(i, 0, str(serviceevent["createdAt"]))
        self.gridECS_Events.SetCellValue(i, 1, serviceevent["message"])
    self.gridECS_Events.AutoSizeColumns()


def aws_ecs_refresh_service(self, event):
    aws_ecs_load_details(self, event)


def aws_ec2_change_desiredcount(self, event):
    # get the selected item
    item = self.treeECS.GetSelection()
    if not item:
        return

    # check, if the selected item is a cluster (has children)
    if self.treeECS.ItemHasChildren(self.treeECS.GetSelection()):
        return

    # now we know, that the selected item is a service
    service = self.treeECS.GetItemText(self.treeECS.GetSelection()).split(" ")[0]
    cluster = self.treeECS.GetItemText(
        self.treeECS.GetItemParent(self.treeECS.GetSelection())
    )

    desired_count_current = self.textCtrlECS_DesiredCount.GetValue()

    # open a dialog and ask the user for the desired count
    dlg = wx.TextEntryDialog(
        self,
        "Please enter the desired count for the service",
        "Desired Count",
        value=desired_count_current,
    )
    dlg.SetMaxLength(2)

    # Accept only integers
    if dlg.ShowModal() == wx.ID_OK:
        desired_count_new = int(dlg.GetValue())

        if desired_count_current != desired_count_new:
            aws_ecs.set_ecs_desired_count(
                settings.read_config()["region"], cluster, service, desired_count_new
            )

        aws_ecs_load_details(self, event)
    dlg.Destroy()


def aws_ecs_open_mgmt_console(self, event):
    item = self.treeECS.GetSelection()
    if not item:
        return

    # check, if the selected item is a cluster (has children)
    if self.treeECS.ItemHasChildren(self.treeECS.GetSelection()):
        return

    # now we know, that the selected item is a service
    service = self.treeECS.GetItemText(self.treeECS.GetSelection()).split(" ")[0]
    cluster = self.treeECS.GetItemText(
        self.treeECS.GetItemParent(self.treeECS.GetSelection())
    )

    if service and cluster:
        webbrowser.open_new_tab(
            "https://"
            + settings.read_config()["region"]
            + ".console.aws.amazon.com/ecs/home?region="
            + settings.read_config()["region"]
            + "#/clusters/"
            + cluster
            + "/services/"
            + service
        )
