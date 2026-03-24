from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_name):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)
        print(f"Added: {pdf}")

    merger.write(output_name)
    merger.close()

    print(f"✅ Merged PDF saved as {output_name}")

if __name__ == "__main__":
    # List your PDF files here
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

    output_file = "merged.pdf"

    merge_pdfs(pdf_files, output_file)