from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from django.shortcuts import get_object_or_404,redirect,render
from .forms import RegisterForm,TransactionForm
from .models import Transaction,Tutorial
def home(request): return redirect("dashboard") if request.user.is_authenticated else render(request,"tracker/home.html")
def register(request):
 form=RegisterForm(request.POST or None)
 if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Account created. Please sign in."); return redirect("login")
 return render(request,"tracker/register.html",{"form":form})
@login_required
def dashboard(request):
 qs=Transaction.objects.filter(user=request.user); sums={x["transaction_type"]:x["total"] or Decimal("0") for x in qs.values("transaction_type").annotate(total=Sum("amount"))}
 credit=sums.get("credit",Decimal("0")); debit=sums.get("debit",Decimal("0"))
 return render(request,"tracker/dashboard.html",{"credit":credit,"debit":debit,"balance":credit-debit,"count":qs.count(),"recent":qs[:8]})
@login_required
def transaction_list(request):
 qs=Transaction.objects.filter(user=request.user); kind=request.GET.get("type"); cat=request.GET.get("category"); date=request.GET.get("date"); amount=request.GET.get("amount")
 if kind in ("credit","debit"): qs=qs.filter(transaction_type=kind)
 if cat: qs=qs.filter(category__icontains=cat)
 if date: qs=qs.filter(date=date)
 if amount: qs=qs.filter(amount=amount)
 return render(request,"tracker/transactions.html",{"transactions":qs,"filters":{"type":kind or "","category":cat or "","date":date or "","amount":amount or ""}})
@login_required
def transaction_add(request,kind):
 if kind not in ("credit","debit"): return redirect("transactions")
 form=TransactionForm(request.POST or None)
 if request.method=="POST" and form.is_valid(): obj=form.save(commit=False); obj.user=request.user; obj.transaction_type=kind; obj.save(); messages.success(request,"Transaction saved."); return redirect("transactions")
 return render(request,"tracker/form.html",{"form":form,"title":"Add "+kind.title()})
@login_required
def transaction_edit(request,pk):
 obj=get_object_or_404(Transaction,pk=pk,user=request.user); form=TransactionForm(request.POST or None,instance=obj)
 if request.method=="POST" and form.is_valid(): form.save(); messages.success(request,"Transaction updated."); return redirect("transactions")
 return render(request,"tracker/form.html",{"form":form,"title":"Edit transaction"})
@login_required
def transaction_delete(request,pk):
 obj=get_object_or_404(Transaction,pk=pk,user=request.user)
 if request.method=="POST": obj.delete(); messages.success(request,"Transaction deleted."); return redirect("transactions")
 return render(request,"tracker/confirm_delete.html",{"object":obj})
@login_required
def reports(request):
 data=Transaction.objects.filter(user=request.user).values("transaction_type","category").annotate(total=Sum("amount"),count=Count("id")).order_by("transaction_type","category")
 return render(request,"tracker/reports.html",{"rows":data})
def tutorial_list(request): return render(request,"tracker/tutorials.html",{"tutorials":Tutorial.objects.filter(is_published=True)})
def tutorial_detail(request,slug): return render(request,"tracker/tutorial_detail.html",{"tutorial":get_object_or_404(Tutorial,is_published=True,slug=slug)})
