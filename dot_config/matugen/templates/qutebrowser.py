# vim:fileencoding=utf-8:foldmethod=marker


def setup(c, samecolorrows=False, mode=None):
    # Qutebrowser color scheme using Matugen template variables
    palette = {
        # Map Material You colors to Catppuccin-style names for compatibility
        "base": "{{ colors.background.default.hex }}",
        "text": "{{ colors.on_background.default.hex }}",
        "red": "{{ colors.error.default.hex }}",
        "green": "{{ colors.tertiary.default.hex }}",
        "yellow": "{{ colors.tertiary_fixed_dim.default.hex }}",
        "blue": "{{ colors.primary.default.hex }}",
        "mauve": "{{ colors.secondary.default.hex }}",
        "teal": "{{ colors.primary_fixed_dim.default.hex }}",
        # Derived colors using Material You palette
        "surface0": "{{ colors.surface_container_low.default.hex }}",
        "peach": "{{ colors.error_container.default.hex }}",
        "sky": "{{ colors.tertiary_fixed.default.hex }}",
        "sapphire": "{{ colors.tertiary_container.default.hex }}",
        "lavender": "{{ colors.primary_container.default.hex }}",
        "pink": "{{ colors.secondary_container.default.hex }}",
        "rosewater": "{{ colors.primary_fixed.default.hex }}",
        "overlay0": "{{ colors.on_surface_variant.default.hex }}",
        # Surface and text variants
        "mantle": "{{ colors.surface.default.hex }}",
        "crust": "{{ colors.surface_container.default.hex }}",
        "surface1": "{{ colors.surface_container_low.default.hex }}",
        "surface2": "{{ colors.surface_container_high.default.hex }}",
        "subtext0": "{{ colors.on_surface_variant.default.hex }}",
        "subtext1": "{{ colors.on_surface.default.hex }}",
        "overlay1": "{{ colors.outline_variant.default.hex }}",
        "overlay2": "{{ colors.outline.default.hex }}",
        # Additional colors
        "flamingo": "{{ colors.error.default.hex }}",
        "maroon": "{{ colors.error_container.default.hex }}",
    }

    # completion {{"{{{"}}
    ## Background color of the completion widget category headers.
    c.colors.completion.category.bg = palette["base"]
    ## Bottom border color of the completion widget category headers.
    c.colors.completion.category.border.bottom = palette["mantle"]
    ## Top border color of the completion widget category headers.
    c.colors.completion.category.border.top = palette["overlay2"]
    ## Foreground color of completion widget category headers.
    c.colors.completion.category.fg = palette["green"]
    ## Background color of the completion widget for even and odd rows.
    if samecolorrows:
        c.colors.completion.even.bg = palette["mantle"]
        c.colors.completion.odd.bg = c.colors.completion.even.bg
    else:
        c.colors.completion.even.bg = palette["mantle"]
        c.colors.completion.odd.bg = palette["crust"]
    ## Text color of the completion widget.
    c.colors.completion.fg = palette["subtext0"]

    ## Background color of the selected completion item.
    c.colors.completion.item.selected.bg = palette["surface2"]
    ## Bottom border color of the selected completion item.
    c.colors.completion.item.selected.border.bottom = palette["surface2"]
    ## Top border color of the completion widget category headers.
    c.colors.completion.item.selected.border.top = palette["surface2"]
    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.fg = palette["text"]
    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.match.fg = palette["rosewater"]
    ## Foreground color of the matched text in the completion.
    c.colors.completion.match.fg = palette["text"]

    ## Color of the scrollbar in completion view
    c.colors.completion.scrollbar.bg = palette["crust"]
    ## Color of the scrollbar handle in completion view.
    c.colors.completion.scrollbar.fg = palette["surface2"]
    # {{"}}}"}}

    # downloads {{"{{{"}}
    c.colors.downloads.bar.bg = palette["base"]
    c.colors.downloads.error.bg = palette["base"]
    c.colors.downloads.start.bg = palette["base"]
    c.colors.downloads.stop.bg = palette["base"]

    c.colors.downloads.error.fg = palette["red"]
    c.colors.downloads.start.fg = palette["blue"]
    c.colors.downloads.stop.fg = palette["green"]
    c.colors.downloads.system.fg = "none"
    c.colors.downloads.system.bg = "none"
    # {{"}}}"}}

    # hints {{"{{{"}}
    ## Palette keys chosen by mode so hint bg/fg contrast (mode from dms IPC).
    if mode == "light":
        c.colors.hints.bg = palette["blue"]
        c.colors.hints.fg = palette["mantle"]
    else:
        c.colors.hints.bg = palette["teal"]
        c.colors.hints.fg = palette["mantle"]

    ## Hints
    c.hints.border = "1px solid " + palette["overlay2"]

    ## Font color for the matched part of hints.
    c.colors.hints.match.fg = palette["text"]
    # {{"}}}"}}

    # keyhints {{"{{{"}}
    if mode == "light":
        c.colors.keyhint.bg = palette["surface2"]
        c.colors.keyhint.fg = palette["text"]
        c.colors.keyhint.suffix.fg = palette["green"]
    else:
        c.colors.keyhint.bg = palette["teal"]
        c.colors.keyhint.fg = palette["mantle"]
        c.colors.keyhint.suffix.fg = palette["green"]
    # {{"}}}"}}

    # messages {{"{{{"}}
    ## Background color of an error message.
    c.colors.messages.error.bg = palette["surface0"]
    ## Background color of an info message.
    c.colors.messages.info.bg = palette["surface0"]
    ## Background color of a warning message.
    c.colors.messages.warning.bg = palette["surface0"]

    ## Border color of an error message.
    c.colors.messages.error.border = palette["mantle"]
    ## Border color of an info message.
    c.colors.messages.info.border = palette["mantle"]
    ## Border color of a warning message.
    c.colors.messages.warning.border = palette["mantle"]

    ## Foreground color of an error message.
    c.colors.messages.error.fg = palette["red"]
    ## Foreground color an info message.
    c.colors.messages.info.fg = palette["text"]
    ## Foreground color a warning message.
    c.colors.messages.warning.fg = palette["peach"]
    # {{"}}}"}}

    # prompts {{"{{{"}}
    ## Background color for prompts.
    c.colors.prompts.bg = palette["mantle"]

    # ## Border used around UI elements in prompts.
    c.colors.prompts.border = "1px solid " + palette["overlay0"]

    ## Foreground color for prompts.
    c.colors.prompts.fg = palette["text"]

    ## Background color for the selected item in filename prompts.
    c.colors.prompts.selected.bg = palette["surface2"]

    ## Background color for the selected item in filename prompts.
    c.colors.prompts.selected.fg = palette["rosewater"]
    # {{"}}}"}}

    # statusbar {{"{{{"}}
    ## Background color of the statusbar.
    c.colors.statusbar.normal.bg = palette["base"]
    ## Background color of the statusbar in insert mode.
    c.colors.statusbar.insert.bg = palette["crust"]
    ## Background color of the statusbar in command mode.
    c.colors.statusbar.command.bg = palette["base"]
    ## Background color of the statusbar in caret mode.
    c.colors.statusbar.caret.bg = palette["base"]
    ## Background color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.bg = palette["base"]

    ## Background color of the progress bar.
    c.colors.statusbar.progress.bg = palette["base"]
    ## Background color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.bg = palette["base"]

    ## Foreground color of the statusbar.
    c.colors.statusbar.normal.fg = palette["text"]
    ## Foreground color of the statusbar in insert mode.
    c.colors.statusbar.insert.fg = palette["rosewater"]
    ## Foreground color of the statusbar in command mode.
    c.colors.statusbar.command.fg = palette["text"]
    ## Foreground color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.fg = palette["peach"]
    ## Foreground color of the statusbar in caret mode.
    c.colors.statusbar.caret.fg = palette["peach"]
    ## Foreground color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.fg = palette["peach"]

    ## Foreground color of the URL in the statusbar on error.
    c.colors.statusbar.url.error.fg = palette["red"]

    ## Default foreground color of the URL in the statusbar.
    c.colors.statusbar.url.fg = palette["text"]

    ## Foreground color of the URL in the statusbar for hovered links.
    c.colors.statusbar.url.hover.fg = palette["sky"]

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.http.fg = palette["teal"]

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.https.fg = palette["green"]

    ## Foreground color of the URL in the statusbar when there's a warning.
    c.colors.statusbar.url.warn.fg = palette["yellow"]

    ## PRIVATE MODE COLORS
    ## Background color of the statusbar in private browsing mode.
    c.colors.statusbar.private.bg = palette["mantle"]
    ## Foreground color of the statusbar in private browsing mode.
    c.colors.statusbar.private.fg = palette["subtext1"]
    ## Background color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.bg = palette["base"]
    ## Foreground color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.fg = palette["subtext1"]

    # {{"}}}"}}

    # tabs {{"{{{"}}
    ## Background color of the tab bar.
    c.colors.tabs.bar.bg = palette["crust"]
    ## Background color of unselected even tabs.
    c.colors.tabs.even.bg = palette["surface2"]
    ## Background color of unselected odd tabs.
    c.colors.tabs.odd.bg = palette["surface1"]

    ## Foreground color of unselected even tabs.
    c.colors.tabs.even.fg = palette["text"]
    ## Foreground color of unselected odd tabs.
    c.colors.tabs.odd.fg = palette["text"]

    ## Color for the tab indicator on errors.
    c.colors.tabs.indicator.error = palette["red"]
    ## Color gradient interpolation system for the tab indicator.
    ## Valid values:
    ##	 - rgb: Interpolate in the RGB color system.
    ##	 - hsv: Interpolate in the HSV color system.
    ##	 - hsl: Interpolate in the HSL color system.
    ##	 - none: Don't show a gradient.
    c.colors.tabs.indicator.system = "rgb"

    # ## Background color of selected even tabs.
    c.colors.tabs.selected.even.bg = palette["base"]
    # ## Background color of selected odd tabs.
    c.colors.tabs.selected.odd.bg = palette["base"]

    # ## Foreground color of selected even tabs.
    c.colors.tabs.selected.even.fg = palette["text"]
    # ## Foreground color of selected odd tabs.
    c.colors.tabs.selected.odd.fg = palette["text"]
    # {{"}}}"}}

    # context menus {{"{{{"}}
    c.colors.contextmenu.menu.bg = palette["base"]
    c.colors.contextmenu.menu.fg = palette["text"]

    c.colors.contextmenu.disabled.bg = palette["mantle"]
    c.colors.contextmenu.disabled.fg = palette["overlay0"]

    c.colors.contextmenu.selected.bg = palette["crust"]
    c.colors.contextmenu.selected.fg = palette["subtext1"]
    # {{"}}}"}}
