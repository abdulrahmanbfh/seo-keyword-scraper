from django.http import HttpResponse
from scraper.scraper import scrape_google

def get_results(request):
    query = request.GET.get('query', '')
    if not query:
        return HttpResponse("Please provide a query parameter.", status=400)

    data = scrape_google(query)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{query}_results.csv"'
    data.to_csv(response, index=False)

    return response