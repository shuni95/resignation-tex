# Resignation Tex

Modelo de Carta de Renuncia parametrizable para Perú

## Ejemplos

```bash
pdflatex "\def\cityDate{Lima, 12 de Septiembre del 2018} \def\receiverMale{} \def\receiverName{José Hernández} \def\jobTitle{Gerente General} \def\businessName{La Abejita} \def\resignationStartDate{28 de Septiembre del 2018} \def\needsExoneration{} \def\docNumber{12341234} \def\fullName{Junior Zavaleta} \input{main.tex}"
```

```bash
python main.py --city=Lima --redactionDate="28 de enero" --receiverSex=M --receiverName="Pedro Paramo" --jobTitle="Dark CTO" --businessName="Naranjita SRL" --resignationDate="29 de Febrero" --needsExoneration=Y --docNumber="91929394" --fullName="Junior Zavaleta
```
