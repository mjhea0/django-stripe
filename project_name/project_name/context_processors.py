from django.conf import settings

def sitewide(request):
	return {
		'settings': settings,
		'user': request.user,
		'ip_address': request.META['REMOTE_ADDR']
	}