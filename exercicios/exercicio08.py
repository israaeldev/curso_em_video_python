salario_funcionario =float(input('digite o salario do seu funcionario:'))
aumento =float(input('digite a porcentagem do aumento:'))
conta = aumento / 100 * salario_funcionario
salario_final = salario_funcionario + conta
print(f'o salario do funcionario que era {salario_funcionario} com {aumento} por cento de aumento ficarar {salario_final}.')