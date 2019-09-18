from django import forms
from operator_form.models import Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('file_no','record_no','entry_date','ref_no','invoice_no','courier_name','con_no','dispatch_date','dispatch_by','sales_date','sales_time','customer_name','mail_address','agent_name','address','city','state','zip_code','customer_phone','credit_card_type','credit_card_number',)

        widgets = {
            'file_no':forms.TextInput(attrs={'placeholder':'File No'}),
            'record_no':forms.TextInput(attrs={'placeholder':'Record No'}),
            'entry_date':forms.TextInput(attrs={'placeholder':'Entry Date'}),
            'ref_no':forms.TextInput(attrs={'placeholder':'Ref No'}),
            'invoice_no':forms.TextInput(attrs={'placeholder':'Invoice No'}),
            'courier_name':forms.TextInput(attrs={'placeholder':'Courier No'}),
            'con_no':forms.TextInput(attrs={'placeholder':'Con No'}),
            'dispatch_date':forms.TextInput(attrs={'placeholder':'Dispatch Date'}),
            'dispatch_by':forms.TextInput(attrs={'placeholder':'Dispatch By'}),
            'sales_date':forms.TextInput(attrs={'placeholder':'Sales Date'}),
            'sales_time':forms.TextInput(attrs={'placeholder':'Sales Time'}),
            'customer_name':forms.TextInput(attrs={'placeholder':'Customer Name'}),
            'mail_address':forms.TextInput(attrs={'placeholder':'Mail Address'}),
            'agent_name':forms.TextInput(attrs={'placeholder':'Agent Name'}),
            'address':forms.TextInput(attrs={'placeholder':'Address'}),
            'city':forms.TextInput(attrs={'placeholder':'City'}),
            'state':forms.TextInput(attrs={'placeholder':'State'}),
            'zip_code':forms.TextInput(attrs={'placeholder':'Zip Code'}),
            'customer_phone':forms.TextInput(attrs={'placeholder':'Customer Phone'}),
            'credit_card_type':forms.TextInput(attrs={'placeholder':'Credit Card Type'}),
            'credit_card_number':forms.TextInput(attrs={'placeholder':'Credit Card Number'}),
        }
