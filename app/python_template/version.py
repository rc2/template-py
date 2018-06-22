import os

package_folder = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(package_folder, 'VERSION')
VERSION = open(path).read()
