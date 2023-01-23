from django import forms
def GenForm(Model,listHiddenfield=[]):
    data = {field:forms.HiddenInput() for field in listHiddenfield}
    class newform(forms.ModelForm):
        class Meta:
            model = Model
            exclude = ('id',)
            widgets = data
        def __init__(self, *args, **kwargs):
            super(newform, self).__init__(*args, **kwargs)
            for f in Model._meta.fields:
                if "DateTimeField" in str(type(f)):
                    print('DateTimeField is present',f.name)
                    try:
                        self.fields[f.name].widget.attrs['class'] = 'vDateTime'
                    except Exception:
                        pass
                if "ForeignKey" in str(type(f)):
                    print('ForeignKey is present',f.name)
                    try:
                        self.fields[f.name].widget  = widgets.RelatedFieldWidgetWrapper(
                        self.fields[f.name].widget,
                        self.instance._meta.get_field(f.name).remote_field,
                        admin_site
                    )
                    except Exception:
                        pass
                if "ManyToManyField" in str(type(f)):
                    print('ManyToManyField is present',f.name)
                    try:
                        pass
                    except Exception:
                        pass 
                           
    return newform  
