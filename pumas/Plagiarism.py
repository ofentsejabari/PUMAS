###############################################################################
from pumas.docxToText import document_lexicon, docx_to_text, compare_documents


def process_files(new_file, allDocuments):

    ''' Allowable file type .pdf, .docx and .doc '''
    allowed_extensions = ['pdf', 'docx', 'doc']
    perc_plag = []

    for file in allDocuments:

        filename, file_extension = file.attachment.url.split('.')
        print(file_extension)
        if file_extension in allowed_extensions:

            '''Do no compare the uploaded file to itself
               Only process approved documents'''
            if file.attachment.path != new_file and file.status == 'approved':

                print("--------------------   FILE PATH  --------------------")
                print(file.attachment.path)
                print("--------------------   DOCUMENT TEXT -----------------")
                print(docx_to_text(file.attachment.path))
                print("--------------------   DOCUMENT LEXICON --------------")
                print(document_lexicon(docx_to_text(file.attachment.path)))

                perc_plag.append(compare_documents(document_lexicon(docx_to_text(file.attachment.path)),
                                                   document_lexicon(docx_to_text(new_file))))

    print("+++++++++++++++", perc_plag, '++++++++++++++')

    if len(perc_plag) != 0:
        return max(perc_plag)
    return 0.0
#################################################################################
# process_files('../../media/uploads/2017/oop.docx')