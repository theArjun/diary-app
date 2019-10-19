from django import forms


class AddForm(forms.Form):

    productivity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'type': 'range',
                'min': '0',
                'max': '10',
                'value': '5',
                'step': '1',
                'class': 'mb-3 form-control'
            }
        ),
        label='Rate Today\'s Productivity',
        required=True
    )

    note = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name this day (anything you like)',
                'class': " form-control mb-3",
            }
        ),
        label='',
        required=True
    )

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
