from django.shortcuts import render, redirect
from django.contrib import messages
from rts_app.forms.articleform import ArticleForm
from rts_app.models.article_models import Article, ProductType, Design, Company, Size, LimitedEdition, ArticleSize
from rts_app.utils.article_generator import generate_article_number
import logging

logger = logging.getLogger(__name__)

def article_create_view(request):
    """View for creating a new article with validation for clothing and size."""

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            # Retrieve selected values
            producttype = form.cleaned_data.get("producttype")
            design = form.cleaned_data.get("design")
            companyname = form.cleaned_data.get("companyname")
            limited_edition = form.cleaned_data.get("limited_edition")

            # Save article without committing (we need an ID first)
            article = form.save(commit=False)
            article.producttype = producttype.typename
            article.design = design.designname
            article.companyname = companyname.companyname
            article.limited_edition = limited_edition

            # Generate article number
            article.articlenr = generate_article_number(producttype, design, None, article.limited_edition)
            article.save()  # Save now

            # Save size input
            if producttype.clothing:
                for size in form.sizes:
                    size_quantity = form.cleaned_data.get(f"size_{size.sizenr}")
                    if size_quantity > 0:
                        ArticleSize.objects.create(article=article, size=size, quantity=size_quantity)

            # Log success
            logger.info("Article successfully saved with article number: %s", article.articlenr)

            # Redirect to success page with article number
            return redirect("article_success", articlenr=article.articlenr)

        else:
            # Log form errors
            logger.error("Form is not valid: %s", form.errors)
            messages.error(request, "Form is not valid. Please check the fields and try again.")

    else:
        form = ArticleForm()

    # Retrieve all LimitedEdition objects to show them in the dropdown
    limited_editions = LimitedEdition.objects.all()

    return render(request, "create_article.html", {
        "form": form,
        "limited_editions": limited_editions
    })


def article_success_view(request, articlenr):
    """Displays the article details after successful creation."""

    try:
        article = Article.objects.get(articlenr=articlenr)
    except Article.DoesNotExist:
        return render(request, "error.html", {"message": "Article not found."})

    return render(request, "article_success.html", {"article": article})
