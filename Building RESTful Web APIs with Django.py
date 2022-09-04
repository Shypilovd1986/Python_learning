# In this project the following modules are installed.
# Django web framework
# Django REST framework for creating REST APIs
# Django-filter a dependency of Django REST framework for filtering model query sets
# Mock for creating mock in the unit test
# Pillow  for image editing

# python -m pip install Pillow
#
#
# xxxxxxxxxx       Creating a Django Rest framework serializer to serialize a model      xxxxxx

#  In general, serializing means to convert an object into format like JSON, YAML, or XML. Specifically, we want to take
#  the product model in this project and serialize it to a JSON format that is served through Our REST API. This class
#  will mock the fields from a Django model into the serialization format. We're going to serialize the id, name, price,
#  and product sales dates. Let's create the serializer .py file, and from rest_framework, we import serializers, and we
#  also import our Product model. We create a model serializer and it has a Meta class and the model is set to Product
#  and the fields that we want to serialize. Let's do something a bit more complicated. Let's modify this serialized
#  representation and add a few extra fields to it. To do this, we override the to_representation method. We call the
#  parent classes to_representation implementation, and then we add our extra fields, in this case, is_on_sale, so we
#  know whether the product is on sale or not, and this will just be a Boolean value, true or false. And then we have
#  our current_price, which is either the sale price or the regular price, depending on whether the product is currently
#  on sale. And we return the data. So with that, we've serialized the fields and we've also added two extra customized
#  fields to the serialization representation. So now we can go to the Django shell and try this out and see what
#  happens.

#                     serializers.py
# from rest_framework import serializers
#
# from store.models import Product
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end')
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['is_on_sale'] = instance.is_on_sale()
#         data['current_price'] = instance.current_price()
#         return data

# ./manage.py shell
# We're going to import our model and take the first product in the database, and then we're going to import the
# serializer that we just created, and create it, and then we serialize the product, to_representation. And now to
# actually get this into a JSON format, we're going to be importing and using the JSONRenderer. We create the renderer
# and then we actually render the serialized data. So as you can see, we serialized the product and then it became JSON
# with a JSONRenderer. The Django shell is a very important tool for rapid prototyping and testing. In production
# environments, it's common to use the Django shell for debugging problems as well.

#
#
# from store.models import Product
# product = Product.objects.all()[0]
# from store.serializers import ProductSerializer
# serializer = ProductSerializer()
# data = serializer.to_representation(product)
#
# from rest_framework.renderers import JSONRenderer
# renderer = JSONRenderer()
# renderer.render(data)


# Requirements
# Python (3.6, 3.7, 3.8, 3.9, 3.10)
# Django (2.2, 3.0, 3.1, 3.2, 4.0)
# We highly recommend and only officially support the latest patch release of each Python and Django series.
# Installation
# Install using pip...
# pip install djangorestframework
# Add 'rest_framework' to your INSTALLED_APPS setting.
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
# ]

# xxxxxxxxxxxxxxxx        Creating a ListAPIView subclass        xxxxxxxxxxxxxxxxx

# - [Instructor] We have a Serializer for products. Now let's create a List API View to use the Product Serializer. The
# API is going to return the list of products and render them into JSON. A ListAPIView is a generic class-based view.
# Django REST Framework provides a number of generic API Views and mixins that can help speed up development. We create
# the API View's file. From rest_framework.generics we import ListAPIView. We import our Serializer, and we import our
# model. Now we can create our ProductList Api View. Set the queryset to all products that exist in our database, and
# the Serializer class is the Product Serializer, which we created. And that's it. By using the generic ListAPIView, we
# only need to define a few configuration fields. The API View will take care of the rendering of the serialized data
# into the JSON format. The generic views in Django REST framework will cover what you need from a REST API in many
# cases. There are rare cases where you will want to use the base APIView to build up an API. One of those cases is if
# you really do not need, or want, any of the functionality that the generic API views provide.

#                       Django REST  Framework Generic Views
# - ListAPIView
# - CreateAPIView
# - DestroyAPIView
# - RetrieveUpdateDestroyAPIView
#
#                       api_views.py
# from rest_framework.generics import ListAPIView
#
# from store.serializers import ProductSerializer
# from store.models import Product
#
# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# xxxxxxxxxxxxxx            Connecting an APIView to a route                xxxxxxxxxxxxxxx
#
# Presently we are taking a look at how to connect the product list API view to a URL route. We start by opening up the
# URL's Configuration for the web app and we see some URLs are already in there. And now we have to connect our List API
# view, the Product List API view, to a route. And we are going to use api_views.ProductList.as_view. And we have to
# import store.api_views. That's all there is to it. This will let us send a GET request to the API V1 product's URL,
# and get back a JSON response that shows a list of products. To run the server, you have to be in the top level
# directory. So we activate virtualenv, and then we run the server. Now here's a cool way of testing to make sure the
# product's List API view is working. We switch to the browser, and we can actually try out the REST API, from the
# browser. This is what makes Django REST framework different from all other REST API frameworks. If you add a docstring
# to your API view subclass, it will actually show up in the web browser as documentation for the API. We can see that
# the list of products is showing up correctly with the model fields, and additional fields we added to the product
# serializer.

#               urls.py from main directory
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path
#
# import store.views
# import store.api_views
#
# urlpatterns = [
#     path('api/v1/products/', store.api_views.ProductList.as_view()),
#
#     path('admin/', admin.site.urls),
#     path('products/<int:id>/', store.views.show, name='show-product'),
#     path('cart/', store.views.cart, name='shopping-cart'),
#     path('', store.views.index, name='list-products'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
# xxxxxxxxxx        Filter back ends with URL query parameters       xxxxxxxxxxxxx

# Now that we have a REST API that lists products, we can add product filtering using URL query parameters. In
# particular, we are going to be filtering products by whether they match a specific product ID, or whether they are on
# sale or not. We import Django-filters, rest framework, filter backend, and then we add it to the product list. We set
# filter backends to the DjangoFilterBackend, and we set the filter fields to just the ID.

