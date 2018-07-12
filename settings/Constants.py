from selenium import webdriver
import ConfigParser


class Constants:
    cfg = ConfigParser.ConfigParser ()
    cfg.read('config.ini')
    pathDriverFirefox = cfg.get('driver', 'pathFirefox')
    pathDriverChrome = cfg.get('driver', 'pathChrome')
