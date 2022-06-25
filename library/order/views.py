from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from .forms import OrderForm
from book.models import Book
from .models import Order
import datetime



def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order/order_list.html', context)


def order_create(request,pk):    
    book = Book.objects.filter(id=pk)[0]
    count =book.count-1;
    book.count=count
    book.save()
    Order.objects.create(
                    user=request.user,
                    book=book,
                    plated_end_at = datetime.datetime.now() + datetime.timedelta(days=15)     
                    )      
   
    context = {"book": book  } 
    return render(request, 'order/info_create.html', context)



def order_delete(request,pk):
    try:
        order = Order.objects.get(id=pk)        
        book = Book.objects.filter(id=order.book.id)[0]
        count =book.count+1;
        book.count=count
        book.save()
        order.delete()
        orders = Order.objects.order_by('created_at', 'plated_end_at')
    except Order.DoesNotExist:    
        pass
    
    return render(request, 'book/orders.html', {'orders': orders})


def order_update(request, pk):
    
    if request.method == "POST":
        order = get_object_or_404(Order, pk=pk)  
        form = OrderForm(request.POST,instance=order)            
        if form.is_valid():
            post = form.save(commit=False)           
            post.save()
        orders = Order.objects.order_by('created_at', 'plated_end_at')
        return render(request, 'book/orders.html', {'orders': orders})
    else:
        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)
        
    return render(request, 'order/update_order.html', {'form': form,'order':order})

def order_return(request, pk):
    try:
        print(pk)
        order = Order.objects.get(id=pk) 
        order.end_at=datetime.datetime.now()
        order.save()          
        orders = Order.objects.order_by('created_at', 'plated_end_at')
    except Order.DoesNotExist:    
        pass
   
    return render(request, 'book/orders.html', {'orders': orders})
