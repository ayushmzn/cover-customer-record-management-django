from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from coverapp import models
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from coverapp.models import user_info, add_customer
from datetime import date
from django.contrib.auth.decorators import login_required


def login_page(request):
    return render(request, 'coverapp/login.html')


def login_done(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/try_again')


def try_again(request):
    global d
    d = {}
    d['error'] = "username or password is incorrect"
    return render(request, 'coverapp/login_try_again.html', d)

@login_required(login_url="/try_again")
def home(request):
    tran = models.customer_transections.objects.all()
    sum = 0
    sum1 = 0
    for x in tran:                #finding all dr money
        sum = sum + x.amount_of_goods
    for x in tran:
        sum1 = sum1 + x.cr_amount
    today = date.today()
    global d
    d = {}
    d['total_sales'] = sum
    d['total_cr'] = sum1
    d['remaining_bal'] = sum-sum1
    d['date'] = today
    current = request.user  # find user who logged in
    id = current.id
    user_information = user_info.objects.get(pk=id)
    d['first_name'] = user_information.first_name
    d['last_name'] = user_information.last_name
    d['dob'] = user_information.dob
    d['mobile'] = user_information.mobile
    return render(request, 'coverapp/home.html', d)

@login_required(login_url="/try_again")
def add_new_customer(request):
    global d
    return render(request, 'coverapp/add_new_customer.html', d)

@login_required(login_url="/try_again")
def add_new_customer_done(request):
    global d
    if request.method == "POST":
        add = models.add_customer()
        add.name = request.POST['name']
        add.shop_name = request.POST['shop_name']
        add.cus_mobile = request.POST['mobile']
        add.city = request.POST['city']
        add.address = request.POST['address']
        add.doc = d['date']
        add.save()
        return HttpResponseRedirect("/home")

@login_required(login_url="/try_again")
def search_customer(request):
    global d
    return render(request, 'coverapp/search_customer.html', d)

@login_required(login_url="/try_again")
def searched_customer(request):
    if request.method == 'POST':
        type = request.POST['seacrh_by']
        search_value = request.POST['search_value']
        if type == 'name':
            global d
            search = models.add_customer.objects.filter(name=search_value)
            d['search'] = search
            return render(request, 'coverapp/searched_customer.html', d)
        elif type == 'mobile':
            search = models.add_customer.objects.filter(cus_mobile=search_value)
            d['search'] = search
            return render(request, 'coverapp/searched_customer.html', d)
        elif type == 'shop_name':
            search = models.add_customer.objects.filter(shop_name=search_value)
            d['search'] = search
            return render(request, 'coverapp/searched_customer.html', d)

        elif type == 'city':
            search = models.add_customer.objects.filter(city=search_value)
            d['search'] = search
            return render(request, 'coverapp/searched_customer.html', d)

@login_required(login_url="/try_again")
def view_all_customers(request):
    view_all = models.add_customer.objects.all()
    global d
    d['view_all'] = view_all
    return render(request, 'coverapp/view_all_customers.html', d)

@login_required(login_url="/try_again")
def Entry_to_send_goods(request):
    global d
    all_customers = models.add_customer.objects.all()
    d['customers'] = all_customers
    return render(request, 'coverapp/Entry_to_send_goods.html', d)

@login_required(login_url="/try_again")
def entry_save(request):
    if request.method == 'POST':
        c = models.add_customer.objects.get(id=request.POST['select_customer'])
        t = models.customer_transections()
        t.customer_shop_name = c.shop_name
        t.customer_id = c.id
        t.items = request.POST['items']
        t.quantity = request.POST['quantity']
        t.rate = request.POST['rate']
        t.amount_of_goods = request.POST['amount_of_goods']
        t.date_of_send_goods = d['date']
        t.cr_amount = 0
        t.save()
        return HttpResponseRedirect("/Entry_to_send_goods")

@login_required(login_url="/try_again")
def Entry_for_deposit_money(request):
    global d
    all_customers = models.add_customer.objects.all()
    d['customers'] = all_customers
    return render(request, 'coverapp/Entry_for_deposit_money.html', d)

@login_required(login_url="/try_again")
def add_credit_money(request):
    if request.method == 'POST':
        c = models.add_customer.objects.get(id=request.POST['select_customer'])
        t = models.customer_transections()
        t.customer_shop_name = c.shop_name
        t.customer_id = c.id
        t.cr_amount = request.POST['amount']
        t.date_of_cr = d['date']
        t.items = 0
        t.quantity = 0
        t.rate = 0
        t.amount_of_goods = 0
        t.save()
        return HttpResponseRedirect("/Entry_for_deposit_money")

@login_required(login_url="/try_again")
def view_customer_details(request):
    c = models.add_customer.objects.get(id=request.GET['customer_id'])
    customer_id = c.id
    details = models.customer_transections.objects.filter(customer_id=customer_id)
    global d
    sum = 0
    sum1 = 0
    for detail in details:            # calculating amount of total goods
        sum = sum + detail.amount_of_goods
    for detail in details:            # calculatiog total amount of cr
        sum1 = sum1 + detail.cr_amount
    left_balance = sum - sum1
    if left_balance < 0:
        left_balance = "Error in amounts"
    d['left_balance'] = left_balance
    d['sum'] = sum
    d['sum1'] = sum1
    d['customer_id'] = c.id  # assign id to dict which was append with url
    d['details'] = details
    d['name'] = c.name
    d['shop_name'] = c.shop_name
    d['address'] = c.address
    d['city'] = c.city
    return render(request, 'coverapp/show_details.html', d)

@login_required(login_url="/try_again")
def Entry_to_send_goods_inside_view_details(request):
    return render(request, 'coverapp/Entry_to_send_goods_inside_view_details.html', d)

@login_required(login_url="/try_again")
def entry_save_inside_view_details(request):
    if request.method == 'POST':
        global d
        customer_id = d['customer_id']
        c = models.add_customer.objects.get(id=customer_id)
        t = models.customer_transections()
        t.customer_shop_name = c.shop_name
        t.customer_id = c.id
        t.items = request.POST['items']
        t.quantity = request.POST['quantity']
        t.rate = request.POST['rate']
        t.amount_of_goods = request.POST['amount_of_goods']
        t.date_of_send_goods = d['date']
        t.cr_amount = 0
        t.save()
        return HttpResponseRedirect('/view_customer_details_edited')

@login_required(login_url="/try_again")
def Entry_for_deposit_money_inside_details(request):
    global d
    return render(request, 'coverapp/Entry_for_deposit_money_inside_details.html', d)

@login_required(login_url="/try_again")
def add_credit_money_inside_view(request):
    if request.method == 'POST':
        global d
        customer_id = d['customer_id']
        c = models.add_customer.objects.get(id=customer_id)
        t = models.customer_transections()
        t.customer_shop_name = c.shop_name
        t.customer_id = c.id
        t.cr_amount = request.POST['amount']
        t.date_of_cr = d['date']
        t.items = 0
        t.quantity = 0
        t.rate = 0
        t.amount_of_goods = 0
        t.save()
        return HttpResponseRedirect('/view_customer_details_edited')

@login_required(login_url="/try_again")
def edit_details(request):
    global d
    tran = models.customer_transections.objects.get(id=request.GET['record_id'])
    d['tran'] = tran
    return render(request, 'coverapp/edit_details.html', d)

@login_required(login_url="/try_again")
def update_details(request):
    global d
    if request.method == 'POST':
        t = models.customer_transections()
        t.id = request.POST['record_id']
        t.customer_shop_name = request.POST['customer_shop_name']
        t.items = request.POST['item']
        t.quantity = request.POST['quantity']
        t.rate = request.POST['rate']
        t.customer_id = request.POST['customer_id']
        t.amount_of_goods = request.POST['amount_of_goods']
        t.date_of_cr = d['date']
        t.date_of_send_goods = d['date']
        t.cr_amount = request.POST['cr_amount']
        t.save()
        d['customer_id'] = request.POST['customer_id']
        return HttpResponseRedirect('/view_customer_details_edited')

@login_required(login_url="/try_again")
def view_customer_details_edited(request):
    global d
    customer_id = d['customer_id']
    c = models.add_customer.objects.get(id=customer_id)
    sum = 0
    sum1 = 0       #declaring variable
    c_id = c.id
    details = models.customer_transections.objects.filter(customer_id=c_id)
    for detail in details:
        sum = sum + detail.amount_of_goods
    for detail in details:            # calculatiog total amount of cr
        sum1 = sum1 + detail.cr_amount
    left_balance = sum-sum1
    if left_balance<0:
        left_balance = "Error in amounts"
    d['left_balance'] = left_balance
    d['sum'] = sum
    d['sum1'] = sum1
    d['customer_id'] = c.id  # assign id to dict which was append with url
    d['details'] = details
    d['name'] = c.name
    d['shop_name'] = c.shop_name
    d['address'] = c.address
    d['city'] = c.city
    return render(request, 'coverapp/show_details.html', d)

@login_required(login_url="/try_again")
def deletedetails(request):
    record_id = request.GET['record_id']
    d['record_id'] = record_id
    detail = models.customer_transections.objects.get(id=record_id)
    d['delete_details'] = detail
    return render(request, 'coverapp/deletedetails.html', d)

@login_required(login_url="/try_again")
def detele_details_confirm(request):
    record_id = d['record_id']
    detail_confirm = models.customer_transections.objects.get(id=record_id)
    d['customer_id'] = detail_confirm.customer_id
    detail_confirm.delete()
    return HttpResponseRedirect('/view_customer_details_edited')

@login_required(login_url="/try_again")
def edit_costomer(request):
    global d
    customer_id = request.GET['customer_id']
    customer_details = models.add_customer.objects.get(id=customer_id)
    d['customer_details'] = customer_details
    d['doc'] = customer_details.doc
    return render(request, 'coverapp/edit_customer.html', d)
@login_required(login_url="/try_again")
def update_customer(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        c = models.add_customer()
        c.id = customer_id
        c.name = request.POST['customer_name']
        c.shop_name = request.POST['shop_name']
        c.cus_mobile = request.POST['cus_mobile']
        c.city = request.POST['city']
        c.address = request.POST['address']
        c.doc =  d['doc']
        c.save()
        return HttpResponseRedirect('/view_all_customers')
@login_required(login_url="/try_again")
def delete_customer(request):
    global d
    customer_id = request.GET['customer_id']
    customer_details = models.add_customer.objects.get(id=customer_id)
    d['customer_details'] = customer_details
    return render(request, 'coverapp/delete_customer.html', d)
@login_required(login_url="/try_again")
def detele_customer_confirm(request):
    customer_id = request.GET['customer_id']
    customer = models.add_customer.objects.get(id = customer_id)
    customer.delete()
    return HttpResponseRedirect('/view_all_customers')
@login_required(login_url="/try_again")
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/try_again")
