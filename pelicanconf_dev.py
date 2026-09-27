# Development configuration - extends pelicanconf.py
import sys
import os

# Import base config
sys.path.insert(0, os.path.dirname(__file__))
from pelicanconf import *

# Override for local development
SITEURL = "http://localhost:8000"
FEED_DOMAIN = "http://localhost:8000"
RELATIVE_URLS = False
