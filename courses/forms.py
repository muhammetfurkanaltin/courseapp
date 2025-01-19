from django import forms
from .models import Course
# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Adı",
#         required=True,
#         error_messages={                                  // Yontem 1
#             "required":"Kurs adı boş bırakılamaz"},
#         widget=forms.TextInput(attrs={"class":"form-control"})
#     )
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imagUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))




class CourseCreateForm(forms.ModelForm):    # Yontem 2
    class Meta:
        model = Course
        fields = ['title','description','imagUrl','slug']
        labels = {'title':'Kurs Adı'
                  }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'imagUrl':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'title':{
                'required':'Kurs adı boş bırakılamaz'
            },
            'description':{
                'required':'description boş bırakılamaz'
            }
        }



class CourseEditForm(forms.ModelForm):    # Yontem 2
    class Meta:
        model = Course
        fields = ['title','description','imagUrl','slug']
        labels = {'title':'Kurs Adı'
                  }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'imagUrl':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'title':{
                'required':'Kurs adı boş bırakılamaz'
            },
            'description':{
                'required':'description boş bırakılamaz'
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField()
    
