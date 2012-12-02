# -*- coding: utf-8 -*-

## Based on the script originally published on
## http://www.jansipke.nl/using-python-to-add-new-posts-in-wordpress/

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

import datetime
import xmlrpclib
from xml.sax.saxutils import escape
import json
import markdown

def html2(text = '', html = ''):
    if 'YouTubeVideo' in text:
        for line in html:
            if 'src=' in line:
                kk = (line.split('src=')[1]).split('\n')[0]
                return 'youtube', kk.split('embed/')[1].split('"')[0]
    elif 'HTML' in text:
        for line in html:
            if 'src=' in line:
                return 'url', (line.split('src=')[1]).split(' ')[0]
    else:
        return 'Nothing Found', None

nbdata = json.loads(open(notebook, 'r').read())
server = xmlrpclib.ServerProxy(wp_url)

## post title
title = escape(nbdata['metadata']['name'])

post = ""

## type of information included in cells different than code or markdown
formats = ['png','jpg','jpeg','gif','html']

count = 0
## Obtaining info from the ipynb file (JSON)
for cell in nbdata['worksheets'][0]['cells'][:]:
    
    if cell['cell_type'] == 'markdown':
        
        for info in cell['source'][:]:
            post += markdown.markdown(info)
            post += """\n"""
        
    if cell['cell_type'] == 'code' and cell['language'] == 'python':
        
        post += """[sourcecode language='python']\n"""
        
        for line in cell['input'][:]:
            
            post += """%s""" % line
            
        post += """[/sourcecode]"""
        post += """\n"""
        
        if cell['outputs']:
            
            if post_language == 'EN':
                
                post += "The output of the previous code will show:"
                
            if post_language == 'ES':
                
                post += """La salida del anterior código mostrará:"""
                
            post += """\n"""
            
            for output in cell['outputs'][:]:
                
                for formato in formats:
                    
                    if formato in output.keys():
                        
                        if formato != 'html':
                            
                            fich = (output[formato]).decode('base64')
                            fich = xmlrpclib.Binary(fich)
                            if formato == 'jpg':
                                
                                ext = 'jpeg'
                                
                            else:
                                
                                ext = formato
                                
                            imgtitle = title.replace(' ','_').replace('.','-')
                            data = {'name': imgtitle + str(count) + '.' + ext,
                                    'type': 'image/' + ext,
                                    'bits': fich,
                                    'overwrite': 'true'}
                            count += 1
                            image_id = server.wp.uploadFile(wp_blogid, 
                                                            wp_username, 
                                                            wp_password, 
                                                            data)
                            urlimg = image_id['url']
                            post += """<img src="%s"/>""" % urlimg
                            post += """\n"""
                            
                        else:
                            
                            out, url = html2(text = output['text'][0], 
                                                html = output[formato])
                            if out == 'youtube':
                                kk = '[youtube=http://www.youtube.com/watch?v='
                                post += """%s%s]\n""" % (kk, url)
                            if out == 'url':
                                
                                if post_language == 'EN':
                                    
                                    post += """Link to <a href="%s">%s</a>\n""" % (url, url)
                                    
                                if post_language == 'EN':
                                    
                                    post += """Enlace a <a href="%s">%s</a>\n""" % (url, url)
                                    
                            post += """\n"""

## Publishing the post
date_created = xmlrpclib.DateTime(datetime.datetime.now())
data = {'title': title, 
        'description': post,
        'post_type': 'post',
        'dateCreated': date_created,
        'mt_allow_comments': 'open',
        'mt_allow_pings': 'open',
        'post_status': 'draft',
        'categories': categories, 
        'mt_keywords': tags}
post_id = server.metaWeblog.newPost(wp_blogid, 
                                    wp_username, 
                                    wp_password, 
                                    data, 
                                    status_published)
