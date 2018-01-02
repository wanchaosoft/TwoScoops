# -*- encoding: utf-8 -*-


from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, View, CreateView
# Create your views here.
from braces.views import LoginRequiredMixin

from products.mixins import FlavorActionMixin
from products.models import FlavorReview


class FlavorDetailView(LoginRequiredMixin, DetailView):
    """通过pk来获取详情"""
    model = FlavorReview


class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):
    """Views and ModelForm"""
    model = FlavorReview

    fields = ('title', 'slug', 'scoops_remaining')
    success_msg = 'Flavor created'  # custom messages

    def form_valid(self, form):
        # Do custom logic here
        messages.info(self.request, self.success_msg)
        """Messages add_message to request._messages
        You can call this var via {{messages}}
        For example:
        {# templates/flavors/flavor_detail.html #}
        {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                <li id="message_{{ forloop.counter }}"
                    {% if message.tags %} class="{{ message.tags }}"
                        {% endif %}>
                    {{ message }}
                </li>
                {% endfor %}
            </ul>
        {% endif %}"""
        return super(FlavorCreateView, self).form_valid(form)

    def form_invalid(self, form):
        # Do custom logic here
        return super(FlavorCreateView, self).form_invalid(form)
