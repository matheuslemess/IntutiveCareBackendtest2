import tabula
import zipfile

tabula.convert_into("anexo.pdf", "anexo.csv", pages="all", output_format="csv")

with zipfile.ZipFile("test2.zip", "w") as myzip:
  myzip.write("anexo.pdf")
  myzip.write("anexo.csv")