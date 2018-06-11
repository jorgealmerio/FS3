"""
generic header
"""
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'graphOptions.ui'))

class GraphOptionsWindow(QDialog, FORM_CLASS):
    """
    generic docstring
    """
    def __init__(self, parent=None):
        super(GraphOptionsWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Graph Options")
