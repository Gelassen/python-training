import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import importlib
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of watcher.py
main_project_dir = os.path.dirname(os.path.dirname(current_dir))  # Goes up to main-project
common_module_path = os.path.join(main_project_dir, '../common-module/src')  # Adjust to common-modul

sys.path.insert(0, os.path.abspath(common_module_path))

import common_module

class ModuleWatcher:
    # def __init__(self):
    #     # Dynamically get the path to the common-module by navigating up and joining paths
    #     current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of watcher.py
    #     main_project_dir = os.path.dirname(os.path.dirname(current_dir))  # Goes up to main-project
    #     common_module_path = os.path.join(main_project_dir, '../common-module/src')  # Adjust to common-module

    #     # Insert the common-module/src directory into sys.path
    #     sys.path.insert(0, os.path.abspath(common_module_path))

    #     # Import the common module
    #     import common_module
    #     self.common_module = common_module
    #     self.common_module_path = os.path.abspath(common_module_path)

    def start_watching(self):
        # Set path to the 'common-module/src' directory
        path = self.common_module_path
        event_handler = self.ChangeHandler(self.common_module)

        observer = Observer()
        observer.schedule(event_handler, path, recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    class ChangeHandler(FileSystemEventHandler):
        def __init__(self, module):
            self.module = module

        def on_modified(self, event):
            # Check if the modified file is in the common-module/src directory
            if event.src_path.endswith("common_module.py"):  # Adjust based on your module structure
                importlib.reload(self.module)
                print("Reloaded common_module")


if __name__ == "__main__":
    watcher = ModuleWatcher()
    watcher.start_watching()
