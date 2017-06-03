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
	defaults = sublime.load_settings('Default.sublime-settings')
	settings = sublime.load_settings('Unity3DReference.sublime-settings')
	platform = sublime.platform()

	use_local_url = settings.get('use_local_url', defaults.get('use_local_url'))
	local_url = settings.get('local_url', defaults.get('local_url'))
	default_url = 'http://docs.unity3d.com/ScriptReference/30_search.html'

	default_browser = settings.get('default_browser', defaults.get('default_browser'))
	if default_browser:
		if platform == 'osx':
			browser_path = 'open -a ' + "\"%s\"" % default_browser
		else:
			browser_path = "\"%s\"" % default_browser
		browser_path += ' %s'
		open_new_tab = webbrowser.get(browser_path).open_new_tab
	else:
		open_new_tab = webbrowser.open_new_tab

	url = use_local_url and local_url or default_url

	open_new_tab(url + '?q={0}'.format(data))
