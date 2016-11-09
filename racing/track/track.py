from abc import ABCMeta
from racing.game.gameobject import GameObjectMdt
from .gfx import _Gfx
from .phys import _Phys
from .gui.gui import TrackGui
from .event import _Event


class Track(GameObjectMdt):
    __metaclass__ = ABCMeta
    gfx_cls = _Gfx
    phys_cls = _Phys
    gui_cls = TrackGui
    event_cls = _Event

    def __init__(self, track_path, cb, split_world, submodels):
        eng.log_mgr.log('init track')
        self.track_path = track_path
        init_lst = [
            [('fsm', self.fsm_cls, [self])],
            [('phys', self.phys_cls, [self, track_path]),
             ('gfx', self.gfx_cls, [self, track_path, split_world, submodels],
              lambda: self.gfx.attach(self.on_loading)),
             ('gui', self.gui_cls, [self, track_path[6:]])],
            [('logic', self.logic_cls, [self])],
            [('audio', self.audio_cls, [self])],
            [('ai', self.ai_cls, [self])],
            [('event', self.event_cls, [self])]]
        GameObjectMdt.__init__(self, init_lst, cb)

    def on_loading(self, txt):
        self.notify('on_loading', txt)
