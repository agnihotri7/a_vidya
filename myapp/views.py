"""
    all business logic here.
"""
from datetime import date
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from myapp.models import Profiles, City, Designation, Skill


def paginate_data(request, query, per_page=25):
    paginator = Paginator(query, per_page) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)
    return query


@login_required
def index(request):
    """
    """
    return render_to_response("home.html", {},
        context_instance=RequestContext(request))


@login_required
def profiles(request):
    """
    """
    ctx = {}
    profiles = Profiles.objects.all()
    skills = Skill.objects.all()
    cities = City.objects.all()
    designations = Designation.objects.all()

    query = {}
    skill_id = request.GET.get('skills')
    if skill_id:
        profiles = profiles.filter(skills__id=int(skill_id))
        query.update({'skills': skill_id})

    ctc = request.GET.get('ctc')
    if ctc:
        query.update({'ctc': ctc})
        ctc_gt = int(ctc.split('-')[0])
        ctc_lt = int(ctc.split('-')[1])
        profiles = profiles.filter(ctc__gte=int(ctc_gt)).filter(ctc__lte=int(ctc_lt))

    location_id = request.GET.get('location')
    if location_id:
        query.update({'location': location_id})
        profiles = profiles.filter(current_city__id=int(location_id))

    experience = request.GET.get('experience')
    if experience:
        query.update({'experience': experience})
        exp_gt = int(experience.split('-')[0])
        exp_lt = int(experience.split('-')[1])
        profiles = profiles.filter(experience__gte=int(exp_gt)).filter(experience__lte=int(exp_lt))

    designation_id = request.GET.get('designation')
    if designation_id:
        query.update({'designation': designation_id})
        profiles = profiles.filter(current_designation__id=int(designation_id))

    if request.GET.get('download') == "True":
        return download_csv(profiles)

    profiles = paginate_data(request, profiles, 10)
    ctx.update({
            'profiles': profiles,
            'skills': skills,
            'designations': designations,
            'cities': cities,
            'query': query,
        })
    return render_to_response("profiles.html", ctx,
        context_instance=RequestContext(request))

def download_csv(profiles):
    import csv
    from django.http import HttpResponse
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    writer = csv.writer(response)
    writer.writerow(['Sno', 'Name', 'Email', 'mobile', 'resume', 'ctc', \
                    'designation', 'city', 'experience'])
    for p in profiles:
        writer.writerow([p.sno, p.name, p.email, p.mobile, p.get_resume_display(), p.ctc,\
                         p.current_designation.name, p.current_city.name, p.experience])
    return response
