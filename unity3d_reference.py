import sublime, sublime_plugin, webbrowser

class SearchScriptReferenceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		first_s = self.view.sel()[0]
		if first_s.empty():
		 	self.view.window().show_input_panel('Unity Script Reference:', '', on_done, on_change, on_cancel)
		else:
			data = self.view.substr(first_s)
			SearchFor(data)

def on_done(data):
	SearchFor(data)

def on_change(data):
	return

def on_cancel():
	return

def SearchFor(data):
	url = 'http://docs.unity3d.com/ScriptReference/30_search.html?q={0}'.format(data)
	webbrowser.open_new_tab(url)