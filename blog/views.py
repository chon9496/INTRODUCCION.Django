from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class BlogListView(View):
    def get(self,request,*args, **kwargs):
        context={

        }
        return render(request,'blog_list.html',context)
