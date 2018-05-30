import pyglet


class Renderer:
    """A tile based object renderer using pyglet.

    Attributes:
        layers: An integer of the amount of layers used by the renderer.
        tile_width: An integer of the width of a tile in pixels.
        tile_height: An integer of the height of a tile in pixels.
        game_objects: An array of every object managed by the renderer.
        group_list: An array of OrderedGroup objects for layers.
        batch: A pyglet.graphics.Batch of all the objects in group_list. Read Only.
    """

    def __init__(self, layers=1, tile_width=1, tile_height=1):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.layers = layers
        self.game_objects = []
        self.group_list = [pyglet.graphics.OrderedGroup(
            x) for x in range(self.layers + 1)]

    def __getitem__(self, index):
        index_x = index.x * self.tile_width
        index_y = index.y * self.tile_width
        objects = [obj for obj in self.game_objects if obj.x
                   == index_x and obj.y == index_y and obj.group
                   == self.group_list[index.z]]
        return objects

    def __setitem__(self, index, game_object):
        game_object.update(x=index.x * self.tile_width,
                           y=index.y * self.tile_height)
        game_object.group = self.group_list[index.z]
        self.game_objects.append(game_object)

    @property
    def batch(self):
        batch = pyglet.graphics.Batch()
        for game_object in self.game_objects:
            game_object.batch = batch

        return batch
