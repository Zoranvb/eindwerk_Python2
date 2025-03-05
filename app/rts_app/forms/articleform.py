from django import forms
from rts_app.models.article_models import Article, ProductType, Design, Size, Company, ArticleSizeQuantity  

class ArticleForm(forms.ModelForm):
    """
    Formulier voor het aanmaken van een nieuw artikel.
    Dit formulier bevat velden voor het selecteren van producttype, design, company,
    het kiezen of het artikel een limited edition is, en het invoeren van maten als het om kleding gaat.
    """
    
    limited_edition = forms.BooleanField(required=False, label="Limited Edition")

    # Dropdowns voor andere modellen
    design = forms.ModelChoiceField(
        queryset=Design.objects.all(), 
        empty_label="Select a design", 
        widget=forms.Select(attrs={"class": "form-control"})
    )
    
    companyname = forms.ModelChoiceField(
        queryset=Company.objects.all(), 
        empty_label="Select a company", 
        widget=forms.Select(attrs={"class": "form-control"})
    )

    producttype = forms.ModelChoiceField(
        queryset=ProductType.objects.all(),
        empty_label="Select a product type",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_producttype"})  # ID toegevoegd voor JS
    )

    class Meta:
        model = Article
        fields = ["producttype", "design", "companyname", "limited_edition", "description"]

    def __init__(self, *args, **kwargs):
        """
        Extra setup bij het initialiseren van het formulier:
        - Ophalen van maten om dynamische velden te genereren als het om kleding gaat.
        """
        super().__init__(*args, **kwargs)

        # Haal alle maten op, maar sluit sizenr=99 uit
        self.sizes = Size.objects.exclude(sizenr=99)

        # Dynamisch velden toevoegen voor maten
        for size in self.sizes:
            field_name = f"size_{size.sizenr}"
            self.fields[field_name] = forms.IntegerField(
                required=False,
                min_value=0,
                initial=0,
                widget=forms.NumberInput(attrs={"class": "form-control size-input", "data-size": size.sizenr}),
                label=f"{size.size}"
            )

    def clean(self):
        """
        Validatie om te controleren of de maat (size) enkel ingevuld wordt als het producttype kleding is.
        """
        cleaned_data = super().clean()
        producttype = cleaned_data.get("producttype")

        if producttype and producttype.clothing:
            has_size = any(
                cleaned_data.get(f"size_{size.sizenr}", 0) > 0 for size in self.sizes
            )
            if not has_size:
                self.add_error(None, "You must enter at least one size quantity for clothing items.")

        return cleaned_data
