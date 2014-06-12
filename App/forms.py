__author__ = 'andong'

# 已废弃

from django import forms

class AncientBookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'span3'}),max_length=30,label="书名")
    writer = forms.CharField(widget=forms.TextInput(attrs={'class':'span3'}),max_length=5,label="姓名")
    nation = forms.CharField(widget=forms.TextInput(attrs={'class':'span2'}),max_length=10,label="朝代")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'area tb-rl'}),label="内容")


class ModernBookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'span3'}),max_length=30,label="书名")
    writer = forms.CharField(widget=forms.TextInput(attrs={'class':'span3'}),max_length=5,label="姓名")
    nation = forms.CharField(widget=forms.TextInput(attrs={'class':'span2'}),max_length=10,label="国家")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'area tb-rl'}),label="内容")