# xxxxxxxxxx      Enabling full-text search filter back end        xxxxxxxxxxxx

# Now let's enable full text search so we can search through product names and descriptions. We are going to use the
# SearchFilter, which is a filter back end built into Django REST framework. We use it in the same way as the Django
# filter back end, by adding it to the product list's filter back ends list. We import it, from REST framework filters.

#  And set up the search fields. This setting is used by the search filter back end to map from the URL query parameters
#  to the model fields of the serialized model.

#  Through the search fields variable we can also control how the search for matching text is conducted. The default
#  matching is a case insensitive partial match. We can add an equals sign if we wanted to do an exact match on the
#  search term instead of a partial match. It's also possible to use Regular Expressions for matching. For example, with
#  a partial, we could find the word ear in the middle of the word appearance. With an exact match, no match will be
#  found for the word ear. With a regular expression, we can match for the word ear at the end of the word appear.

#               from api_views.py
# from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
#
# from store.serializers import ProductSerializer
# from store.models import Product
#
# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend,SearchFilter)
#     filter_fields = ('id',)
#     search_fields = ('name', 'description')


# xxxxxxxxx     Enabling pagination of querysets in API responses     xxxxxxxxxx

#  Sometimes we may have a lot of results to return from the query set in our API response. Django REST framework
#  provides three ways to paginate results: by PageNumber, by Limit OffSet, and by Cursor. The PageNumber pagination
#  defaults to using Django's built-in paginator class and let's API consumers pass in a page number to get a page of
#  results. The LimitOffset pagination is more nuanced and let's API consumers pass in two query parameters. The Limit
# which controls how many items appear on a page and the OffSet which controls which page appears. The Cursor pagination
# uses the database cursor for paginating results. The key reason to use this is when you have very large datasets and
# using the other paginator types would be to inefficient.

#  Now let's add pagination to our product list API view. From REST framework, we import the pagination type we're going
#  to use which is Limit OffSet pagination. And we create our own new pagination subclass ProductsPagination. We set a
# default limit of 10 search results and a max limit of 100. The max limit is the maximum size of a page that can be set
# by the API client. Now we can use this custom pagination class for the product list API view. This will add support
# for the Limit and OffSet URL query parameters which we can adjust in order to show fewer or more products. With the
# server already running, we can try this out in the browser. We can see the full list of products. Now let's see what
# happens when we set the URL parameter Limit to one. We narrow the view to just one product per page. The other thing
# to notice is that the next field provides a link to the next page of results. Now let's try setting the Limit to two
# and the OffSet to one. We can see that we are actually between two pages. So you can see with the Limit and OffSet
# pagination style, we have more control over the number of items appearing in the results and which set of products
# appears. And that's how we paginate an API view with Django REST framework.
#
# http://127.0.0.1:4000/api/v1/products/?limit=1
# http://127.0.0.1:4000/api/v1/products/?limit=2&offset=2
# limit is parameter which shows count of products on page
# offset is paramater which shows number of page

#                   api_views.py
# from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import LimitOffsetPagination
#
# from store.serializers import ProductSerializer
# from store.models import Product
#
# class ProductPagination(LimitOffsetPagination):
#     default_limit = 10
#     max_limit = 100
#
#
# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     filter_fields = ('id',)
#     search_fields = ('name', 'description')
#     pagination_class = ProductPagination

# xxxxxxxxxx      Creating a CreateAPIView subclass      xxxxxxxxxx

# Now we want the ability to create new products through the API. In the API views we will create the product creation
# API view. From REST framework we're going to import the exceptions that we need, and import the create API view. The
# bottom of the file we're going to create our new product creation, API view. Reusing our serialiser class. And then
# overwriting the creating method. We're going to extract the price from the parameters. We're going to ensure that the
# price is set And that the price is above $0, so that it is not free. If either of these conditions fail, we just raise
# a validation error on the price field, saying must be above $0. We also ... cache the value error exception just in
# case parsing the price doesn't work. And then we'll erase another validation error, and we say that the price needs to
# be a number. After that we just call super and create. The validation of the price is to prevent anyone using the REST
# API from accidentally creating a product that's free. Note that when raising a validation error, you can attach a
# custom error message to a specific field. This is why REST APIs are powerful. Instead of creating models through the
# admin interface, we can use the API to build new interfaces that are very specific to certain scenarios. Once scenario
# that I have encountered many times in real world projects, has been importing products from an Excel spreadsheet. It's
# possible to load product data from each row in a spreadsheet and simply use the REST API to create the product.
# REST APIs can be used to create a lot of data much more quickly than through our user-friendly web interface. You can
# check out course called Learning REST APIs in the library if you want to learn more.

# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import ListAPIView, CreateAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import LimitOffsetPagination
#
# from store.serializers import ProductSerializer
# from store.models import Product
#
# class ProductPagination(LimitOffsetPagination):
#     default_limit = 10
#     max_limit = 100
#
#
# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     filter_fields = ('id',)
#     search_fields = ('name', 'description')
#     pagination_class = ProductPagination
#
# class ProductCreate(CreateAPIView):
#     serializer_class = ProductSerializer
#
#     def create(self, request, *args, **kwargs):
#         try:
#             price = request.data.get('price')
#             if price is not None and float(price) <= 0.0:
#                 raise ({'price': 'Must be above $0.0'})
#         except ValueError:
#             raise ValidationError({'price': 'A valid number is required'})
#         return super().create(self, request, *args, **kwargs)


# xxxxxxxxxx     Connecting a CreateAPIView to the router         xxxxxxxxxxxx

