from django import forms

class TrackerForm(forms.Form):
    WORK_MODE_CHOICES = [
        ('work_from_home', 'Work from Home'),
        ('work_from_office', 'Work from Office'),
    ]
    
    SHIFT_TIMINGS = [
        ('10am_to_8pm',  '10am to 8pm'),
        ('9pm_to_6am',   '9pm to 6am' ),


    ]

    TEAM_LEAD_CHOICES = [
        ('mahi', 'Mahi'),
        ('geetha', 'Geetha'),
        ('sita', 'Sita'),
        ('other', 'Other'),
    ]

    working_date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    work_mode = forms.ChoiceField(choices=WORK_MODE_CHOICES, required=True)
    shift_timings =  forms.ChoiceField(choices=SHIFT_TIMINGS, required=True)

    team_lead = forms.ChoiceField(choices=TEAM_LEAD_CHOICES, required=True)
    other_team_lead = forms.CharField(required=False)
    tasks = forms.CharField(widget=forms.Textarea, required=True)
