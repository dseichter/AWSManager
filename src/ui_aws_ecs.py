# import the newly created GUI file
import wx

import aws_ecs
import settings
import iconsaws


def aws_ecs_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    ecs_cluster = image_list.Add(iconsaws.arch_amazon_elastic_container_service_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    ecs_service = image_list.Add(iconsaws.res_amazon_elastic_container_service_service_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    self.treeECS.AssignImageList(image_list)
    # now, start loading the data
    clusters = aws_ecs.get_ecs_clusters(settings.read_config()['region'])
    self.treeECS.DeleteAllItems()
    root = self.treeECS.AddRoot('Clusters')
    for cluster in clusters:
        cluster_name = cluster.split('/')[1]
        item = self.treeECS.AppendItem(root, cluster_name)
        self.treeECS.SetItemImage(item, ecs_cluster, wx.TreeItemIcon_Normal)
        services = aws_ecs.get_ecs_services(settings.read_config()['region'], cluster_name)
        for service in services:
            service_name = service.split('/')[2]
            service_details = aws_ecs.get_ecs_service_details(settings.read_config()['region'], cluster_name, service_name)
            item = self.treeECS.AppendItem(item, service_name + ' (' + str(service_details['services'][0]['desiredCount']) + '/' + str(service_details['services'][0]['runningCount']) + ')' + ' - ' + service_details['services'][0]['status'])
            self.treeECS.SetItemImage(item, ecs_service, wx.TreeItemIcon_Normal)
    self.treeECS.ExpandAll()
