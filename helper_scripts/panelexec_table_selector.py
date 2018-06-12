# me - this DAT
# panelValue - the PanelValue object that changed
# 
# Make sure the corresponding toggle is enabled in the Panel Execute DAT.

ref		= op('../null_attr')

def onOffToOn(panelValue):
	active_cell 		= parent().panel.celloverid.val
	parent().store('active_cell', active_cell)
	
	lookup_val 				= active_cell + 1
	lookup_op				= op(ref[lookup_val,'path'].val + '/base_workspace')
	target_pane 			= ui.panes[1]
	target_pane.owner 		= lookup_op
	target_pane.home()
	
	return

def whileOn(panelValue):
	return

def onOnToOff(panelValue):
	return

def whileOff(panelValue):
	return

def onValueChange(panelValue):
	return
	