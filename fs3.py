# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:12:02 2018

@author: Tanner Lee
https://github.com/tleecsm
"""

from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from .fs3Run import FS3MainWindow

from .resources import *

class FS3Plugin:
    """
    FS3Plugin handles the linking to QGIS.
    The icon is declared here
    The plugin is loaded to the toolbar here
    And the main interface is called here
    """
    def __init__(self, iface):
        self.iface = iface
        self.mainWindow = FS3MainWindow()
        self.iconPath = ":/plugins/FS3/FS3Icon.png"
        self.icon = QIcon(self.iconPath)
        self.action = QAction(self.icon,
                              "FS3 -- FieldStats3",
                              self.iface.mainWindow())


    def initGui(self):
        """
        initGui is a required method
        Used by QGIS to make the icon and the menu items for the plugin
        """
        self.action.setObjectName("FS3 Plugin")
        self.action.setWhatsThis("Configuration for FS3")
        self.action.setStatusTip("This is a tip")
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&FS3 Plugin", self.action)


    def unload(self):
        """
        unload is a required method
        Used by QGIS to remove the plugin from the menu and toolbar
        """
        self.iface.removePluginMenu("&FS3 Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        """
        Acts as the entry point to the main program
        Creates and runs an instance of the window
        """
        print("Running!")
        self.mainWindow.show()