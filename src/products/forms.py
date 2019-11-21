from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    desc = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Product
        fields ={
            'title'
            , 'desc'
            , 'price'
        }

    # buat validasi title
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        print(title)
        if 'CFE' in title:
            raise forms.ValidationError('Not valid')
        else:
            return title


    def clean_email(self, *args, **kwargs):
        title = self.cleaned_data.get('email')
        print(title)
        if 'CFE' in title:
            raise forms.ValidationError('Not valid')
        else:
            return title

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    desc = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)
    
