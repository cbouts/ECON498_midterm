from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()