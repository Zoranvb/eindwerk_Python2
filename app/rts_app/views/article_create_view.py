from django.shortcuts import render, redirect
from rts_app.forms.articleform import ArticleForm
from rts_app.models.article_models import ProductType, Design, Company, Size, ArticleSize  

def article_create_view(request):
    """View voor het maken van een nieuw artikel met validatie voor kleding en maat."""

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            # Ophalen van geselecteerde waarden
            producttype = form.cleaned_data.get("producttype")
            design = form.cleaned_data.get("design")
            companyname = form.cleaned_data.get("companyname")

            # Artikel opslaan zonder committen (we hebben eerst een ID nodig)
            article = form.save(commit=False)
            article.producttype = producttype
            article.design = design
            article.companyname = companyname
            article.save()  # Sla eerst het artikel op zodat het een ID krijgt

            # Check of producttype kleding is
            if producttype and producttype.clothing:
                sizes = Size.objects.exclude(sizenr=99)
                # Verwerk de maten en aantallen
                for size in Size.objects.all():
                    size_key = f"size_{size.sizenr}"  # input name in HTML
                    quantity = request.POST.get(size_key, 0)

                    try:
                        quantity = int(quantity)
                    except ValueError:
                        quantity = 0  # Ongeldige invoer wordt 0

                    if quantity > 0:
                        ArticleSize.objects.create(article=article, size=size, quantity=quantity)

            return redirect("success_page")

    else:
        form = ArticleForm()

    return render(request, "create_article.html", {"form": form})
