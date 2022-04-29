from django.db import models

from django.utils.timezone import now


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs (Demitindo)"
        HIRING_FREEZE = "Hiring Freeze (Não está contratando)"
        HIRING = "Hiring (Contratando)"
        ENCERRANDO_ATIVIDADES = "Fechando as portas"
        UNKNOWN = "Ainda não sabemos o status"

    class ComentarioPadrao(models.TextField):
        TEXTO = "Teste de texto padrão"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(choices=CompanyStatus.choices, default=CompanyStatus.UNKNOWN, max_length=40)
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = models.URLField(max_length=100, blank=True)
    comentario_thiaguinho = models.TextField(blank=True, default=ComentarioPadrao.TEXTO)

    def __str__(self):
        return f'{self.name} [{self.status}]'


class Operadores(models.Model):
    class OperadoresSatusCLT(models.TextChoices):
        ATIVO = 'Ativa'
        DESLIGADO = 'Desligado'
        CONTRATO_TEMPORARIO = 'Contrato Temporário'

    class OperadorGenero(models.TextChoices):
        MASCULINO = 'Masculino'
        FEMININO = 'Feminino'
        TRANS = 'Trans'
        NÃO_ME_IDENTIFICO = 'Não me identifico'

    class OperadorStatusCivil(models.TextChoices):
        CASADO = 'Casado'
        SOLTEIRO = 'Solteiro'
        DIVORCIADO = 'Divorciado'
        VIUVO = 'Viúvo'

    nome = models.CharField(max_length=50, null=False)
    dt_nasc = models.DateField(null=False)
    sexo = models.CharField(choices=OperadorGenero.choices, max_length=20)
    status_civil = models.CharField(choices=OperadorStatusCivil.choices, max_length=20, editable=True)
    status_clt = models.CharField(choices=OperadoresSatusCLT.choices, max_length=30)
    data_contratacao = models.DateField(auto_now=True, editable=True)
    data_demissao = models.DateField(null=True)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.nome} ({self.cpf}) [ {self.status_clt} ]'

class TabulacoesOperacao(models.Model):
    class TabulacoesTipo(models.TextChoices):
        TELEFONIA = 'Telefonia'
        ALO = 'Alô'
        CPC = 'Cpc'
        CPCA = 'Cpca'
        CONVERSÃO = 'Conversão'

    class TabulacaoSubtipo(models.TextChoices):
        BLACKLIST = 'Blacklist'
        PRODUTIVO = 'Produtivo'
        IMPRODUTIVO = 'Improdutivo'

    class TabulacaoOperacao(models.TextChoices):
        BLENDED = 'Blended'
        RECEPTIVO = 'Receptivo'
        ATIVO = 'Ativo'
    tabulacao = models.CharField(max_length=50)
    tipo_tabulacao = models.CharField(choices=TabulacoesTipo.choices, max_length=30)
    subtipo_taublacao = models.CharField(choices=TabulacaoSubtipo.choices, max_length=30)
    renitencia = models.IntegerField
