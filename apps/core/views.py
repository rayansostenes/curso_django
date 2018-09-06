import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from django.http import FileResponse, StreamingHttpResponse, HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Person

from core.forms import PersonForm

import pypandoc
import json

class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'email', 'is_active']
    success_url = '/core/person/list'
    # template_name = 'base_form.html

class PersonFormView(FormView):
    success_url = '/core/person/list'
    form_class = PersonForm
    template_name = 'core/person_form.html'

    def form_valid(self, form):
        print('FORM VALIDO')
        return HttpResponse('Form Valido')


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

class PersonList(LoginRequiredMixin, ListView):
    model = Person
    context_object_name = 'pessoas'
    login_url = '/core/login'

    def get_context_data(self, *args, **kw):
        result = super().get_context_data(*args, **kw)
        result['test_dict'] = {
            'foo': 'Bar'
        }
        result['counter'] = Counter()
        result['collumns'] = (
            ('Nome', 'name'),
            ('E-mail', 'email'),
            ('Ativo', 'is_active'),
        )
        return result


class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'email', 'is_active']
    success_url = '/core/person/list'


class PersonDelete(DeleteView):
    model = Person
    success_url = '/core/person/list'
    

def create_docx(request):
    buffer = io.BytesIO
    input_text = """
        # Titulo
        ## Subtitulo
        lorem 
        > Citacao

        ```python
            import sys
        ```
    """

    with open('file.md', 'w') as md_file:
        md_file.write(input_text)
    
    output = pypandoc.convert_file('file.md', 'docx', format='md', outputfile='file.docx')
    with open('file.docx', 'rb') as doc_file:
        return FileResponse(doc_file, as_attachment=True, filename='file.docx')


class Echo:
    def write(self, value):
        return value

def create_csv(request):
    import csv
    buffer = Echo()
    writer = csv.writer(buffer)
    rows = (
        writer.writerow((f'Linha {i}', i**2, i**3, i**4, i**5))
        for i in range(100)
    )
    response = StreamingHttpResponse(rows, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    return response


def create_pdf(request):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica', 12)

    for i in range(2):
        pdf.drawString(30,750,'OFFICIAL COMMUNIQUE')
        pdf.drawString(30,735,'OF ACME INDUSTRIES')
        pdf.drawString(500,750,"12/12/2010")
        pdf.line(480,747,580,747)
        
        pdf.drawString(275,725,'AMOUNT OWED:')
        pdf.drawString(500,725,"$1,000.00")
        pdf.line(378,723,580,723)
        
        pdf.drawString(30,703,'RECEIVED BY:')
        pdf.line(120,700,580,700)
        pdf.drawString(120,703,"JOHN DOE")
        pdf.showPage()

    # Fechar Arquivo
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, filename='hello_world.pdf', as_attachment=False)


def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()