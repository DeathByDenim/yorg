from panda3d.bullet import BulletWorld, BulletDebugNode


class PhysMgr:

    def __init__(self):
        '''Inits the engine.'''
        self.collision_objs = []
        self.__coll_dct = {}
        self.world_np = None
        self.world_phys = None
        self.__debug_np = None

    def init(self):
        self.collision_objs = []
        self.__coll_dct = {}
        self.world_np = render.attachNewNode('world')
        self.world_phys = BulletWorld()
        self.world_phys.setGravity((0, 0, -9.81))
        debug_node = BulletDebugNode('Debug')
        debug_node.showBoundingBoxes(True)
        self.__debug_np = render.attachNewNode(debug_node)
        self.world_phys.setDebugNode(self.__debug_np.node())

    def start(self):
        '''Starts the engine.'''
        taskMgr.add(self.__update, 'Engine::update')

    def __update(self, task):
        '''Called on each frame.'''
        if self.world_phys:
            d_t = globalClock.getDt()
            self.world_phys.doPhysics(d_t, 10, 1/180.0)
            self.__do_collisions()
            messenger.send('on_frame')
            return task.cont

    def stop(self):
        '''Stops the engine.'''
        self.world_phys = None
        self.world_np.removeNode()
        self.__debug_np.removeNode()

    def __process_contact(self, obj, node, to_clear):
        '''Processes a physics contact.'''
        if node != obj:
            if obj in to_clear:
                to_clear.remove(obj)
            coll_dct = self.__coll_dct[obj]
            if not node in [coll_pair[0] for coll_pair in coll_dct]:
                self.__coll_dct[obj] += [(node, globalClock.getFrameTime())]
                messenger.send('on_collision', [obj, node.getName()])

    def __do_collisions(self):
        '''Computes the collisions.'''
        to_clear = self.collision_objs[:]
        for obj in self.collision_objs:
            if not obj in self.__coll_dct:
                self.__coll_dct[obj] = []
            result = self.world_phys.contactTest(obj)
            for contact in result.getContacts():
                self.__process_contact(obj, contact.getNode0(), to_clear)
                self.__process_contact(obj, contact.getNode1(), to_clear)
        for obj in to_clear:
            for coll_pair in self.__coll_dct[obj]:
                if globalClock.getFrameTime() - coll_pair[1] > .25:
                    self.__coll_dct[obj].remove(coll_pair)

    def toggle_debug(self):
        '''Toggles the physics debug.'''
        is_hidden = self.__debug_np.isHidden()
        (self.__debug_np.show if is_hidden else self.__debug_np.hide)()
