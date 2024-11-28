from django.http import HttpResponse
from scraper.scraper import scrape_google

def get_results(request):
    query = request.GET.get('query', '')
    if not query:
        return HttpResponse("Please provide a query parameter.", status=400)

        # Get the max_results parameter (optional)
    max_results = request.GET.get('max_results')
    if max_results:
        try:
            max_results = int(max_results)
        except ValueError:
            return HttpResponse("Invalid max_results parameter. It must be an integer.", status=400)
    else:
        max_results = 100  # Default value if not provided

    data = scrape_google(query, max_results)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{query}_results.csv"'
    data.to_csv(response, index=False)

    return response