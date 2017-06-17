from Newfoundland.Camera import Camera
from Newfoundland.Controllers import Controllers
from Newfoundland.Player import Player
from Newfoundland.Floor import Floor
from Newfoundland.BaseGame import BaseGame

class Game( BaseGame ):

    def initialize(self):
        self.camera         = self.create_tickable( Camera( p = [0.0,0.0], zoom = 0.25 ) )
        self.controllers    = self.create_tickable( Controllers() )
        self.player         = Player( controllers = self.controllers ) 
        self.floor          = self.create_tickable( Floor( width = 64, height = 64, camera = self.camera, player = self.player ) )

        self.player.p = [ -4,-4 ]
        self.camera.p = self.player.p

    def render(self):
        self.floor.render()

    def tick(self):
        BaseGame.tick(self)

