from django.db import models  # Dit is de juiste import

class Article(models.Model):
    articlenr = models.BigIntegerField(primary_key=True)
    producttype = models.ForeignKey("ProductType", on_delete=models.CASCADE, null=True)
    design = models.ForeignKey("Design", on_delete=models.SET_NULL, null=True)
    companyname = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True)
    limited_edition = models.BooleanField(default=False)
    description = models.TextField(null=True)

    def __str__(self):
        return f"Article {self.articlenr} - {self.producttype}"

    class Meta:
        db_table = "articles"
        app_label = "rts_app"

class Company(models.Model):
    companynr = models.AutoField(primary_key=True)
    companyname = models.TextField(null=True)
    address = models.TextField(null=True)
    postalcode = models.CharField(max_length=255, null=True)
    location = models.TextField(null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.companyname

    class Meta:
        db_table = "company"
        app_label = "rts_app"

class Design(models.Model):
    designnr = models.AutoField(primary_key=True)
    designname = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.designname

    class Meta:
        db_table = "designs"
        app_label = "rts_app"

class LimitedEdition(models.Model):
    lenr = models.AutoField(primary_key=True)
    le = models.TextField(null=True)

    class Meta:
        db_table = "limited_edition"
        app_label = "rts_app"

class ProductType(models.Model):
    typenr = models.AutoField(primary_key=True)
    typename = models.TextField(null=True)
    clothing = models.BooleanField(default=False)  # Nieuw veld om kleding te identificeren

    def __str__(self):
        return self.typename

    class Meta:
        db_table = "producttype"
        app_label = "rts_app"

class ReleaseYear(models.Model):
    releaseyear = models.IntegerField(null=True)

    class Meta:
        db_table = "releaseyear"
        app_label = "rts_app"

class Size(models.Model):
    sizenr = models.AutoField(primary_key=True)
    size = models.TextField(null=True)

    def __str__(self):
            if self.sizenr == 99:
                return '' 
        
            return self.size

    class Meta:
        db_table = "sizes"
        app_label = "rts_app"

class Venue(models.Model):
    venuenr = models.AutoField(primary_key=True)
    venuename = models.TextField(null=True)
    address = models.TextField(null=True)
    postalcode = models.CharField(max_length=255, null=True)
    location = models.TextField(null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.venuename

    class Meta:
        db_table = "venues"
        app_label = "rts_app"

class ArticleSize(models.Model):
    """Koppeltabel om per artikel meerdere maten en aantallen op te slaan."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.article} - {self.size} ({self.quantity})"

    class Meta:
        db_table = "article_sizes"
        app_label = "rts_app"

class ArticleSizeQuantity(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Startwaarde op 0

    class Meta:
        db_table = "article_size_quantity"
        app_label = "rts_app"
