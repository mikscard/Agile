from django.urls import path  # type: ignore
from . import views  # type: ignore

app_name = "agile"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("value", views.ValueView.as_view(), name="value_view"),
    path(
        "characteristic", views.CharacteristicView.as_view(), name="characteristic_view"
    ),
    path("add_value/", views.add_value),
    path("delete_value/<int:value_id>", views.delete_value),
    path("update_value/<int:value_id>", views.update_value),
    path("add_characteristic/", views.add_characteristic),
    path("delete_characteristic/<int:characteristic_id>", views.delete_characteristic),
    path("update_characteristic/<int:characteristic_id>", views.update_characteristic),
]
