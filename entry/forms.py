from django import forms


class AddForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            {
                'placeholder': 'Write what you feel...',
                'class': " form-control quilljs-textarea",
                'row': "15"
            }
        ),
        label='',
        required=True
    )
