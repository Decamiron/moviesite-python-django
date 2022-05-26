from django import forms
from users.models import FilmUsersInfo


class Comments(forms.ModelForm):
    raiting = forms.ChoiceField(label='Оценка', choices=FilmUsersInfo.RAITING,
                                widget=forms.Select(attrs={'class': 'form-select w-50 bg-dark text-warning fs-4'}))
    comment = forms.CharField(label='Текст комментария', max_length=1000,
                              widget=forms.Textarea(attrs={'class': 'form-control bg-dark text-warning'}))

    class Meta:
        model = FilmUsersInfo
        fields = ('raiting', 'comment')

