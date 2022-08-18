from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(object):
    def __init__(self):
        pass
    
    @method_decorator(login_required)
    def main(self, request):
        """Main function for home page

        Args:
            request: request object

        Returns:
            Renders to html page
        """
        
        return render(request, 'index.html', {})
