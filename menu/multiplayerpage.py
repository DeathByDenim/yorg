from direct.gui.DirectButton import DirectButton
from yyagl.engine.gui.page import Page
from yyagl.gameobject import GameObjectMdt
from .serverpage import ServerPage, ServerPageProps
from .clientpage import ClientPage
from .thankspage import ThanksPageGui


class MultiplayerPageProps(object):

    def __init__(
            self, cars, car_path, phys_path, tracks, tracks_tr, track_img,
            player_name, drivers_img, cars_img, drivers):
        self.cars = cars
        self.car_path = car_path
        self.phys_path = phys_path
        self.tracks = tracks
        self.tracks_tr = tracks_tr
        self.track_img = track_img
        self.player_name = player_name
        self.drivers_img = drivers_img
        self.cars_img = cars_img
        self.drivers = drivers


class MultiplayerPageGui(ThanksPageGui):

    def __init__(self, mdt, menu, mp_props):
        self.props = mp_props
        ThanksPageGui.__init__(self, mdt, menu)

    def build_page(self):
        menu_gui = self.menu.gui
        serverpage_props = ServerPageProps(
            self.props.cars, self.props.car_path, self.props.phys_path,
            self.props.tracks, self.props.tracks_tr, self.props.track_img,
            self.props.player_name, self.props.drivers_img,
            self.props.cars_img, self.props.drivers)
        scb = lambda: self.menu.push_page(ServerPage(self.menu,
                                                     serverpage_props))
        menu_data = [
            ('Server', scb),
            ('Client', lambda: self.menu.push_page(ClientPage(self.menu)))]
        widgets = [
            DirectButton(text=menu[0], pos=(0, 1, .4-i*.28), command=menu[1],
                         **menu_gui.btn_args)
            for i, menu in enumerate(menu_data)]
        map(self.add_widget, widgets)
        ThanksPageGui.build_page(self)


class MultiplayerPage(Page):
    gui_cls = MultiplayerPageGui

    def __init__(self, menu, mp_props):
        self.menu = menu
        init_lst = [
            [('event', self.event_cls, [self])],
            [('gui', self.gui_cls, [self, self.menu, mp_props])]]
        GameObjectMdt.__init__(self, init_lst)
