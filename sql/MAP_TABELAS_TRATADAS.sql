/**
	Objetivo: Tabelas mapeadas para receber os dados tratados.	
	Data: 16/04/2025
	Autor: Cristiano Fernandes
***/
DROP TABLE TabEstabelecimento
CREATE TABLE TabEstabelecimento
(
	teoID INT IDENTITY NOT NULL,
	teoCnpj VARCHAR(14) NOT NULL,	
	teoIdMatrizFilial VARCHAR(500),
	teoNomeFantasia VARCHAR(250),
	teoRazaoSocial VARCHAR(250),
	teoSituacaoCadastral VARCHAR(500),
	teoDataSitCadastral DATE,
	teoMotivoSitCadastral VARCHAR(500),
	teoNomeCidadeExterior VARCHAR(500),	
	teoDataInicioAtividade DATE,
	teoCnaePrincipal INT,
	teoCnaeSecundario VARCHAR(500),
	-- DADOS DE ENDEREÇO
	teoTipoLogradouro VARCHAR(50),
	teoLogradouro VARCHAR(250),
	teoNumero INT,
	teoComplemento VARCHAR(100),
	teoBairro VARCHAR(250),
	teoCEP VARCHAR(10),	
	teoMunicipio VARCHAR(250),
	teoUF CHAR(2),
	teoPais INT,

	teoEmail VARCHAR(250),

	teoSituacaoEspecial VARCHAR(500),
	teoDataSitEspecial DATE,

	teoDataInclusao DATETIME NOT NULL
	CONSTRAINT PK_TabEstabelecimento PRIMARY KEY (teoID)
)
GO

ALTER TABLE TabEstabelecimento
ADD teoExcluido BIT

CREATE INDEX IDX_TabEstabelecimento_teoCnpj ON TabEstabelecimento (teoCnpj);

ALTER TABLE TabEstabelecimento
ADD CONSTRAINT DF_TabEstabelecimento_teoDataInclusao DEFAULT GETDATE() FOR teoDataInclusao

CREATE TABLE TabContato
(
	tcoID INT IDENTITY NOT NULL,
	tcoDDD INT NOT NULL,
	tcoTelefone BIGINT NOT NULL,
	tcoFax BIT NOT NULL,
	tcoEstabelecimentoID INT NOT NULL,
	tcoDataInclusao DATETIME NOT NULL
	CONSTRAINT PK_TabContato PRIMARY KEY (tcoID),
	CONSTRAINT FK_TabContato_TabEstabelecimento FOREIGN KEY (tcoEstabelecimentoID)
		REFERENCES TabEstabelecimento (teoID)	
)

ALTER TABLE TabContato
ADD CONSTRAINT DF_TabContato_tcoFax DEFAULT 0 FOR tcoFax

ALTER TABLE TabContato
ADD CONSTRAINT DF_TabContato_tcoDataInclusao DEFAULT GETDATE() FOR tcoDataInclusao