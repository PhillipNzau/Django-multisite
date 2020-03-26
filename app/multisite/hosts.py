


from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'multisite.blog_urls', name='www'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'product', 'multisite.product_urls', name='product'),
    host(r'sports', 'multisite.sports_urls', name='sports'),
    host(r'lifestyle', 'multisite.lifestyle_urls', name='lifestyle'),
   
    
)