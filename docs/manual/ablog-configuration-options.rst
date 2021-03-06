.. _config:

ABlog Configuration Options
===========================

.. post:: May 10, 2014
   :tags: config
   :author: Ahmet
   :category: Manual
   :location: Pittsburgh


This post describes ABlog configuration options that goes in
:ref:`Sphinx build configuration file <sphinx:build-config>`.

General options
---------------

.. confval:: blog_path

   A path relative to the configuration directory for blog archive pages.
   Default is ``'blog'``.


.. confval:: blog_title

   The “title” for the blog, used in acthive pages.  Default is ``'Blog'``.

.. confval:: blog_baseurl

   Base URL for the website, required for generating feeds.


Authors & locations
-------------------

.. confval:: blog_authors

   A dictionary of author names mapping to author full display names and
   links. Dictionary keys are what should be used in ``post`` directive
   to refer to the author.  Default is ``{}``. Example::

     blog_authors = {
         'Ahmet': ('Ahmet Bakan', 'http://ahmetbakan.com'),
         'Durden': ('Tyler Durden',
                    'http://en.wikipedia.org/wiki/Tyler_Durden'),
     }

.. confval:: blog_locations

   A dictionary of location names mapping to full display names and
   links of these locations. Similar to :confval:`blog_authors`, dictionary
   keys should be used in ``post`` directive to refer to the locations.
   Default is ``{}``.


.. confval:: blog_default_author

   Name of the default author defined in :confval:`blog_authors`.
   Default is ``None``.

.. confval:: blog_default_location

   Name of the default location defined in :confval:`blog_locations`.
   Default is ``None``.


Post related
------------

.. confval:: post_date_format

   Date display format (default is ``'%b %d, %Y'``) for published posts that
   goes as input to :meth:`datetime.date.strftime`.

.. confval:: post_auto_excerpt

   Number of paragraphs (default is ``1``) that will be displayed as an excerpt
   from the post. Setting this ``0`` will result in displaying no post excerpt
   in archive pages.  This option can be set on a per post basis using
   :rst:dir:`post` directive option ``excerpt``.

   See :ref:`post-excerpts-and-images` for a more detailed discussion.

.. confval:: post_redirect_refresh

   Number of seconds (default is ``5``) that a redirect page waits before
   refreshing the page to redirect to the post.

.. _fa:

Font awesome
------------

ABlog templates will use of `Font Awesome`_ icons if one of the following
is ``True``:

.. _Font Awesome: http://fontawesome.io/


.. confval:: fontawesome_link_cdn

   Link to `Font Awesome`_ at `Bootstrap CDN`_ and use icons in sidebars
   and post footers.  Default: ``False``


   .. _Bootstrap CDN: http://www.bootstrapcdn.com/#fontawesome_tab

.. confval:: fontawesome_included

   Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``

Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
with the following configuration option:

.. confval:: fontawesome_css_file

   Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
   be linked to in HTML output by ABlog.

.. _disqus-integration:

Disqus integration
------------------

Of course one cannot think of a blog that doesn't allow for visitors to
comment.  You can enable Disqus_ by setting ``disqus_shortname`` variable.

.. confval:: disqus_shortname

   Disqus_ short name for the website.

.. confval:: disqus_pages

   Choose to disqus pages that are not posts, default is ``False``.

.. confval:: disqus_drafts

   Choose to disqus posts that are drafts (without a published date),
   default is ``False``.

.. _sidebars:

Blog sidebars
-------------

Finally, there are seven sidebars you can include in your HTML output
using Sphinx_ :confval:`html_sidebars` configuration option.  Sidebars that
you see on the left are listed below in the same order:

.. code-block:: python

   html_sidebars = {
      '**': [...,
             'postcard.html', 'recentposts.html',
             'tagcloud.html', 'categories.html',
             'archives.html', ]
   }


:file:`postcard.html` provides information regarding the current post.
:file:`recentposts.html` lists most recent five posts.  Others provide a
link to a archive pages generated for each tag, category, and year.
In addition, there are ``authors.html`` and ``locations.html``
sidebars that link to author and location archive pages.


