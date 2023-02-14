from PyPDF2 import PdfReader, PdfWriter, Transformation
import sys

if __name__ == "__main__":
    pdfI = sys.argv[1]
    aux = pdfI.split(".")

    pdfO = aux[0] + "_wide.pdf"
    pdfI = PdfReader(pdfI)
    writer = PdfWriter()  # create a writer to save the updated results
    for page in pdfI.pages:
        page.scale(sx=2, sy=1)

        op = Transformation().scale(sx=0.5, sy=1)
        page.add_transformation(op)

        writer.add_page(page)
    with open(pdfO, "wb+") as f:
        writer.write(f)
