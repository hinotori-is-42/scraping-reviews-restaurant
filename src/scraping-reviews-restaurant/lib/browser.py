from playwright.sync_api import sync_playwright


class Browser :

    def __init__( self , head = False ) :
        self.playwright = sync_playwright().start() 
        self.browser = self.playwright.chromium.launch(headless=( not head ))

    def __getattr__( self , attr ):
        return getattr( self.browser, attr )

    def close( self ):
        if self.browser :
            self.browser.close()
            self.browser = None
        if self.playwright :
            self.playwright.stop()
            self.playwright = None

    def __del__( self ):
        self.close()
