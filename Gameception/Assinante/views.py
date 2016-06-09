from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User

from .models import Assinante
from .models import EnderecoAssinatura
from .models import DadosAssinatura
from .models import DadosBancarios
from .models import Genero
from .models import SistOp
from .models import Processadores
from .models import ChaveDownload
from .models import HistoricoJogos
from .models import Pedido
from .models import Jogo


def MinhaConta(request): #O NOME DESSA FUNCAO DEVE SER O MESMO DO .HTML, SENAO DA ERRO.
    #endereco = EnderecoAssinatura.objects.get(id=1) #peguei um endereco de assinatura que registrei no bd, so pra teste
    context_dict = {}

    try:
        infos_pagamento = DadosBancarios.objects.get(assinatura=request.user)
        context_dict['tem_infos_pagamento'] = True
        context_dict['infos_pagamento'] = infos_pagamento
    except:
        context_dict['tem_infos_pagamento'] = False

    try:
        infos_endereco = EnderecoAssinatura.objects.get(assinatura=request.user)
        context_dict['tem_infos_endereco'] = True
        context_dict['infos_endereco'] = infos_endereco
    except:
        context_dict['tem_infos_endereco'] = False

    try:
        assinatura = DadosAssinatura.objects.get(assinatura=request.user)
        context_dict['tem_assinatura'] = True
        context_dict['assinatura'] = assinatura
        context_dict['generos'] = assinatura.generosPessoais.all()
        print('a',assinatura.generosPessoais.all())
    except:
        context_dict['tem_assinatura'] = False
        context_dict['generos'] = []

    try:
        historico = HistoricoJogos.objects.get(assinatura=request.user)
        pedidos = Pedido.objects.filter(historico=historico)
        if len(pedidos) > 0:
            context_dict['tem_pedido_para_mostrar'] = True
            pedido_recente = pedidos.order_by('-numero')[0]
            context_dict['pedido_recente'] = pedido_recente
            if pedido_recente.tipoMidia == 'DIGITAL':
                context_dict['digital'] = True
                try:
                    context_dict['chaves'] = ChaveDownload.objects.filter(pedido=pedido_recente)
                except:
                    pass
            else:
                context_dict['digital'] = False
        else:
            context_dict['tem_pedido_para_mostrar'] = False
    except:
        context_dict['tem_pedido_para_mostrar'] = False

    context_dict['dados_completos'] = context_dict['tem_infos_endereco'] and context_dict['tem_infos_pagamento']



    return render(request, 'Assinante/Assinante.html', context_dict)
# esse nome no final (endereco) vai ser referenciado no .html pra mostrar os dados
# no fim, nao precisava dos gets tambem, mas deixei la por enquanto

def Historico(request):
    return render(request, 'MainPage2.html', {})

def HistoricoPedido(request, num_pedido):
    num = int(num_pedido)
    historico = HistoricoJogos.objects.get(assinatura=request.user)
    pedidos = Pedido.objects.filter(historico=historico)
    try:
        pedido = Pedido.objects.get(historico=historico,numero=num)
    except:
        pedido = None
    print(pedido)
    antecessor = num -1
    pode_antecessor = True
    sucessor = num + 1
    pode_sucessor = True
    if num >= len(pedidos) - 1:
        pode_sucessor = False
    if num <= 0:
        pode_antecessor = False
    context_dict = {'num_pedido' : num_pedido, 'pedido' : pedido}
    context_dict['antecessor'] = antecessor
    context_dict['pode_antecessor'] = pode_antecessor
    context_dict['sucessor'] = sucessor
    context_dict['pode_sucessor'] = pode_sucessor

    if pedido.tipoMidia == 'DIGITAL':
        context_dict['digital'] = True
        try:
            context_dict['chaves'] = ChaveDownload.objects.filter(pedido=pedido)
        except:
            pass
    else:
        context_dict['digital'] = False

    return render(request, 'Assinante/HistoricoPedido.html', context_dict)

def Assinatura(request):
    return render(request, 'Assinante/Assinatura.html', {})

