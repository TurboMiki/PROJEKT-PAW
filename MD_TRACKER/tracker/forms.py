from django import forms
from .models import Room,Equipment,Usage

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment 
        fields = "__all__"

class UsageForm(forms.ModelForm):
    use_from = forms.DateTimeField(
        input_formats='%Y-%m-%d %H:%M',
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={'type':'datetime'}
        )
    )
    use_to = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={'type':'datetime-local'}
        )
    )
    class Meta:
        model = Usage
        fields = ["user","equipment","room"]