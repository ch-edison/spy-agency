# -*- coding: utf-8 -*-
from django import forms
from .models import Hit
from apps.users.models import User


class HitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(HitForm, self).__init__(*args, **kwargs)
        if self.user.groups.filter(name="Manager").exists():
            self.fields['assigned_to'].queryset = User.objects.filter(manager=self.user).exclude(username=self.user)
        else:
            self.fields['assigned_to'].queryset = User.objects.filter().exclude(username=self.user)
    objetive_name = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Objetivo'}))
    description = forms.CharField(widget=forms.Textarea(attrs=
                                                        {'class': 'form-control',
                                                         'placeholder': 'Descripción',
                                                         "rows": "3"
                                                         }))
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Seleccione el agente a asignar")

    class Meta:
        model = Hit
        fields = ("objetive_name", "description", "assigned_to")
