import pygetwindow as gw

class WindowManager:
    def focus_by_handle(self, handle):
        window = self.get_by_handle(handle)
        if window:
            window.activate()
        else:
            print(f"Window with ID {handle} not found")

    def get_active(self, keyword):
        windows = self.get_all()
        if keyword:
            windows = self.filter_by_title(windows, keyword)
        windows = self.remove_empty_titles(windows)
        windows = self.sort_by_position(windows)
        return windows
    
    def get_by_keyword(self, keyword):
         windows = gw.getAllWindows()
         return self.filter_by_title(windows, keyword)

    def get_by_handle(self, handle):
        windows = gw.getAllWindows()
        for window in windows:
            if str(window._hWnd) == str(handle):
                return window
        return None

    def get_all(self):
        windows = gw.getAllWindows()
        
        # filter out windows without title
        windows = [window for window in windows if window.title]
        
        # order by left and top position
        windows = sorted(windows, key=lambda window: window.left)
        windows = sorted(windows, key=lambda window: window.top)

        return windows

    def filter_by_title(self, windows, keyword):
        return [window for window in windows if keyword.lower() in window.title.lower()]

    def remove_empty_titles(self, windows):
        return [window for window in windows if window.title]

    def sort_by_position(self, windows):
        windows = sorted(windows, key=lambda window: window.left)
        windows = sorted(windows, key=lambda window: window.top)
        return windows