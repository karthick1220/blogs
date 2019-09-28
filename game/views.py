# from django.http import HttpResponse
# from django.views import View
# #from django.shortcuts import render
# #
# # Create your views here.
# #from django.http.response import HttpResponse
# 
# # from django.http import HttpResponse
# #from django.views import View
# # import datetime
# # 
# # class MyView(View):
# #     def get(self,request):
# #         now = datetime.datetime.now()
# #         html = "<html><body> hi! it is now %s.</body></html>" % now
# #         return HttpResponse(html)
# #         
# 
# 
# class GreetingView(View):
#     greeting="Good Day"
#     def get(self,request):
#         return HttpResponse(self.greeting)
#     
# class MorningGreetingView(GreetingView):
#     greeting = "Morning to ya"

#Decorations
# from django.http import HttpResponse
# def myfun(request):
#     
#     def good_function():
#         return ' I am a good function'
#     
#     def  vgood_function(func):
#         def vbad_function():
#             return func
#         return ' i am very bad function'
#     
#     result = vgood_function(good_function)
#     return HttpResponse(result)

#function decorators
# from django.http import HttpResponse
# def myfun(request):
#      
#     def get_text(name):
#         return "My name is {0} sir".format(name)
#      
#     def b_decorate(func):
#         def func_wrapper(name):
#             return "<b>{0}</b>".format(func(name))
#         return func_wrapper
#     
#      
#     my_get_text = b_decorate(get_text)
#     return HttpResponse(my_get_text("John"))

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>You are ok with DJango app")

     
