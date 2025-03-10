from . import pathList
from urllib.parse import urljoin
import time

class PathList_ind(pathList.PathList) :

    def __init__( self , config , head = False ) :
        super().__init__( head )
        self.config = config
        self.page.goto(self.config["httpsPath"])
        time.sleep(1)

    def next_page_element( self ) :
        next_elements = self.page.locator(self.config["nextElement"])
        return next_elements if next_elements.count() > 0 else None

    def get_paths( self ) :
        return (
            [
                a.get_attribute("href")
                for a in self.page.locator(self.config["links"]).all() 
            ]
        )
