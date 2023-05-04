# from django.shortcuts import render,get_object_or_404
# from .forms import DocumentForm
# from .models import Archivo
# from django.core.paginator import Paginator

# from django.conf import settings
# from django.http import HttpResponse
# import os

# from django.views.generic import ListView




#! ____________________________________________________________________________________________________________________

# def upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = DocumentForm()
#     return render(request, 'carta/upload.html', {'form': form})

#! ____________________________________________________________________________________________________________________


# class BuscadorView(ListView):
#     model = Archivo
#     template_name = 'archivo_list.html'
#     paginate_by = 3

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             return Archivo.objects.filter(nombre__icontains=query)
#         else:
#             return Archivo.objects.all()

#! ____________________________________________________________________________________________________________________

# def ver_pdf(request, archivo_id):
#     archivo = Archivo.objects.get(id=archivo_id)
#     pdf_url = archivo.archivo.url
#     pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_url[1:])
#     with open(pdf_path, 'rb') as pdf:
#         response = HttpResponse(pdf.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=' + os.path.basename(pdf_path)
#         return response


