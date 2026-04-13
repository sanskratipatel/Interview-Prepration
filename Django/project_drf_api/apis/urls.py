from django.urls import include ,path 
from . import views

urlpatterns = [ 
    path('students/', views.studentsView) ,
    path('employess/<int:pk>/',views.EmployeesDetailsViews.as_view()) , 
    path('employess/',views.Employees.as_view()) ,
    path('employessm/<int:pk>/',views.EmployeesMixinDetails.as_view()) , 
    path('employessm/',views.EmployeesMixin.as_view()), 
    path('comments/' ,views.CommentsView.as_view() ) , 
    path('blogs' , views.BlogsView.as_view()), 
    path('comments/<int:pk>/',views.CommentDetailView.as_view()), 
    path('blogss/<int:pk>/',views.BlogDetailView.as_view())
]