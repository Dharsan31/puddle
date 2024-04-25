from django import forms
from models import ConverasationMessage,Conversation

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConverasationMessage
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs=
                                     {
                                    "class":"w-full py-4 px-6 rounded-xl border"
                                     })
        }