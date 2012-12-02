ipynb2wp
========

Script to publish an ipython notebook on a wordpress platform
via XML-RPC.

Name | ipynb2wp
---- | --------
Website | https://github.com/kikocorreoso/ipynb2wp
Author | Kiko Correoso
Version | -3.14

ipynb2wp is a script to publish an ipython notebook with limited
functionality directly on wordpress.com or in a wordpress platform
with 'remote publishing' enabled (see http://codex.wordpress.org/XML-RPC_Support
for more info).

Functionality:
==============

1. Cells with python code in the ipynb file would appear as enclosed by `[sourcecode language="python"][/sourcecode]` tags in wordpress.
2. Cells with markdown formatted text would be transformed to HTML using http://pypi.python.org/pypi/Markdown/.
3. Inline images would be uploaded to wordpress and linked in the post. If the image is linked from other site you will get a copy in your site so take care about copyright and other restrictions.
4. Output with youtube videos would be enclosed with `[youtube]` tag in wordpress.
5. IPython.disply.HTML would be transformed to a link. There is a problem with the python code representation because wordpress escapes code like '<iframe>'.
6. Whatever you want to add...

Requirements:
=============

* [Markdown package](http://pypi.python.org/pypi/Markdown/)

Warnings and future:
====================

This script is just a proof of concept so may evolve to a very different stage.

Usage
=====

Just customize this code in [ipynb2wp.py file](https://github.com/kikocorreoso/ipynb2wp/blob/master/ipynb2wp.py):

  #############################################################################
  ## User modifications defining the site where the ipynb should be published
  wp_url = "http://yourblog.wordpress.com/xmlrpc.php"
  wp_username = "wp-user"
  wp_password = "wp-password"
  notebook = '/path/to/your/file.ipynb'
  wp_blogid = ""
  post_language = "ES" ## "EN" for english and "ES" for spanish
  ## The category should exist in your wordpress
  categories = ["Recursos"]
  ## Tags for the post
  tags = [ "ipython", "XML-RPC", "prueba de concepto","ipynb", 'notebook']
  ## Boolean value, 0 == not published (draft) and 1 == published
  status_published = 0
  ## That's all
  #############################################################################

Examples
========

This [ipython notebook](http://nbviewer.ipython.org/4185988/) was published on 
[pybonacci blog](http://pybonacci.wordpress.com/2012/12/02/publicando-directamente-en-wordpress-com-con-python/) using this 
[script](https://github.com/kikocorreoso/ipynb2wp/blob/master/ipynb2wp.py).


Bug reporting
=============

Please refer to the `issue tracker`_ on GitHub.

.. _`issue tracker`: https://github.com/kikocorreoso/ipynb2wp/issues

License
=======

ipynb2wp is released under a 2-clause BSD license, hence allowing commercial use
of the library.

See also
========

* [Ipython site](http://ipython.org/).
* [Blogging with the ipython notebook by Fernando Pérez](http://blog.fperez.org/2012/09/blogging-with-ipython-notebook.html)
