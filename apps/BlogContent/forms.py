from django import forms
from apps.BlogContent.models import BlogPost

class BlogForm(forms.ModelForm):
	class Meta:
		model = BlogPost

		fields = [
		'title',
		'content1',
		'content2',
		'ref_code',
		'github_link',
		'references',
		]

		labels = {
		'title': "Title of your post",
		'content1': "Main content",
		'content2': "Additional Content",
		'ref_code': "Reference Code",
		'github_link': "Github Link",
		'references': "References",
		}

		widgets = {
		'title': forms.TextInput(attrs={'class':'form-control'}),
		'content1': forms.TextInput(attrs={'class':'form-control'}),
		'content2': forms.TextInput(attrs={'class':'form-control'}),
		'ref_code': forms.TextInput(attrs={'class':'form-control'}),
		'github_link': forms.TextInput(attrs={'class':'form-control'}),
		'references': forms.TextInput(attrs={'class':'form-control'}),
		}