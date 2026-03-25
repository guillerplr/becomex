
CREATE PROCEDURE dbo.proc_TransformacaoDados
AS
BEGIN

	SET NOCOUNT ON;

	IF OBJECT_ID('tempdb..#tempEmpresa') IS NOT NULL
		DROP TABLE #tempEmpresa

	 ; WITH estabelecimentos AS
	 (
		SELECT TOP 1000 * FROM [dbo].TabEstabelecimentoArquivo 
	 )
	 SELECT DISTINCT tea.teoCnpjBasico
		, tea.teoRazaoSocial
		, tea.teoCapitalSocial
		, teoa.teaNomeFantasia
		, CASE tea.teoPorteEmpresa 
			WHEN '00' THEN 'NÃO INFORMADO' 
			WHEN '01' THEN 'MICRO EMPRESA' 
			WHEN '03' THEN 'EMPRESA DE PEQUENO PORTE' 
			WHEN '05' THEN 'DEMAIS' 
			END  PorteEmpresa
		, CAST(teoa.teaDataInicioAtividade AS DATE) DataInicioAtividade
		, CONCAT(teoa.teaCnpjBasico, teoa.teaCnpjOrdem, teoa.teaCnpjDV) CNPJ
		, CASE teoa.teaSituacaoCadastral 
			WHEN '01' THEN 'NULA' 
			WHEN '02' THEN 'ATIVA' 
			WHEN '03' THEN 'SUSPENSA' 
			WHEN '04' THEN 'INAPTA' 
			WHEN '08' THEN 'BAIXADA' 
			END SituacaoCadastral 
		, tmoa.tmoDescricao
		, CAST(teoa.teaDataSitCadastral AS DATE) DataSitCadastral	
		, tca.tcaDescricao CnaePrincipal
		, tm.tmaDescricao Municipio
		, teoa.teaUF UF
		, teoa.teaEmail Email
		, teoa.teaCnaePrincipal
		, teoa.teaCnaeSecundario
		, tmoa.tmoDescricao MotivoSitCadastral
		INTO #tempEmpresa
	FROM estabelecimentos teoa
	INNER JOIN TabEmpresaArquivo tea ON teoa.teaCnpjBasico = tea.teoCnpjBasico
	LEFT JOIN TabMotivoArquivo tmoa ON tmoa.tmoCodigo = teoa.teaMotivoSitCadastral
	INNER JOIN TabCnaeArquivo tca ON tca.tcaCodigo = teoa.teaCnaePrincipal
	INNER JOIN TabMunicipioArquivo tm ON tm.tmaCodigo = teoa.teaMunicipio


	MERGE dbo.TabEstabelecimento AS Destino
	USING #tempEmpresa AS Origem ON (Origem.CNPJ = Destino.teoCnpj)
	WHEN MATCHED AND ( 
							   Destino.teoSituacaoCadastral != Origem.SituacaoCadastral
							OR Destino.teoDataSitCadastral != Origem.DataSitCadastral											
						)
	THEN UPDATE SET	
		Destino.teoSituacaoCadastral = Origem.SituacaoCadastral,
		Destino.teoDataSitCadastral = Origem.DataSitCadastral
	WHEN NOT MATCHED BY TARGET THEN
			INSERT ([teoCnpj], [teoNomeFantasia], [teoRazaoSocial], [teoSituacaoCadastral], [teoDataSitCadastral], [teoMotivoSitCadastral], [teoDataInicioAtividade]
					, [teoCnaePrincipal], [teoCnaeSecundario], [teoMunicipio], [teoUF], [teoEmail])		
			VALUES (Origem.CNPJ, Origem.teaNomeFantasia, Origem.teoRazaoSocial, Origem.SituacaoCadastral, Origem.DataSitCadastral, Origem.MotivoSitCadastral
						,Origem.DataInicioAtividade, Origem.teaCnaePrincipal, Origem.teaCnaeSecundario, Origem.Municipio, Origem.UF, Origem.Email);


	DROP TABLE #tempEmpresa;

END


 

 
 