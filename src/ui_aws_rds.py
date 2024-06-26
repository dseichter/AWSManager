# import the newly created GUI file
import wx

import aws_rds
import settings
import iconsaws


def aws_rds_reload(self, event):
    # first, create the icons for the tree and assign them to the tree
    image_list = wx.ImageList(16, 16)
    rds_database = image_list.Add(iconsaws.arch_amazon_rds_48.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
    self.treeRDS.AssignImageList(image_list)
    # now, start loading the data
    databases = aws_rds.get_rds_databases(settings.read_config()['region'])
    self.treeRDS.DeleteAllItems()
    root = self.treeRDS.AddRoot('Databases')
    for database in databases:
        database_name = database['DBName']
        database_engine = database['Engine']
        database_status = database['DBInstanceStatus']
        item = self.treeRDS.AppendItem(root, database_name + ' (' + database_engine + ') - ' + database_status)
        self.treeRDS.SetItemImage(item, rds_database, wx.TreeItemIcon_Normal)
    self.treeRDS.ExpandAll()
