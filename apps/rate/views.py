from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django_tables2 import SingleTableView

from apps.rate.forms import RateIntervalForm
from apps.rate.models import RateInterval
from apps.rate.tables import RateIntervalTable
from apps.room.models import RoomType


@login_required
def rates_availability_view(request):
    return redirect('rate_interval_index')


class RateIntervalListView(LoginRequiredMixin, SingleTableView):
    model = RateInterval
    table_class = RateIntervalTable
    template_name = 'home/rate/interval/index.html'

    def get_queryset(self):
        room_type_id = self.request.GET.get('room_type')
        if room_type_id:
            return RateInterval.objects.filter(room_type__id=room_type_id)
        return RateInterval.objects.all()

    def dispatch(self, request, *args, **kwargs):
        room_type_id = self.request.GET.get('room_type')
        room_types = RoomType.objects.first()
        if room_type_id is None and room_types:
            room_type_id = room_types.id
            return redirect(f"{self.request.path}?room_type={room_type_id}")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RateIntervalListView, self).get_context_data(**kwargs)
        context['form'] = RateIntervalForm()
        context['room_types'] = RoomType.objects.all()

        return context


@login_required
def rate_interval_edit_view(request, pk):
    item = get_object_or_404(RateInterval, pk=pk)
    if request.method == 'POST':
        form = RateIntervalForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('rate_interval_index') + f"?room_type={item.room_type.id}")
    else:
        form = RateIntervalForm(instance=item)
        context = {'form': form}
        context['room_types'] = RoomType.objects.all()
        return render(request, 'home/rate/interval/create.html', context)


@login_required
def rate_interval_create_view(request):
    room_type = RoomType.objects.filter(pk=request.GET.get('room_type')).first()
    if request.GET.get('room_type') is None or not room_type:
        return redirect('rate_interval_index')
    if request.method == 'POST':
        form = RateIntervalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rate_interval_index') + f"?room_type={room_type.id}")
    else:
        form = RateIntervalForm(initial={'room_type': room_type.id})
    context = {'form': form}
    context['room_types'] = RoomType.objects.all()
    return render(request, 'home/rate/interval/create.html', context)
