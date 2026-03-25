/**
	Objetivo: Tabelas mapeadas com objetivo de receber todos os dados referente aos arquivos baixados.
		Todos os dados nas tabelas em questão passará pelo processo de transformação, e serão tratados.	
	Data: 16/04/2025
	Autor: Cristiano Fernandes
***/

CREATE TABLE TabEstabelecimentoArquivo
(
	teaCnpjBasico VARCHAR(MAX),
	teaCnpjOrdem VARCHAR(MAX),
	teaCnpjDV VARCHAR(MAX),
	teaIdMatrizFilial VARCHAR(MAX),
	teaNomeFantasia VARCHAR(MAX),
	teaSituacaoCadastral VARCHAR(MAX),
	teaDataSitCadastral VARCHAR(MAX),
	teaMotivoSitCadastral VARCHAR(MAX),
	teaNomeCidadeExterior VARCHAR(MAX),
	teaPais VARCHAR(MAX),
	teaDataInicioAtividade VARCHAR(MAX),
	teaCnaePrincipal VARCHAR(MAX),
	teaCnaeSecundario VARCHAR(MAX),
	teaTipoLogradouro VARCHAR(MAX),
	teaLogradouro VARCHAR(MAX),
	teaNumero VARCHAR(MAX),
	teaComplemento VARCHAR(MAX),
	teaBairro VARCHAR(MAX),
	teaCEP VARCHAR(MAX),
	teaUF VARCHAR(MAX),
	teaMunicipio VARCHAR(MAX),
	teaDDD1 VARCHAR(MAX),
	teaTelefone1 VARCHAR(MAX),
	teaDDD2 VARCHAR(MAX),
	teaTelefone2 VARCHAR(MAX),
	teaDDDFax VARCHAR(MAX),
	teaFax VARCHAR(MAX),
	teaEmail VARCHAR(MAX),
	teaSituacaoEspecial VARCHAR(MAX),
	teaDataSitEspecial VARCHAR(MAX)
)
GO


CREATE TABLE TabEmpresaArquivo
(
	teoCnpjBasico VARCHAR(500),
	teoRazaoSocial VARCHAR(500),
	teoNatJuridica VARCHAR(500),
	teoQualificacaoResponsavel VARCHAR(500),
	teoCapitalSocial VARCHAR(500),
	teoPorteEmpresa VARCHAR(500),
	teoEnteFederativoRes VARCHAR(500)
)
GO


CREATE TABLE TabSocioArquivo
(
	tsaCnpjBasico VARCHAR(MAX),
	tsaIdentificador VARCHAR(MAX),
	tsaNomeSocio VARCHAR(MAX),
	tsaCPFCNPJ VARCHAR(MAX),
	tsaCodigoQualificacao VARCHAR(MAX),
	tsaDataEntrada VARCHAR(MAX),
	tsaPais VARCHAR(MAX),
	tsaCPFRepresentanteLegal VARCHAR(MAX),
	tsaNomeRepresentante VARCHAR(MAX),
	tsaCodQualificacaoRepresentante VARCHAR(MAX),
	tsaFaixaEtaria VARCHAR(MAX)
)
GO

CREATE TABLE TabCnaeArquivo
(
	tcaCodigo VARCHAR(500),
	tcaDescricao VARCHAR(500)
)
GO

CREATE TABLE TabNaturezaJuridicaArquivo
(
	tnjCodigo VARCHAR(500),
	tnjDescricao VARCHAR(500)
)
GO

CREATE TABLE TabQualificacaoSocioArquivo
(
	tqsCodigo VARCHAR(500),
	tqsDescricao VARCHAR(500)
)
GO

CREATE TABLE TabPaisArquivo
(
	tpaCodigo VARCHAR(500),
	tpaDescricao VARCHAR(500)
)
GO

CREATE TABLE TabMunicipioArquivo
(
	tmaCodigo VARCHAR(500),
	tmaDescricao VARCHAR(500)
)
GO

CREATE TABLE TabMotivoArquivo
(
	tmoCodigo VARCHAR(500),
	tmoDescricao VARCHAR(500)
)
GO

CREATE TABLE TabSimplesArquivo
(
	tssCnpjBasico VARCHAR(500),
	tssOpcaoSimples VARCHAR(500),
	tssDataOpcaoSimples VARCHAR(500),
	tssDataExclusaoSimples VARCHAR(500),
	tssOpcaoMEI VARCHAR(500),
	tssDataOpcaoMEI VARCHAR(500),
	tssDataExclusaoMEI VARCHAR(500),
)
GO