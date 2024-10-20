import sys
import os

class Router:

    def add_common_module(self) -> 'Router':
        print("[start] add_common_module")
        """
             Just an example how it should be imported
        """
        # Dynamically add the path to the common module
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of main.py
        project_root = os.path.dirname(os.path.dirname(current_dir))  # Goes to /project-root
        common_module_path = os.path.join(project_root, 'common-module', 'src')  # Path to common-module/src

        # Insert the common-module/src into sys.path
        sys.path.insert(0, common_module_path)

        return self

    def add_network_module(self) -> 'Router':
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of main.py
        project_root = os.path.dirname(os.path.dirname(current_dir))  # Goes to /project-root
        network_module_path = os.path.join(project_root, 'network-module', 'src')  # Path to network-module/src

        # Insert the network-module/src into sys.path
        sys.path.insert(0, network_module_path)

        return self