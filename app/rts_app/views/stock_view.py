# views.py
from django.shortcuts import render
from django.db.models import Sum
from rts_app.models.article_models import Article, ArticleSize

def stock_view(request):
    """View voor het weergeven van de voorraadpagina met filters."""

    # Filters instellen
    producttype_filter = request.GET.get('producttype')
    design_filter = request.GET.get('design')
    company_filter = request.GET.get('companyname')

    # Basis query om alle artikelen op te halen
    articles = Article.objects.all()

    # Filteren op producttype als er een filter is
    if producttype_filter:
        articles = articles.filter(producttype_id=producttype_filter)

    # Filteren op design als er een filter is
    if design_filter:
        articles = articles.filter(design_id=design_filter)

    # Filteren op companyname als er een filter is
    if company_filter:
        articles = articles.filter(companyname__icontains=company_filter)

    # Voorraad per artikel ophalen
    stock = []
    for article in articles:
        total_quantity = ArticleSize.objects.filter(article=article).aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
        stock.append({
            'article': article,
            'total_quantity': total_quantity
        })

    # Verkrijg de beschikbare filters (voor dropdowns)
    producttypes = Article.objects.values('producttype').distinct()
    designs = Article.objects.values('design').distinct()
    companies = Article.objects.values('companyname').distinct()

    return render(request, "stock_page.html", {
        'stock': stock,
        'producttypes': producttypes,
        'designs': designs,
        'companies': companies,
    })