# Now we can create a route in the URL configuration for creating a product through the product create API view. We add
# a new URL path that points to the product create view. With that done, let's run the server. To test the API to create
# a new product, let's use the curl command on the console. We set the method to post and point to the API URL that we
# just added. We set the price to one dollar, set the product name to 'My Product', and set the description 'Hello
# World'. As you can see we get a response from the API indicating that the product was created. This is something I do
# very often when I work with Rust APIs. The development team shares the curl scripts with each other so we can quickly
# create new models and test APIs to make sure they are working correctly. Now, let's see how this looks in the browser.
# Django REST Framework provides a nice interface that makes it easy for us to test creating new products. So you can
# see we have a nice form with multiple fields for the product model that we can enter and then create another product.

#  curl -X POST http://127.0.0.1:7000/api/v1/products/new -d price=1.00 -d name='My product' -d description='Some
#  description'

#                       urls.py
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path
#
# import store.views
# import store.api_views
#
# urlpatterns = [
#     path('api/v1/products/', store.api_views.ProductList.as_view()),
#     path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
#
#     path('admin/', admin.site.urls),
#     path('products/<int:id>/', store.views.show, name='show-product'),
#     path('cart/', store.views.cart, name='shopping-cart'),
#     path('', store.views.index, name='list-products'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# xxxxxxxxxxxxx         Creating a DestroyAPIView subclass       xxxxxxxxxxxxxxxxx

# We can use the generic view DestroyAPIView to create an API for that. We import it, and then we create our DestroyView
# We set the queryset to All Products and the lookup_field to id. There isn't much to creating an API View to destroy an
# object. We just need to set the queryset and the lookup field. In a real world situation, however, a product being
# destroyed may also mean that all caches that store data related to that product have to be cleared. Clearing the cache
# when a model is destroyed frees up cache space for other objects that are more likely to be used. Let's see how that
# looks. We override the delete method, we extract the product_id from the request, we proceed with deleting the object,
# and if the product was deleted successfully, we're going to import the django.cache and delete the product_data from
# the cache. Then we just return to response, as per usual, and that's it. And that's how we create a DestroyAPIView
# with additional complex logic in the delete method.

#               api_view.py
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import LimitOffsetPagination
#
# from store.serializers import ProductSerializer
# from store.models import Product
#
# class ProductPagination(LimitOffsetPagination):
#     default_limit = 10
#     max_limit = 100
#
# class ProductDestroy(DestroyAPIView):
#     queryset = Product.objects.all()
#     lookup_field = 'id'
#
#     def delete(self, request, *args, **kwargs):
#         product_id = request.data.get('id')
#         response = super().delete(self, request, *args, **kwargs)
#         if response.status_code == 204:
#             from django.core.cache import cache
#             cache.delete('product_data_{}'.format(product_id))
#         return response
#
# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     filter_fields = ('id',)
#     search_fields = ('name', 'description')
#     pagination_class = ProductPagination
#
#     def get_queryset(self):
#         on_sale = self.request.query_params.get('on_sale', None)
#         if on_sale is None:
#             return super().get_queryset()
#         queryset = Product.objects.all()
#
#         if on_sale.lower() == 'true':
#             from django.utils import timezone
#             now = timezone.now()
#             return queryset.filter(
#                 sale_start__lte=now,
#                 sale_end__gte=now
#             )
#         return queryset
#
#
# class ProductCreate(CreateAPIView):
#     serializer_class = ProductSerializer
#
#     def create(self, request, *args, **kwargs):
#         try:
#             price = request.data.get('price')
#             if price is not None and float(price) <= 0.0:
#                 raise ({'price': 'Must be above $0.0'})
#         except ValueError:
#             raise ValidationError({'price': 'A valid number is required'})
#         return super().create(self, request, *args, **kwargs)


# xxxxxxxx          Connecting a DestroyAPIView to the router       xxxxxxxxxxxxxx

# Let's connect the destroy product API view to the router, so that we can start using it in our API. In the URL's
# configuration we add a new URL path with the lookup field so that we can destroy a product using the ProductDestroy
# API view. With the server running let's try this out on the browser. First we find the ID of an existing product, and
# then we can delete the product. We click the destroy button and confirm the action. We can also delete products
# through a curl command on the command line.
# curl -X DELETE http://localhost:7001/api/v1/products/2/destroy

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path
#
# import store.views
# import store.api_views
#
# urlpatterns = [
#     path('api/v1/products/', store.api_views.ProductList.as_view()),
#     path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
#     path('api/v1/products/<int:id>/destroy', store.api_views.ProductDestroy.as_view()),
#
#     path('admin/', admin.site.urls),
#     path('products/<int:id>/', store.views.show, name='show-product'),
#     path('cart/', store.views.cart, name='shopping-cart'),
#     path('', store.views.index, name='list-products'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# xxxxxxxxxxxxxx      Creating an UpdateAPIView subclass         xxxxxxxxxxxxxx
#
# And what if we also wanted to update and individual products data, whether fully updating it or partially updating it?
# We would again have to create another APIView this time using UpdateAPIView. But why do all of that when we can just
# use Django rest frameworks generic view that combines all of those. With the RetrieveUpdateDestroyAPIView we cam reuse
# code and configuration. For example, the serialiszer_class or queryset and other configuration options for generic
# views. And on top of that we can use One URL to handle multiple HTTP methods. To allow for this combination of actions
# we're going to re-factor the ProductDestroyAPIView into the RetrieveUPdateDestroyAPIView. We need to import it
# (typing) and then re-factor the ProductDestroy class. We rename it (typing) to ProductRetrieveUpdateDestroy to
# ProductRetrieveUpdateDestroy and we also change the parent class and we also add the serializer class. (typing) The
# delete method will stay the same, but we want it to update the product. So, we override the update method. (typing) We
# call the super update method (typing) and if the product was updated correctly (typing) we're going to use the cache
# again to mirror what we did in the delete method. (typing) So, you use cache.set to store product data in the cache.
# (typing) We store the name of the product, (typing) the description (typing) of the product (typing) and its price.
# (typing) Then we return the response. Cool. Now that we re-factored the DestroyAPIView we can have one RestAPIN point
# to interact with the product where we can retrieve update or destroy it.

