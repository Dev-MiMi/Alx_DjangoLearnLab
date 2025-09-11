from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

# Admin view
@user_passes_test(check_role('Admin'))           def admin_view(request):                             return render(request, 'relationship_app/admin_view.html')                                    
