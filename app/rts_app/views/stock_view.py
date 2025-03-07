# UNDER CONSTRUCTION : This view is not yet implemented in the application and needs testing first.

from django.shortcuts import render
from django.db.models import Model, Sum
from rts_app.models.article_models import Article, ArticleSize

def stock_view(request):
    """View voor het weergeven van de voorraadpagina met filters."""

    producttype_filter = request.GET.get('producttype')
    design_filter = request.GET.get('design')
    company_filter = request.GET.get('companyname')

    articles = Article.objects.all()

    if producttype_filter:
        articles = articles.filter(producttype_id=producttype_filter)

    if design_filter:
        articles = articles.filter(design_id=design_filter)

    if company_filter:
        articles = articles.filter(companyname__icontains=company_filter)

    stock = []
    for article in articles:
        total_quantity = ArticleSize.objects.filter(article=article).aggregate(total_quantity=model.Sum('quantity'))['total_quantity'] or 0
        stock.append({
            'article': article,
            'total_quantity': total_quantity
        })

    producttypes = Article.objects.values('producttype').distinct()
    designs = Article.objects.values('design').distinct()
    companies = Article.objects.values('companyname').distinct()

    return render(request, "stock_page.html", {
        'stock': stock,
        'producttypes': producttypes,
        'designs': designs,
        'companies': companies,
    })
