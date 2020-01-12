from django import forms

class FeedbackForm(forms.Form):
    Name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your name',
                'class':'form-control'
            }
        )
    )

    Rating=forms.IntegerField(
        label="Give Rating",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Rating',
                'class':'form-control'
            }
        )
    )

    Feedback=forms.CharField(
        label="Enter feedback",
        widget=forms.Textarea(
            attrs={
                'placeholder':' Your Feedback',
                'class':'form-control'

            }
        )
    )
