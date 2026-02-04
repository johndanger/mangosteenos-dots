import os

config.load_autoconfig()

if os.path.exists(config.configdir / "dms/__init__.py"):
    from dms import setup

    setup(c)

# enable dark mode
c.colors.webpage.darkmode.enabled = True

# save tabs
c.auto_save.session = True
