from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import Usuario
from django.http import HttpResponse
from paginapp.models import Articulos
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
Usuario = get_user_model()

class RegistroUsuarioView(CreateView):
    model = Usuario
    form_class = CustomUserCreationForm
    template_name = 'registro.html'
    success_url = '/login'



def form_valid(self, form):

    Usuario = form.save(commit=False)
    Usuario.set_password(form.cleaned_data['password'])
    Usuario.save()
    login(self.request, Usuario)
    return super().form_valid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        Usuario = authenticate(request, username=username, password=password)
        if Usuario is not None:
            login(request, Usuario)
            return redirect('inicio')
    else:
        return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'inicio.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Usuario = form.save()
            login(request, Usuario)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Artículo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)




def enviar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST['name']
        email = request.POST['email']
        asunto = request.POST['subject']
        mensaje = request.POST['message']

        send_mail(
            f"{asunto} - {nombre}",
            mensaje,
            email,
            [''],
            fail_silently=False,
        )
        return render(request, 'contacto_exitoso.html')
    return render(request, 'contacto.html')


@login_required
def indice(request):
    return render(request, 'indice.html')


def indice(request):
    return render(request, 'indice.html')


def home(request):
    return render(request, 'paginapp/home.html')


