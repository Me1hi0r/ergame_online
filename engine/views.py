from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm


def create_user(request):
    if request.user.is_authenticated:
        return redirect('intro')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}.')
                return redirect('login')

        context = {'form': form}
        return render(request, 'engine/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('intro')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('start')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'engine/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def start_page(request):
    start_text = \
    """
    You have a chance to investigate a mystery from the past:
    the year 2020, an opening of the time capsule solemnly buried in
    2000 turns into a worldwide mystery when strange files named
    SARS-CoV-2 are discovered among its contents.

    Now is the time to gather your thoughts and call friends (zoom, facetime, etc)
    Before you start, be sure to read the rules of the game.
    """
    context = {
        'start_text': start_text,
        'video': 'blur',
        'btn_show': False,
    }
    return render(request, 'engine/start.html', context)


@login_required(login_url='login')
def intro1(request):
    return render(request, 'engine/intro1.html', {'video': 'intro'})


@login_required(login_url='login')
def intro2(request):
    return render(request, 'engine/intro2.html', {'video': 'at'})


# @login_required(login_url='login')
# def intro2(request):
#     return render(request, 'engine/intro2.html', {'video': 'at'})

# 'button_list': ['test'],

    #  {% for button in button_list %}
    #     <li class="nav-item">
    #         <a class="nav-link" href="/{{button}}">
    #             {{button}}
    #         </a>
    #     </li>
    # {% endfor %}


@login_required(login_url='login')
def lab(request):
    context = {'picture': '/static/engine/images/lab.jpg'}
    return render(request, 'engine/laboratory.html', context)


@login_required(login_url='login')
def lab_3d(request):
    context = {'picture': '/static/engine/images/lab.jpg'}
    return render(request, 'engine/laboratory3d.html', context)


@login_required(login_url='login')
def lab_table(request, watch=False):
    context = {'picture': '/static/engine/images/table.jpg'}
    if watch:
        context = {'picture': '/static/engine/images/table.jpg',
                   'watch': True}
    return render(request, 'engine/lab_tab.html', context)


@login_required(login_url='login')
def lab_table_video(request):
    ctx = {'video': 'virus_table'}
    return render(request, 'engine/lab_tab_video.html', ctx)


@login_required(login_url='login')
def lab_table_news(request):
    ctx = {'picture': '/static/engine/images/news_page.jpg'}
    return render(request, 'engine/lab_tab_news.html', ctx)


@login_required(login_url='login')
def lab_table_news_check(request, answer='text text'):
    print(request)
    ans = request.GET.get('answer')
    print(ans)
    if ans.lower() == 'plague':
        answer = """
        The purple vaccine should
but below the blue,
and not next to it
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tab_news_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/news_page.jpg'}
        return render(request, 'engine/lab_tab_news.html', ctx)


@login_required(login_url='login')
def lab_table_paper(request):
    ctx = {'picture': '/static/engine/images/paper.jpg'}
    return render(request, 'engine/lab_tab_paper.html', ctx)


@login_required(login_url='login')
def lab_tv(request):
    ctx = {'picture': '/static/engine/images/tv.jpg'}
    return render(request, 'engine/lab_tv.html', ctx)


@login_required(login_url='login')
def lab_tv_video(request, video):
    if video == 1:
        ctx = {'video': 'Mutation'}
    if video == 2:
        ctx = {'video': 'Mutation2'}
    return render(request, 'engine/lab_tv_video.html', ctx)


@login_required(login_url='login')
def lab_tv_puzzle(request):
    print(request)
    ans1 = request.GET.get('ans1')
    ans2 = request.GET.get('ans2')
    ans3 = request.GET.get('ans3')
    ans4 = request.GET.get('ans4')
    print(ans1, ans2, ans3, ans4)
    if ans1 == 'GH' and ans2 == 'DA' and ans3 == 'EB' and ans4 == 'CF':
        answer = """
        The yellow vaccine should be next to red
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tv_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/mutation.jpg'}
        return render(request, 'engine/lab_tv_puzzle.html', ctx)


@login_required(login_url='login')
def lab_probes(request):
    ctx = {'picture': '/static/engine/images/probs.jpg'}
    return render(request, 'engine/lab_probes.html', ctx)


@login_required(login_url='login')
def lab_probes_check(request):
    print(request)
    ans1 = request.GET.get('ans1')
    ans2 = request.GET.get('ans2')
    ans3 = request.GET.get('ans3')
    ans4 = request.GET.get('ans4')
    print(ans1, ans2, ans3, ans4)
    if ans1.upper() == 'EBOLA' and ans2.upper() == 'MERS' and ans3.upper() == 'FLU' and ans4.upper() == 'CORONA':
        answer = """
        The purple vaccine should be above the green but not next to it
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tab_news_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/probs.jpg'}
        return render(request, 'engine/lab_probes.html', ctx)


@login_required(login_url='login')
def lab_reagents(request):
    ctx = {'picture': '/static/engine/images/Reagents.jpg'}
    return render(request, 'engine/lab_reagents.html', ctx)


@login_required(login_url='login')
def lab_suites(request):
    ctx = {'picture': '/static/engine/images/him.jpg'}
    return render(request, 'engine/lab_suites.html', ctx)


# @login_required(login_url='login')
# def main(request):
#     return render(request, 'engine/main.html', {})




# @login_required(login_url='login')
# def panel(request):
#     return render(request, 'engine/game_panel.html', {})