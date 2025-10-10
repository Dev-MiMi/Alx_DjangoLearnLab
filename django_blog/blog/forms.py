from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment, Post, Tag

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment..."}),
        max_length=2000,
        label=""
    )

    class Meta:
        model = Comment
        fields = ["content"]

    def clean_content(self):
        data = self.cleaned_data["content"].strip()
        if not data:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(data) < 2:
            raise forms.ValidationError("Comment is too short.")
        return data

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Add tags separated by commas")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tags_str = self.cleaned_data.get("tags", "")
        tags_list = [t.strip() for t in tags_str.split(",") if t.strip()]
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return instance
