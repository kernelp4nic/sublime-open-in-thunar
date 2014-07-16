import sublime_plugin
import os
import subprocess


class ThunarCommand():
    def get_path(self, paths):
        if paths:
            return paths[0]
        elif self.window.active_view():
            return os.path.split(self.window.active_view().file_name())[0]
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            return '.'

class OpenThunarCommand(sublime_plugin.WindowCommand, ThunarCommand):
    def run(self, paths=[], parameters=None):
        subprocess.Popen(['thunar', self.get_path(paths)])
