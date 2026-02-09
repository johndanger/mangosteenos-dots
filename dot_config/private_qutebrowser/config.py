import os
import subprocess

config.load_autoconfig()


def _dms_theme_mode():
    """Get current theme mode from Dank Linux (dms) IPC. Returns 'dark', 'light', or None."""
    try:
        r = subprocess.run(
            ["dms", "ipc", "call", "theme", "getMode"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip().lower()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None

if os.path.exists(config.configdir / "dms/__init__.py"):
    from dms import setup

    mode = _dms_theme_mode()
    try:
        setup(c, mode=mode)
    except TypeError:
        setup(c)


# Sync webpage dark mode with DMS theme (dark = enable, light = disable).
# Keyhint colors come from the dms/matugen theme (setup(c) above) using
# Material You semantic colors that contrast properly in both light and dark themes.
_dms_mode = _dms_theme_mode()
if _dms_mode == "dark":
    c.colors.webpage.darkmode.enabled = True
elif _dms_mode == "light":
    c.colors.webpage.darkmode.enabled = False
else:
    # DMS not available or unknown; default to dark
    c.colors.webpage.darkmode.enabled = True

# save tabs
c.auto_save.session = True

c.content.blocking.method = 'both'

config.bind('xs', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle tabs.show always never;; config-cycle statusbar.show always never')
