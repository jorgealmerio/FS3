# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FieldStatsDialog
                                 A QGIS plugin
 Generate basic statistic for numeric and text field in a vector layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-05-17
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Orden Aitchedji, Mckenna Duzac,
                                           Andreas Foulk, Tanner Lee
        email                : afoulk@mines.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'fs_3_dialog_base.ui'))


class FieldStatsDialog(QtWidgets.QMainWindow, FORM_CLASS):
    """
    Set up the user interface from Designer.
    After setupUI you can access any designer object by doing
    self.<objectname>, and you can use autoconnect slots - see
    http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
    #widgets-and-dialogs-with-auto-connect
    """
    def __init__(self, parent=None):
        super(FieldStatsDialog, self).__init__(parent)
        self.setupUi(self)
