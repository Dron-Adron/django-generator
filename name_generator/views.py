from django.shortcuts import render
import names

# Create your views here.

def main(request):
    return render(request, 'main_page/main.html')

def home_name(request):
    return render(request, 'name_generator/home_name.html')

def name(request):
    parameters = request.GET.get('parameters')
    gender = request.GET.get('gender')
    def generate_name(gend):
        if parameters == "first":
            return names.get_first_name(gender=gend)
        elif parameters == "last":
            return names.get_last_name()
        else:
            return names.get_full_name(gender=gend)
        
    return render(request, 'name_generator/name.html', {'name':generate_name(gender)})