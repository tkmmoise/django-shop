from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from shop.models import Category, Product, Article

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']
    
    def validate_price(self, value):
        if value < 1:
            raise ValidationError('Price should be greater than 1')
        return value

    def validate_product(self, value):
        if value.active is False:
            raise ValidationError('Product must be active!')
        return value


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated',  'name', 'category', 'ecoscore']
class ProductDetailSerializer(ModelSerializer):
    articles = SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated',
                  'name', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description']
    
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise ValidationError('Category already exists!')
        return value

    def validate(self, data):
        if data['name'] not in data['description']:
            raise ValidationError('Name must be in description')
        return data
class CategoryDetailSerializer(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'active', 'description',
                  'date_created', 'date_updated', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductDetailSerializer(queryset, many=True)
        return serializer.data