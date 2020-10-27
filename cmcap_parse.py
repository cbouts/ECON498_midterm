from bs4 import BeautifulSoup
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


one_file_name = "html_files/coinmarketcap-----.html"
os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
