import django_filters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator

from apps.ish.forms import ClientCreateForm, ClientSawCreateForm
from apps.ish.models import Client, Saw


class HomePageView(ListView):
    model = Client
    template_name = "work/home.html"
    context_object_name = "clients"


class WorkView(ListView):
    model = Client
    template_name = "work/works.html"
    context_object_name = "clients"


class ListSawView(View):
    def get(self, request):
        queryset = Saw.objects.all()
        param = request.GET.get("saw")
        if param is not None:
            queryset = queryset.filter(
                Q(name__icontains=param) | Q(color_id__name__icontains=param)
            )
        context = {"saw": queryset, "param": param}
        return render(request, "work/client-saw.html", context=context)


class ClientListView(ListView):
    model = Client
    paginate_by = 40
    template_name = "work/client-list.html"
    context_object_name = "clients"

    def get_queryset(self):
        return Client.objects.all().order_by("-created_at")


class ClientSawListView(ListView):
    model = Saw
    paginate_by = 40
    template_name = "work/client-saw.html"
    context_object_name = "saw"

    def get_queryset(self):
        return Saw.objects.all().order_by("-created_at")


@login_required()
def client_create(request):
    if request.method == "POST":
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            client = Client(
                name=form.cleaned_data["name"],
                metr=form.cleaned_data["metr"],
                color_id=form.cleaned_data["color_id"],
                edge_id=form.cleaned_data["edge_id"],
            )
            client.save()
            messages.success(request, "Client mufafiqiyatli qo'shildi")
            return redirect(reverse("work:client"))
        else:
            return render(request, "work/post_form.html", {"form": form})
    else:
        form = ClientCreateForm()
        return render(request, "work/post_form.html", {"form": form})


@login_required()
def client_saw_create(request):
    if request.method == "POST":
        form = ClientSawCreateForm(request.POST)
        if form.is_valid():
            client_saw = Saw(
                name=form.cleaned_data["name"],
                list_list=form.cleaned_data["list_list"],
                color_id=form.cleaned_data["color_id"],
                laminate=form.cleaned_data["laminate"],
                price=form.cleaned_data["price"]
            )
            client_saw.save()
            messages.success(request, "Client mufafiqiyatli qo'shildi")
            return redirect(reverse("work:client-saw"))
        else:
            return render(request, "work/post-form-saw.html", {"form": form})
    else:
        form = ClientSawCreateForm()
        return render(request, "work/post-form-saw.html", {"form": form})


class ListView(View):
    def get(self, request):
        queryset = Client.objects.all()
        param = request.GET.get("q")
        if param is not None:
            queryset = queryset.filter(
                Q(name__icontains=param) | Q(color_id__name__icontains=param)
            )
        context = {"clients": queryset, "param": param}
        return render(request, "work/client-list.html", context=context)


class ClientMetrView(ListView):
    model = Client.metr
    template_name = "work/client-list.html"
    context_object_name = "clients"


def listing(request):
    contact_list = Client.objects.all()
    paginator = Paginator(contact_list, 50)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "work/client-list.html", {"page_obj": page_obj})
