###############################################################################
# ICE Explorer: Application for viewing and inspecting ICE cache data.
# Copyright (C) 2010  M.A. Belzile
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

from PyQt4 import QtCore, QtGui
import multiprocessing as mp

class ICEPreferences( QtGui.QDialog ):
    
    def __init__( self, parent=None ):
        super( ICEPreferences, self).__init__(parent)
        self.setWindowTitle("Preferences")

        # dialog layout
        vbox = QtGui.QVBoxLayout()      

        # process count
        hbox = QtGui.QHBoxLayout()      
        self.process_count_edit = QtGui.QLineEdit(self)
        self.process_count_edit.setValidator( QtGui.QIntValidator() )
        self.process_count_edit.setText( str(mp.cpu_count()) )
        
        label = QtGui.QLabel('Number of processes', self)
        
        hbox.addWidget(label)
        hbox.addWidget(self.process_count_edit)

        vbox.addLayout(hbox)

        # export folder
        hbox = QtGui.QHBoxLayout()      
        label = QtGui.QLabel('Export Folder', self)
        self.export_folder_edit = QtGui.QLineEdit(self)
        self.export_folder_edit.setText( r'c:\temp' )
        hbox.addWidget(label)
        hbox.addWidget(self.export_folder_edit)

        vbox.addLayout(hbox)

        # dialog buttons
        ok_btn = QtGui.QPushButton('OK', self)
        ok_btn.setDefault(True)
        ok_btn.pressed.connect( self._on_click_ok )
        
        cancel_btn = QtGui.QPushButton('Cancel', self)
        cancel_btn.pressed.connect( self._on_click_cancel )
        
        hbox = QtGui.QHBoxLayout()      
        hbox.addWidget(ok_btn)
        hbox.addWidget(cancel_btn)
        vbox.addLayout(hbox)
       
        self.setLayout(vbox)

    @property
    def process_count(self):
        return int(self.process_count_edit.text())

    @property
    def export_folder(self):
        return self.export_folder_edit.text()

    def _on_click_ok( self ):
        self.accept()
       
    def _on_click_cancel( self ):
        self.reject()
           