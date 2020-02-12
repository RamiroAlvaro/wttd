from django.views.generic import DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription

new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')

detail = DetailView.as_view(model=Subscription)

# def new(request):
#     if request.method == 'POST':
#         return create(request)
#
#     return empty_form(request)
#
#
# def empty_form(request):
#     return render(request, 'subscriptions/subscription_form.html',
#                   {'form': SubscriptionForm()})
#
#
# def create(request):
#     form = SubscriptionForm(request.POST)
#     if not form.is_valid():
#         return render(request, 'subscriptions/subscription_form.html',
#                       {'form': form})
#
#     # Con forms.ModelForm
#     subscription = form.save()
#
#     # Con forms.Form
#     # subscription = Subscription.objects.create(**form.cleaned_data)
#
#     # Send email
#     _send_mail('Confirmação de inscrição',
#                settings.DEFAULT_FROM_EMAIL,
#                subscription.email,
#                'subscriptions/subscription_email.txt',
#                {'subscription': subscription})
#
#     return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


# def detail(request, pk):
#     subscription = get_object_or_404(Subscription, pk=pk)
#     return render(request, 'subscriptions/subscription_detail.html',
#                   {'subscription': subscription})


# def _send_mail(subject, from_, to, template_name, context):
#     body = render_to_string(template_name, context)
#     mail.send_mail(subject, body, from_, [from_, to])
