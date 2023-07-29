from colorama import Fore, Back, Style
from tqdm import tqdm, trange
import time
import AutoUpdate

AutoUpdate.set_url("<FILE URL HERE>")
AutoUpdate.set_download_link("<DOWNLOAD LINK HERE>")
AutoUpdate.set_current_version("0.0.1")

if not AutoUpdate.is_up_to_date():
    AutoUpdate.download("<PATH TO FILE HERE>")


print(Fore.RED + "Game name ?")
game_wanted = input()
print(game_wanted + " is being searched, please wait few seconds")
for i in tqdm([1, 2, 3, 4, 5]):
    time.sleep(0.2)
print('done')