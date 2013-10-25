from django.shortcuts import render_to_response


def launch(request):
    context = {
        'widgets': ['hello world', 'hi there', ],
    }
    return render_to_response('launch.html', context)
