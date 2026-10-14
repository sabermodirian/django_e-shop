from django.urls import path


from products.views import CommentCreateView , ProductDetailsView , ProductListView

urlpatterns = [
	path('' , ProductListView.as_view() , name = 'product_list'),
	path('<int:pk>/' , ProductDetailsView.as_view() , name = 'product_details'),
	path('comment/<int:prdct_id>/',CommentCreateView.as_view(), name = 'create_cmmnt')
]