from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
class SiteLogin:
    "This middleware requires a login for every view"
    def process_request(self, request):
        if request.path != 'passApp/accounts/login/' and request.user.is_anonymous():
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('passApp/accounts/login/?next=%s' % request.path)