def EditarCadastro(request):
    return render(request, 'Assinante/EditarCAdastro.html', {})

def InfoPagamento(request):
    finalizado = False
    if request.method == 'POST':
        form = InfoPagamentoForm(request.POST)      #Se o request for POST o usuario esta submetendo o formulario
        if form.is_valid():
            numeroCartao = form.cleaned_data['numeroCartaoForm']        #Obtem os valores submetidos pelo usuario atraves do formulario
            codigoSeguranca = form.cleaned_data['codigoSegurancaForm']
            nomeTitular = form.cleaned_data['nomeTitularForm']
            vencimento = form.cleaned_data['vencimentoForm']
            username = request.user.get_username()                  #Obtem o nome do usuario
            user = User.objects.get(username=username)
            try:
                dados = DadosBancarios.objects.get(assinatura=user)     #Verifica se o usuario em questao ja possui dados bancarios
            except:     #Colocar o tipo do except
                dados = DadosBancarios.objects.create(assinatura=user)  #Se o usuario nao possuir dados bancarios ainda um objeto eh criado para armazena-los
            dados.numeroCartao = numeroCartao                   #Armazena os dados obtidos do formulario no objeto dados
            dados.codigoSeguranca = codigoSeguranca
            dados.nomeTitular = nomeTitular
            dados.vencimento = vencimento
            dados.save()                            #Salva as alteracoes para o banco de dados
            finalizado = True
    else:
        form = InfoPagamentoForm()
        try:
            username = request.user.get_username()
            user = User.objects.get(username=username)
            dados = DadosBancarios.objects.get(assinatura=user)         #Verifica se o usuario ja possui dados bancarios
            form.fields["numeroCartaoForm"].initial = dados.numeroCartao
            form.fields["codigoSegurancaForm"].initial = dados.codigoSeguranca     #Se existem dados bancarios antigos, estes sao mostrados ao usuario
            form.fields["nomeTitularForm"].initial = dados.nomeTitular             #permitindo a ele alterar alguns valores sem ter que reescrever os demais
            form.fields["vencimentoForm"].initial = dados.vencimento
        except:     #Colocar o tipo do except
            pass
    return render(request, 'Assinante/InfoPagamento.html', {'form': form, 'finalizado': finalizado})

def CadastroEndereco(request):
    registrado = False
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            rua = form.cleaned_data['ruaForm']
            numeroRua = form.cleaned_data['numeroRuaForm']
            complemento = form.cleaned_data['complementoForm']
            CEP = form.cleaned_data['CEPForm']
            try:
                endereco = EnderecoAssinatura.objects.get(assinatura=request.user)
            except:
                endereco = EnderecoAssinatura.objects.create(assinatura=request.user)
            endereco.rua = rua
            endereco.numeroRua = numeroRua
            endereco.complemento = complemento
            endereco.CEP = CEP
            endereco.save()
            registrado = True
    else:
        form = EnderecoForm()
        try:
            endereco = EnderecoAssinatura.objects.get(assinatura=request.user)
            form.fields['ruaForm'].initial = endereco.rua
            form.fields['numeroRuaForm'].initial = endereco.numeroRua
            form.fields['complementoForm'].initial = endereco.complemento
            form.fields['CEPForm'].initial = endereco.CEP
        except:
            pass
    return render(request, 'Assinante/CadastroEndereco.html', {'form': form, 'registrado': registrado})

