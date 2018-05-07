# -*- coding: utf-8-*-
def strip_tags(html):
    import re
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html)
    return dd
