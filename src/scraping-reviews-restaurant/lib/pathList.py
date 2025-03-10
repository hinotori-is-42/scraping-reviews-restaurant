from . import browser
from abc import ABC, abstractmethod
import time


class PathList(ABC) :

    def __init__( self , head = False ) :
        self.driver = browser.Browser(head)
        self.page = self.driver.new_page()

    def get_path_list( self ):
        # 各ページのリンクを収集
        paths = list()
        while True :
            paths += self.get_paths()
            if next_element := self.next_page_element() :
                next_element.click()
                time.sleep(1)
            else :
                break
        self.close()
        return paths

    def close( self ):
        if self.driver :
            self.driver.close()
            self.driver = None
        if self.page :
            self.page = None

    @abstractmethod
    def next_page_element( self ) :
        pass

    @abstractmethod
    def get_paths( self ) :
        pass

    def __del__( self ):
        self.close()
