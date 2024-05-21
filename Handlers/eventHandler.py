import pygame


class eventHandler:

    def __init__(self):
        # TODO rename this
        # You may add build-in events here idk if it will work but i hope they will :3
        self.eventList = {}

    def handleEvents(self, events):

        for event in events:
            try:
                self.eventList[event.type]()
            except Exception as e:
                pass
                # print(f"An error {e} occured in event handler")

    def register(self, function, event):
        self.eventList[event] = function
