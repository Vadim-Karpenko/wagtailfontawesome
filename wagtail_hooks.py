from django.utils.html import format_html
from pkg_resources import parse_version

try:
    from django.templatetags.static import static
except ImportError:  # fallback for Django <2.1
    from django.contrib.staticfiles.templatetags.staticfiles import static

try:
    from wagtail import __version__ as WAGTAIL_VERSION
    from wagtail.core import hooks
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailcore import hooks
    from wagtail.wagtailcore import __version__ as WAGTAIL_VERSION


def import_wagtailfontawesome_stylesheet():
    return format_html('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/fontawesome.min.css" integrity="sha256-/sdxenK1NDowSNuphgwjv8wSosSNZB0t5koXqd7XqOI=" crossorigin="anonymous" />')


# New Wagtail versions support importing CSS throughout the admin.
# Fall back to the old hook (editor screen only) for older versions.
if parse_version(WAGTAIL_VERSION) >= parse_version('1.4'):
    admin_stylesheet_hook = 'insert_global_admin_css'
else:
    admin_stylesheet_hook = 'insert_editor_css'

hooks.register(admin_stylesheet_hook, import_wagtailfontawesome_stylesheet)