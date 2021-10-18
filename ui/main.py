
"""
main UI module of rhino_awesome_pave.
"""

import System
import Eto.Forms as forms
import Eto.Drawing as drawing

from imp import reload

import pavetab
reload(pavetab)

###

class Form(forms.Form):
    
    # Initializer
    def __init__(self):
        # basic style
        self.Title = "rhino_awesome_pave"
        self.Padding = drawing.Padding(10)
        self.Resizable = True
        # state management
        self.tab_count = 0
        # content
        self.Content = self.Create()
    
    # Create the dialog content
    def Create(self):
        # create default tab
        self.TabControl = forms.TabControl()
        self.TabControl.TabPosition = forms.DockPosition.Top
        self.CreateTab()
        # create stack layout item for tabs
        tab_items = forms.StackLayoutItem(self.TabControl, True)
        # create layout for buttons
        button_layout = forms.StackLayout()
        button_layout.Orientation = forms.Orientation.Horizontal
        button_layout.Items.Add(None)
        button_layout.Items.Add(self.AddTab())
        button_layout.Items.Add(self.RemoveTab())
        button_layout.Items.Add(None)
        # create stack layout for content
        layout = forms.StackLayout()
        layout.Spacing = 5
        layout.HorizontalContentAlignment = forms.HorizontalAlignment.Stretch
        # add the stuff above to this layout
        layout.Items.Add(button_layout)
        layout.Items.Add(tab_items)
        return layout
    
    # add a new tab to self.TabControl
    def CreateTab(self):
        self.tab_count += 1
        tab = pavetab.Form( str(self.tab_count) )
        self.TabControl.Pages.Add(tab)
    
    # AddTab button click handler
    def AddTabClick(self, sender, e):
        print( self.TabControl.Pages[0].Text )
        self.CreateTab()
    
    # Creates an add tab button
    def AddTab(self):
        button = forms.Button()
        button.Text = "New Pave"
        button.Click += self.AddTabClick
        return button
    
    # RemoveTab button click handler
    def RemoveTabClick(self, sender, e):
        if (self.TabControl.SelectedIndex >= 0 and self.TabControl.Pages.Count > 0):
            self.TabControl.Pages.RemoveAt(self.TabControl.SelectedIndex)
    
    # Creates a remove tab button
    def RemoveTab(self):
        button = forms.Button()
        button.Text = "Delete Pave"
        button.Click += self.RemoveTabClick
        return button