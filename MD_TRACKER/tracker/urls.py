from django.urls import path
from . import views

urlpatterns = [
    path("tracker/rooms",views.RoomView,name="rooms"),
    path("tracker/rooms/delete",views.DeleteRoomView,name="delete"),
    path("tracker/equipment",views.EqView,name="equipment"),
    path("tracker/usage",views.UsageView,name="usage")
]
