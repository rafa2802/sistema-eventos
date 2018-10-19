from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Evento, Atividade, Palestrante
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddAtividadeForm

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        if self.request.user.is_staff:
            eventos_adm = Evento.objects.filter(dono = self.request.user).order_by('-criado')
            return render(request, 'evento/home_adm.html', {'eventos_adm': eventos_adm})
        eventos = Evento.objects.all().order_by('-criado')
        return render(request, 'evento/home.html', {'eventos': eventos})

    def post(self, request):
        evento = Evento(dono = self.request.user, nome = request.POST.get('nome'))
        evento.save()
        return redirect('evento:sucesso', pk = evento.pk)

class Sucesso(View):
    def get(self, request, pk):
        evento = Evento.objects.filter(id = pk).first()
        return render(request, 'evento/sucesso.html', {'evento': evento})

class EventoAdmin(View):
    def get(self, request, pk):
        evento = Evento.objects.filter(id=pk).first()
        palestrantes = Palestrante.objects.all()
        return render(request, 'evento/detalhes_adm.html', {'evento': evento, 'palestrantes': palestrantes})

    def post(self, request, pk):
        print(request.POST)
        if request.form is valid:
            form.save()
            return redirect('evento:detalhes-evento-adm', pk = pk)

class AddPalestrante(View):
    def post(self, request, pk):
        palestrante = Palestrante(nome = request.POST.get('nome'))
        palestrante.save()
        return redirect('evento:evento-detalhe-adm', pk = pk)

class AddAtividade(View):
    def post(self, request, pk):
        palestrante = Palestrante.objects.filter(id = request.POST.get('palestrante')).first()
        atividade = Atividade(palestrante = palestrante, nome = request.POST.get('nome'), duracao = request.POST.get('duracao'), data = request.POST.get('data'), hora = request.POST.get('hora'), tipo = request.POST.get('tipo'))
        atividade.save()
        evento = Evento.objects.filter(id = pk).first()
        if request.POST.get('tipo') == '0':
            evento.palestras.add(atividade)
        else:
            evento.minicursos.add(atividade)
        evento.save()
        return redirect('evento:evento-detalhe-adm', pk = pk)

class EventoDetalhe(View):
    def get(self, request, pk):
        evento = Evento.objects.filter(id = pk).first()
        return render(request, 'evento/detalhes_evento.html', {'evento': evento})

class ExcluirEvento(View):
    def post(self, request, pk):
        evento = Evento.objects.filter(id = pk).first()
        if len(evento.palestras.all()) != 0:
            for palestra in evento.palestras.all():
                palestra.delete()
        if len(evento.minicursos.all()) != 0:
            for minicurso in evento.minicursos.all():
                minicurso.delete()
        evento.delete()
        return redirect('evento:home')

class EditarEvento(View):
    def post(self, request, pk):
        evento = Evento.objects.filter(id = pk).first()
        evento.nome = request.POST.get('nome')
        evento.save()
        return redirect('evento:evento-detalhe-adm', pk = pk)

class AtividadeAdmin(View):
    def get(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        palestrantes = Palestrante.objects.all()
        return render(request, 'evento/detalhes_atividade_adm.html', {'atividade': atividade, 'palestrantes': palestrantes})

class EditarAtividade(View):
    def post(self, request, pk):
        palestrante = Palestrante.objects.filter(id = request.POST.get('palestrante')).first()
        atividade = Atividade.objects.filter(id = pk).first()
        atividade.palestrante = palestrante
        atividade.nome = request.POST.get('nome')
        atividade.duracao = request.POST.get('duracao')
        atividade.hora = request.POST.get('hora')
        atividade.save()
        return redirect('evento:detalhes-atividade', pk = pk)

class ExcluirAtividade(View):
    def post(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        atividade.delete()
        return redirect('evento:home')

class GerarLista(View):
    def get(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        if len(atividade.inscritos.all()) == 0:
            return render(request, 'evento/error.html', {'mensagem': 'Não foi possível gerar a lista, pois não há inscrições para essa atividade!'})
        return render(request, 'evento/gerar_lista.html', {'atividade': atividade})

class Participando(View):
    def get(self, request, pk):
        eventos = Evento.objects.all()
        eventos_user = []
        if len(eventos) != 0:
            for evento in eventos:
                aux = 0
                for minicurso in evento.minicursos.all():
                    if self.request.user in minicurso.inscritos.all():
                        aux += 1
                for palestra in evento.palestras.all():
                    if self.request.user in palestra.inscritos.all():
                        aux += 1
                if aux != 0:
                    eventos_user.append(evento)
        return render(request, 'evento/eventos_user.html', {'eventos': eventos_user})

class Inscrever(View):
    def post(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        if atividade.tipo == 0:
            atividade.inscritos.add(self.request.user)
            atividade.save()
            return redirect('evento:detalhes-atividade', pk = pk)
        eventos = Evento.objects.all()
        for evento in eventos:
            if atividade in evento.minicursos.all():
                eventos = evento
                break
        aux = 0
        for minicurso in eventos.minicursos.all():
            if self.request.user in minicurso.inscritos.all():
                aux += 1
        if aux == 2:
            return render(request, 'evento/error.html', {'mensagem': 'Você não pode se inscrever em mais de 2 minicursos!'})
        atividade.inscritos.add(self.request.user)
        atividade.save()
        return redirect('evento:detalhes-atividade', pk = pk)

class Cancelar(View):
    def post(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        atividade.inscritos.remove(self.request.user)
        atividade.save()
        return redirect('evento:detalhes-atividade', pk = pk)