# class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     lookup_field = 'id'
#     serializer_class = ProductSerializer
#
#
#     def delete(self, request, *args, **kwargs):
#         product_id = request.data.get('id')
#         response = super().delete(self, request, *args, **kwargs)
#         if response.status_code == 204:
#             from django.core.cache import cache
#             cache.delete('product_data_{}'.format(product_id))
#         return response
#
#     def update(self, request, *args, **kwargs):
#         response = super().update(self, request, *args, **kwargs)
#         if response.status_code==200:
#             from django.core.cache import cache
#             product=response.data
#             cache.set('product_data_{}'.format(product['id']), {
#                 'name':product['name'],
#                 'description': product['description'],
#                 'price': product['price']
#             })
#         return response

# xxxxxxxxx      Connecting an UpdateAPIView to the router     xxxxxxxxxx

# We refactored the destroy API view and now we have to update the URL configuration to reflect the refactoring. In our
# URL patterns configuration, we are going to remove the destroy API view and replace it with the retrieve update
# destroy API view. First we replace the view and we update the URL and that's it. Now let's see how this looks in the
# browser. Go to one product and retrieve its data. As you can see, we have retrieve, update, and destroy. Let's try
# changing the name. So we renamed the product and we can also change the price. And now let's delete this product. As
# you can see, we use Django REST framework's built in views, to make implementing common REST API operations very quick
# and easy to do.

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path
#
# import store.views
# import store.api_views
#
# urlpatterns = [
#     path('api/v1/products/', store.api_views.ProductList.as_view()),
#     path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
#     path('api/v1/products/<int:id>/', store.api_views.ProductRetrieveUpdateDestroy.as_view()),
#
#     path('admin/', admin.site.urls),
#     path('products/<int:id>', store.views.show, name='show-product'),
#     path('cart/', store.views.cart, name='shopping-cart'),
#     path('', store.views.index, name='list-products'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# xxxxxxxxxx      Serializer with only selected fields        xxxxxxxxxxxxxx
#
# In the product serializer, we already have selected some fields for rendering through the serializer. However, we can
# do a little bit of refactoring to simplify how we added custom field data. We can take the attributes that we set in
# the two representation method and refactor them using serializer fields. We have a boolean field for is on sale. It is
# a read-only field. And for the current price, we have a float field which is also read-only. We can now delete two
# representation and add the fields to metafields so that they appear in the serializer. The read-only serializer field
# configuration parameter sets whether or not we can write to the field through the serializer. Another example of a
# serializer field configuration is the source keyword argument. This can be used if you want to rename a field. For
# instance, if you want the rest API to return a field called 'product name' rather than just 'name'. Back to the code,
# we can add a description field that overrides the serializer field for description with a char field. We set the
# minimum length to two and the max length to 200. So now we have validation for this field and the field is already in
# metafields and we can try this out in the browser. So if we look at the product here, we have is on sale in current
# price still there and we have the description field and now we can try and change the description to a single letter
# A and see that it fails with the proper validation. It has to be at least two characters and we can say hello world
# and see that it still works.

#                   serializers.py
# from store.models import Product
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price'
#         )

# xxxxxxxxxxxxxx     Serializer that shows model relationships      xxxxxxxxxxxxxxx

#  For each user shopping on our e-commerce site they will be putting products into shopping carts. But from a developer
#  perspective, we have multiple shopping carts to look at. We have some questions, we want to answer, so that we can
#  build a sales report. Questions, such as "How many vitamins were sold in total?" and "What was the average number of
#  mineral water bottles added to a shopping cart?" Now imagine trying to do this for thousands of shopping carts. We
#  need to first create a Shopping Cart Item Serializer. It is also a Model Serializer. And in the Meta, we set up the
#  Model, as the Shopping Cart Item. And the Fields, as the Product and the Quantity. We import Shopping Cart Item from
#  the models, then we add Cart Items, as a Field to the Product Serializer. And it is a Serializer Method Field. We add
#  this new Field to the Meta Fields variable. And then we define the method that will actually return the Shopping Cart
#  Items where this Cart Items' Field. So the Items all belong to this Product. And then we return the Cart Item
#  Serializer with those Items serialiazed into a list. The Serializer Method Field will by default call the method, Get
#  "underscore" cart item. For other fields, it will use the Get "underscore" as a prefix to the field name. In the Get
#  cart item's method, the Many parameter is used to control whether one cart item is serialized or whether a list
#  serializer is automatically created to serialize a collection of cart items.

# many = True , creates list of serialized model instances
# many = False , (the default), will serialize only one model instance

# from rest_framework import serializers
#
# from store.models import Product, ShoppingCartItem
#
# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShoppingCartItem
#         fields = ('product', 'quantity')
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     cart_items = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price', 'cart_items'
#         )
#
#     def get_cart_items(self, instance):
#         items = ShoppingCartItem.objects.filter(product=instance)
#         return CartItemSerializer(items, many=True).data


# in command shell , python manage.py shell
# import json
# from store.models import *
# from store.serializers import *
# product = Product.objects.all().first()
#  cart = ShoppingCart()
# cart.save()
# item = ShoppingCartItem(shopping_cart=cart, product = product, quantity=5 )
# item.save()
# serializer = ProductSerializer(product)
# print(json.dumps(serializer.data, indent=2))


# xxxxxxxxxxx         Number fields with serializers            xxxxxxxxxxxx

