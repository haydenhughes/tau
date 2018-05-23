import pyglet


class Renderer:
    """A tile based object renderer using pyglet.

    :Parameters:
        `layers` : int
            The amount of layers in the z direction which objects can be
            placed on.
        `tile_width` : int
            The width of a tile in pixels.
        `tile_height` : int
            The height of a tile in pixels.
    """

    def __init__(self, layers=1, tile_width=1, tile_height=1):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.game_objects = []
        self.group_list = [pyglet.graphics.OrderedGroup(
            x) for x in range(layers + 1)]
        self.camera_offset_x = 0
        self.camera_offset_y = 0
        self.camera_zoom = 0

    def __getitem__(self, index):
        """Returns the game objects at a location.

        :type: Vector2D
        """
        index_x = index.x * self.tile_width
        index_y = index.y * self.tile_width + self.camera_offset_y
        list = []
        for game_object in self.game_objects:
            if game_object.x == index_x and game_object.y == index_y:
                list.append(game_object)
        return list

    def __setitem__(self, index, game_object):
        """Sets a game object at a location.

        :type: Vector3D
        """
        game_object.update(x=index.x * self.tile_width,
                           y=index.y * self.tile_height)

        self.game_objects.append(game_object)

    def scale(self, factor):
        """ Scales objects.

        Scales all objects by a factor specified.

        :type: float
        """
        for game_object in self.game_objects:
            game_object.scale = factor

    @property
    def batch(self):
        """The batch of objects handled by the renderer. Read Only.

        :type: pyglet.graphics.Batch
        """
        batch = pyglet.graphics.Batch()
        for game_object in self.game_objects:
            game_object.batch = batch

        return batch
