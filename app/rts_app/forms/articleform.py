import logging
from django import forms
from rts_app.models.article_models import Article, ProductType, Design, Size, Company

logger = logging.getLogger(__name__)

class ArticleForm(forms.ModelForm):
    """
    Form for creating a new article.
    This form includes fields for selecting product type, design, company,
    choosing whether the article is a limited edition, and entering sizes if it is clothing.
    """

    # Dropdown for Limited Edition: '01' = Limited Edition, '02' = Regular Edition
    LIMITED_EDITION_CHOICES = [
        ('01', 'Limited Edition'),
        ('02', 'Regular Edition'),
    ]
    limited_edition = forms.ChoiceField(
        choices=LIMITED_EDITION_CHOICES,
        required=False,
        label="Limited Edition",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    # Dropdowns for other models
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
        widget=forms.Select(attrs={"class": "form-control", "id": "id_producttype"})
    )

    class Meta:
        model = Article
        fields = ["producttype", "design", "companyname", "limited_edition"]
        error_messages = {
            'producttype': {
                'required': 'This field is required.',
            },
            'design': {
                'required': 'This field is required.',
            },
            'companyname': {
                'required': 'This field is required.',
            },
            'limited_edition': {
                'invalid_choice': 'Select a valid choice. Limited Edition is not one of the available choices.',
            },
        }

    def __init__(self, *args, **kwargs):
        """
        Extra setup when initializing the form:
        - Fetch sizes to dynamically generate fields if it is clothing.
        """
        super().__init__(*args, **kwargs)

        # Log the initial data to debug
        logger.debug("Initial data: %s", self.initial)

        # Fetch all sizes, but exclude sizenr=99
        self.sizes = Size.objects.exclude(sizenr=99)

        # Dynamically add fields for sizes
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
        Validation to check if the size is only filled in if the product type is clothing.
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
