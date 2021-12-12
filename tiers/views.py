from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import random
from django.http import HttpResponse
from django.db.models import F

from .models import  Word_sta, Word_gen

def tier_submit(request):
    try:
        lev = request.GET['level']
    except:
        lev = 3
        return render(request,'tiers/tier.html', {'lev':lev,'error_message':"err",})
    else:
        word_sta_list=Word_sta.objects.all().filter(levels__exact=lev)[:30]
        word_gen_list=random.sample(list(Word_gen.objects.all().filter(levels__exact=lev)[:100]),1)
        return render(request,'tiers/tier.html', {'word_sta_list':word_sta_list,
            'lev':lev,'word_gen_list':word_gen_list,'undo_id':word_gen_list[0].id,'undo_num':0,})

class tierMView(generic.ListView):
    model = Word_sta
    paginate_by = 30
    template_name = 'tiers/tier.html'
    context_object_name = 'word_sta_list'

    def get_queryset(self):
        lev = Word_gen.objects.get(id=int(self.kwargs['id'])).levels
        return Word_sta.objects.all().filter(levels__exact=lev)[:30]

    def get_context_data(self, **kwargs):
        word_id = int(self.kwargs['id'])
        num = int(self.kwargs['num'])
        lev = Word_gen.objects.get(id=word_id).levels
        Word_gen.objects.filter(id=int(self.kwargs['id'])).update(levels=F('levels')-num)
        context = super(tierMView, self).get_context_data(**kwargs)
        context.update({
            'undo_id':word_id,
            'undo_num':-num,
            'lev':lev,
            'word_gen_list':list(Word_gen.objects.all().filter(levels__exact=lev)[:1])
        })
        return context

def tier(request,level):
    word_sta_list=Word_sta.objects.all().filter(levels__exact=level)[:30]
    word_gen_list=random.sample(list(Word_gen.objects.all().filter(levels__exact=level)[:100]),1)
    return render(request,'tiers/tier.html', {'word_sta_list':word_sta_list,
        'lev':level,'word_gen_list':word_gen_list,'undo_id':word_gen_list[0].id,'undo_num':0,})
