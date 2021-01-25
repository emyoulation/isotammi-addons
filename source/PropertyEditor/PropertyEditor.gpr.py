from gramps.version import major_version

register(GRAMPLET,
         id = "PropertyEditor",
         name = _("PropertyEditor"),
         description = _("Gramplet to edit attributes of multiple objects"),
         status = STABLE,
         version = '1.0.8',
         gramps_target_version = major_version,
         fname = "PropertyEditor.py",
         gramplet = 'PropertyEditor',
         height = 375,
         detached_width = 510,
         detached_height = 480,
         expand = True,
         gramplet_title = _("PropertyEditor"),
         help_url="PropertyEditor Gramplet",
         include_in_listing = True,
         #navtypes=["Source"],
        )
