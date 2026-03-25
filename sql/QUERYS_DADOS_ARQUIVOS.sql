 /*
 
 SELECT * FROM [dbo].[TabMunicipioArquivo]  
 SELECT * FROM [dbo].[TabNaturezaJuridicaArquivo] 
 SELECT TOP 1000 * FROM [dbo].TabEstabelecimentoArquivo 
 SELECT TOP 1000 * FROM [dbo].[TabEmpresaArquivo]
 SELECT * FROM [dbo].TabCnaeArquivo
 SELECT * FROM [dbo].TabPaisArquivo
 SELECT * FROM [dbo].TabMotivoArquivo
 SELECT TOP 1000 * FROM [dbo].TabSocioArquivo (nolock)
 SELECT * FROM [dbo].TabQualificacaoSocioArquivo
 SELECT TOP 1000 * FROM [dbo].TabSimplesArquivo (nolock)

 CNAE 5250-8/03 – Agenciamento de Cargas, Exceto para Transporte Marítimo
 CNAE 5231-1/02 – Agenciamento Marítimo
 CNAE 5250-8/04 - Refere-se à organização logística do transporte de carga.


 Dados Improtantes:
	Empresa: Rzao Social, cnpj, nome, endereço
	CNAes
	Representantes legais
	Filiais

 */

 

 sp_help TabSocioArquivo

 SELECT TOP 100 *
	, CASE tea.teoPorteEmpresa 
		WHEN '00' THEN 'NÃO INFORMADO' 
		WHEN '01' THEN 'MICRO EMPRESA' 
		WHEN '03' THEN 'EMPRESA DE PEQUENO PORTE' 
		WHEN '05' THEN 'DEMAIS' 
		END  PorteEmpresa
 FROM TabEmpresaArquivo tea 
 INNER JOIN TabNaturezaJuridicaArquivo tnja ON tnja.tnjCodigo = tea.teoNatJuridica
 INNER JOIN TabQualificacaoSocioArquivo tqsa ON tqsa.tqsCodigo = tea.teoQualificacaoResponsavel



  ; WITH estabelecimentos AS
  (
	 SELECT TOP 1000 * FROM [dbo].TabEstabelecimentoArquivo 
  )
  SELECT DISTINCT tea.teoCnpjBasico
	, tea.teoRazaoSocial
	, tea.teoCapitalSocial
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
	--, teoa.*
	FROM estabelecimentos teoa
 INNER JOIN TabEmpresaArquivo tea ON teoa.teaCnpjBasico = tea.teoCnpjBasico
 LEFT JOIN TabMotivoArquivo tmoa ON tmoa.tmoCodigo = teoa.teaMotivoSitCadastral
 INNER JOIN TabCnaeArquivo tca ON tca.tcaCodigo = teoa.teaCnaePrincipal
 INNER JOIN TabMunicipioArquivo tm ON tm.tmaCodigo = teoa.teaMunicipio

 --CREATE INDEX IDX_TabEstabelecimentoArquivo_CnpjBasico ON TabEstabelecimentoArquivo (teaCnpjBasico)
 --CREATE INDEX IDX_TabEmpresaArquivo_CnpjBasico ON TabEmpresaArquivo (teoCnpjBasico)

   ; WITH estabelecimentos AS
  (
	 SELECT TOP 1000 * FROM [dbo].TabEstabelecimentoArquivo 
  )
  SELECT tea.teoCnpjBasico
	, tea.teoRazaoSocial
	, tea.teoCapitalSocial
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
	, tca.tcaDescricao
	, tm.tmaDescricao
	, teoa.teaUF
	, teoa.teaEmail
	, taao.tsaNomeSocio
	, CASE taao.tsaIdentificador 
		WHEN '1' THEN 'PESSOA JURÍDICA' 
		WHEN '2' THEN 'PESSOA FÍSICA' 
		WHEN '3' THEN 'ESTRANGEIRO'
		END Identificador  
	, tqsa.tqsDescricao
	, CAST(taao.tsaDataEntrada AS DATE) DataEntrada
	, CASE taao.tsaFaixaEtaria 
		WHEN '1' THEN '0 A 12 ANOS' 
		WHEN '2' THEN '13 A 20 ANOS'
		WHEN '3' THEN '21 A 30 ANOS'
		WHEN '4' THEN '31 A 40 ANOS'
		WHEN '5' THEN '41 A 50 ANOS' 
		WHEN '6' THEN '51 A 60 ANOS'
		WHEN '7' THEN '61 A 70 ANOS' 
		WHEN '8' THEN '71 A 80 ANOS'
		WHEN '9' THEN 'MAIORES DE 80 ANOS'
		ELSE 'NÃO SE APLICA'
		END Identificador  
	FROM estabelecimentos teoa
 INNER JOIN TabEmpresaArquivo tea ON teoa.teaCnpjBasico = tea.teoCnpjBasico
 LEFT JOIN TabMotivoArquivo tmoa ON tmoa.tmoCodigo = teoa.teaMotivoSitCadastral
 INNER JOIN TabCnaeArquivo tca ON tca.tcaCodigo = teoa.teaCnaePrincipal
 INNER JOIN TabMunicipioArquivo tm ON tm.tmaCodigo = teoa.teaMunicipio
 INNER JOIN TabSocioArquivo taao ON taao.tsaCnpjBasico = teoa.teaCnpjBasico
 INNER JOIN TabQualificacaoSocioArquivo tqsa ON tqsa.tqsCodigo = taao.tsaCodigoQualificacao

 SELECT TOP 1000 * FROM TabEstabelecimentoArquivo teoa
 WHERE 1 = 1
 AND CAST(teoa.teaDataInicioAtividade AS DATE) > '2025-01-01'
 AND teoa.teaCnaePrincipal IN ('5250803', '5231102', '5250804')

 SELECT TOP 1000 
	CASE teoa.teaIdMatrizFilial 
		WHEN '1' THEN 'MATRIZ' 
		WHEN '2' THEN 'FILIAL' 		
		END Identificador  	
	, CNAES.value
	, tca.tcaDescricao
 FROM TabEstabelecimentoArquivo teoa
 OUTER APPLY STRING_SPLIT(teoa.teaCnaeSecundario, ',') CNAES
 INNER JOIN TabCnaeArquivo tca ON tca.tcaCodigo = CNAES.value
 WHERE 1 = 1
 AND CAST(teoa.teaDataInicioAtividade AS DATE) > '2025-04-01'
 AND ( teoa.teaCnaeSecundario LIKE '%5250803%' OR teoa.teaCnaeSecundario LIKE '%5231102%' OR teoa.teaCnaeSecundario LIKE '%5250804%' )
 AND teoa.teaCnpjBasico = '38627222'
 ORDER BY teoa.teaCnpjBasico, teoa.teaCnpjOrdem


 SELECT * FROM TabCnaeArquivo tca WHERE tca.tcaCodigo IN ('5250803', '5231102', '5250804')


