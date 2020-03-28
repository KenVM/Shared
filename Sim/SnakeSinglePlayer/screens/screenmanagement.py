from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

# Singleton used for this class
class ScreenManagement(ScreenManager):
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        #print("get instance screen management")
        if ScreenManagement.__instance == None:
            ScreenManagement()
        return ScreenManagement.__instance

    def __init__(self, **kwargs):
        print("initialize screen management")
        super().__init__(**kwargs)
        if ScreenManagement.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ScreenManagement.__instance = self
            ScreenManagement.speed = 1
