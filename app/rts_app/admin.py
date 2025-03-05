from .models.article_models import Article, Company, Design, LimitedEdition, ProductType, ReleaseYear, Size, Venue
from .models.user import User
from django.contrib import admin


admin.site.register(Article)
admin.site.register(Company)
admin.site.register(Design)
admin.site.register(LimitedEdition)
admin.site.register(ProductType)
admin.site.register(ReleaseYear)
admin.site.register(Size)
admin.site.register(User)
admin.site.register(Venue)
