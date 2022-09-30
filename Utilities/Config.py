import time
from pathlib import Path

import os
meralco_online = "https://fuat-meralco.cs73.force.com/customers/s/splash"
yopmail = "https://yopmail.com/en/"
root_dir = Path(__file__).parent

# screenshot folder
stamp = time.strftime("%Y%m%d_%H%M%S")

screenshot_folder = f"{root_dir.parent}\\Screenshots\\"
