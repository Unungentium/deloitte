from django.shortcuts import render, redirect
from .models import CompanyName as Company
# Create your views here.

def index(response):
        companies = Company.objects.all()
        if response.method=="POST":
  
                old_text = response.POST.get("text_input", None)
                text_list = list(old_text.split(" "))
                new_list=[]
                for word in text_list:
                    for company in companies:
                        if word == company.name:
                            word = word+"©"
                    new_list.append(word)

                new_text = ' '.join(new_list)
                return render(response, 'bigc/index.html',{'new_text': new_text})
  
        else:
            return render(response, 'bigc/index.html',{})

    
