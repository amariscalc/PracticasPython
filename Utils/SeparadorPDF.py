# Separador de ficheros PDF. Selecciona un fichero y crea un fichero nuevo por página.
# Especial agradecimiento a "Pildoras de Programación". https://linktr.ee/Pildorasdeprogramacion
# https://www.facebook.com/reel/964369837988928?fs=e&s=TIeQ9V

from PyPDF2 import PdfReader, PdfWriter

path_file_orig = input ("Introduce fichero a separar: ")
pages_separator = list ()

enter_number = True

while enter_number:
    try:
        number = int (input ("Introduce número de página: "))
    except ValueError as error_value:
        print ("No has introducido un número válido.")
    else:
        pages_separator.append(number)
    finally:
        add_number = input ("¿Deseas introducir una nueva página a separar?")

        if add_number.lower() != "si":
            enter_number = False
        else:
            enter_number = True


pdf_original = PdfReader (path_file_orig)

for index,page in enumerate (pdf_original.pages):
    for i in pages_separator:
        if index + 1 == i:
            pdf_writer = PdfWriter ()
            pdf_writer.add_page (page)
            with open (f"Page_{index+1}.pdf","wb") as out:
                pdf_writer.write(out)