# - [Lecturer] We are now going to use number fields with the product serializer. Let's update the CartItemSerializer
# first with an IntegerField for the quantity. We're going to ensure that only between one and 100 items of a particular
# type can be added to the shopping cart. And now for products, we want to ensure that whenever we create or update them
# through the API, that the minimum price is set to at least $1 and the maximum price is never more than $100,000. We
# can do this through the FloatField Configuration keyword arguments, min_value and max_value. For example, most e-
# commerce sites will only allow free items through 100% off coupons and discount codes, such as the Bungie store
# website for the Destiny game which uses a very large price for products that require a discount code. Now let's
# implement the FloatField for the product price. We set the min_value to $1 and the max_value to 100,000. The
# DecimalField is more powerful than the FloatField and actually is in better alignment with what we want to do when
# storing prices. The configuration for the FloatField only allows a minimum and maximum value to be validated.
# In contrast, the configuration for the DecimalField allows the control of the resolution of the number and whether
# there's rounding of the number and the number of decimal places. So we copy this over and we change FloatField to
# DecimalField and we set the max_digits to none and the decimal_places to two. Now let's try and update a product price
# in the browser. So we can see our current price is 100. And now we're going to set it to 299.999, which is three
# decimal places and recall that we just set it to a maximum of two decimal places and we can see an error message shows
# up, exactly in that field, so we'll just remove one and set it and now our price is correctly updated, and we tested
# the validation. Exactly what we want.

# from rest_framework import serializers
#
# from store.models import Product, ShoppingCartItem
#
# class CartItemSerializer(serializers.ModelSerializer):
#     quantity = serializers.IntegerField(min_value=1, max_value= 100)
#
#     class Meta:
#         model = ShoppingCartItem
#         fields = ('product', 'quantity')
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     cart_items = serializers.SerializerMethodField()
#     price = serializers.FloatField(min_value=1.0, max_value=100000.0)
#     price = serializers.DecimalField(
#         min_value=1.0, max_value=100000.0,
#         max_digits= None, decimal_places=2
#     )
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price', 'cart_items'
#         )
#
#     def get_cart_items(self, instance):
#         items = ShoppingCartItem.objects.filter(product=instance)
#         return CartItemSerializer(items, many=True).data


# xxxxxxxxxxxx       Date and time fields with serializers         xxxxxxxxxxx

# input_formats    for the date/time input formats , default is iso-8601
# format     is the output format (default is DateTime object)
# help_text     that  appears in the browser for the REST API
# style    controls how the field appears in the browser for the REST API (place holder and input_type can be set with
# this )

#  Now we want to be able to set the sales dates for our product through the REST API. We are going to use the DateTime
#  field to set the start and end dates of a sale. A Date/Time field can be configured with its input format, the output
# format, the help text, and style. Let's override the sales start and sale end fields in the Product Serializer. So the
# sale start is a DateTimeField, and we're setting the input formats. I'm setting the format to None, and we will allow
# null, it's not a required field, and we are also setting up the help text with the accepted format, and the style that
# will render this field with a nice placeholder and then we'd do the same for the sale end field. The output format is
# set to none, so that the sale start date and end date are always DateTime objects. The input formats list can contain
# any custom format that is accepted by Python's string to time conversion function. The default is iso-8601, but we are
# using a custom format that accepts the hour, minute, whether it's the AM or PM for the hour, and then the day, month,
# and year, in that order. Let's try it out in the browser. We can see that the sale start and end here are set to null.
# And in the field here we have the placeholder, and we also have our help text, and now we can enter 12:01 AM and
# 11:59 PM and so the sale here will run for one day, and we save it and we can see that when it is stored, it's stored
# in the iso-8601 format, and here again our accepted format is our custom format.

# from rest_framework import serializers
#
# from store.models import Product, ShoppingCartItem
#
# class CartItemSerializer(serializers.ModelSerializer):
#     quantity = serializers.IntegerField(min_value=1, max_value= 100)
#
#     class Meta:
#         model = ShoppingCartItem
#         fields = ('product', 'quantity')
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     cart_items = serializers.SerializerMethodField()
#     # price = serializers.FloatField(min_value=1.0, max_value=100000.0)
#     price = serializers.DecimalField(
#         min_value=1.0, max_value=100000.0,
#         max_digits=None, decimal_places=2
#     )
#     sale_start = serializers.DateTimeField(
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#     sale_end = serializers.DateTimeField(
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price', 'cart_items',
#         )
#
#     def get_cart_items(self, instance):
#         items = ShoppingCartItem.objects.filter(product=instance)
#         return CartItemSerializer(items, many=True).data

#
# xxxxxxxxxxxxxxxxxx      Lists, dicts, and JSON objects        xxxxxxxxxxxxxxxx

# ] In order to gather daily, weekly, or monthly product and shopping cart data for our sales report, we need to create
# a new serializer that uses composite fields. We start by creating the new serializer. It is not a model serializer.
# It's just a plain serializer, because it's not tied to any specific model. So, it only contains one field. It's a
# DictField, which has the child parameter set to a ListField, which has its own child parameter set to an IntegerField

#  So, this is a composite of a composite field. The dictionary keys will be the date as a string. For each value in the
#  dictionary, we're expecting a list of numbers which is the quantity from each shopping cart that the product appeared
#  in. Next, we create a generic API view. We import GenericAPIView. We import the rest_framework_response object. And
#  then, we also import our ProductStatSerializer. Now we can create our stat API view, ProductStats The lookup field is
#  the product id. The serializer class is the ProductStatSerializer. And the queryset is all products. We override the
#  get method. We get the object, which is a product. We load up the serializer and provide it with our fake sales data.
#  And then the stats field, and then we have the date key with the sales data, list of numbers. And another date. And
#  another list of numbers. And then we return a response with that serialized data. Now we add the APIView to our URLs.
#  We create a new path with the lookup ID, and ending with stats. With the server already running, let's see how these
# composite fields look like in the browser. As you can see, the data that comes back is structured as a dictionary with
# a list of numbers. It's also all stored under the stats field. With the data we have here, there's no one-to-one
# mapping between the sales data and the product model, or the shopping cart item model. For example, we can group sales
# data from multiple product categories rather than for just one product like this. Composite fields are highly useful
# when you're trying to return data that needs to be structured in a specific way that may not map to any model.

