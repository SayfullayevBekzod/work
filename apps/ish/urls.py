from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.ish.views import (
    HomePageView,
    ClientListView,
    ClientSawListView,
    client_create,
    client_saw_create,
    ListView,
    ListSawView,
    WorkView,
)

app_name = "work"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("raspil/client/", ClientListView.as_view(), name="client"),
    path("raspil/client-saw/", ClientSawListView.as_view(), name="client-saw"),
    path("raspil/create-client/", login_required(client_create), name="create-client"),
    path("raspil/create-client-saw/", client_saw_create, name="create-client-saw"),
    path("raspil/client-list/", ListView.as_view(), name="list"),
    path("raspil/client-saw-list/", ListSawView.as_view(), name="list-saw"),
    path("raspil/work/", WorkView.as_view(), name="work"),
]
