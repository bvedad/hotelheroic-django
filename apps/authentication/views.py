from allauth.account.forms import LoginForm
from allauth.account.utils import get_next_redirect_url
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_request_param
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from allauth.account.views import RedirectAuthenticatedUserMixin, \
    AjaxCapableProcessFormViewMixin, sensitive_post_parameters_m
from django.views.generic.edit import FormView

User = get_user_model()


class LoginView(
    RedirectAuthenticatedUserMixin, AjaxCapableProcessFormViewMixin, FormView
):
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = None
    redirect_field_name = "next"

    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_form_class(self):
        return LoginForm

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response

    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (
                get_next_redirect_url(self.request, self.redirect_field_name)
                or self.success_url
        )
        return ret

    def get_context_data(self, **kwargs):
        ret = super(LoginView, self).get_context_data(**kwargs)
        redirect_field_value = get_request_param(self.request, self.redirect_field_name)
        site = get_current_site(self.request)

        ret.update(
            {
                "site": site,
                "redirect_field_name": self.redirect_field_name,
                "redirect_field_value": redirect_field_value,
            }
        )
        return ret