# from rest_framework import serializers
#
# from store.models import Product, ShoppingCartItem
#
# class CartItemSerializer(serializers.ModelSerializer):
#     quantity = serializers.IntegerField(min_value=1, max_value= 100)
#
#     class Meta:
#         model = ShoppingCartItem
#         fields = ('product', 'quantity')
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     cart_items = serializers.SerializerMethodField()
#     # price = serializers.FloatField(min_value=1.0, max_value=100000.0)
#     price = serializers.DecimalField(
#         min_value=1.0, max_value=100000.0,
#         max_digits=None, decimal_places=2
#     )
#     sale_start = serializers.DateTimeField(
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#     sale_end = serializers.DateTimeField(
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price', 'cart_items',
#         )
#
#     def get_cart_items(self, instance):
#         items = ShoppingCartItem.objects.filter(product=instance)
#         return CartItemSerializer(items, many=True).data
#
# class ProductStatSerializers(serializers.Serializer):
#     stats = serializers.DictField(
#         child=serializers.ListField(
#             child=serializers.IntegerField(),
#         )
#     )


#                   api_views.py
#
# class ProductsStat(GenericAPIView):
#     lookup_field = 'id'
#     serializer_class = ProductStatSerializers
#     queryset = Product.objects.all()
#
#     def get(self, request, format=None, id=None):
#         obj = self.get_object()
#         serializer = ProductStatSerializers({
#             'stats': {
#                 '2019-01-01': [5, 10, 15],
#                 '2019-01-02': [],
#             }
#         })
#         return Response(serializer.data)

#     urls.py
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path
#
# import store.views
# import store.api_views
#
# urlpatterns = [
#     path('api/v1/products/', store.api_views.ProductList.as_view()),
#     path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
#     path('api/v1/products/<int:id>/', store.api_views.ProductRetrieveUpdateDestroy.as_view()),
#     path('api/v1/products/<int:id>/stats', store.api_views.ProductsStats.as_view()),
#
#     path('admin/', admin.site.urls),
#     path('products/<int:id>', store.views.show, name='show-product'),
#     path('cart/', store.views.cart, name='shopping-cart'),
#     path('', store.views.index, name='list-products'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
#  xxxxxxxxxxxx     Serializer with ImageField and FileField         xxxxxxxxxxxxxxxxx

# Serializer Field Configuration write_    only=True    means a field can be written to but will not appear in any API
# response

# Through the REST API we should be able to update existing product images or upload new product photos. So, let's add
# the photo field. Go to the product serializer. We add the photo field. And we add it to the list of fields... in meta.
# Recall that serializer fields can be set as read-only. They can also be set as write-only. This means that when we
# write to the field the data does not get saved to the model. Now let's do something more interesting. We're going to
# allow the uploading of a warranty file for a product. We use the file field for this, but since the product model does
# not have a warranty file field in the model itself, we're going to be adding the write-only configuration option.
# We're going to override... the update method, so that we can make use of the warranty field. If a warranty file is
# supplied, we're going to add it to the description of the product. We read-in all the lines from the file, and then we
# return the instance. Validated data in the update method is the data that will be used to update the model. It is safe
# to access because it is already passed through the validation process. So we know, for example, that the price of the
# product here is between $1 and $100,000 and that the description is between two and 200 characters. Cool, let's try
# this out in the browser. So, as you can see right now we don't have the photo or warranty fields. When we reload we
# have the photo field appearing. And now let's upload a warranty file. As you can see the product description has been
# updated with the warranty information.

# from rest_framework import serializers
#
# from store.models import Product, ShoppingCartItem
#
# class CartItemSerializer(serializers.ModelSerializer):
#     quantity = serializers.IntegerField(min_value=1, max_value= 100)
#
#     class Meta:
#         model = ShoppingCartItem
#         fields = ('product', 'quantity')
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     cart_items = serializers.SerializerMethodField()
#     # price = serializers.FloatField(min_value=1.0, max_value=100000.0)
#     price = serializers.DecimalField(
#         min_value=1.0, max_value=100000.0,
#         max_digits=None, decimal_places=2
#     )
#     sale_start = serializers.DateTimeField(
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#     sale_end = serializers.DateTimeField(
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#     photo = serializers.ImageField(default=None)
#     warranty = serializers.FileField(write_only=True, default=None)
#
#
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price', 'cart_items', 'photo'
#         )
#
#     def get_cart_items(self, instance):
#         items = ShoppingCartItem.objects.filter(product=instance)
#         return CartItemSerializer(items, many=True).data
#
#     def update(self, instance, validated_data):
#         if validated_data.get('warranty', None):
#             instance.discription += '\n\nWarranty Information :\n'
#             instance.description += b';'.join(
#                 validated_data['warranty'].readlines()
#             ).decode()
#         return instance


# xxxxxxxxxxxxx      Testing API View      xxxxxxxxxxxxxxxx

# xxxxxxxxxxxxx      Test case for a CreateAPIView subclass        xxxxxxxxxxxxxx

# Django REST framework  has four types of API test cases

# APISimpleTestCase
# APITransactionTestCase
# APITestCase
# APILiveServerTestCase
#
# Use the JSON format when testing API client request
# self.client.post(url, data, format='json')


#                   test.py
# from rest_framework.test import APITestCase
#
# from store.models import Product
#
# class ProductCreateTestCase(APITestCase):
#     def test_create_product(self):
#         initial_product_count = Product.objects.count()
#         product_attrs = {
#             'name': 'New product',
#             'description': 'Awesome product',
#             'price': '123.45',
#         }
#         response = self.client.post('api/v1/products/new/', product_attrs)
#         if response.status_code != 201:
#             print(response.data)
#         self.assertEqual(
#             Product.objects.count(),
#             initial_product_count +1,
#         )
#         for attr, expected_value in product_attrs.items():
#             self.assertEqual(response.data[attr], expected_value)
#         self.assertEqual(response.data['is_on_sale', False])
#         self.assertEqual(
#             response.data['current_price'],
#             float(product_attrs['price']),
#         )


#               serialisers.py

