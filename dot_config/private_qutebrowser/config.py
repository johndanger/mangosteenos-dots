import os

config.load_autoconfig()

if os.path.exists(config.configdir / "dms/__init__.py"):
    from dms import setup

    setup(c)

# enable dark mode
c.colors.webpage.darkmode.enabled = True

# save tabs
c.auto_save.session = True

c.content.blocking.method = 'both'

config.bind('xs', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle tabs.show always never;; config-cycle statusbar.show always never')
