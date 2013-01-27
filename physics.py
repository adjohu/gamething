class Physics:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Apply(self, entity):
        entity.y_vel += 1

    def Notify(self, event):
        ""
