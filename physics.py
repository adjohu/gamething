class Physics:
    GRAVITY = 9.81

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Apply(self, entity, delta_time):
        self.ApplyGravity(entity, delta_time)

    def ApplyGravity(self, entity, delta_time):
        entity.y_vel += self.GRAVITY * delta_time

    def Notify(self, event):
        ""
