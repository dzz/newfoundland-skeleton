from Newfoundland import Camera, Controllers, Player, Floor, BaseGame

class Game( BaseGame ):

    def initialize(self):
        self.camera         = self.create_tickable( Camera( p = [0.0,0.0], zoom = 0.5 ) )
        self.controllers    = self.create_tickable( Controllers() )
        self.player         = self.create_tickable( Player( controllers = self.controllers ) )
        self.floor          = self.create_tickable( Floor( width = 200, height = 200, camera = self.camera, player = self.player ) )

    def render(self):
        self.floor.render()

    def tick(self):
        BaseGame.tick(self)

