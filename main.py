#!/usr/bin/python

import argparse, subprocess

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("--city", help='Ciudad donde labora')
    parser.add_argument("--redactionDate", help='Fecha en la que se redacto la carta')
    parser.add_argument("--receiverSex", help="Sexo del destinatoario(M/F)")
    parser.add_argument("--receiverName", help="Nombre del destinatario")
    parser.add_argument("--jobTitle", help="Cargo del destinatario")
    parser.add_argument("--businessName", help="Razón social de la empresa")
    parser.add_argument("--resignationDate", help="Fecha último día de opraciones")
    parser.add_argument("--needsExoneration", help="necesita exonerción por renunciar antes de los 30 días?(Y/N)")
    parser.add_argument("--docNumber", help="Número del DNI")
    parser.add_argument("--fullName", help="Nombre completo")

    args = parser.parse_args()
    
    city = input("Ingrese la ciudad donde labora: ") if args.city is None else args.city
    redactionDate = input("Ingrese la fecha en la que dice que redacto la carta: ") if args.redactionDate is None else args.redactionDate
    receiverSex = input("Sexo del destinatario?(M/F): ") if args.receiverSex is None else args.receiverSex
    receiverName = input("Ingrese el nombre del destinatario: ") if args.receiverName is None else args.receiverName
    jobTitle = input("Ingrese el cargo del destinatario: ") if args.jobTitle is None else args.jobTitle
    businessName = input("Razón social de la empresa: ") if args.businessName is None else args.businessName
    resignationDate = input("Ingrese la fecha de su último día de operaciones: ") if args.resignationDate is None else args.resignationDate
    needsExoneration = input("Necesita exoneración por renunciar antes de los 30 días por ley?(Y/N): ") if args.needsExoneration is None else args.needsExoneration
    docNumber = input("Ingrese su número de DNI: ") if args.docNumber is None else args.docNumber
    fullName = input("Ingrese su nombre: ") if args.fullName is None else args.fullName

    cityDate = "\\def\\cityDate{" + (city + ", " + redactionDate) + "}"
    male = "\\def\\receiverMale{}" if receiverSex == 'M' else "" 
    receiverName = "\\def\\receiverName{" + receiverName + "}"
    jobTitle = "\\def\\jobTitle{" + jobTitle + "}"
    businessName = "\\def\\businessName{" + businessName + "}"
    resignationDate = "\\def\\resignationStartDate{" + resignationDate + "}"
    needsExoneration = "\\def\\needsExoneration{}" if male == 'Y' else "" 
    docNumber = "\\def\\docNumber{" + docNumber + "}"
    fullName = "\\def\\fullName{" + fullName + "}"
    latexFile = "\\input{main.tex}"

    command = "pdflatex \"{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\"".format(
        cityDate, 
        male,
        receiverName,
        jobTitle,
        businessName,
        resignationDate,
        needsExoneration,
        docNumber,
        fullName,
        latexFile)
    subprocess.call(command, shell=True)
        
if __name__ == "__main__":
   main()