def Assinatura(request):
    registrado = False
    if request.method == 'POST':
        form = DadosAssinaturaForm(request.POST)
        if form.is_valid():
            generosPessoais = form.cleaned_data['generosPessoaisForm']
            quantidade = form.cleaned_data['quantidadeForm']
            precoPorJogo = form.cleaned_data['precoPorJogoForm']
            tipoMidia = form.cleaned_data['tipoMidiaForm']
            sistOp = form.cleaned_data['sistOpForm']
            memRAM = form.cleaned_data['memRAMForm']
            processador = form.cleaned_data['processadorForm']
            memVideo = form.cleaned_data['memVideoForm']
            try:
                dados = DadosAssinatura.objects.get(assinatura=request.user)
            except:
                dados = DadosAssinatura.objects.create(assinatura=request.user)
            dados.generosPessoais = generosPessoais
            dados.quantidade = quantidade
            dados.precoPorJogo = precoPorJogo
            dados.tipoMidia = tipoMidia
            dados.sistOp = sistOp
            dados.memRAM = memRAM
            dados.processador = processador
            dados.memVideo = memVideo
            dados.atividade = True
            dados.save()
            registrado = True
    else:
        form = DadosAssinaturaForm()
        try:
            dados = DadosAssinatura.objects.get(assinatura=request.user)
            form.fields['generosPessoaisForm'].initial = dados.generosPessoais.all()
            form.fields['quantidadeForm'].initial = dados.quantidade
            form.fields['precoPorJogoForm'].initial = dados.precoPorJogo
            form.fields['tipoMidiaForm'].initial = dados.tipoMidia
            form.fields['sistOpForm'].initial = dados.sistOp
            form.fields['memRAMForm'].initial = dados.memRAM
            form.fields['processadorForm'].initial = dados.processador
            form.fields['memVideoForm'].initial = dados.memVideo
        except:
            pass
    return render(request, 'Assinante/CadastroAssinatura.html', {'form': form, 'registrado': registrado})

def ContatoAdmin(request):
    return render(request, 'Assinante/ContatoAdmin.html', {})

def Cadastro(request):
    registrado = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        assinante_form = AssinanteForm(data=request.POST)
        if user_form.is_valid() and assinante_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            assinante = assinante_form.save(commit=False)
            assinante.usuario = user
            assinante.save()
            print(assinante.usuario)
            registrado = True
        else:
            print (user_form.errors, assinante_form.errors)
    else:
        user_form = UserForm()
        assinante_form = AssinanteForm()
    return render(request,
            'Assinante/Cadastro.html',
            {'user_form': user_form, 'registrado': registrado, 'assinante_form' : assinante_form} )

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/Assinante/')
            else:
                return HttpResponse(" account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'Assinante/Login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

class DadosAssinaturaForm(forms.Form):
    generosPessoaisForm = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Genero.objects.all())
    quantidadeForm = forms.IntegerField(min_value=1)
    precoPorJogoForm = forms.IntegerField(min_value=1)
    tipoMidiaForm = forms.ChoiceField(widget=forms.Select(), choices=(('FISICA', 'Fisica'),('DIGITAL', 'Digital'),))
    sistOpForm = forms.ModelChoiceField(widget=forms.Select(), queryset=SistOp.objects.all())
    memRAMForm = forms.IntegerField(min_value=1)
    processadorForm = forms.ModelChoiceField(widget=forms.Select(), queryset=Processadores.objects.all())
    memVideoForm = forms.IntegerField(min_value=1)
    def __init__(self, *args, **kwargs):
        super(DadosAssinaturaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if(field != self.fields['generosPessoaisForm']):
                field.widget.attrs['class'] = 'form-control'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AssinanteForm(forms.ModelForm):
    class Meta:
        model = Assinante
        fields = ('CPF', 'nome')

class EnderecoForm(forms.Form):
    ruaForm = forms.CharField(label='rua', max_length=200)
    numeroRuaForm = forms.IntegerField(label='numeroRua', min_value=1)
    complementoForm = forms.CharField(label='complemento', max_length=200)
    CEPForm = forms.CharField(label='CEP', min_length=8, max_length=8)
    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class InfoPagamentoForm(forms.Form):
    numeroCartaoForm = forms.CharField(label='Numero do cartao', max_length=16, min_length=16)
    codigoSegurancaForm = forms.CharField(label='Codigo de seguranca', max_length=3, min_length=3)
    nomeTitularForm = forms.CharField(label='Nome do titular', max_length=200, min_length=2)
    vencimentoForm = forms.CharField(label='Ano de vencimento', max_length=4, min_length=4)

class ContatoAdminForm(forms.Form):
    assunto = forms.CharField(label='Assunto')
    menssagem = forms.CharField(label='Menssagem')
