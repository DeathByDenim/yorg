# BUGS =====

# TODO LIST =====

# 0.9 (network)
# #network at end of a multiplayer race wait for other cars
# #network wheels' animations
# #network physics (collisions to players' car)
# #network drivers' names on their cars during multiplayer matches
# #network print if the port is closed when creating the server
# #network send game packets using udp in place of tcp
# #network weapons


# WAITING =====

# (Panda3D 1.10) preload weapons
# (Panda3D 1.10) #shaders shadows
#     https://www.panda3d.org/forums/viewtopic.php?f=8&t=18798


# MAYBE/SOMEDAY =====

# use txo files in place of png and jpg
# ai: only one (rotated) ray for obstacles and ground
# contour detection
# more power for the drifting; the length of the inertia+engine should not
#  be bigger than max engine's force
# apply drifting force during the drifting
# preloading shaders by creating cards, applying shaders and call render_frame
# 3D audio (from player's car)
# refactor: notify done by evt (from mdt externally);
#   Colleague.notify invokes that; GO's attach redirected to evt;
#   only evt is a Subject
# refactor: don't share eng with every colleague, instead share only the
#   useful components e.g. PhysComponent has PhysComponent.phys_mgr and
#   PhysComponent.log_mgr
# remove mdt from colleague
# change/improve linux installer
# make scons for yyagl
# embed into a wx / pyqt window
# port to python 3
# deferred shading, tone mapping
# hardware instancing
# multi-threading physics loading
# make uml diagrams with pyreverse into devinfo
# unit tests
# django webapp for scores
# particles: presize and use the Python buffer protocol
# particles: use images in place of points
