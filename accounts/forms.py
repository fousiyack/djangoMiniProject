from django import forms

class ProductForm(forms.Form):
#    class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email']
#         labels ={
#             'firs_tname':'first name',
#             'last_name': 'last name',
#             'username':'username',
#             'email':'email',
#         }       
    
        name=forms.CharField(max_length=255)
        price=forms.FloatField()
        stock=forms.IntegerField()
        image=forms.CharField(max_length=2500)