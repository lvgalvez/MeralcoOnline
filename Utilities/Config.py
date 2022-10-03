import time
from pathlib import Path

import os
wait_time = 30
meralco_online = "https://fuat-meralco.cs73.force.com/customers/s/splash"
yopmail = "https://yopmail.com/en/"
cxe_apply = "https://fuat-meralco.cs73.force.com/customers/s/cxe-apply"
root_dir = Path(__file__).parent

# screenshot folder
stamp = time.strftime("%Y%m%d_%H%M%S")

screenshot_folder = f"{root_dir.parent}\\Screenshots\\"
