class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        print "registered listener", listener
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def Post(self, event):
        for listener in self.listeners.keys():
            listener.Notify(event)
