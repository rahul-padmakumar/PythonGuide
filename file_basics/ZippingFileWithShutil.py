import shutil

shutil.make_archive('sh_zip', 'zip',
                    'extracted_contents')

shutil.unpack_archive('sh_zip.zip', "extracted", 'zip')

