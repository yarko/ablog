# -*- coding: utf-8 -*-
import os
import sys


import alabaster
import ablog

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    #'IPython.sphinxext.ipython_directive',
    #'IPython.sphinxext.ipython_console_highlighting',
    'alabaster',
    'ablog'
]


# PROJECT

version = release = ablog.__version__
project = u'ABlog'
copyright = u'2014, Ahmet Bakan'
master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['_build']


# HTML OUTPUT

html_title = "ABlog"
html_static_path = ['_static']
html_use_index = True
html_domain_indices = False
html_show_sourcelink = True
html_favicon = '_static/ablog.ico'

# ABLOG

templates_path = [ablog.get_html_templates_path()]

if os.environ.get('READTHEDOCS', None) == 'True':
    skip_pickling = True

blog_title = 'ABlog'
blog_baseurl = 'http://ablog.readthedocs.org'
blog_locations = {
    'Pittsburgh': ('Pittsburgh, PA', None),
    'SF': ('San Francisco, CA', None),
}
blog_authors = {
    'Ahmet': ('Ahmet Bakan', 'http://ahmetbakan.com'),
    'Napi': ('Lord Napi', 'http://ahmetbakan.com'),
}
disqus_shortname = 'ablogforsphinx'
disqus_pages = True
fontawesome_css_file = 'css/font-awesome.css'


# THEME

html_style = 'alabaster.css'
html_theme = 'alabaster'
html_sidebars = {
   '**': ['about.html',
          'postcard.html', 'recentposts.html',
          'tagcloud.html', 'categories.html',
          'archives.html',
          'searchbox.html']
}
html_theme_path = [alabaster.get_path()]
html_theme_options = {
    'travis_button': False,
    'github_user': 'abakan',
    'github_repo': 'ablog',
    'description': 'ABlog for blogging with Sphinx',
    'logo': 'ablog.png',
}

# SPHINX

intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'sphinx': ('http://sphinx-doc.org/', None)
}
extlinks = {
    'wiki': ('http://en.wikipedia.org/wiki/%s', ''),
}

rst_epilog = '''
.. _Sphinx: http://sphinx-doc.org/
.. _Python: http://python.org
.. _pip: http://www.pip-installer.org/
.. _Disqus: http://disqus.com/
.. _Werkzeug: http://werkzeug.pocoo.org/
.. _GitHub: https://github.com/abakan/ablog
.. _PyPI: https://pypi.python.org/pypi/ablog
.. _Read The Docs: https://readthedocs.org/
'''

import re
from sphinx import addnodes


event_sig_re = re.compile(r'([a-zA-Z-]+)\s*\((.*)\)')

def parse_event(env, sig, signode):
    m = event_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    signode += addnodes.desc_name(name, name)
    plist = addnodes.desc_parameterlist()
    for arg in args.split(','):
        arg = arg.strip()
        plist += addnodes.desc_parameter(arg, arg)
    signode += plist
    return name


def setup(app):
    from sphinx.ext.autodoc import cut_lines
    from sphinx.util.docfields import GroupedField
    app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    fdesc = GroupedField('parameter', label='Parameters',
                         names=['param'], can_collapse=True)
    app.add_object_type('event', 'event', 'pair: %s; event', parse_event,
                        doc_field_types=[fdesc])