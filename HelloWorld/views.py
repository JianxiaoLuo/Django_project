from django.shortcuts import render
 
def test(request):
    context          = {}
    context['hello'] = 'Hello World!'
    view_list = ['list1', 'list2', 'list3']
    return render(request, 'test.html', {"view_list": view_list})