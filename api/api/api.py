from rest_framework import routers
from products import views as product_views

router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewset)