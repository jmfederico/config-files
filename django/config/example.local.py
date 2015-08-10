"""Local settings file."""

from .base import *

###############################################################################
#
# Base Django settings
#
# Override Django settings.
#
###############################################################################

INSTALLED_APPS += (
    'debug_toolbar',
    'debug_panel',
    'template_timings_panel',
    'template_profiler_panel',
)

MIDDLEWARE_CLASSES += (
    'debug_panel.middleware.DebugPanelMiddleware',
)

###############################################################################
#
# Apps settings
#
###############################################################################

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    # Extra
    'debug_toolbar.panels.profiling.ProfilingPanel',
    # Contrib
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'template_profiler_panel.panels.template.TemplateProfilerPanel',
]
