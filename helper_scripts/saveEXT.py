def save(current_touch_comp):
	external 			= current_touch_comp.par.externaltox.val
	external_path 		= '{project}/{tox}'.format( project=project.folder, tox = external)
	default_ui_color 	= ui.colors['worksheet.bg']
	saveing_color 		= (0.314, 0, 0.1736)
	delay_script 		= "ui.colors['worksheet.bg'] = args[0]"
	message_buttons 	= ['Cancel', 'Continue']
	message_title 		= 'Save Warning'
	message 			= "You're about to save over an existing TOX"

	if ".tox" in external:
		# save external test

		save_test = ui.messageBox(message_title, message, buttons=message_buttons)
		if save_test:
			# change the bg color 
			ui.colors['worksheet.bg'] = saveing_color

			# save tox
			op(current_touch_comp).save(external_path)
			print("{} saved".format(external))

			# return ui to default color
			run(delay_script, default_ui_color, delayFrames = 1)
		else:
			pass
	else:
		pass
	return
