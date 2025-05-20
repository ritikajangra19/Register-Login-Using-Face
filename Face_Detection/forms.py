from django import forms
from .models import UserProfile

class ResgistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'face_id',
            'name',
            'address',
            'job',
            'phone',
            'email',
            'bio',
            'image'
        ]

        widgets = {
            'face_id': forms.TextInput(attrs={'placeholder': 'Face ID'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'address': forms.Textarea(attrs={'placeholder': 'Address', 'rows': 3}),
            'job': forms.TextInput(attrs={'placeholder': 'Job'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Bio', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Disable editing face_id during update
            self.fields['face_id'].widget.attrs['readonly'] = True

    def clean_face_id(self):
        face_id = self.cleaned_data.get('face_id')

        # If we're editing, skip validation if face_id hasn't changed
        if self.instance and self.instance.pk:
            # Return existing face_id (readonly field won't change)
            return self.instance.face_id

        # New registration or attempt to change face_id
        if UserProfile.objects.filter(face_id=face_id).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This Face ID is already in use. Please try another one.")
        return face_id
