# Separador de ficheros PDF.
# Selecciona un fichero y crea un fichero nuevo por página.

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
        more_number = input ("¿Deseas introducir una nueva página a separar?")
        print (more_number)
        if more_number.lower() != "si":
            enter_number = False
        else:
            enter_number = True


pdf_original = PdfReader (path_file_orig)

for index,page in enumerate (pdf_original.pages):
    print ("el valor de index es: %d " %(index))
    for i in pages_separator:
        print ("valor de i %d" %(i))
        if index + 1 == i:
            pdf_writer = PdfWriter ()
            pdf_writer.add_page (page)
            with open (f"Page_{index+1}.pdf","wb") as out:
                pdf_writer.write(out)