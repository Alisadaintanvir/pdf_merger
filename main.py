from PyPDF2 import PdfWriter


def pdf_combiner(*argv):
    merger = PdfWriter()

    for pdf in argv:
        merger.append(pdf)
    merger.write('merged.pdf')
    merger.close()


pdf_combiner('dummy.pdf', 'wtr.pdf', 'twopage.pdf')
