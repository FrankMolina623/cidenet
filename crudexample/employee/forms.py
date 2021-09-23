from django import forms  
from employee.models import Employee  
from datetime import datetime
from django import forms  
from django.forms import ModelForm, Textarea
import floppyforms

COUNTRY_CHOICES =['Colombia', 'Estados Unidos']
ID_TYPE_CHOICES = [
    'Cédula de Ciudadanía',
    'Cédula de Extranjería',
    'Pasaporte',
    'Permiso Especial'
    ]

AREA_CHOICES = ['Administración', 'Financiera', 'Compras', 'Infraestructura', 'Operación', 'Talento Humano', 'Servicios Varios']

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
        widgets = {
            'firstLastname': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'Primer apellido'
                                    }),

            'secondLastname': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'Segundo apellido'
                                    }),

            'firstName': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'Primer nombre'
                                    }),

            'otherName': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'Otro nombre'
                                    }),

            'contractCountry': floppyforms.widgets.Input(datalist=COUNTRY_CHOICES),

            'id_type': floppyforms.widgets.Input(datalist=ID_TYPE_CHOICES),

            'id_number': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'Username: Id de identificación'
                                    }),

            'email': forms.EmailInput(attrs={
                                'class': 'form-control',
                                'id': 'Correo institucional'
                            }),

            'company_area': floppyforms.widgets.Input(datalist=AREA_CHOICES),

            'state': forms.TextInput(attrs={
                                'class': 'form-control',
                                'id': 'Estado'
                            }),
        }
    
    def clean_firstLastname(self):
        firstLastname =self.cleaned_data.get('firstLastname')

        if (firstLastname.islower() == False):
            raise forms.ValidationError("Este campo debe estar en minúsculas")

        if (firstLastname.count("ñ") > 0):
            raise forms.ValidationError("Este campo no puede contener la letra ñ")

        if len(firstLastname) > 20:
            raise forms.ValidationError("Este campo no pude ser mayor a 20 carácteres")

        if (any(map(str.isdigit, firstLastname)) == True):
            raise forms.ValidationError("Este campo no puede contener números")

        restricted_caracters = ("á","é", "í", "ó", "ú")

        for a in restricted_caracters:
            cuenta = firstLastname.count(a)
            if cuenta > 0:
                raise forms.ValidationError("El nombre no puede contener acentos")

        only_words = 'abcdefghijklmnopqrstuvwxyz '
        cuenta=[]
        for b in firstLastname:
            if b not in only_words: 
                raise forms.ValidationError("Este campo solo debe contener letras de la A a la Z")
        
        return firstLastname
    
    def clean_secondLastname(self):
        secondLastname =self.cleaned_data.get('secondLastname')

        if (secondLastname.islower() == False):
            raise forms.ValidationError("Este campo debe estar en minúsculas")

        if (secondLastname.count("ñ") > 0):
            raise forms.ValidationError("Este campo no puede contener la letra ñ")

        if len(secondLastname) > 20:
            raise forms.ValidationError("Este campo no pude ser mayor a 20 carácteres")

        if (any(map(str.isdigit, secondLastname)) == True):
            raise forms.ValidationError("Este campo no puede contener números")

        restricted_caracters = ("á","é", "í", "ó", "ú")

        for a in restricted_caracters:
            cuenta = secondLastname.count(a)
            if cuenta > 0:
                raise forms.ValidationError("El nombre no puede contener acentos")

        only_words = 'abcdefghijklmnopqrstuvwxyz '
        cuenta=[]
        for b in secondLastname:
            if b not in only_words: 
                raise forms.ValidationError("Este campo solo debe contener letras de la A a la Z")
        
        return secondLastname


    def clean_firstName(self):
        firstName =self.cleaned_data.get('firstName')

        if (firstName.islower() == False):
            raise forms.ValidationError("Este campo debe estar en minúsculas")

        if (firstName.count("ñ") > 0):
            raise forms.ValidationError("Este campo no puede contener la letra ñ")

        if len(firstName) > 20:
            raise forms.ValidationError("Este campo no pude ser mayor a 20 carácteres")

        if (any(map(str.isdigit, firstName)) == True):
            raise forms.ValidationError("Este campo no puede contener números")

        restricted_caracters = ("á","é", "í", "ó", "ú")

        for a in restricted_caracters:
            cuenta = firstName.count(a)
            if cuenta > 0:
                raise forms.ValidationError("El nombre no puede contener acentos")

        only_words = 'abcdefghijklmnopqrstuvwxyz '
        cuenta=[]
        for b in firstName:
            if b not in only_words: 
                raise forms.ValidationError("Este campo solo debe contener letras de la A a la Z")
        
        return firstName


    def clean_otherName(self):
        otherName =self.cleaned_data.get('otherName')

        if (otherName.islower() == False):
            raise forms.ValidationError("Este campo debe estar en minúsculas")

        if (otherName.count("ñ") > 0):
            raise forms.ValidationError("Este campo no puede contener la letra ñ")

        if len(otherName) > 20:
            raise forms.ValidationError("Este campo no pude ser mayor a 20 carácteres")

        if (any(map(str.isdigit, otherName)) == True):
            raise forms.ValidationError("Este campo no puede contener números")

        restricted_caracters = ("á","é", "í", "ó", "ú")

        for a in restricted_caracters:
            cuenta = otherName.count(a)
            if cuenta > 0:
                raise forms.ValidationError("El nombre no puede contener acentos")

        only_words = 'abcdefghijklmnopqrstuvwxyz '
        cuenta=[]
        for b in otherName:
            if b not in only_words: 
                raise forms.ValidationError("Este campo solo debe contener letras de la A a la Z")
        
        return otherName


    def clean_contractCountry(self):
        contractCountry =self.cleaned_data.get('contractCountry')
        list_countries = ['colombia', 'estados unidos']

        if (contractCountry.lower() not in list_countries):
            raise forms.ValidationError("Opciones válidas: Colombia y Estados Unidos")

        return contractCountry

    def clean_id_type(self):
        id_type =self.cleaned_data.get('id_type')
        list_id_type = ['Cédula de Ciudadanía', 'Cédula de Extranjería', 'Pasaporte', 'Permiso Especial']

        if (id_type not in list_id_type):
            raise forms.ValidationError("Opciones válidas: Cédula de Ciudadanía, Cédula de Extranjería, Pasaporte, Permiso Especial")

        return id_type
    
    def clean_id_number(self):

        id_number =self.cleaned_data.get('id_number')
        if Employee.objects.filter(id_number = id_number).exists():
            raise forms.ValidationError("Este número de id ya existe, por favor seleccione otro")

        return id_number
    
    def clean_email(self):

        input_mail =self.cleaned_data.get('email')

        first =self.cleaned_data.get('firstName')
        second =self.cleaned_data.get('firstLastname')
        id =self.cleaned_data.get('id_number')

        try:
            email = first + '.' + second + '.'+ id + '@cidenet.con.us'
            if input_mail != email:
                raise forms.ValidationError(f"El correo electrónico que le corresponde es {email}")
            else:
                email = email
            i = 1
            while  Employee.objects.filter(email = email).exists():
                email = first + '.' + second + '.'+ id + f'{i}@cidenet.con.us'
                i=+1
        except TypeError:
            print("ingresando email")
            email = self.cleaned_data.get('email')

        return email


