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