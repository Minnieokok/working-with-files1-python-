import os,sys
from payment import pay_detail
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))
def course():
    print("this is my course file")
pay_detail.payment()