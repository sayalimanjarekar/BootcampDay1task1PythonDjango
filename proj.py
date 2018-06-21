
from django import proj


class ContactForm(proj.Form):
    fname= proj.CharField(max_length=30)
    lname= proj.CharField(max_length=30)
    email = proj.EmailField(max_length=254)
    pno= proj.NumberField(max_length=30)
    country= proj.CharField(max_length=30)
    city= proj.CharField(max_length=30)
   
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
         fname = cleaned_data.get('fname')
         lname = cleaned_data.get('lname')
        email = cleaned_data.get('email')
         pno = cleaned_data.get('pno')
          country = cleaned_data.get('country')
           city = cleaned_data.get('city')
        
        if not fname and not lname and not email and not pno and not country  and not city:
            raise proj.ValidationError('You have to write something!')