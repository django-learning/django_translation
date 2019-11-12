from django.shortcuts import render
from django.utils.translation import gettext as _, activate


def blog_view(request):
    # Translator: This Message blog Title
    title = _('Welcome.')
    print(request.LANGUAGE_CODE)
    return render(request, 'blog/blog_index.html', {"title": title})


def blog_ajax_view(request):
    title = _('Welcome.')
    lang = request.POST.get('lang')
    if request.POST.get('lang'):
        activate(lang)
        request.LANGUAGE_CODE = lang
        LANGUAGE_CODE = lang
    else:
        activate('en')
        request.LANGUAGE_CODE = 'en'
        LANGUAGE_CODE = 'en'
    return render(request, 'blog/blog_ajajx_index.html', {"title": title, "LANGUAGE_CODE": LANGUAGE_CODE})
