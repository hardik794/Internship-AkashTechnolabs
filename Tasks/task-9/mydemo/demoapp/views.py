from django.shortcuts import render

# Create your views here.
def index(request):

    if request.method == 'POST':
        fn = request.POST.get("fn")
        ln = request.POST.get("ln")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        date = request.POST.get("date")
        contact= request.POST.get("contact")
        address= request.POST.get("address")
        college = request.POST.get("college")
        dept = request.POST.get("dept")

        context={
            'fn':fn,
            'ln':ln,
            'email':email,
            'gender':gender,
            'contact':contact,
            'address' :address,
            'date':date,
            'college':college,
            'dept':dept
        }
        return render(request,'userdata.html',context)

    return render(request,"index.html")