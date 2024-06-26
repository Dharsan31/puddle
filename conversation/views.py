from django.shortcuts import render,get_object_or_404,redirect
from items.models import Item
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    if( item.created_by == request.user):
        return redirect('dashboard:index')
    conversations=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        pass
    
    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect('items:details',pk=item_pk)
    else:
        form=ConversationMessageForm()
        return render(request,'conversation/new.html',{
            'form':form
        })
            
@login_required
def inbox(request):
    conversations=Conversation.objects.filter(members__in=[request.user.id])
    return render(request,'conversation/inbox.html',{'conversations':conversations,
                                                     })
@login_required
def detail(request,pk):
    conversations=Conversation.objects.filter(pk=pk).filter(members__in=[request.user.id])
    for conversation in conversations:
        conversation1=conversation
    if request.method=='POST':
       form =  ConversationMessageForm(request.POST)
       if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation1
            conversation_message.created_by=request.user
            conversation_message.save()
            conversation1.save()
            return redirect('conversation:detail',pk=pk)
    else:
        form =  ConversationMessageForm(request.POST)
    return render(request,'conversation/detail.html',{'conversations':conversations,
                                                      'form':form
                                                     })


# Create your views here.
