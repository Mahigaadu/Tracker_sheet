from django.shortcuts import render,redirect
from .forms import *
from .mongodb import *

# Create your views here.
def home(rquest):
    return render(rquest,'trackerapp/home.html')

# this is used to process fields created using html

def tracker_form(request):
    if request.method == 'POST':
        working_date = request.POST.get('working_date')
        work_mode = request.POST.get('work_mode')
        shift_timings = request.POST.get('shift_timings')
        team_lead = request.POST.get('team_lead')
        if team_lead == 'other':
            team_lead = request.POST.get('other_team_lead')
        tasks = request.POST.get('tasks')
        # saving  data to database
        db = get_db()
        data = {
            'working_date': working_date,
            'shift_timings': shift_timings,
            'work_mode': work_mode,
            'team_lead': team_lead,
            'tasks': tasks
        }
        db.employee_data.insert_one(data)

        # Process the data as needed

        return redirect('success')

    return render(request, 'trackerapp/tracker_html.html')

# this function is used to process fields created using form.py to display in  the template
'''
def tracker_form(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            working_date = form.cleaned_data['working_date']
            work_mode = form.cleaned_data['work_mode']
            team_lead = form.cleaned_data['team_lead']
            if team_lead == 'other':
                team_lead = form.cleaned_data['other_team_lead']
            tasks = form.cleaned_data['tasks']

            # Process the data as needed

            return redirect('success')
    else:
        form = TrackerForm()

    return render(request, 'trackerapp/tracker_form.html', {'form': form})
'''
def success(request):
    return render(request, 'trackerapp/success.html')

# this function displays the data stored in mongodb
def display_data(request):
    db = get_db()
    collection = db['employee_data']
    data = list(collection.find())

    return render(request, 'trackerapp/display_data.html', {'data': data})
