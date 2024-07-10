# import the newly created GUI file
import wx

import aws_ecs
import settings
import iconsaws


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
    self.gridECS_Events.AppendRows(len(serviceevents))
    self.gridEC2_Volumes.SetColLabelSize(18)
    # add six columns to the grid
    self.gridEC2_Volumes.SetColLabelValue(0, "Timestamp")
    self.gridEC2_Volumes.SetColLabelValue(1, "Message")
    for i, serviceevent in enumerate(serviceevents):
        self.gridECS_Events.SetCellValue(i, 0, str(serviceevent["createdAt"]))
        self.gridECS_Events.SetCellValue(i, 1, serviceevent["message"])
    self.gridECS_Events.AutoSizeColumns()


def aws_ecs_refresh_service(self, event):
    print("Implement me: refresh service")


def aws_ec2_change_desiredcount(self, event):
    print("Implement me: change desired count")


def aws_ecs_open_mgmt_console(self, event):
    print("Implement me: open management console")
