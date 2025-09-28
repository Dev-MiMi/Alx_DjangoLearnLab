from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")
