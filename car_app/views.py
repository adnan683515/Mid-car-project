from django.shortcuts import render,redirect
from car_app.forms import signup,user_change_form
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib.auth.forms import authenticate,AuthenticationForm

from django.views.generic import DetailView
from car_app.models import car,Buy
from car_app.forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = signup()
    return render(request,'sign_up.html',{'form':form})

class class_vased_register(CreateView):
    form_class = signup
    template_name = 'sign_up.html'
    success_url = reverse_lazy('log_in')




def log_out(request):
    logout(request)
    return redirect('log_in')





# @method_decorator(login_required, name='dispatch')
class class_vased_details(DetailView):
    model = car
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    
    def car(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object # post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
   
    
    
@login_required
def buy_car(request,id):
    carobj=car.objects.get(pk=id) # oi car take dorlam 
    
    if carobj.quantity>0: # oi car ar quantity check korlam
        
        carobj.quantity -= 1 # 1 komai lam

        carobj.save() # oi car obj ta abr oi khane save kore dilam
        
        Buy.objects.create(car=carobj,buy_user=request.user) # buy ar jonno obj create korlam
        
        return redirect('homepage')
    else:
        
        return redirect('homepage')
    
    

   
@login_required 
def buy_car_detais(request):
    car_store = Buy.objects.filter(buy_user=request.user)
    return render(request,'buy_car.html',{'car_store':car_store})
    print(car_store)
    
@login_required
def user_change_data(request):
    
    if request.method == 'POST':
        form =user_change_form(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = user_change_form(instance = request.user)
    return render(request,'sign_up.html',{'form':form})





def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            
            user = authenticate(username = user_name,password = pass_word)
            if user is not None:
                login(request,user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request,'sign_up.html',{'form':form})
            



class class_vased_logIn(LoginView):
    template_name = 'sign_up.html'
    

    def get_success_url(self):
        return reverse_lazy('homepage')
        
    
    def  form_valid(self, form):
        messages.success(self.request,'logged in successful')
        return super().form_valid(form)
    

    def form_invalid(self,form):
        messages.success(self.request,'Logged in information incorrect!')
        return super().form_invalid(form)

