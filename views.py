from django.shortcuts import render

class Home(object):
    def __init__(self):
        pass
      
    def main(self, request):
        """Main function for home page

        Args:
            request: request object

        Returns:
            Renders to html page
        """
        
        return render(
            request, 
            'index.html', 
            {}
        )
