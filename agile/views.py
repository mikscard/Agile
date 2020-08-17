from django.http import HttpResponseRedirect  # type: ignore
from django.views import generic  # type: ignore
from django.urls import reverse  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.utils.decorators import method_decorator  # type: ignore
from django.views.generic import TemplateView  # type: ignore
from .models import Value, Characteristic  # type: ignore


@method_decorator(login_required(login_url="/accounts/login"), name="dispatch")
class IndexView(generic.ListView):
    template_name = "agile/index.html"
    context_object_name = "value_list"

    def get_queryset(self):
        return Value.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["characteristic_list"] = Characteristic.objects.all()
        return context


@method_decorator(login_required(login_url="/accounts/login"), name="dispatch")
class ValueView(generic.ListView):
    template_name = "agile/value_edit.html"
    context_object_name = "value_list"

    def get_queryset(self):
        return Value.objects.all()


@method_decorator(login_required(login_url="/accounts/login"), name="dispatch")
class CharacteristicView(generic.ListView):
    template_name = "agile/characteristic_edit.html"
    context_object_name = "characteristic_list"

    def get_queryset(self):
        return Characteristic.objects.all()


def add_value(request):
    content = request.POST["content"]
    v = Value(value_text=content)
    v.save()
    return HttpResponseRedirect(reverse("agile:index"))


def delete_value(request, value_id):
    Value.objects.get(id=value_id).delete()
    return HttpResponseRedirect(reverse("agile:index"))


def update_value(request, value_id):
    content = request.POST["content"]
    v = Value.objects.get(id=value_id)
    v.value_text = content
    v.save()
    return HttpResponseRedirect(reverse("agile:index"))


def add_characteristic(request):
    content = request.POST["content"]
    c = Characteristic(characteristic_text=content)
    c.save()
    return HttpResponseRedirect(reverse("agile:index"))


def delete_characteristic(request, characteristic_id):
    Characteristic.objects.get(id=characteristic_id).delete()
    return HttpResponseRedirect(reverse("agile:index"))


def update_characteristic(request, characteristic_id):
    content = request.POST["content"]
    c = Characteristic.objects.get(id=characteristic_id)
    c.characteristic_text = content
    c.save()
    return HttpResponseRedirect(reverse("agile:index"))
