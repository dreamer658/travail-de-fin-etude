from django import template
register = template.Library()

@register.filter
def get_name(value):
    spam = value.split('/')[-1]         # assume value be /python/web-scrapping
                                        # spam would be 'web-scrapping'
    spam = ' '.join(spam.split('-'))    # now spam would be 'web scrapping'
    return spam

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    """ This in order to fix the pagination with the search bar included in the website
    We'll grab the url and transform it so we can return it in the format we which. """


    #We're trying to cut the diffrent part of the url into a list named url
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name,querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url
