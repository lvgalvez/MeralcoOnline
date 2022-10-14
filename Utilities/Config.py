import time
from pathlib import Path

import os
wait_time = 30
meralco_online = "https://fuat-meralco.cs73.force.com/customers/s/splash"
yopmail = "https://yopmail.com/en/"
cxe_apply = "https://fuat-meralco.cs73.force.com/customers/s/cxe-apply"
cxe = "https://meralco--fuat.lightning.force.com/lightning/page/home"
gmail = "https://mail.google.com/mail/u/0/#inbox"
outage_external_guest = "https://fuat-meralco.cs73.force.com/customers/s/outagemap"
root_dir = Path(__file__).parent

# screenshot folder
stamp = time.strftime("%Y%m%d_%H%M%S")

screenshot_folder = f"{root_dir.parent}\\Screenshots\\"
