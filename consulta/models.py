from django.db import models

class pacientes(models.Model):
    paciente_id = models.IntegerField()
    nome = models.CharField( max_length=50)
    data_nascimento = models.DateField((""), auto_now=False, auto_now_add=False)
    cpf = models.CharField( max_length=50)
    telefone = models.CharField( max_length=50)
    endereco = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_at = models.TimeField(auto_now=False, auto_now_add=False)

class consultas(models.Model):
    paciente_id = models.ForeignKey(pacientes, on_delete=models.CASCADE)
    medico_id = models.IntegerField()
    data_hora = models.DateField(auto_now=False, auto_now_add=False)
    motivo = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now=False, auto_now_add=False)
    consulta_id = models.IntegerField(enumerate)

class prontuarios(models.Model):
    prontuario_id = models.IntegerField(enumerate)
    consulta_id = models.ForeignKey(consultas, on_delete=models.CASCADE)
    diagnostico = models.TextField(max_length=200)
    prescicao = models.TextField(max_length=200)
    observacoes = models.TextField(max_length=200)
    created_at = models.TimeField(auto_now=False, auto_now_add=False)

class medicos(models.Model):
    medico_id = models.IntegerField(enumerate)
    nome = models.CharField(max_length=50)
    crm = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField (max_length=254)
    created_at = models.TimeField(auto_now=False, auto_now_add=False)

class medico_especialidade(models.Model):
    medico_especialidade_id = models.IntegerField(enumerate)
    medico_id = models.ForeignKey(medicos, on_delete=models.CASCADE)
    medico_especialidade_id = models.IntegerField(enumerate)

class especialidade(models.Model):
    especialidade_id = models.ForeignKey(medico_especialidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=300)