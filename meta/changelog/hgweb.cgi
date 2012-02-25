#!/usr/bin/env python
#
# An example hgweb CGI script, edit as necessary
# See also http://mercurial.selenic.com/wiki/PublishingRepositories

# Uncomment and adjust if Mercurial is not installed system-wide
# (consult "installed modules" path from 'hg debuginstall'):
import sys; sys.path.insert(0, "/kunden/homepages/22/d89915628/htdocs/local/lib/python2.4/site-packages")

# Uncomment to send python tracebacks to the browser if an error occurs:
# import cgitb; cgitb.enable()

from mercurial import demandimport; demandimport.enable()
from mercurial.hgweb import hgweb, wsgicgi
application = hgweb("/kunden/homepages/22/d89915628/htdocs/personal", "Harish Narayanan's Personal Site")
wsgicgi.launch(application)