# Testing Django REST framework API views is a bit different compared to testing Django views. Django REST framework
# provides test case classes. Each of the test case classes implements the same interface as Django's test cases.
# However, they use Django REST framework's HTTP client instead of Django's client to specifically test API views. We
# are going to write a unit test for the create product API. Instead of importing test case from Django we import API
# test case from REST framework. We import our product model, and then we begin to write our test. We keep track of the
# initial product count, and we're going to be creating a new product with a specific name, description, and a price.
# We're going to be checking the response from the client, and POSTing to the product's new endpoint. If for whatever
# reason we couldn't create a new product, we're going to print out whatever response we got, so that we can see if
# there's an invalid field or any other information. We're going to make sure a new product was created, by checking the
# count of all products, against initial product count, and then we're going to be checking the values that were set for
# the product, and making sure they're set exactly right. We also have some custom fields, so we want to make sure
# they're values are correct as well. The product is not on sale, so this should be false, and the product's current
# price should be equal to the price we initially set. In the real world, with customized REST APIs, there could be a
# lot of additional custom fields added. This is done so that clients of the API have access to more data. However, we
# need to thoroughly test this custom data that's added to API responses to ensure that API consumers do not fail, or
# crash. So now let's run the test and see what happens. So we can see that the tests are failing, and the product is
# not created because the sale start and sale end fields are required. So let's fix this by going to the serializers
# file, and making both of those fields optional, by setting required is false. We do the same for sale end, and then we
# go back here and run the test again. So it looks like we have a new error, and this time it's the warranty field that
# is affected and the error is that the warranty is not part of product creation. So we have to go back to the
# serializer and implement the create method, and the new implement the create method which is similar to the update
# method. We're going to remove the warranty from the validated data, and then return the product as created without
# that warranty field. So now let's try running the tests again, It looks like everything passes, awesome.

# from rest_framework import serializers

#
# from store.models import Product, ShoppingCartItem
#
# class CartItemSerializer(serializers.ModelSerializer):
#     quantity = serializers.IntegerField(min_value=1, max_value= 100)
#
#     class Meta:
#         model = ShoppingCartItem
#         fields = ('product', 'quantity')
#
# class ProductSerializer(serializers.ModelSerializer):
#     is_on_sale = serializers.BooleanField(read_only=True)
#     current_price = serializers.FloatField(read_only=True)
#     description = serializers.CharField(min_length=2, max_length=200)
#     cart_items = serializers.SerializerMethodField()
#     # price = serializers.FloatField(min_value=1.0, max_value=100000.0)
#     price = serializers.DecimalField(
#         min_value=1.0, max_value=100000.0,
#         max_digits=None, decimal_places=2
#     )
#     sale_start = serializers.DateTimeField(
#         required=False,
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#     sale_end = serializers.DateTimeField(
#         required=False,
#         input_formats=['%I: %M %p %d %B %Y'], format=None, allow_null=True,
#         help_text='Accepted format is "12:01 PM 16 April 2019"',
#         style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019 '},
#     )
#
#     photo = serializers.ImageField(default=None)
#     warranty = serializers.FileField(write_only=True, default=None)
#
#
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end',
#                   'is_on_sale', 'current_price', 'cart_items', 'photo'
#         )
#
#     def get_cart_items(self, instance):
#         items = ShoppingCartItem.objects.filter(product=instance)
#         return CartItemSerializer(items, many=True).data
#
#     def update(self, instance, validated_data):
#         if validated_data.get('warranty', None):
#             instance.discription += '\n\nWarranty Information :\n'
#             instance.description += b';'.join(
#                 validated_data['warranty'].readlines()
#             ).decode()
#         return instance
#
#     def create(self, validated_data):
#         validated_data.pop('warranty')
#         return Product.objects.create(**validated_data)
#
# class ProductStatSerializers(serializers.Serializer):
#     stats = serializers.DictField(
#         child=serializers.ListField(
#             child=serializers.IntegerField(),
#         )
#     )

# xxxxxxxxxxxxx        Test case for a DestroyAPIView subclass          xxxxxxxxxxxxxx

# We tested creating products through the API, so let's test destroying and deleting products through the API. We write
# a new test case (typing) for ProductDestroy. (typing) We're going to be checking the product count... (typing) and
# making sure that the product doesn't exist anymore (typing) after we delete it. So we use the client, called the
# delete method, on it, (typing) and then we make sure that there's one less object in the database. (typing) And we
# also make sure that if we try and retrieve that particular product, it no longer exists. (typing) In the real world,
# we would also check to ensure that caches or any other data related to the product model are also destroyed and
# cleaned up. So now let's run the test. (typing) It looks like all test paths and products can be deleted.

#                       test.py
# class ProductDestroyTestCase(APITestCase):
#     def test_delete_product(self):
#         initial_product_count = Product.objects.count()
#         product_id = Product.objects.first().id
#         self.client.delete('/api/v1/products/{}/'.format(product_id))
#         self.assertEqual(
#             Product.objects.count(),
#             initial_product_count - 1,
#         )
#         self.assertRaises(
#             Product.DoesNotExist,
#             Product.objects.get, id =  product_id,
#         )

# xxxxxxxxxxxx        Test case for a ListAPIView subclass       xxxxxxxx

#  Let's write a test case for the list of products from the API. ProductListTestCase is the name and it also uses the
#  APITestCase. We're going to keep track of the product's count. And we are checking the response for call and get on
#  the products list. And we are asserting that all the pagination fields exist and that they are the right values. And
#  we're checking that the number of products is correct, not only in the count but in the results themselves. Notice
#  that we don't have to check each product, because we are already testing the product serializer in another test case.
#  Now we run the tests and it looks like they all passed.

#                   test.py
# class ProductListTestCase(APITestCase):
#     def test_list_product(self):
#         products_count = Product.objects.count()
#         response = self.client.get('api/v1/products/')
#         self.assertIsNone(response.data['next'])
#         self.assertIsNone(response.data['previous'])
#         self.assertEqual(response.data['count',  products_count])
#         self.assertEqual(len(response.data['results']), products_count)

