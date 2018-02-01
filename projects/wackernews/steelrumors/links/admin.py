from django.contrib import admin
from .models import Link, Vote
from django.contrib


class LinkAdmin(admin.ModelAdmin): pass
admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin): pass
admin.site.register(Vote, VoteAdmin)

