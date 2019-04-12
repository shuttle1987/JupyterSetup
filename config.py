# Disable the auto completion of quotes and brackets
# https://www.customprogrammingsolutions.com/tutorial/2019-03-24/configuring-jupyter-auto-completion/
from notebook.services.config import ConfigManager
c = ConfigManager()
c.update('notebook', {"CodeCell": {"cm_config": {"autoCloseBrackets": False}}})