# xxxxxxxxxxx         Unit test for an UpdateAPIView subclass       xxxxxxxxx

# We write another API test case. And this one is going to be using the PATCH method for partially updating the model.
# Going to grab the first product, and then, we call PATCH from the client, pointing to that specific product's API URL.
# We're going to be updating the name to new product, updating the description, and then updating the price. Format of
# the request is JSON, and then we retrieve the updated product from the database, and we're going to make sure that the
# name has actually updated. Now let's run the test and see what happens. It looks like the product's data doesn't
# update. So let's try and fix this. Let's go to the serializers, and it looks like an issue with the product serializer
# and in the UPDI method, it looks like we update the data with the warranty information, but then we actually forget to
# call the super method, so that the product is updated correctly. So let's do that now. Now with this change, let's try
# running the tests again. Looks like it works.

#                   tests.py
# class ProductUpdateTestCase(APITestCase):
#     def test_update_product(self):
#         product = Product.objects.first()
#         response = self.client.patch(
#             'api/v1/products/{}'.format(product.id),
#             {
#                 'name': 'New product',
#                 'description': 'Awesome product',
#                 'prie': 123.34,
#             },
#             format='json',
#         )
#         updated = Product.objects.get(id=product.id)
#         self.assertEqual(updated.name, 'New product')

#                   serialisers.py
#     def update(self, instance, validated_data):
#         if validated_data.get('warranty', None):
#             instance.discription += '\n\nWarranty Information :\n'
#             instance.description += b';'.join(
#                 validated_data['warranty'].readlines()
#             ).decode()
#         return super().update(instance, validated_data)


# xxxxxxxxxx          Handling image uploads in a unit test         xxxxxxxxxxxxx

# We're able to update the product, so let's test updating a product with a new product image upload. We begin by
# importing OS.Path, since we are dealing with files and images. And we're going to import Django settings. And then we
# go to the product update Test Case, and we add a New Test Case to it, for Upload Product Photo. We're going to use the
# first product in the database. We're going to store the original photo. And then we're going to create the Path to the
# new photo, and just re-use an existing product photo from our Media Root. And then, with that photo, Path open, going
# to to store that photo data, and use it to update the product photo. And the format is not Json, but it is Multipart
# because it is an upload. And immediately after that, we're going to be checking to ensure that the Response Status
# Code was a 200 and okay. After that, we want to make sure that the photo from the response is no longer the original
# photo. We also want to try an assertion here, we're going to check the updated product from the database. And we're
# going to construct the Expected Photo Path. And then we're going to try and assert that the new Updated Photo Path
# starts with the Expected Photo Path. And finally, if we had any issues with this, we want to make sure that the new
# photo, the newly update photo is always deleted. Let's try running the test. As you can see, it works. For your own
# projects, it's very important to check file and image uploads are working because failed uploads are very noticeable
# and can cause a bad user experience.

# import os.path
# from django.conf import settings
#
# from rest_framework.test import APITestCase
#
# from store.models import Product
#
# class ProductCreateTestCase(APITestCase):
#     def test_create_product(self):
#         initial_product_count = Product.objects.count()
#         product_attrs = {
#             'name': 'New product',
#             'description': 'Awesome product',
#             'price': '123.45',
#         }
#         response = self.client.post('api/v1/products/new/', product_attrs)
#         if response.status_code != 201:
#             print(response.data)
#         self.assertEqual(
#             Product.objects.count(),
#             initial_product_count +1,
#         )
#         for attr, expected_value in product_attrs.items():
#             self.assertEqual(response.data[attr], expected_value)
#         self.assertEqual(response.data['is_on_sale', False])
#         self.assertEqual(
#             response.data['current_price'],
#             float(product_attrs['price']),
#         )
#
# class ProductDestroyTestCase(APITestCase):
#     def test_delete_product(self):
#         initial_product_count = Product.objects.count()
#         product_id = Product.objects.first().id
#         self.client.delete('/api/v1/products/{}/'.format(product_id))
#         self.assertEqual(
#             Product.objects.count(),
#             initial_product_count - 1,
#         )
#         self.assertRaises(
#             Product.DoesNotExist,
#             Product.objects.get, id =  product_id,
#         )
#
# class ProductListTestCase(APITestCase):
#     def test_list_product(self):
#         products_count = Product.objects.count()
#         response = self.client.get('api/v1/products/')
#         self.assertIsNone(response.data['next'])
#         self.assertIsNone(response.data['previous'])
#         self.assertEqual(response.data['count',  products_count])
#         self.assertEqual(len(response.data['results']), products_count)
#
# class ProductUpdateTestCase(APITestCase):
#     def test_update_product(self):
#         product = Product.objects.first()
#         response = self.client.patch(
#             'api/v1/products/{}'.format(product.id),
#             {
#                 'name': 'New product',
#                 'description': 'Awesome product',
#                 'prie': 123.34,
#             },
#             format='json',
#         )
#         updated = Product.objects.get(id=product.id)
#         self.assertEqual(updated.name, 'New product')
#
#     def test_upload_product_photo(self):
#         product = Product.objects.first()
#         original_photo = product.photo
#         photo_path = os.path.join(
#             settings.MEDIA_ROOT, 'products', 'vitamin-iron.jpg',
#         )
#         with open(photo_path, 'rb') as photo_data:
#             response = self.client.patch(
#                 '/api/v1/products/{}/'.format(product.id),
#                 {'photo': photo_data},
#                 format='multipart',
#             )
#         self.assertEqual(response.status_code, 200)
#
#         self.assertNotEqual(response.data['photo', original_photo])
#          try:
#              updated = Product.objects.get(id=product.id)
#              expected_photo = os.path.join(
#                  settings.MEDIA_ROOT, 'products', 'vitamin-iron.jpg',
#              )
#              self.assertTrue(
#                  updated.photo.path.startswith(expected_photo)
#              )
#          finally:
#              os.remove(updated.photo.path)

#