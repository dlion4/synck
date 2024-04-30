from .form import ContactForm


def core_context_processor(request):
    return dict(form=ContactForm())
