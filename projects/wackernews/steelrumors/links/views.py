from django.views.generic import ListView
from .models import Link, Vote
from django.views.generic import ListView, DetailView
from .models import UserProfile


# Create your views here.

class LinkListView(ListView):
   model = Link
   queryset = Link.with_votes.all()
   paginate_by = 3

class UserProfileDetailView(DetailView)
   model = get_user_model()
   slug_field = "username"
   template_name = "user_detail.html"

